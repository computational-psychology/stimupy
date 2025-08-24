
triangle
========


.. image:: /_static/generated_stimuli/components.shapes.triangle.png
   :alt: triangle stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/triangle.html>`__





.. py:function:: stimupy.components.shapes.triangle(visual_size=None, ppd=None, shape=None, triangle_size=None, intensity_triangle=1.0, intensity_background=0.0, include_corners=True, rotation=0.0)


   Draw a triangle

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param triangle_size: triangle size [height width], in degrees visual angle
   :type triangle_size: Number, Sequence[Number, Number]
   :param intensity_triangle: intensity value for triangle, by default 1.0
   :type intensity_triangle: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "triangle_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 