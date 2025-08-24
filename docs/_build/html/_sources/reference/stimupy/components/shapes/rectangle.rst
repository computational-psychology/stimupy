
rectangle
=========


.. image:: /_static/generated_stimuli/components.shapes.rectangle.png
   :alt: rectangle stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/rectangle.html>`__





.. py:function:: stimupy.components.shapes.rectangle(visual_size=None, ppd=None, shape=None, rectangle_size=None, rectangle_position=None, intensity_rectangle=1.0, intensity_background=0.0, rotation=0.0)


   Draw a rectangle

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param rectangle_size: rectangle size [height, width], in degrees visual angle
   :type rectangle_size: Number, Sequence[Number, Number]
   :param rectangle_position: position of the rectangle, in degrees visual angle.
                              If None, rectangle will be placed in center of image.
   :type rectangle_position: Number, Sequence[Number, Number], or None (default)
   :param intensity_rectangle: intensity value for rectangle, by default 1.0
   :type intensity_rectangle: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "rectangle_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 