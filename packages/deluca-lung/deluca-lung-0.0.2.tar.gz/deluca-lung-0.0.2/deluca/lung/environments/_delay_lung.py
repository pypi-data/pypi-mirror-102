import torch
import numpy as np

from deluca.lung.environments.core import Environment


# 2nd attempt at vent simulation
# observed pressure comes from delayed control signal, with back-pressure from deluca.lung
class DelayLung(Environment):
    def __init__(self, delay=10, **kwargs):
        # dynamics hyperparameters
        self.params = {
            "min_volume": 1.5,
            "R_lung": 10,
            "C_lung": 6,
            "inertia": 0.995,
            "control_gain": 0.02,
        }
        self.delay = delay
        self.params = {key: self.tensor(val) for key, val in self.params.items()}
        if kwargs is not None:
            for p in kwargs:
                self.params[p] = kwargs[p]

        # reset states
        self.r0 = (3 * self.params["min_volume"] / (4 * np.pi)) ** (1 / 3)
        self.reset()

    def reset(self):
        self.volume = self.tensor(self.params["min_volume"])
        self.pipe_pressure = self.tensor(0.0)

        self.controls_in, self.controls_out = [], []
        self.volumes, self.pressures = [], []
        self.compute_aux_states()

    def compute_aux_states(self):
        # compute all other state vars, which are just functions of volume
        r = (3 * self.volume / (4 * np.pi)) ** (1 / 3)
        self.vent_pressure = self.params["C_lung"] * (1 - (self.r0 / r) ** 6) / (self.r0 ** 2 * r)

        if len(self.controls_in) < self.delay:
            self.pipe_impulse = 0
            self.peep = 0
        else:
            self.pipe_impulse = self.params["control_gain"] * self.controls_in[-self.delay]
            self.peep = self.controls_out[-self.delay]

        self.pipe_pressure = self.params["inertia"] * self.pipe_pressure + self.pipe_impulse
        self.pressure = torch.max(self.tensor(0.0), self.pipe_pressure - self.vent_pressure)

        if self.peep:
            self.pipe_pressure *= 0.995

    def forward(self, u_in, u_out, t):
        u_in = max(0, u_in)

        self.controls_in.append(u_in)
        self.controls_out.append(u_out)

        dt = self.dt

        # 2-dimensional action per timestep
        flow = self.pressure / self.params["R_lung"]

        # update by flow rate
        self.volume = torch.max(self.volume + flow * dt, self.params["min_volume"])

        # compute and record state
        self.compute_aux_states()
        self.pressures.append(self.pressure)
        self.volumes.append(self.volume)
