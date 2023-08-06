import torch
import numpy as np
import sklearn.preprocessing
import matplotlib.pyplot as plt

from deluca.lung.utils.analyzer import Analyzer
from deluca.lung.core import VentObj

def resample(tt, f, dt=0.03, snap_left=False, return_grid=False):
    # resample a continuous-time function interpolated from non-uniform samples
    num_tt = int((tt[-1] - tt[0]) / dt)
    tt_grid = np.arange(num_tt)*dt + tt[0]

    if snap_left:
        f_grid = f[np.searchsorted(tt, tt_grid)]
    else:
        f_grid = np.interp(tt_grid, tt, f)

    if return_grid:
        return tt_grid, f_grid
    else:
        return f_grid

class Munger(VentObj):
    def __init__(self, paths, to_round=False, dt_resample=False, clip=(2, -1), **kwargs):
        self.paths = paths
        self.analyzers = []
        self.data = []
        self.splits = {}
        self.to_round = to_round

        # Add data
        self.add_data(paths, dt_resample, clip, **kwargs)

        # Shuffle and split data
        self.split_data(**kwargs)

        # Compute mean, std for u_in and pressure
        self.u_scaler, self.p_scaler = self.fit_scalers(**kwargs)

    # Note: the following methods are meant to be run in order
    def add_data(self, paths, dt_resample=True, clip=(2, -1), **kwargs):
        if isinstance(paths, str):
            paths = [paths]

        failed = 0
        for path in paths:
            try:
                analyzer = Analyzer(path)

                self.analyzers.append(analyzer)
                inspiratory_clips = analyzer.infer_inspiratory_phases()

                for start, end in inspiratory_clips[clip[0]:clip[1]]:  # skip first 2 & last breaths

                    if self.to_round:
                        u_in = np.round(analyzer.u_in[start:end])
                    else:
                        u_in = analyzer.u_in[start:end]

                    pressure = analyzer.pressure[start:end]

                    if dt_resample:
                        tt = analyzer.tt[start:end]
                        u_in = resample(tt, u_in)
                        pressure = resample(tt, pressure)

                    self.data.append((u_in, pressure))

            except Exception as e:
                print(path, e)
                failed += 1

        print(f"Added {len(self.data)} breaths from {len(self.paths) - failed} paths.")

    def split_data(self, seed=0, keys=["train", "test"], splits=[0.9, 0.1], **kwargs):
        rng = np.random.default_rng(seed)

        # Determine split boundaries
        splits = (np.array(splits) / np.sum(splits) * len(self.data)).astype("int")[:-1]

        # Everyday I'm shuffling
        rng.shuffle(self.data)

        # Splitting
        self.splits = {key: val for key, val in zip(keys, np.split(self.data, splits))}

    def fit_scalers(self, key="train"):
        u_scaler = sklearn.preprocessing.StandardScaler()
        u_scaler.fit(np.concatenate([u for u, p in self.splits[key]]).reshape(-1, 1))
        print(f"u_in: mean={u_scaler.mean_}, std={u_scaler.scale_}")

        p_scaler = sklearn.preprocessing.StandardScaler()
        p_scaler.fit(np.concatenate([p for u, p in self.splits[key]]).reshape(-1, 1))
        print(f"pressure: mean={p_scaler.mean_}, std={p_scaler.scale_}")

        return u_scaler, p_scaler

    def scale_and_window(self, key, u_window=5, p_window=3):
        X, y = [], []
        for u, p in self.splits[key]:
            T = len(u)
            u_scaled = self.u_scaler.transform(u.reshape(-1, 1))
            p_scaled = self.p_scaler.transform(p.reshape(-1, 1))

            for t in range(max(u_window, p_window) + 1, T):
                features = np.concatenate(
                    [u_scaled[t - u_window : t, 0], p_scaled[t - p_window : t, 0]]
                )
                target = p_scaled[t, 0]
                X.append(features)
                y.append(target)

        return torch.tensor(X), torch.tensor(y)

    def scale_and_window_boundary(self, key, boundary_index):
        X, y = [], []

        if boundary_index == 0:  # special case: no features, predict p[0]
            for u, p in self.splits[key]:
                p_scaled = self.p_scaler.transform([[p[0]]])
                target = p_scaled[0][0]
                y.append(target)
            return None, torch.tensor(y)

        # otherwise, collate [first B inputs, first B pressures] -> (next pressure) pairs
        for u, p in self.splits[key]:
            T = len(u)
            if T < boundary_index + 1:  # if trajectory is too short, abort
                continue

            u_scaled = self.u_scaler.transform(u[:boundary_index].reshape(-1, 1)).flat
            p_scaled = self.p_scaler.transform(p[: boundary_index + 1].reshape(-1, 1)).flat

            features = np.concatenate([u_scaled, p_scaled[:-1]])
            target = p_scaled[-1]

            X.append(features)
            y.append(target)

        return torch.tensor(X), torch.tensor(y)

    def get_data_loader(self, key, u_window=5, p_window=3, batch_size=512, shuffle=True):
        X, y = self.scale_and_window(key, u_window, p_window)
        dataset = torch.utils.data.TensorDataset(X, y)
        return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    def get_boundary_data_loader(self, key, boundary_index, batch_size=512, shuffle=True):
        X, y = self.scale_and_window_boundary(key, boundary_index)
        dataset = torch.utils.data.TensorDataset(X, y)
        return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    def unscale_pressures(self, p):
        if type(p) is float:
            p = np.array([p])
        return self.p_scaler.inverse_transform(p.reshape(-1, 1))[:, 0]

    ###########################################################################
    # Plotting methods
    ###########################################################################

    def plot_boundary_pressures(self):
        plt.rc("figure", figsize=(16, 4))

        for tau in range(1, 6):
            plt.subplot(150 + tau)

            u_init = []
            p_init = []

            for u, p in self.splits["train"]:
                u_init.append(u[:tau].mean())
                p_init.append(p[tau])

            plt.xlim([0, 105])
            plt.ylim([2, 33])
            plt.xlabel(f"u_in[0:{tau}].mean")
            plt.title(f"pressure[{tau}]")

            plt.scatter(u_init, p_init, s=1)
