
bessel
======


.. image:: /_static/generated_stimuli/components.waves.bessel.png
   :alt: bessel stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/components/waves/bessel.html>`__





.. py:function:: stimupy.components.waves.bessel(visual_size=None, ppd=None, shape=None, frequency=None, order=0, intensities=(1.0, 0.0), origin='mean')


   Draw a Bessel stimulus, i.e. draw circular rings following an nth order
   Bessel function of a given frequency.

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: spatial frequency of circular grating, in cycles per degree
   :type frequency: Number, or None (default)
   :param order: n-th order Bessel function
   :type order: int
   :param intensities: intensity values of rings, first value indicating center intensity
   :type intensities: (float, float)
   :param origin: if "corner": set origin to upper left corner
                  if "mean": set origin to hypothetical image center (default)
                  if "center": set origin to real center (closest existing value to mean)
   :type origin: "corner", "mean" or "center"

   :returns: dict with the stimulus (key: "img"),
             empty mask (key: "ring_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 