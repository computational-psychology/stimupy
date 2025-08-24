
staircase_rectilinear
=====================


.. image:: /_static/generated_stimuli/stimuli.waves.staircase_rectilinear.png
   :alt: staircase_rectilinear stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/waves/staircase_rectilinear.html>`__





.. py:function:: stimupy.stimuli.waves.staircase_rectilinear(visual_size=None, ppd=None, shape=None, frequency=None, n_frames=None, frame_width=None, period='ignore', rotation=0.0, phase_shift=0, intensity_frames=(0.0, 1.0), target_indices=(), intensity_target=0.5, origin='mean', round_phase_width=True, clip=False, intensity_background=0.5)


   Rectilinear staircase, with some frame(s) as target(s)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of grating, in cycles per degree visual angle
   :type frequency: Number, or None (default)
   :param n_frames: number of frames in the grating
   :type n_frames: int, or None (default)
   :param frame_width: width of a single frame, in degrees visual angle
   :type frame_width: Number, or None (default)
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either" or "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
   :param intensity_frames: if len(intensity_frames)==2, intensity range of staircase (default 0.0, 1.0);
                            if len(intensity_frames)>2, intensity value for each frame.
                            Can specify as many intensity_frames as n_frames.
                            If fewer intensity_frames are passed than n_frames, cycles through intensities.
   :type intensity_frames: Sequence[float, ...]
   :param target_indices: indices segments where targets will be placed
   :type target_indices: int, or Sequence[int, ...]
   :param intensity_target: intensity value for each target, by default 0.5.
                            Can specify as many intensities as number of target_indices;
                            If fewer intensities are passed than target_indices, cycles through intensities
   :type intensity_target: float, or Sequence[float, ...], optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"
   :param round_phase_width: if True, round width of frames given resolution
   :type round_phase_width: Bool
   :param clip: if True, clip stimulus to image size (default: False)
   :type clip: Bool
   :param intensity_background: intensity value of background (if clipped), by default 0.5
   :type intensity_background: float (optional)

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 