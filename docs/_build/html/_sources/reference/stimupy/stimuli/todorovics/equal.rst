
equal
=====


.. image:: /_static/generated_stimuli/stimuli.todorovics.equal.png
   :alt: equal stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/todorovics/equal.html>`__





.. py:function:: stimupy.stimuli.todorovics.equal(visual_size=None, ppd=None, shape=None, cross_size=None, cross_thickness=None, cover_size=None, intensity_background=0.0, intensity_target=0.5, intensity_covers=1.0)


   Cross target and four rectangular covers added at inner cross corners

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param cross_size: size of target cross in visual angle
   :type cross_size: float or (float, float)
   :param cross_thickness: thickness of target cross in visual angle
   :type cross_thickness: float or (float, float)
   :param cover_size: size of covers in visual angle
   :type cover_size: float or (float, float)
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_target: intensity value for target
   :type intensity_target: float
   :param intensity_covers: intensity value for covers
   :type intensity_covers: float

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




 