
wedge
=====


.. image:: /_static/generated_stimuli/components.angulars.wedge.png
   :alt: wedge stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/angulars/wedge.html>`__





.. py:function:: stimupy.components.angulars.wedge(visual_size=None, ppd=None, shape=None, angle=None, radius=None, rotation=0.0, inner_radius=0.0, intensity_wedge=1.0, intensity_background=0.0, origin='mean')


   Draw a wedge, i.e., segment of a disc

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param angle: angular-width (in degrees) of segment
   :type angle: float
   :param radius: radius of disc, in degrees visual angle
   :type radius: float
   :param rotation: rotation (in degrees) from 3 o'clock, counterclockwise, by default 0.0
   :type rotation: float, optional
   :param inner_radius: inner radius (in degrees visual angle), to turn disc into a ring, by default 0
   :type inner_radius: float, optional
   :param intensity_wedge: intensity value of wedge, by default 1.0
   :type intensity_wedge: float, optional
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: float, optional
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each segment (key: "wedge_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 