
grating_induction
=================


.. image:: /_static/generated_stimuli/stimuli.gratings.grating_induction.png
   :alt: grating_induction stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/gratings/grating_induction.html>`__





.. py:function:: stimupy.stimuli.gratings.grating_induction(visual_size=None, ppd=None, shape=None, frequency=None, n_bars=None, bar_width=None, period='ignore', rotation=0.0, phase_shift=0, intensities=(0.0, 1.0), target_width=None, intensity_target=0.5, origin='corner')


   Grating induction illusion using a sinewave grating

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of grating, in cycles per degree visual angle
   :type frequency: Number, or None (default)
   :param n_bars: number of bars in the grating
   :type n_bars: int, or None (default)
   :param bar_width: width of a single bar, in degrees visual angle
   :type bar_width: Number, or None (default)
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either" or "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
   :param intensity_bars: intensity value for each bar, by default (1.0, 0.0).
                          Can specify as many intensities as n_bars;
                          If fewer intensities are passed than n_bars, cycles through intensities
   :type intensity_bars: Sequence[float, ...]
   :param target_width: width of target stripe in degrees visual angle
   :type target_width: float
   :param intensities: min and max intensity of sinewave
   :type intensities: Sequence[float, float] or None (default)
   :param origin: if "corner": set origin to upper left corner (default)
                  if "mean": set origin to hypothetical image center
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   McCourt, M. E. (1982).
       A spatial frequency dependent grating-induction effect.
       Vision Research, 22, 119-134.
       https://doi.org/10.1016/0042-6989(82)90173-0




 