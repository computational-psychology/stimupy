
dipole
======


.. image:: /_static/generated_stimuli/components.lines.dipole.png
   :alt: dipole stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/lines/dipole.html>`__





.. py:function:: stimupy.components.lines.dipole(visual_size=None, ppd=None, shape=None, line_length=None, line_width=0, line_gap=None, rotation=0.0, intensity_lines=(0.0, 1.0))


   Draw a two centered parallel lines

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param line_length: length of the line, in degrees visual angle
   :type line_length: Number
   :param line_width: width of the line, in degrees visual angle;
                      if line_width=0 (default), line will be one pixel wide
   :type line_width: Number
   :param line_gap: distance between line centers, in degrees visual angle
   :type line_gap: Number
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_lines: intensity value of the line (default: (0, 1));
                           background intensity is the mean of these two values
   :type intensity_lines: (Number, Number)

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each line (key: "line_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 