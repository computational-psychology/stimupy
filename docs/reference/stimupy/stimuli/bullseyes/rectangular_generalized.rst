
rectangular_generalized
=======================


.. image:: /_static/generated_stimuli/stimuli.bullseyes.rectangular_generalized.png
   :alt: rectangular_generalized stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/bullseyes/rectangular_generalized.html>`__





.. py:function:: stimupy.stimuli.bullseyes.rectangular_generalized(visual_size=None, ppd=None, shape=None, radii=None, rotation=0.0, intensity_frames=(0.0, 1.0), intensity_background=0.5, intensity_target=0.5, origin='mean')


   Draw sequential set of square frames with specified radii with central target

   :param frame_radii: radii of each frame, in degrees visual angle
   :type frame_radii: Sequence[Number]
   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radii: radii of each frame, in degrees visual angle
   :type radii: Sequence[Number] or None (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_frames: min and max intensity of square-wave, by default (0.0, 1.0)
   :type intensity_frames: Sequence[float, float]
   :param intensity_background: intensity value of background, by default 0.5
   :type intensity_background: float (optional)
   :param intensity_target: intensity value for each target, by default 0.5.
                            Can specify as many intensities as number of target_indices;
                            If fewer intensities are passed than target_indices, cycles through intensities
   :type intensity_target: float, or Sequence[float, ...], optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each frame (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 