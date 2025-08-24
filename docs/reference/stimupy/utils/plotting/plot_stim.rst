
plot_stim
=========



.. py:function:: stimupy.utils.plotting.plot_stim(stim, mask=False, stim_name='stim', ax=None, vmin=0, vmax=1, save=None, units='deg', origin='mean')


   Plot a stimulus

   Plots the stimulus-array (key: "img") directly from stim dict.
   Optionally also plots mask.

   :param stim: stimulus dict containing stimulus-array (key: "img")
   :type stim: dict
   :param mask: If True, plot mask on top of stimulus image (default: False).
                If string is provided, plot this key from stimulus dictionary as mask
   :type mask: bool or str, optional
   :param stim_name: Stimulus name used for plotting (default: "stim")
   :type stim_name: str, optional
   :param ax: If not None (default), plot in the specified Axis object
   :type ax: Axis object, optional
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

   :returns: **ax** -- If ax was passed and plotting is None, returns updated Axis object.
   :rtype: Axis object




 