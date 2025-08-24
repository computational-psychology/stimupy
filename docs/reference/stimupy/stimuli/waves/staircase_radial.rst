
staircase_radial
================


.. image:: /_static/generated_stimuli/stimuli.waves.staircase_radial.png
   :alt: staircase_radial stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/waves/staircase_radial.html>`__





.. py:function:: stimupy.stimuli.waves.staircase_radial(visual_size=None, ppd=None, shape=None, frequency=None, n_rings=None, ring_width=None, period='ignore', rotation=0.0, phase_shift=0, intensity_rings=(0.0, 1.0), target_indices=(), intensity_target=0.5, origin='mean', round_phase_width=True, clip=False, intensity_background=0.5)


   Radial staircase, with some ring(s) as target(s)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of grating, in cycles per degree visual angle
   :type frequency: Number, or None (default)
   :param n_rings: number of rings in the grating
   :type n_rings: int, or None (default)
   :param ring_width: width of a single ring, in degrees visual angle
   :type ring_width: Number, or None (default)
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either" or "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
   :param intensity_rings: if len(intensity_rings)==2, intensity range of staircase (default 0.0, 1.0);
                           if len(intensity_rings)>2, intensity value for each ring.
                           Can specify as many intensity_rings as n_rings.
                           If fewer intensity_bars are passed than n_rings, cycles through intensities.
   :type intensity_rings: Sequence[float, ...]
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
   :param round_phase_width: if True, round width of rings given resolution
   :type round_phase_width: Bool
   :param clip: if True, clip stimulus to image size (default: False)
   :type clip: Bool
   :param intensity_background: intensity value of background (if clipped), by default 0.5
   :type intensity_background: float (optional)

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 