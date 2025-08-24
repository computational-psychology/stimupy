
staircase
=========


.. image:: /_static/generated_stimuli/components.waves.staircase.png
   :alt: staircase stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/waves/staircase.html>`__





.. py:function:: stimupy.components.waves.staircase(visual_size=None, ppd=None, shape=None, frequency=None, n_phases=None, phase_width=None, period='ignore', rotation=0.0, phase_shift=0.0, origin='center', distance_metric=None, round_phase_width=False, intensities=(0.0, 1.0))


   Draw a luminance staircase

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of grating, in cycles per degree visual angle
   :type frequency: Number, or None (default)
   :param n_phases: number of phases in the grating
   :type n_phases: int, or None (default)
   :param phase_width: width of a single phase, in degrees visual angle
   :type phase_width: Number, or None (default)
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either", "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param phase_shift: phase shift of grating in degrees, by default 0.o
   :type phase_shift: float
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean", or "center" (default)
   :param distance_metric: if "horizontal", use distance from origin in x-direction,
                           if "vertical", use distance from origin in x-direction;
                           if "oblique", use combined and rotated distance from origin in x-y;
                           if "radial", use radial distance from origin,
                           if "angular", use angular distance from origin,
                           if "rectilinear", use rectilinear/cityblock/Manhattan distance from origin
   :type distance_metric: str or None
   :param round_phase_width: if True, round width of bars given resolution, by default False
   :type round_phase_width: bool
   :param intensities: if len(intensities)==2, intensity range of staircase (default 0.0, 1.0);
                       if len(intensities)>2, intensity value for each phase.
                       Can specify as many intensities as n_phases.
                       If fewer intensities are passed than n_phases, cycles through intensities.
   :type intensities: Sequence[float, ...]

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each phase (key: "grating_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 