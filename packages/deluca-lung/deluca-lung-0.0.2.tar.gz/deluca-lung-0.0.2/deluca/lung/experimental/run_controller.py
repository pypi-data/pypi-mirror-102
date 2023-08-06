from deluca.lung.controllers.core import Controller
from deluca.lung.environments._physical_lung import PhysicalLung
from deluca.lung.utils.core import BreathWaveform
from deluca.lung.experimental.core import save_data_and_plot

import os
import click
import pickle


def run_controller(path, R, C, PEEP, waveform, T, dt, abort, name=None):
    directory = os.path.dirname(os.path.realpath(path))
    experiment = os.path.basename(directory)
    pickle.dump(locals(), open(os.path.join(directory, "meta.pkl"), "wb"))

    controller = Controller.load(path)

    if waveform is not None:
        controller.waveform = waveform
        controller.reset()

    lung = PhysicalLung()

    result = lung.run(controller, R=R, C=C, PEEP=PEEP, T=T, dt=dt, abort=abort)

    if name is not None:
        save_data_and_plot(result, directory, name)

    return result


@click.command()
@click.argument("path", type=click.Path(exists=True), required=1)
@click.option("-R", type=int, default=50, help="R value for phsyical lung")
@click.option("-C", type=int, default=10, help="C value for phsyical lung")
@click.option("--PEEP", type=int, default=5, help="PEEP")
@click.option("--waveform", type=BreathWaveform, default=None, help="Waveform")
@click.option("-T", type=int, default=1000, help="Default timesteps")
@click.option("--dt", type=float, default=0.03, help="Time to wait")
@click.option("--abort", type=float, default=60, help="Abort pressure")
def _run_controller(path, r, c, peep, waveform, t, dt, abort):
    return run_controller(path, r, c, peep, waveform, t, dt, abort)


if __name__ == "__main__":
    _run_controller()
