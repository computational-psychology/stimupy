
gabor
=====


.. image:: /_static/generated_stimuli/stimuli.gabors.gabor.png
   :alt: gabor stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/gabors/gabor.html>`__





.. py:function:: stimupy.stimuli.gabors.gabor(visual_size=None, ppd=None, shape=None, frequency=None, n_bars=None, bar_width=None, period='ignore', rotation=0.0, phase_shift=0, intensities=(0.0, 1.0), origin='center', round_phase_width=False, sigma=None)


   Draw a Gabor: a sinewave grating in a Gaussian envelope

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of grating, in cycles per degree visual angle
   :type frequency: Number, or None (default)
   :param n_bars: number of bars in the grating
   :type n_bars: Number, or None (default)
   :param bar_width: width of a single bar, in degrees visual angle
   :type bar_width: Number, or None (default)
   :param sigma: sigma of Gaussian in degree visual angle (y, x)
   :type sigma: float or (float, float)
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either" or "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
   :param intensities: maximal intensity value for each bar, by default (0.0, 1.0).
   :type intensities: Sequence[float, ...]
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each bar (key: "grating_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 