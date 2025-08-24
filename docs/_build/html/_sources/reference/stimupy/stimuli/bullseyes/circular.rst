
circular
========


.. image:: /_static/generated_stimuli/stimuli.bullseyes.circular.png
   :alt: circular stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/bullseyes/circular.html>`__





.. py:function:: stimupy.stimuli.bullseyes.circular(visual_size=None, ppd=None, shape=None, frequency=None, n_rings=None, ring_width=None, phase_shift=0, intensity_target=0.5, intensity_rings=(0.0, 1.0), intensity_background=0.5, origin='mean', clip=True)


   Circular Bullseye stimulus

   Circular grating, where the target is the central disc.
   Alias for circular_white(target_indices=0,...)

   Specification of the number of rings, and their width can be done in two ways:
   a ring_width (in degrees) and n_rings, and/or by specifying the spatial frequency
   of a circular grating (in cycles per degree)

   The total shape (in pixels) and visual size (in degrees) has to match the
   specification of the rings and their widths.
   Thus, not all 6 parameters (visual_size, ppd, shape, frequency, ring_width, n_rings)
   have to be specified, as long as both the resolution, and the distribution of rings,
   can be resolved.

   Note: all rings in a grating have the same width -- if more control is required
   see disc_and_rings

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of circular grating, in cycles per degree
   :type frequency: Number, or None (default)
   :param n_rings: number of rings
   :type n_rings: int, or None (default)
   :param ring_width: width of a single ring, in degrees
   :type ring_width: Number, or None (default)
   :param phase_shift: phase shift of grating in degrees
   :type phase_shift: float
   :param intensity_target: intensity value of target ring(s), by default 0.5
   :type intensity_target: float (optional)
   :param intensity_rings: intensity value for each ring, from inside to out, by default [1,0]
                           If fewer intensities are passed than number of radii, cycles through intensities
   :type intensity_rings: Sequence[Number, ...]
   :param intensity_background: intensity value of background, by default 0.5
   :type intensity_background: float (optional)
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
   Hong, S. W., and Shevell, S. K. (2004).
       Brightness contrast and assimilation from patterned inducing backgrounds.
       Vision Research, 44, 35-43.
       https://doi.org/10.1016/j.visres.2003.07.010
   Howe, P. D. L. (2005).
       White's effect:
       removing the junctions but preserving the strength of the illusion.
       Perception, 34, 557-564.
       https://doi.org/10.1068/p5414




 