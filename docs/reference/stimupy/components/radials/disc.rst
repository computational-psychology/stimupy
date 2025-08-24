
disc
====


.. image:: /_static/generated_stimuli/components.radials.disc.png
   :alt: disc stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/radials/disc.html>`__





.. py:function:: stimupy.components.radials.disc(visual_size=None, ppd=None, shape=None, radius=None, intensity_disc=1.0, intensity_background=0.0, origin='mean')


   Draw a central disc

   Essentially, `dics(radius)` is an alias for `ring(radii=[0, radius])`

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radius: outer radius of disc in degree visual angle
   :type radius: Number
   :param intensity_disc: intensity value of disc, by default 1.0
   :type intensity_disc: Number, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center", optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each ring (key: "ring_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 