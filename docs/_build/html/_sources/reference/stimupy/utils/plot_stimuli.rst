
plot_stimuli
============



.. py:function:: stimupy.utils.plot_stimuli(stims, mask=False, vmin=0, vmax=1, save=None, units='deg', ncols=None, nrows=None)


   Plot multiple stimuli

   Plots the stimulus-arrays (keys: "img") directly from stim dicts.
   Arranges stimuli in a grid.
   Optionally also plots masks.

   :param stims: dictionary composed of stimulus dicts containing stimulus-array (key: "img")
   :type stims: dict of dicts
   :param mask: If True, plot mask on top of stimulus image (default: False).
                If string is provided, plot this key from stimulus dictionary as mask
   :type mask: bool or str, optional
   :param vmin: Minimal intensity value for plotting. The default is 0.
   :type vmin: float, optional
   :param vmax: Minimal intensity value for plotting. The default is 1.
   :type vmax: float, optional
   :param save: If None (default), do not save the plot.
                If string is provided, save plot under this name.
   :type save: None or str, optional
   :param units: what units to put on the axes, by default degrees visual angle ("deg").
                 If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
                 it must be the key to a tuple in stim
   :type units: "px", "deg" (default), or str
   :param ncols: number of columns in gridspec, or figure it out (default)
   :type ncols: int or None, optional
   :param nrows: number of rows in gridspec, or figure it out (default)
   :type nrows: int or None, optional




 