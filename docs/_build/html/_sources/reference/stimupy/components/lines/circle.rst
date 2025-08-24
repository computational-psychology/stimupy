
circle
======


.. image:: /_static/generated_stimuli/components.lines.circle.png
   :alt: circle stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/lines/circle.html>`__





.. py:function:: stimupy.components.lines.circle(visual_size=None, ppd=None, shape=None, radius=None, line_width=0, intensity_line=1.0, intensity_background=0.0)


   Draw a circle given the input parameters

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radius: radius of circle in degrees visual angle
   :type radius: Number
   :param line_width: width of the line, in degrees visual angle;
                      if line_width=0 (default), line will be one pixel wide
   :type line_width: Number
   :param intensity_line: intensity value of the line (default: 1)
   :type intensity_line: Number
   :param intensity_background: intensity value of the background (default: 0)
   :type intensity_background: Number

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each line (key: "line_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 