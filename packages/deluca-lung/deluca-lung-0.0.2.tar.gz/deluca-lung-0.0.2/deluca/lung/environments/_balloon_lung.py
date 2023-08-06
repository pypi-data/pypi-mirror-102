import torch
import numpy as np

from deluca.lung.environments.core import Environment


def PropValve(x):  # copied from Controller.__SimulatedPropValve
    y = 3 * x
    flow_new = 1.0 * (torch.tanh(0.03 * (y - 130)) + 1)
    return torch.clamp(flow_new, 0.0, 1.72)


def Solenoid(x):  # copied from Controller.__SimulatedSolenoid
    if x > 0:
        return x / x
    else:
        return x * 0.


# balloon physics vent ported from Cohen lab's repository
# Sources:
# https://github.com/CohenLabPrinceton/deluca.lunglator-Dev/blob/master/sandbox/HOWTO_RunController.ipynb
# https://github.com/CohenLabPrinceton/deluca.lunglator-Dev/blob/master/vent/controller/control_module.py
class BalloonLung(Environment):
    def __init__(self, min_volume=6, peep_valve=5, PC=40, RP=1, leak=False, **kwargs):
        # dynamics hyperparameters
        self.min_volume = self.tensor(min_volume)
        self.PC = self.tensor(PC)
        self.RP = self.tensor(RP)
        self.P0 = self.tensor(0.0)
        self.leak = leak
        self.peep_valve = self.tensor(peep_valve)

        self.r0 = (3 * self.min_volume / (4 * np.pi)) ** (1 / 3)
        # reset states
        self.reset()

    def reset(self):
        # keep volume as the only free parameter
        self.volume = self.min_volume
        self.compute_aux_states()

        self.pips, self.peeps = [], []
        self.volumes, self.pressures = [], []

    def compute_aux_states(self):
        # compute all other state vars, which are just functions of volume
        r = (3 * self.volume / (4 * np.pi)) ** (1 / 3)
        self.pressure = self.P0 + self.PC * (1 - (self.r0 / r) ** 6) / (self.r0 ** 2 * r)

    def forward(self, u_in, u_out, t):
        self.pips.append(u_in)
        self.peeps.append(u_out)

        dt = self.dt

        # 2-dimensional action per timestep: PIP/PEEP voltages

        flow = torch.clamp(PropValve(u_in), 0, 2) * self.RP
        if self.pressure > self.peep_valve:
            flow = flow - torch.clamp(Solenoid(u_out), 0, 2) * 0.05 * self.pressure

        # update by flow rate
        self.volume = self.volume + flow * dt

        # simulate leakage
        if self.leak:
            RC = 5
            s = dt / (RC + dt)
            self.volume = self.volume + s * (self.min_volume - self.volume)

        # compute and record state
        self.compute_aux_states()
        self.volumes.append(self.volume)
        self.pressures.append(self.pressure)
