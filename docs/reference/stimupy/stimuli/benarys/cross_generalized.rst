
cross_generalized
=================


.. image:: /_static/generated_stimuli/stimuli.benarys.cross_generalized.png
   :alt: cross_generalized stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/benarys/cross_generalized.html>`__





.. py:function:: stimupy.stimuli.benarys.cross_generalized(visual_size=None, ppd=None, shape=None, cross_thickness=None, target_size=None, target_type='r', target_rotation=0.0, target_x=None, target_y=None, intensity_background=1.0, intensity_cross=0.0, intensity_target=0.5)


   Benary's Cross Illusion

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
   :param target_type: type of targets to use; option: r (rectangle), t (triangle); as many targets as types
   :type target_type: tuple of strings
   :param target_rotation: tuple with rotation of targets in deg, counterclockwise, as many targets as rotations
   :type target_rotation: tuple of floats, or float
   :param target_x: tuple with x coordinates of targets in degrees, as many targets as coordinates
   :type target_x: tuple of floats
   :param target_y: tuple with y coordinates of targets in degrees, as many targets as coordinates
   :type target_y: tuple of floats
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




 