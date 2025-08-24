
sine_waves
==========


.. image:: /_static/generated_stimuli/stimuli.plaids.sine_waves.png
   :alt: sine_waves stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/plaids/sine_waves.html>`__





.. py:function:: stimupy.stimuli.plaids.sine_waves(grating_parameters1, grating_parameters2, weight1=1, weight2=1)


   Draw plaid consisting of two sine-wave gratings

   :param grating_parameters1: kwargs to generate first sine-wave grating
   :type grating_parameters1: dict
   :param grating_parameters2: kwargs to generate second sine-wave grating
   :type grating_parameters2: dict
   :param weight1: weight of first grating (default: 1)
   :type weight1: float
   :param weight2: weight of second grating (default: 1)
   :type weight2: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each phase (key: "grating_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 