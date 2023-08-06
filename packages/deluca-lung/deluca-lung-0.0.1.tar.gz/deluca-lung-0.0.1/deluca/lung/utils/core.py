import os
import numpy as np
import torch

DEFAULT_PRESSURE_RANGE = (5.0, 35.0)
DEFAULT_KEYPOINTS = [1e-8, 1.0, 1.5, 3.0]
DEFAULT_BPM = 20


class BreathWaveform:
    """Waveform generator with shape |‾\_"""

    def __init__(self, range=None, keypoints=None, bpm=DEFAULT_BPM, kernel=None, dt=0.01):
        self.range = range
        self.lo, self.hi = range or DEFAULT_PRESSURE_RANGE
        self.fp = [self.lo, self.hi, self.hi, self.lo, self.lo]

        self.xp = np.zeros(len(self.fp))
        self.xp[1:] = np.array(keypoints or DEFAULT_KEYPOINTS)
        self.xp[-1] = 60 / bpm

        self._keypoints = self.xp

        pad = 0
        num = int(1 / dt)
        if kernel is not None:
            pad = 60 / bpm / (num - 1)
            num += len(kernel) // 2 * 2

        tt = np.linspace(-pad, 60 / bpm + pad, num)
        self.fp = self.at(tt)
        self.xp = tt

        if kernel is not None:
            self.fp = np.convolve(self.fp, kernel, mode="valid")
            self.xp = np.linspace(0, 60 / bpm, int(1 / dt))

    @property
    def keypoints(self):
        if hasattr(self, "_keypoints"):
            return self._keypoints
        else:
            return self.xp

    @property
    def period(self):
        return self.xp[-1]

    @property
    def PIP(self):
        if hasattr(self, "range"):
            return self.range[1]
        else:
            return np.max(self.fp)

    @property
    def PEEP(self):
        if hasattr(self, "range"):
            return self.range[0]
        else:
            return np.min(self.fp)

    def at(self, t):
        return np.interp(t, self.xp, self.fp, period=self.period)

    def elapsed(self, t):
        return t % self.period

    def decay(self, t):
        elapsed = self.elapsed(t)
        if elapsed < self.keypoints[2]:
            return None
        elif elapsed < self.keypoints[3]:
            return 0.0
        else:
            return 5 * (1 - np.exp(5 * (self.keypoints[3] - elapsed)))

    def phase(self, t):
        return np.searchsorted(self.keypoints, t % self.period, side="right")


class TorchStandardScaler:
    def __init__(self, scaler=None, dtype=None, device="cpu"):
        if dtype is None:
            torch.get_default_dtype()
        if scaler is not None:
            self.mean = torch.tensor(scaler.mean_, dtype=dtype, device=device)
            self.std = torch.tensor(scaler.scale_, dtype=dtype, device=device)

    def fit(self, x):
        self.mean = x.mean(0, keepdim=True)
        self.std = x.std(0, unbiased=False, keepdim=True)

    def transform(self, x):
        return (x - self.mean) / self.std

    def inverse_transform(self, x):
        return x * self.std + self.mean

    def to(self, device):
        self.mean.to(device)
        self.std.to(device)
