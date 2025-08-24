
on_grating
==========


.. image:: /_static/generated_stimuli/stimuli.gratings.on_grating.png
   :alt: on_grating stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/gratings/on_grating.html>`__





.. py:function:: stimupy.stimuli.gratings.on_grating(small_grating_params, large_grating_params)


   Small grating on a larger grating

   :param small_grating_params: kwargs to generate small grating
   :type small_grating_params: dict
   :param large_grating_params: kwargs to generate larger grating
   :type large_grating_params: dict

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   White, M. (1981).
       The effect of the nature of the surround on the perceived lightness
       of grey bars within square-wave test grating.
       Perception, 10, 215-230.
       https://doi.org/10.1068/p100215




 