import os
import torch

from deluca.lung.hal import Hal
from deluca.lung.controllers.core import Controller
from deluca.lung.controllers.core import ControllerRegistry
from deluca.lung.environments.core import Environment
from deluca.lung.environments.core import EnvironmentRegistry
from deluca.lung.utils import BreathWaveform
from deluca.lung.utils.experiment import experiment

ROOT = os.path.dirname(os.path.realpath(os.path.join(__file__, "..")))

# NOTE: We set this here for convenience, but should think of a better way to
# do this
torch.manual_seed(0)

torch.set_default_dtype(torch.float64)

__all__ = [
    "Hal",
    "Controller",
    "ControllerRegistry",
    "Environment",
    "EnvironmentRegistry",
    "BreathWaveform",
    "experiment",
]
