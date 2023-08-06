import numpy as np
import tqdm

from deluca.lungollers import PID
from deluca.lungonments import PhysicalLung
from deluca.lung import Analyzer, BreathWaveform

from deluca.lungimental.core import run_calibration

DEFAULT_VALUES = np.concatenate((np.linspace(0, 0.9, 10), np.linspace(1, 10, 10)))


def pid_grid(
    Ps=DEFAULT_VALUES,
    Is=DEFAULT_VALUES,
    Ds=[0.0],
    PIPs=[10, 15, 20, 25, 30, 35],
    R=50,
    C=10,
    PEEP=5,
    abort=60,
    T=300,
    directory=None,
    vent=None,
    **kwargs,
):
    analyzers = []
    vent = vent or PhysicalLung()

    print("Running calibration")
    run_calibration(R, C, PEEP, directory)

    print("Running grid")
    for PIP in tqdm.tqdm(PIPs):
        for P in tqdm.tqdm(Ps, leave=False):
            for I in tqdm.tqdm(Is, leave=False):
                for D in tqdm.tqdm(Ds, leave=False):
                    vent.reset()

                    waveform = BreathWaveform((PEEP, PIP))
                    pid = PID(K=[P, I, D], waveform=waveform)
                    analyzer = vent.run(
                        pid,
                        R=R,
                        C=C,
                        PEEP=PEEP,
                        abort=abort,
                        directory=directory,
                        T=T,
                        use_tqdm=False,
                        **kwargs,
                    )
                    analyzers.append(analyzer)

    print("Running calibration")
    run_calibration(R, C, PEEP, directory)

    return analyzers
