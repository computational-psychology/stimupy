
with_dots
=========


.. image:: /_static/generated_stimuli/stimuli.sbcs.with_dots.png
   :alt: with_dots stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/sbcs/with_dots.html>`__





.. py:function:: stimupy.stimuli.sbcs.with_dots(visual_size=None, ppd=None, shape=None, n_dots=None, dot_radius=None, distance=None, target_shape=None, intensity_background=0.0, intensity_dots=1.0, intensity_target=0.5)


   Simultaneous contrast stimulus with dots

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param n_dots: stimulus size defined as the number of dots in y and x-directions
   :type n_dots: int or (int, int)
   :param dot_radius: radius of dots
   :type dot_radius: float
   :param distance: distance between dots in degree visual angle
   :type distance: float
   :param target_shape: target shape defined as the number of dots that fit into the target
   :type target_shape: int or (int, int)
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_dots: intensity value for dots
   :type intensity_dots: float
   :param intensity_target: intensity value for target
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Bressan, P., & Kramer, P. (2008).
       Gating of remote effects on lightness.
       Journal of Vision, 8(2), 16-16.
       https://doi.org/10.1167/8.2.16




 