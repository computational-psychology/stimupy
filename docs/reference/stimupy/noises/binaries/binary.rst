
binary
======


.. image:: /_static/generated_stimuli/noises.binaries.binary.png
   :alt: binary stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/noises/binaries/binary.html>`__





.. py:function:: stimupy.noises.binaries.binary(visual_size=None, ppd=None, shape=None, intensity_range=(0, 1))


   Draw binary noise texture

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param intensity_range: minimum and maximum intensity value; default: (0, 1).
                           be aware that not every instance has mean=(max-min)/2.
   :type intensity_range: Sequence[Number, Number]

   :returns: dict with the stimulus (key: "img"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 