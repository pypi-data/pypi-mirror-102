import os
import time
import datetime
import tqdm
import dill as pickle
import torch
import glob
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import logging

from deluca.lung.core import VentObj
from deluca.lung.utils.analyzer import Analyzer
from deluca.lung.utils.munger import Munger

from deluca.lung.controllers._impulse import Impulse
from deluca.lung.controllers._predestined import Predestined
from deluca.lung.controllers._pid import PID

from deluca.lung.utils.core import BreathWaveform

EnvironmentRegistry = []

logger = logging.getLogger(__name__)


class Environment(VentObj):
    def __new__(cls, *args, **kwargs):
        obj = VentObj.__new__(cls)
        obj.__setattr__("pressure", 0)
        obj.__setattr__("flow", 0)
        obj.__setattr__("tt", 0)
        obj.__setattr__("dt", 0.03)
        obj.__setattr__("abort", 70)

        obj.kwargs(**kwargs)

        return obj

    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        if cls.__name__ not in [env.__name__ for env in EnvironmentRegistry]:
            EnvironmentRegistry.append(cls)

    # Define overrideable properties for run function. We could omit the
    # underscore, but since run is a function we won't touch and Environment
    # writers will likely want to use self.pressure as a float, we do this way
    @property
    def _pressure(self):
        return self.pressure

    @property
    def _flow(self):
        return self.flow

    @property
    def time(self):
        return self.tt * self.dt

    @property
    def is_real(self):
        return False

    def reset(self):
        self.pressure = 0
        self.flow = 0
        self.tt = 0

    def get_start_time(self):
        return 0

    def should_abort(self, pressure, flow, timestamp):
        return False

    def wait(self, duration):
        pass

    def forward(self, u_in, u_out, t):
        raise NotImplementedError()

    def run_cleanup(self):
        pass

    def run(
        self,
        controller,
        R=20,
        C=20,
        PEEP=5,
        T=3000,
        abort=None,
        sleep=None,
        directory=None,
        device="cpu",
        dt=None,
        use_tqdm=True,
    ):
        # Backwards compatibility...
        if abort is not None:
            self.abort = abort
        if dt is not None:
            self.dt = dt
        if PEEP is not None:
            self.PEEP = PEEP
        if sleep is not None:
            self.sleep = sleep

        result = {
            "controller": controller,
            "R": R,
            "C": C,
            "PEEP": self.PEEP,
            "dt": self.dt,
            "abort": self.abort,
            "T": T,
            "sleep": sleep,
            "directory": directory,
        }

        try:
            self.reset()
            controller.reset()

            self.tt = 0
            tt = range(T)

            timestamps = np.zeros(T)
            pressures = np.zeros(T)
            flows = np.zeros(T)
            u_ins = np.zeros(T)
            u_outs = np.zeros(T)

            begin = self.get_start_time()
            timestamp = begin

            pressure = 0

            if use_tqdm:
                tt = tqdm.tqdm(tt, leave=False)

            for i, t in enumerate(tt):
                pressure = self._pressure
                flow = self._flow

                prev_timestamp = timestamp
                timestamp = self.time - begin

                if self.should_abort(pressure, flow, timestamp):
                    break

                if device is not None and self.is_real:
                    pressure = torch.tensor(pressure, device=device)

                u_in, u_out = controller(pressure, timestamp)

                if device is not None and self.is_real:
                    u_in = u_in.item()
                    u_out = u_out.item()

                self(u_in, u_out, timestamp)

                timestamps[i] = timestamp
                pressures[i] = pressure
                flows[i] = flow
                u_ins[i] = u_in
                u_outs[i] = u_out

                duration = self.time - timestamp - begin
                self.wait(max(self.dt - duration, 0))

                self.tt += 1
        finally:
            self.run_cleanup()

        timeseries = {
            "timestamp": np.array(timestamps),
            "pressure": np.array(pressures),
            "flow": np.array(flows),
            "target": controller.waveform.at(timestamps),
            "u_in": np.array(u_ins),
            "u_out": np.array(u_outs),
        }

        for key, val in timeseries.items():
            timeseries[key] = val[: self.tt + 1]

        result["timeseries"] = timeseries

        if directory is not None:
            if not os.path.exists(directory):
                os.makedirs(directory)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
            pickle.dump(result, open(f"{directory}/{timestamp}.pkl", "wb"))

        return result

    def plot_impulse_responses(
        self,
        impulses=np.arange(0, 101, 10),
        zero=5,
        start=0.5,
        end=0.65,
        ylim=100,
        dt=0.03,
        T=100,
        use_tqdm=False,
        abort=70,
        **kwargs,
    ):
        analyzers = []

        for impulse in impulses:
            ir = Impulse(impulse, start, end)

            run_data = self.run(ir, dt=dt, T=T, PEEP=zero, use_tqdm=use_tqdm, abort=abort, **kwargs)
            analyzer = Analyzer(run_data)
            analyzers.append(analyzer)

        loss = 0
        colors = plt.cm.winter(np.linspace(0, 1, len(analyzers)))
        for i, analyzer in enumerate(analyzers):
            plt.plot(analyzer.tt, analyzer.pressure, color=colors[-i - 1])
            if impulses[0] == 0 and i == 0:
                loss += np.abs(analyzer.pressure - zero).mean()

        print(f"MAE for zero response: {loss}")

        plt.ylim(0, ylim)
        plt.show()

        return analyzers

    def plot_pids(self):
        plt.rc("figure", figsize=(8, 2))

        for coeff in np.linspace(0.0, 0.5, 20):
            pid = PID([coeff, 0.5 - coeff, 0], waveform=BreathWaveform((5, 35)))
            self.reset()
            result = self.run(pid, T=333, abort=100)
            analyzer = Analyzer(result)

            cmap = matplotlib.cm.get_cmap("rainbow")
            plt.plot(analyzer.tt, analyzer.pressure, "b", c=cmap(2 * coeff))
