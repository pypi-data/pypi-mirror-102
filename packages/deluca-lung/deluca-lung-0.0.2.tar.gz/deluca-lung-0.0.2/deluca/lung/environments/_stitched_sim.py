import numpy as np
import torch
from copy import deepcopy

from deluca.lung.environments.core import Environment
from deluca.lung.utils.core import TorchStandardScaler


class StitchedSim(Environment):
    def __init__(self, inspiratory_model, u_window, p_window, u_scaler, p_scaler, to_round=False):
        super().__init__()

        self.inspiratory_model = inspiratory_model

        self.u_window = u_window
        self.p_window = p_window

        self.u_scaler = TorchStandardScaler(u_scaler)
        self.p_scaler = TorchStandardScaler(p_scaler)

        self.to_round = to_round

        self.reset()

    def reset(self):
        self.scaled_peep = self.tensor(self.inspiratory_model.boundary_dict["0"]().item())
        self.state = {"t_in": 0, "u_history": [], "p_history": [self.scaled_peep]}
        self.sync_unscaled_pressure()

    def set_current_pressure(self, pressure):
        self.state["p_history"][-1] = self.p_scaler.transform(pressure.detach().clone()).squeeze()
        self.sync_unscaled_pressure()

    def sync_unscaled_pressure(self):
        self.pressure = self.p_scaler.inverse_transform(self.state["p_history"][-1]).squeeze()

    def copy_state(self, state):
        new_state = {}
        new_state["t_in"] = state["t_in"]
        new_state["u_history"] = [u.detach().clone() for u in state["u_history"]]
        new_state["p_history"] = [u.detach().clone() for u in state["p_history"]]
        return new_state

    def cache_state(self, return_state=False):
        # set up a snapshot for rewind_state
        state_copy = self.copy_state(self.state)
        if return_state:
            return state_copy
        else:
            self.cached_state = state_copy

    def rewind_state(self, state=None):
        # load a history state cached by cache_state
        if state:
            self.state = self.copy_state(state)
        else:
            self.state = self.copy_state(self.cached_state)
        self.sync_unscaled_pressure()

    def forward(self, u_in, u_out, t):

        if u_out == 1:
            if self.state["t_in"] > 0:  # reset once per u_out=1
                self.state = {"t_in": 0, "u_history": [], "p_history": [self.scaled_peep]}
                self.sync_unscaled_pressure()

        else:
            if self.to_round:
                u_in_scaled = self.u_scaler.transform(torch.round(u_in)).squeeze()
            else:
                u_in_scaled = self.u_scaler.transform(u_in).squeeze()

            self.state["u_history"].append(u_in_scaled)

            self.state["t_in"] += 1
            t_key = str(self.state["t_in"])

            if t_key in self.inspiratory_model.boundary_dict:  # predict from boundary model
                features = torch.cat(
                    [
                        torch.stack(self.state["u_history"]),
                        torch.stack(self.state["p_history"]),
                    ]
                )
                scaled_pressure = self.inspiratory_model.boundary_dict[t_key](features)
            else:  # predict from default model
                features = torch.cat(
                    [
                        torch.stack(self.state["u_history"][-self.u_window :]),
                        torch.stack(self.state["p_history"][-self.p_window :]),
                    ]
                )
                scaled_pressure = self.inspiratory_model.default_model(features)

            self.state["p_history"].append(scaled_pressure.squeeze())
            self.sync_unscaled_pressure()
