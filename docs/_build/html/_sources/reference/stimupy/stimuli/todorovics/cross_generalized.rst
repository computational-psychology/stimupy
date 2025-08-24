
cross_generalized
=================


.. image:: /_static/generated_stimuli/stimuli.todorovics.cross_generalized.png
   :alt: cross_generalized stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/todorovics/cross_generalized.html>`__





.. py:function:: stimupy.stimuli.todorovics.cross_generalized(visual_size=None, ppd=None, shape=None, cross_size=None, cross_thickness=None, covers_size=None, covers_x=None, covers_y=None, intensity_background=0.0, intensity_target=0.5, intensity_covers=1.0)


   Cross target and rectangular covers added with flexible number of covers and flexible cover placement

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param cross_size: size of target cross in visual angle
   :type cross_size: float or (float, float)
   :param cross_thickness: thickness of target cross in visual angle
   :type cross_thickness: float
   :param covers_size: size of covers in degrees visual angle (height, width)
   :type covers_size: float or (float, float)
   :param covers_x: x coordinates of covers; as many covers as there are coordinates
   :type covers_x: tuple of floats
   :param covers_y: y coordinates of covers; as many covers as there are coordinates
   :type covers_y: tuple of floats
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_target: intensity value for target
   :type intensity_target: float
   :param intensity_covers: intensity value for covers
   :type intensity_covers: Sequence[Number, ...] or Number

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Blakeslee, B., & McCourt, M. E. (1999).
       A multiscale spatial ﬁltering account
       of the White eﬀect, simultaneous brightness contrast and grating induction.
       Vision Research, 39, 4361-4377.
   Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
       Lightness and junctions: variations on White's display.
       Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
   Todorovic, D. (1997).
       Lightness and junctions. Perception, 26, 379-395.




 