
gabors
======


.. image:: /_static/generated_stimuli/stimuli.plaids.gabors.png
   :alt: gabors stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/plaids/gabors.html>`__





.. py:function:: stimupy.stimuli.plaids.gabors(gabor_parameters1, gabor_parameters2, weight1=1, weight2=1)


   Draw plaid consisting of two gabors

   :param gabor_parameters1: kwargs to generate first Gabor
   :type gabor_parameters1: dict
   :param gabor_parameters2: kwargs to generate second Gabor
   :type gabor_parameters2: dict
   :param weight1: weight of first Gabor (default: 1)
   :type weight1: float
   :param weight2: weight of second Gabor (default: 1)
   :type weight2: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each phase (key: "grating_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 