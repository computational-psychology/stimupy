
cross_rectangles
================


.. image:: /_static/generated_stimuli/stimuli.benarys.cross_rectangles.png
   :alt: cross_rectangles stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/benarys/cross_rectangles.html>`__





.. py:function:: stimupy.stimuli.benarys.cross_rectangles(visual_size=None, ppd=None, shape=None, cross_thickness=None, target_size=None, intensity_background=1.0, intensity_cross=0.0, intensity_target=0.5)


   Benary's Cross stimulus with two rectangular targets with default placement

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param cross_thickness: width of the cross bars in degrees visual angle
   :type cross_thickness: float
   :param target_size: size of all target(s) in degrees visual angle
   :type target_size: (float, float)
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_cross: intensity value for cross
   :type intensity_cross: float
   :param intensity_target: intensity value for target
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Benary, W. (1924).
       Beobachtungen zu einem Experiment über Helligkeitskontrast.
       Psychologische Forschung, 5, 131-142.
       https://doi.org/10.1007/BF00402398




 