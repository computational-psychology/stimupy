
anderson
========


.. image:: /_static/generated_stimuli/stimuli.whites.anderson.png
   :alt: anderson stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/whites/anderson.html>`__





.. py:function:: stimupy.stimuli.whites.anderson(visual_size=None, ppd=None, shape=None, frequency=None, n_bars=None, bar_width=None, period='ignore', intensity_bars=(0.0, 1.0), intensity_target=0.5, target_indices_top=None, target_indices_bottom=None, target_center_offset=0, target_height=None, intensity_stripes=(0.0, 1.0), stripe_center_offset=0, stripe_height=None, round_phase_width=True)


   Anderson variation of White's stimulus

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
   :param intensity_bars: intensity values of bars
   :type intensity_bars: (float, float)
   :param intensity_target: intensity value of target
   :type intensity_target: float
   :param target_indices_top: bar indices where top target(s) will be placed. As many targets as ints.
   :type target_indices_top: int or tuple of ints
   :param target_indices_bottom: bar indices where bottom target(s) will be placed. As many targets as ints.
   :type target_indices_bottom: int or tuple of ints
   :param target_center_offset: offset from target centers to image center in degree visual angle.
   :type target_center_offset: float
   :param target_height: height of targets in degrees visual angle
   :type target_height: float, or Sequence[float, ...]
   :param intensity_stripes: intensity values of horizontal stripes
   :type intensity_stripes: (float, float)
   :param stripe_center_offset: offset from stripe centers to image center in degree visual angle.
   :type stripe_center_offset: float
   :param stripe_height = float: stripe height in degrees visual angle
   :param round_phase_width: if True (default), round phase width of grating
   :type round_phase_width: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Anderson, B. L. (2001).
       Contrasting theories of White's illusion.
       Perception, 30, 1499-1501.
   Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
       Oriented multiscale spatial ﬁltering and contrast normalization:
       a parsimonious model of brightness induction in a continuum
       of stimuli including White, Howe and simultaneous brightness contrast.
       Vision Research, 45, 607-615.




 