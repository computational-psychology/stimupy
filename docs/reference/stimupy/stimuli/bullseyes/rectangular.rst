
rectangular
===========


.. image:: /_static/generated_stimuli/stimuli.bullseyes.rectangular.png
   :alt: rectangular stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/bullseyes/rectangular.html>`__





.. py:function:: stimupy.stimuli.bullseyes.rectangular(visual_size=None, ppd=None, shape=None, frequency=None, n_frames=None, frame_width=None, rotation=0.0, phase_shift=0, intensity_frames=(0.0, 1.0), intensity_background=0.5, intensity_target=0.5, origin='mean', clip=True)


   Square "bullseye", i.e., set of rings with target in center

   Essentially frames(target_indices=1)

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
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
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
   :param clip: if True, clip stimulus to image size (default: True)
   :type clip: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Bindman, D., & Chubb, C. (2004).
       Brightness assimilation in bullseye displays.
       Vision Research, 44, 309-319.
       https://doi.org/10.1016/S0042-6989(03)00430-9




 