
frames
======


.. image:: /_static/generated_stimuli/components.frames.frames.png
   :alt: frames stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/frames/frames.html>`__





.. py:function:: stimupy.components.frames.frames(visual_size=None, ppd=None, shape=None, radii=None, rotation=0.0, intensity_frames=(0.0, 1.0), intensity_background=0.5, origin='mean')


   Draw sequential set of square frames with specified radii

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radii: radii of each frame, in degrees visual angle
   :type radii: Sequence[Number]
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_frames: intensity value for each frame, by default (1.0, 0.0).
                            Can specify as many intensities as number of frame_widths;
                            If fewer intensities are passed than frame_widhts, cycles through intensities
   :type intensity_frames: Sequence[float, ...], optional
   :param intensity_background: intensity value of background, by default 0.5
   :type intensity_background: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center", optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each frame (key: "frame_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 