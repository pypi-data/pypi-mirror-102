from deluca.lung.controllers._pid import PID
from deluca.lung.environments._physical_lung import PhysicalLung
from deluca.lung.utils.analyzer import Analyzer

import pickle
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_data_and_plot(result, directory, name):
    pickle.dump(result, open(f"{directory}/{name}.pkl", "wb"))
    Analyzer(result).plot()
    plt.savefig(f"{directory}/{name}.png")


def run_calibration(R, C, PEEP, directory, name=None, T=300):
    vent = PhysicalLung()
    pid = PID(K=[1.0, 0.0, 0.0])
    result = vent.run(
        pid, R=R, C=C, PEEP=PEEP, T=T, directory=f"{directory}/calibration", abort=60
    )

    if name is not None:
        save_data_and_plot(result, directory, name)

    return result
