from deluca.lung.utils.munger import Munger

import math
import torch
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt


class SNN(torch.nn.Module):
    def __init__(self, in_dim, out_dim, hidden_dim, n_layers, dropout_prob=0.0):
        super().__init__()
        layers = OrderedDict()
        for i in range(n_layers - 1):
            if i == 0:
                layers[f"fc{i}"] = torch.nn.Linear(in_dim, hidden_dim, bias=False)
            else:
                layers[f"fc{i}"] = torch.nn.Linear(hidden_dim, hidden_dim, bias=False)
            layers[f"selu_{i}"] = torch.nn.SELU()
            layers[f"dropout_{i}"] = torch.nn.AlphaDropout(p=dropout_prob)
        layers[f"fc_{i+1}"] = torch.nn.Linear(hidden_dim, out_dim, bias=True)
        self.network = torch.nn.Sequential(layers)
        self.reset_parameters()

    def forward(self, x):
        return self.network(x)

    def reset_parameters(self):
        for layer in self.network:
            if not isinstance(layer, torch.nn.Linear):
                continue
            torch.nn.init.normal_(layer.weight, std=1 / math.sqrt(layer.out_features))
            if layer.bias is not None:
                fan_in, _ = torch.nn.init._calculate_fan_in_and_fan_out(layer.weight)
                bound = 1 / math.sqrt(fan_in)
                torch.nn.init.uniform_(layer.bias, -bound, bound)

    def track_layer_activations(self, x):
        activations = []
        for layer in self.network:
            x = layer.forward(x)
            if isinstance(layer, torch.nn.SELU):
                activations.append(x.data.flatten())
        return activations

    def train(
        self,
        munger_path,
        u_window=5,
        p_window=3,
        train_key="train",
        test_key="test",
        batch_size=512,
        epochs=500,
        optimizer=torch.optim.Adam,
        optimizer_params={"lr": 1e-3},
        scheduler=torch.optim.lr_scheduler.ReduceLROnPlateau,
        scheduler_params={"factor":0.9, "patience":15},
        loss_fn=torch.nn.L1Loss,
        loss_fn_params={},
        print_loss=100,
    ):
        munger = Munger.load(munger_path)
        loader = munger.get_data_loader(
            key=train_key, u_window=u_window, p_window=p_window, batch_size=batch_size
        )
        X_tensor, y_tensor = munger.scale_and_window(
            key=train_key, u_window=u_window, p_window=p_window
        )
        X_test_tensor, y_test_tensor = munger.scale_and_window(
            key=test_key, u_window=u_window, p_window=p_window
        )

        optim = optimizer(self.parameters(), **optimizer_params)
        schedule = scheduler(optim, **scheduler_params)
        loss_fn = loss_fn(**loss_fn_params)

        for epoch in range(epochs):
            for X_batch, y_batch in loader:
                self.zero_grad()
                preds = self(X_batch).squeeze()
                loss = loss_fn(preds, y_batch)
                loss.backward()
                optim.step()
            schedule.step(loss)

            if epoch % print_loss == 0:
                with torch.no_grad():
                    # expensive end-of-epoch eval, just for intuition
                    preds = self(X_tensor).squeeze()
                    train_loss = loss_fn(preds, y_tensor)

                    # cross-validation
                    preds = self(X_test_tensor).squeeze()
                    test_loss = loss_fn(preds, y_test_tensor)

                print(
                    f"Epoch {epoch:2d}: train={train_loss.item():.5f}, test={test_loss.item():.5f}"
                )

    def plot_residuals(self, munger_path, u_window=5, p_window=3, figsize=(10, 10), s=5, alpha=0.5):
        munger = Munger.load(munger_path)
        plt.rc('figure', figsize=figsize)

        X_test, y_test = munger.scale_and_window('test', u_window=u_window, p_window=p_window)

        with torch.no_grad():
            y_pred = self(X_test).numpy()

        unscaled_truth = munger.unscale_pressures(y_test)
        unscaled_preds = munger.unscale_pressures(y_pred)

        x = np.linspace(0, 45, 1000)

        plt.xlabel('true pressure')
        plt.ylabel('predicted pressure')

        plt.scatter(unscaled_truth, unscaled_preds, s=s, alpha=alpha)
        plt.plot(x, x, linestyle='-', color = "red", label = "f(x) = x");


class BoundaryDict(torch.nn.Module):
    def __init__(self, models=None, const_trainable=True):
        self.dict = {}

        if models is None:
            models = []

        models.insert(0, ConstantModel(trainable=const_trainable))

        for i, model in enumerate(models):
            self.dict[i] = model

        self.width = i

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, val):
        self.dict[key] = val

    def __delitem__(self, key):
        del self.dict[key]

    def items(self):
        return self.dict.items()

    def train(
        self,
        munger_path,
        train_key="train",
        test_key="test",
        batch_size=16,
        epochs=800,
        optimizer=torch.optim.SGD,
        optimizer_params={"lr": 1e-2, "weight_decay": 1e-3},
        scheduler=torch.optim.lr_scheduler.ReduceLROnPlateau,
        scheduler_params={"factor":0.9, "patience":15},
        loss_fn=torch.nn.L1Loss,
        loss_fn_params={},
        print_loss=100,
    ):
        munger = Munger.load(munger_path)
        loss_fn = loss_fn(**loss_fn_params)

        for idx, model in self.dict.items():
            if idx == 0:
                _, y = munger.scale_and_window_boundary(train_key, boundary_index=0)
                self[0].update_constant(y.mean().item())
                continue

            loader = munger.get_boundary_data_loader(train_key, idx, batch_size=batch_size)

            # TODO: figure out if we want to pull out 'test'
            X_test, y_test = munger.scale_and_window_boundary(test_key, idx)
            optim = optimizer(model.parameters(), **optimizer_params)
            schedule = scheduler(optim, **scheduler_params)

            if print_loss is not None:
                print("Boundary model #", idx)

            for epoch in range(epochs):
                for X_batch, y_batch in loader:
                    model.zero_grad()
                    preds = model(X_batch).squeeze()
                    loss = loss_fn(preds, y_batch)
                    loss.backward()
                    optim.step()
                schedule.step(loss)

                if epoch % print_loss == 0:
                    with torch.no_grad():
                        test_loss = loss_fn(model(X_test).squeeze(), y_test)

                    print(f"Epoch {epoch:2d}: test={test_loss.item():.5f}")

            self[idx] = model

    def plot_boundary_performance(self, munger_path, key="test"):
        munger = Munger.load(munger_path)

        plt.rc("figure", figsize=(16, 4))

        for boundary_index in range(1, self.width + 1):
            plt.subplot(2, 5, boundary_index)

            model = self[boundary_index]

            X_test, y_test = munger.scale_and_window_boundary(key, boundary_index)

            with torch.no_grad():
                y_pred = model(X_test).numpy()

            unscaled_truth = munger.unscale_pressures(y_test)
            unscaled_preds = munger.unscale_pressures(y_pred)

            x = np.linspace(0, 25, 1000)

            plt.xlabel("true pressure")
            plt.ylabel("predicted pressure")

            plt.scatter(
                unscaled_truth, unscaled_preds, s=5, label=f"Boundary Model #{boundary_index}"
            )
            plt.plot(x, x, linestyle="-", color="red", label="f(x) = x")


class ShallowBoundaryModel(torch.nn.Module):  # Paula's boundary model
    def __init__(self, in_dim, hidden_dim=100, out_dim=1):
        super().__init__()
        layers = OrderedDict()
        layers["fc1"] = torch.nn.Linear(in_dim, hidden_dim, bias=False)
        layers["tanh_1"] = torch.nn.Tanh()
        layers["fc_2"] = torch.nn.Linear(hidden_dim, out_dim, bias=True)
        self.model = torch.nn.Sequential(layers)

    def forward(self, x):
        out = self.model(x)
        return out


class RegressionBoundaryModel(torch.nn.Module):
    def __init__(self, in_dim, out_dim=1):
        super().__init__()
        layers = OrderedDict()
        layers["fc_1"] = torch.nn.Linear(in_dim, out_dim, bias=True)
        self.model = torch.nn.Sequential(layers)

    def forward(self, x):
        out = self.model(x)
        return out


class ConstantModel(torch.nn.Module):  # boundary model to predict first pressure with no features
    def __init__(self, const_out=0., trainable=True):
        super().__init__()

        # Assume we want to fix trainable at initialization
        self.trainable = trainable
        self.update_constant(const_out)

    def update_constant(self, const_out):
        # Note: we have this round-about logic b/c torch complains about
        # updating a parameter with a tensor value
        const_out = torch.tensor(const_out)
        if self.trainable:
            self.const_out = torch.nn.parameter.Parameter(const_out)
        else:
            self.const_out = const_out

    def forward(self, x=None):
        return self.const_out


class InspiratoryModel(
    torch.nn.Module
):  # manager of a family of trained boundary models + general model
    def __init__(self, default_model, boundary_dict):
        super().__init__()

        self.default_model = default_model
        self.boundary_dict = torch.nn.ModuleDict({str(i): m for i, m in boundary_dict.items()})

    def forward(self, t, features):  # placeholder for stitching
        if t in self.boundary_dict:
            return self.boundary_dict[str(t)](features)
        return self.default_model(features)
