
narrowband
==========


.. image:: /_static/generated_stimuli/noises.narrowbands.narrowband.png
   :alt: narrowband stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/noises/narrowbands/narrowband.html>`__





.. py:function:: stimupy.noises.narrowbands.narrowband(visual_size=None, ppd=None, shape=None, center_frequency=None, bandwidth=None, intensity_range=(0, 1), pseudo_noise=False)


   Draw narrowband noise texture

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param center_frequency: noise center frequency in cpd
   :type center_frequency: float
   :param bandwidth: bandwidth of the noise in octaves
   :type bandwidth: float
   :param intensity_range: minimum and maximum intensity value; default: (0, 1).
                           be aware that not every instance has mean=(max-min)/2.
   :type intensity_range: Sequence[Number, Number]
   :param pseudo_noise: if True, generate pseudo-random noise with ideal power spectrum.
   :type pseudo_noise: bool

   :returns: dict with the stimulus (key: "img"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 