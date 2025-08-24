
basic
=====


.. image:: /_static/generated_stimuli/stimuli.sbcs.basic.png
   :alt: basic stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/sbcs/basic.html>`__





.. py:function:: stimupy.stimuli.sbcs.basic(visual_size=None, ppd=None, shape=None, target_size=None, intensity_background=0.0, intensity_target=0.5)


   Simultaneous contrast stimulus with central target

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param target_size: size [height, width] of the target, in degrees visual angle
   :type target_size: float or (float, float)
   :param intensity_background: intensity value for background, by default 0.0
   :type intensity_background: float, optional
   :param intensity_target: intensity value for target, by default 0.5
   :type intensity_target: float, optional

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Chevreul, M. (1855).
       The principle of harmony and contrast of colors.




 