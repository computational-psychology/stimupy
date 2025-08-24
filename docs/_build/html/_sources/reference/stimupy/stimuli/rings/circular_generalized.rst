
circular_generalized
====================


.. image:: /_static/generated_stimuli/stimuli.rings.circular_generalized.png
   :alt: circular_generalized stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/rings/circular_generalized.html>`__





.. py:function:: stimupy.stimuli.rings.circular_generalized(visual_size=None, ppd=None, shape=None, radii=None, intensity_rings=(0.0, 1.0), intensity_background=0.5, target_indices=(), intensity_target=0.5, origin='mean')


   Sequential set of circular rings with specified radii and targets

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radii: radii of each ring, in degrees visual angle
   :type radii: Sequence[Number] or None (default)
   :param intensity_rings: intensities of rings, by default (1.0, 0.0)
   :type intensity_rings: Sequence[float, float]
   :param intensity_background: intensity value of background, by default 0.5
   :type intensity_background: float (optional)
   :param target_indices: indices rings where targets will be placed
   :type target_indices: int, or Sequence[int, ...]
   :param intensity_target: intensity value for each target, by default 0.5.
                            Can specify as many intensities as number of target_indices;
                            If fewer intensities are passed than target_indices, cycles through intensities
   :type intensity_target: float, or Sequence[float, ...], optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each ring (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 