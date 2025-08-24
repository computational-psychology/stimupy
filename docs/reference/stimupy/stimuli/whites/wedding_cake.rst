
wedding_cake
============


.. image:: /_static/generated_stimuli/stimuli.whites.wedding_cake.png
   :alt: wedding_cake stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/whites/wedding_cake.html>`__





.. py:function:: stimupy.stimuli.whites.wedding_cake(visual_size=None, ppd=None, shape=None, L_size=None, target_height=None, target_indices1=None, target_indices2=None, intensity_bars=(0.0, 1.0), intensity_target=0.5)


   Wedding cake stimulus

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param L_size: size of individual jags (height, width, thickness) in degree visual angle
   :type L_size: (float, float, float)
   :param target_height: height of targets in degree visual angle
   :type target_height: float
   :param target_indices1: target indices with intensity1-value; as many tuples as there are targets
                           each with (y, x) indices
   :type target_indices1: nested tuples
   :param target_indices2: target indices with intensity2-value; as many tuples as there are targets
                           each with (y, x) indices
   :type target_indices2: nested tuples
   :param intensity_bars: intensity values of the bars
   :type intensity_bars: (float, float)
   :param intensity_target: intensity value of targets
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Clifford, C. W. G., & Spehar, B. (2003).
       Using colour to disambiguate contrast and assimilation in White's effect.
       Journal of Vision, 3, 294a.
       https://doi.org/10.1167/3.9.294




 