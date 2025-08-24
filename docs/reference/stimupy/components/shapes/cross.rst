
cross
=====


.. image:: /_static/generated_stimuli/components.shapes.cross.png
   :alt: cross stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/cross.html>`__





.. py:function:: stimupy.components.shapes.cross(visual_size=None, ppd=None, shape=None, cross_size=None, cross_thickness=None, cross_arm_ratios=(1.0, 1.0), intensity_cross=1.0, intensity_background=0.0, rotation=0.0)


   Draw a cross

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param cross_size: cross size [height, width], in degrees visual angle
   :type cross_size: Number, Sequence[Number, Number]
   :param cross_thickness: thickness of cross in degrees visual angle
   :type cross_thickness: Number, Sequence[Number, Number]
   :param cross_arm_ratios: ratio used to create arms (up-down, left-right)
   :type cross_arm_ratios: float or (float, float)
   :param intensity_cross: intensity value for cross, by default 1.0
   :type intensity_cross: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "cross_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 