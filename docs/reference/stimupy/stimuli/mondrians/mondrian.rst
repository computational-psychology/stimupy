
mondrian
========


.. image:: /_static/generated_stimuli/stimuli.mondrians.mondrian.png
   :alt: mondrian stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/mondrians/mondrian.html>`__





.. py:function:: stimupy.stimuli.mondrians.mondrian(visual_size=None, ppd=None, shape=None, positions=None, sizes=None, intensities=None, intensity_background=0.5)


   Draw Mondrian of given size and intensity at given position

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param positions: position (y, x) of each Mondrian in degrees visual angle
   :type positions: Sequence[tuple, ... ] or None (default)
   :param sizes: size (height, width, depth) of Mondrian parallelograms in degrees visual angle;
                 if only one number is given, squares will be drawn
   :type sizes: Sequence[tuple, ... ] or None (default)
   :param intensities: intensity values of each Mondrian, if only one number is given
                       all will have the same intensity
   :type intensities: Sequence[Number, ... ] or None (default)
   :param intensity_background: intensity value of background
   :type intensity_background: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each Mondrian (key: "mondrian_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 