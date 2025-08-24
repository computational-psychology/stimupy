
line
====


.. image:: /_static/generated_stimuli/components.lines.line.png
   :alt: line stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/lines/line.html>`__





.. py:function:: stimupy.components.lines.line(visual_size=None, ppd=None, shape=None, line_position=None, line_length=None, line_width=0, rotation=0.0, intensity_line=1.0, intensity_background=0.0, origin='corner')


   Draw a line

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param line_position: line position (y, x) given the chosen origin;
                         if None (default), the lines will go through the image center
   :type line_position: Sequence[Number, Number], Number, or None (default)
   :param line_length: length of the line, in degrees visual angle
   :type line_length: Number
   :param line_width: width of the line, in degrees visual angle;
                      if line_width=0 (default), line will be one pixel wide
   :type line_width: Number
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_line: intensity value of the line (default: 1)
   :type intensity_line: Number
   :param intensity_background: intensity value of the background (default: 0)
   :type intensity_background: Number
   :param origin: if "corner": set origin to upper left corner (default)
                  if "mean" or "center": set origin to center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each line (key: "line_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 