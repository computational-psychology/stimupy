
segments
========


.. image:: /_static/generated_stimuli/components.angulars.segments.png
   :alt: segments stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/angulars/segments.html>`__





.. py:function:: stimupy.components.angulars.segments(visual_size=None, ppd=None, shape=None, angles=None, rotation=0.0, intensity_background=0.5, intensity_segments=(0.0, 1.0), origin='mean')


   Generate mask with integer indices for sequential angular segments

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param angles: upper-limit of each segment, in angular degrees 0-360
   :type angles: Sequence[Number] or None (default)
   :param rotation: rotation (in degrees) from 3 o'clock, counterclockwise, by default 0.0
   :type rotation: float, optional
   :param intensity_background: intensity value for background; default is 0.5.
   :type intensity_background: Number
   :param intensity_segments: intensity value for each segment, from inside to out.
                              If fewer intensities are passed than number of radii, cycles through intensity_segments
   :type intensity_segments: Sequence[Number, ...]
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)angles
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each segment (key: "segment_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 