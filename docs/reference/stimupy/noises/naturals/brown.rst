
brown
=====


.. image:: /_static/generated_stimuli/noises.naturals.brown.png
   :alt: brown stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/noises/naturals/brown.html>`__





.. py:function:: stimupy.noises.naturals.brown(visual_size=None, ppd=None, shape=None, intensity_range=(0, 1), pseudo_noise=False)


   Draw brown (1 / (f**2.0)) noise texture

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param intensity_range: minimum and maximum intensity value; default: (0, 1)
                           be aware that not every instance has mean=(max-min)/2.
   :type intensity_range: Sequence[Number, Number]
   :param pseudo_noise: if True, generate pseudo-random noise with ideal power spectrum
   :type pseudo_noise: bool

   :rtype: A stimulus dictionary with the noise array ['img']




 