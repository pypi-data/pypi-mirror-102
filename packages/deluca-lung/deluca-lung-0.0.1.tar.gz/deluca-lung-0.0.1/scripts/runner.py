import sys
import torch
import click
import datetime
import time
import numpy as np
import re
import os
import logging

from venti.controllers.core import Controller
from venti.utils import Analyzer
from venti.utils import BreathWaveform
from venti.experimental import run_controller
from venti.experimental.core import run_calibration
from venti.experimental.core import save_data_and_plot


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

pattern = re.compile(".+R(\d+)_C(\d+)_PEEP(\d+).*")
RUNDIR = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs"))


def runner(run, r, c, peep, t, dt, abort, calibrate):
    log.info(locals())
    waveforms = [BreathWaveform((peep, pip)) for pip in [10, 15, 20, 25, 30, 35]]

    try:
        # If we specify R, C, and PEEP and they don't match the current lung
        # settings, skip
        match = pattern.match(run)
        if match is not None and not np.all(
            [int(setting) for setting in match.groups()] == [r, c, peep]
        ):
            log.info(
                f"Skipping {run}; wrong lung settings (found {match.groups()}, expecting ({r}, {c}, {peep}))"
            )
            sys.exit(1)

        controller_path = os.path.join(run, "controller.pkl")
        controller = Controller.load(controller_path)
        controller(torch.tensor(0.0), 0)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        run_name = os.path.basename(run.replace("./", ""))

        if calibrate:
            run_calibration(r, c, peep, run, name="calib1")

        link = f"https://github.com/MinRegret/venti/tree/main/runs/completed/{run_name}"

        results = []
        plots = []
        for waveform in waveforms:
            name = f"result_{str(int(np.max(waveform.fp)))}"

            result = run_controller(
                controller_path,
                r,
                c,
                peep,
                waveform,
                t,
                dt,
                abort,
                name=name,
            )

            results.append(result)
            plots.append(f"### {name}\n![{name}]({name}.png)")

        if calibrate:
            run_calibration(r, c, peep, run, name="calib2")

        with open(os.path.join(RUNDIR, "report.md"), "r") as f:
            report = f.read().format(**{"title": run_name, "plots": "\n".join(plots)})

        with open(os.path.join(run, "README.md"), "w") as f:
            f.write(report)

        row = [f"[{run_name}]({link})"]
        total_loss = 0
        for result in results:
            analyzer = Analyzer(result)
            loss = analyzer.default_metric()
            row.append(f"{loss:.2f}")
            total_loss += loss
        row.append(f"{total_loss / len(results):.2f}")
        row.extend([str(x) for x in [r, c, peep, timestamp]])
        row = f"|{'|'.join(row)}|\n"

        with open(os.path.join(RUNDIR, "README.md"), "a") as f:
            f.write(row)

    except Exception as e:
        log.error(e)
        sys.exit(2)


@click.command()
@click.argument("run", type=click.Path(exists=True))
@click.option("-R", type=int, default=50, help="R value for phsyical lung")
@click.option("-C", type=int, default=10, help="C value for phsyical lung")
@click.option("--PEEP", type=int, default=5, help="PEEP")
@click.option("-T", type=int, default=600, help="Default timesteps")
@click.option("--dt", type=float, default=0.03, help="Time to wait")
@click.option("--abort", type=float, default=60, help="Abort pressure")
@click.option("--calibrate/--no-calibrate", default=True, help="Run calibration routine?")
@click.option("--sleep", type=int, default=60, help="Default time to sleep before trying again")
def _runner(run, r, c, peep, t, dt, abort, calibrate, sleep):
    runner(run, r, c, peep, t, dt, abort, calibrate)


if __name__ == "__main__":
    _runner()
