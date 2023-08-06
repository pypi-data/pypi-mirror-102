import torch
from deluca.lung.controllers.core import Controller


# generic PID controller
class PID(Controller):
    def __init__(self, K=[3, 4, 0], RC=0.5, trainable=False, **kwargs):
        self.init_K = self.tensor(K)

        self.K = self.init_K if not trainable else torch.nn.Parameter(self.init_K)
        self.RC = RC

        self.reset()

    def reset(self):
        self.coef = self.tensor([0.0, 0.0, 0.0])

    @property
    def P(self):
        return self.coef[0]

    @property
    def I(self):
        return self.coef[1]

    @property
    def D(self):
        return self.coef[2]

    def compute_action(self, state, t):
        err = torch.tensor(self.waveform.at(t)) - state
        dt = self.dt(t)
        decay = dt / (dt + self.RC)

        self.coef = self.coef + self.tensor(
            [
                err - self.P,
                decay * (err - self.I),
                decay * (err - self.P - self.D),
            ]
        )

        u_in = torch.clamp(torch.dot(self.K, self.coef), min=0.0, max=100.0)

        return (u_in, self.u_out(t))
