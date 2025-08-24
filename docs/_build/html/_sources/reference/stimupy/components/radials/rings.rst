
rings
=====


.. image:: /_static/generated_stimuli/components.radials.rings.png
   :alt: rings stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/radials/rings.html>`__





.. py:function:: stimupy.components.radials.rings(visual_size=None, ppd=None, shape=None, radii=None, intensity_rings=(0.0, 1.0), intensity_background=0.5, origin='mean')


   Draw a central solid disc with zero or more solid rings (annuli)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radii: outer radii of rings (& disc) in degree visual angle
   :type radii: Sequence[Number]
   :param intensity_rings: intensity value for each ring, from inside to out, by default (0.0, 1.0)
                           If fewer intensities are passed than number of radii, cycles through intensities
   :type intensity_rings: Sequence[Number, ...], optional
   :param intensity_background: value of background, by default 0.5
   :type intensity_background: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center", optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each ring (key: "ring_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 