
square
======


.. image:: /_static/generated_stimuli/stimuli.sbcs.square.png
   :alt: square stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/sbcs/square.html>`__





.. py:function:: stimupy.stimuli.sbcs.square(target_radius, visual_size=None, ppd=None, shape=None, surround_radius=None, rotation=0.0, intensity_surround=0.0, intensity_background=0.5, intensity_target=0.5, origin='mean')


   Simultaneous contrast stimulus with square target and surround field

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param target_radius: radius of target, in degrees visual angle
   :type target_radius: float
   :param surround_radius: radius of surround context field, in degrees visual angle
   :type surround_radius: float
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_surrond: intensity of surround context field, by default 0.0
   :type intensity_surrond: float, optional
   :param intensity_background: intensity value of background, by default 0.5
   :type intensity_background: float, optional
   :param intensity_target: intensity value for each target, by default 0.5.
   :type intensity_target: float, or Sequence[float, ...], optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each frame (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 