
one_over_f
==========


.. image:: /_static/generated_stimuli/noises.naturals.one_over_f.png
   :alt: one_over_f stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/noises/naturals/one_over_f.html>`__





.. py:function:: stimupy.noises.naturals.one_over_f(visual_size=None, ppd=None, shape=None, exponent=None, intensity_range=(0, 1), pseudo_noise=False, rng=None)


   Draw 1 / (f**exponent) noise texture

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param exponent: exponent used to create 1 / (f**exponent) noise
   :param intensity_range: minimum and maximum intensity value; default: (0, 1).
                           be aware that not every instance has mean=(max-min)/2.
   :type intensity_range: Sequence[Number, Number]
   :param pseudo_noise: if True, generate pseudo-random noise with ideal power spectrum.
   :type pseudo_noise: bool
   :param rng: Random number generator to use. If None, a new default_rng is created.
               By passing in a custom rng, you can control the randomness of the noise generation,
               e.g., make it replicable.
   :type rng: numpy.random.Generator, optional

   :returns: dict with the stimulus (key: "img"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 