
ring
====


.. image:: /_static/generated_stimuli/components.shapes.ring.png
   :alt: ring stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/shapes/ring.html>`__





.. py:function:: stimupy.components.shapes.ring(visual_size=None, ppd=None, shape=None, radii=None, intensity_ring=1.0, intensity_background=0.0, origin='mean')


   Draw a ring (annulus)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param radii: inner and outer radius of ring in degree visual angle
   :type radii: Sequence[Number, Number]
   :param intensity_ring: intensity value of ring, by default 1.0
   :type intensity_ring: Number, optional
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

   :raises ValueError: if passed in less/more than 2 radii (inner, outer)
   :raises ValueError: if passed in less/more than 1 intensity




 