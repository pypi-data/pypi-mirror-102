import os
from enum import Enum
import numpy as np
import dill as pickle
import torch

from deluca.lung.utils.core import BreathWaveform
from deluca.lung.core import VentObj


ControllerRegistry = []


class Phase(Enum):
    RAMP_UP = 1
    PIP = 2
    RAMP_DOWN = 3
    PEEP = 4


class Controller(VentObj):
    def __new__(cls, *args, **kwargs):
        obj = VentObj.__new__(cls)
        obj.__setattr__("time", float("inf"))
        obj.__setattr__("waveform", BreathWaveform())

        obj.kwargs(**kwargs)

        return obj

    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        if cls.__name__ not in [ctrl.__name__ for ctrl in ControllerRegistry]:
            ControllerRegistry.append(cls)

    def reset(self):
        pass

    def compute_action(self, state, t):
        pass

    def forward(self, state, t):
        u_in, u_out = self.compute_action(state, t)
        self.time = t

        torched = isinstance(u_out, torch.Tensor)
        decay = (u_out if not torched else u_out.item()) == 1
        if decay:
            u_in = self.waveform.decay(t)
            if torched:
                u_in = self.tensor(u_in)
        return u_in, u_out

    def u_out(self, t):
        phase = self.phase(t)
        u_out = np.zeros_like(phase)
        u_out[np.equal(phase, Phase.RAMP_DOWN.value)] = 1
        u_out[np.equal(phase, Phase.PEEP.value)] = 1

        return self.tensor(u_out)

    def dt(self, t):
        dt = max(0, t - self.time)
        return dt

    def cycle_phase(self, t):
        return t % self.waveform.period

    def phase(self, t):
        return self.waveform.phase(t)

    def train(
        self,
        sim,
        duration=3,
        dt=0.03,
        epochs=100,
        use_noise = False,
        optimizer=torch.optim.Adam,
        optimizer_params={"lr": 1e-3, "weight_decay": 1e-4},
        loss_fn=torch.nn.L1Loss,
        loss_fn_params={},
        scheduler=torch.optim.lr_scheduler.ReduceLROnPlateau,
        scheduler_params={},
        use_tqdm=True,
        print_loss=1,
        shuffle=False,
        device="cpu",
    ):
        optimizer = optimizer(self.parameters(), **optimizer_params)
        scheduler = scheduler(optimizer, **scheduler_params)
        loss_fn = loss_fn(**loss_fn_params)

        tt = torch.linspace(0, duration, int(duration / dt))
        losses = []

        torch.autograd.set_detect_anomaly(True)

        # TODO: handle device-awareness
        for epoch in range(epochs):
            self.reset()
            sim.reset()

            loss = torch.tensor(0.0, device=device, requires_grad=True)

            self.zero_grad()

            for t in tt:
                sim.pressure += use_noise * torch.normal(mean=torch.tensor(1.), std=1.)
                pressure = sim.pressure
                u_in, u_out = self(pressure, t)
                sim(u_in, u_out, t)

                if u_out == 0:
                    loss = loss + loss_fn(torch.tensor(self.waveform.at(t)), pressure)

            loss.backward(retain_graph=True)
            optimizer.step()
            scheduler.step(loss)
            per_step_loss = loss / len(tt)
            losses.append(per_step_loss)
            if epoch % print_loss == 0:
                print(
                    f"Epoch: {epoch}\tLoss: {per_step_loss:.2f}\tLR: {optimizer.param_groups[0]['lr']}"
                )

        return losses
