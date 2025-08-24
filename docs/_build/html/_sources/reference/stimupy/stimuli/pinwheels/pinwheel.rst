
pinwheel
========


.. image:: /_static/generated_stimuli/stimuli.pinwheels.pinwheel.png
   :alt: pinwheel stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/pinwheels/pinwheel.html>`__





.. py:function:: stimupy.stimuli.pinwheels.pinwheel(visual_size=None, ppd=None, shape=None, frequency=None, n_segments=None, segment_width=None, rotation=0.0, target_indices=(), target_width=None, target_center=None, intensity_segments=(0.0, 1.0), intensity_background=0.5, intensity_target=0.5, origin='mean')


   Pinwheel / radial White stimulus

   :param visual_size: The shape of the stimulus in degrees of visual angle. (y,x)
   :type visual_size: (float, float)
   :param ppd: pixels per degree (visual angle)
   :type ppd: int
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[int, int], int, or None (default)
   :param frequency: angular frequency of angular grating, in cycles per angular degree
   :type frequency: Number, or None (default)
   :param n_segments: number of segments
   :type n_segments: int, or None (default)
   :param segment_width: angular width of a single segment, in degrees
   :type segment_width: Number, or None (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional
   :param target_indices: indices segments where targets will be placed
   :type target_indices: int, or Sequence[int, ...]
   :param target_width: target width (outer - inner radius) in deg visual angle, by default 1.0
                        Can specify as many target_widths as target_indices;
                        if fewer widths are passed than indices, cycles through intensities
   :type target_width: float, or Sequence[float, ...], optional
   :param target_center: center (radius) in deg visual angle where each target will be placed
                         within its segment, by default 1.0.
                         Can specify as many centers as target_indices;
                         if fewer centers are passed than indices, cycles through intensities
   :type target_center: float, or Sequence[float, ...], optional
   :param intensity_segments: intensity value for each segment, by default (1.0, 0.0).
                              Can specify as many intensities as n_segments;
                              If fewer intensities are passed than n_segments, cycles through intensities
   :type intensity_segments: Sequence[float, ...]
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
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Robinson, A. E., Hammon, P. S., & de Sa, V. R. (2007).
       Explaining brightness illusions
       using spatial filtering and local response normalization.
       Vision Research, 47(12), 1631-1644.
       https://doi.org/10.1016/j.visres.2007.02.017




 