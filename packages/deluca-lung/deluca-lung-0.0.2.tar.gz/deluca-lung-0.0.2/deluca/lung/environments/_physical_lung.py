import time
import numpy as np
import datetime

from deluca.lung.environments.core import Environment


class PhysicalLung(Environment):
    def __init__(
        self,
        hal=None,
        sleep=3.0,
        abort=50,
        PEEP=5,
        dt_threshold=1.25,
        dt_patience=10,
        peep_threshold=0.5,
        peep_patience=10,
        peep_breaths=2,
    ):
        if hal is None:
            from deluca.lung import Hal

            hal = Hal()
        self.hal = hal
        self.sleep = sleep

        self.abort = abort
        self.PEEP = PEEP
        self.dt_threshold = dt_threshold
        self.dt_patience = dt_patience
        self.peep_threshold = peep_threshold
        self.peep_patience = peep_patience

        self.breaths = 0
        self.peep_breaths = peep_breaths

        self.reset()

    def reset(self):
        self.prev_timestamp = float("-inf")
        self.dt_window = np.ones(self.dt_patience) * self.dt
        self.pressure_window = np.ones(self.peep_patience) * self.PEEP
        self.breaths = 0

    @property
    def _pressure(self):
        return self.hal.pressure

    @property
    def time(self):
        return time.time()

    @property
    def is_real(self):
        return True

    def get_start_time(self):
        return datetime.datetime.now().timestamp()

    def should_abort(self, pressure, flow, timestamp):
        if pressure > self.abort:
            print(f"Pressure of {pressure} > {self.abort}; quitting")
            return True

        self.dt_window = np.roll(self.dt_window, 1)
        self.dt_window[0] = timestamp - max(self.dt, self.prev_timestamp)
        self.prev_timestamp = timestamp

        if np.mean(self.dt_window) > self.dt * self.dt_threshold:
            # print(
                # f"dt averaged {100 * self.dt_threshold:.1f}% higher over the last {self.dt_patience} timesteps; quitting"
            # )
            return False

        if self.breaths > self.peep_breaths:
            self.pressure_window = np.roll(self.pressure_window, 1)
            self.pressure_window[0] = pressure

        if np.mean(self.pressure_window) < self.PEEP * self.peep_threshold:
            print("Pressure drop, did you blow up?")
            return True

        return False

    def wait(self, duration):
        time.sleep(duration)

    def forward(self, u_in, u_out, t):
        if u_out == 1:
            self.breaths += 1
        self.hal.setpoint_in = u_in
        self.hal.setpoint_ex = u_out

    def run_cleanup(self):
        self.hal.setpoint_in = 0
        self.hal.setpoint_ex = 1
        time.sleep(self.sleep)
        self.hal.setpoint_ex = 0
