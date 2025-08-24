
parallelogram
=============


.. image:: /_static/generated_stimuli/components.shapes.parallelogram.png
   :alt: parallelogram stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/parallelogram.html>`__





.. py:function:: stimupy.components.shapes.parallelogram(visual_size=None, ppd=None, shape=None, parallelogram_size=None, intensity_parallelogram=1.0, intensity_background=0.0, rotation=0.0)


   Draw a parallelogram

   :param visual_size: visual size [height, width] of image, in degrees visual angle
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param parallelogram_size: parallelogram size [height, width, depth], in degrees visual angle
   :type parallelogram_size: [Number, Number, Number], [Number, Number], Number or None (default)
   :param intensity_parallelogram: intensity value for parallelogram, by default 1.0
   :type intensity_parallelogram: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the shape (key: "parallelogram_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 