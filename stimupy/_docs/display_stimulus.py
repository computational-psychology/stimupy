import matplotlib.pyplot as plt
import panel as pn
import param
from stimupy.utils import plot_stim

pn.extension()


class InteractiveStimDisplay:
    def __init__(self, stim_func, stim_params):
        self.params = stim_params
        self.stim_func = stim_func

        self.param_panel = pn.Param(self.params, width=300, show_name=False, margin=(10, 10))

        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.fig.patch.set_facecolor("white")

        self.plot_pane = pn.pane.Matplotlib(self.fig, width=400, height=400, margin=(10, 10))

        self.params.param.watch(self.update_plot, list(self.params.param.values().keys()))
        self.update_plot()
        self.layout = pn.Row(self.param_panel, self.plot_pane)

    def update_plot(self, *args):
        stim_params = self.params.get_stimulus_params()
        try:
            stim = self.stim_func(**stim_params)

            self.ax.clear()
            plot_stim(stim, ax=self.ax, stim_name=None)

        except Exception as e:
            self.ax.clear()
            self.ax.text(
                0.5,
                0.5,
                f"Error: {str(e)}",
                ha="center",
                va="center",
                transform=self.ax.transAxes,
                fontsize=12,
                color="red",
            )

        self.plot_pane.param.trigger("object")
