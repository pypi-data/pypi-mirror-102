import os
import numpy as np
import matplotlib
import dill as pickle
import matplotlib.pyplot as plt

from deluca.lung.utils import BreathWaveform


class Analyzer:
    def __init__(self, path):
        self.data = path if isinstance(path, dict) else pickle.load(open(path, "rb"))
        self.controller = self.data["controller"]
        timeseries = self.data["timeseries"]
        self.tt = timeseries["timestamp"]
        self.u_in = timeseries["u_in"]
        self.u_out = timeseries["u_out"]
        self.pressure = timeseries["pressure"]
        self.target = timeseries["target"]
        self.flow = timeseries["flow"]

    ###########################################################################
    # Plotting methods
    ###########################################################################

    def plot(
        self,
        title=None,
        axes=None,
        figsize=None,
        xlim=None,
        ylim=[0, 60],
        legend=False,
        control=True,
        **kwargs
    ):
        matplotlib.pyplot.figure(figsize=(figsize or (12, 6)))
        # trash
        if axes is None:
            axes = matplotlib.pyplot.axes()

        if xlim is not None:
            axes.set_xlim(xlim)

        axes.set_xlabel("Time (s)")
        plts = []
        (pressure,) = axes.plot(
            self.tt, self.pressure, color="blue", label="actual pressure", **kwargs
        )
        (target,) = axes.plot(
            self.tt, self.target, color="orange", label="target pressure", **kwargs
        )
        axes.set_ylabel("Pressure (cmH2O)")
        axes.set_ylim(ylim)
        expiratory = axes.fill_between(
            self.tt,
            axes.get_ylim()[0],
            axes.get_ylim()[1],
            where=self.u_out.astype(bool),
            color="dimgray",
            alpha=0.3,
            label="expiratory",
        )
        inspiratory = axes.fill_between(
            self.tt,
            axes.get_ylim()[0],
            axes.get_ylim()[1],
            where=np.logical_not(self.u_out.astype(bool)),
            color="lightgray",
            alpha=0.3,
            label="inspiratory",
        )
        plts.extend([pressure, target, inspiratory, expiratory])

        if control:
            twin_ax = axes.twinx()
            twin_ax.set_ylim([-2, 102])
            (u_in,) = twin_ax.plot(
                self.tt, np.clip(self.u_in, 0, 100), c="gray", label="u_in", **kwargs
            )
            twin_ax.set_ylabel("Control")
            plts.append(u_in)

        if title is not None:
            plt.title(title)

        if legend:
            labels = [p.get_label() for p in plts]
            plt.legend(
                plts,
                labels,
                bbox_to_anchor=(-.05, 1.02, 1.1, 0.05),
                mode="expand",
                ncol=4,
                loc="lower left",
            )

    def plot_inspiratory_clips(self, **kwargs):
        inspiratory_clips = self.infer_inspiratory_phases()

        plt.subplot(121)
        plt.title("u_in")
        for start, end in inspiratory_clips:
            u_in = self.u_in[start:end]
            plt.plot(self.tt[start:end] - self.tt[start], u_in, "k", alpha=0.1)

        plt.subplot(122)
        plt.title("pressure")
        for start, end in inspiratory_clips:
            pressure = self.pressure[start:end]
            plt.plot(self.tt[start:end] - self.tt[start], pressure, "b", alpha=0.1)

    ###########################################################################
    # Utility methods
    ###########################################################################

    def infer_inspiratory_phases(self, use_cached=True):
        # finds inspiratory phase intervals from expiratory valve controls
        # returns list of endpoints so that u_out[lo:hi] == 1

        if not use_cached or not hasattr(self, "cached_inspiratory_phases"):
            d_u_out = np.diff(self.u_out, prepend=1)

            starts = np.where(d_u_out == -1)[0]
            ends = np.where(d_u_out == 1)[0]

            self.cached_inspiratory_phases = list(zip(starts, ends))

        return self.cached_inspiratory_phases

    ###########################################################################
    # Metric methods
    ###########################################################################

    def losses_per_breath(self, target, loss_fn=None):
        # computes trapezoidally integrated loss per inferred breath

        loss_fn = loss_fn or np.square

        # handle polymorphic targets
        if isinstance(target, int):
            target_fn = lambda _: target
        elif isinstance(target, BreathWaveform):
            target_fn = lambda t: target.at(t)
        else:
            raise ValueError("unrecognized type for target")

        breaths = self.infer_inspiratory_phases()
        losses = []

        # integrate loss for each detected inspiratory phase
        for start, end in breaths:
            errs = loss_fn(target_fn(self.tt[start:end]) - self.pressure[start:end])
            loss = np.trapz(errs, self.tt[start:end])
            losses.append(loss)

        return np.array(losses)

    def default_metric(self, target=None, loss_fn=np.abs):
        # I suggest keeping a separate function for default settings
        # so nobody has to change code if we change the benchmark
        # as it stands: average loss across breaths, discounting first breath
        target = target or self.controller.waveform

        return self.losses_per_breath(target, loss_fn)[1:].mean()
