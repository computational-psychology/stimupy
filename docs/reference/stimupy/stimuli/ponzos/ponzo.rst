
ponzo
=====


.. image:: /_static/generated_stimuli/stimuli.ponzos.ponzo.png
   :alt: ponzo stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/ponzos/ponzo.html>`__





.. py:function:: stimupy.stimuli.ponzos.ponzo(visual_size=None, ppd=None, shape=None, outer_lines_length=None, outer_lines_width=0, outer_lines_angle=15, target_lines_length=None, target_lines_width=0, target_distance=None, intensity_outer_lines=1.0, intensity_target_lines=0.5, intensity_background=0.0)


   Ponzo's (1910) illusion

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param outer_lines_length: length of outer lines in degrees visual angle
   :type outer_lines_length: Number
   :param outer_lines_width: line width of outer lines in degrees visual angle
                             if 0 (default), set line width to 1 px
   :type outer_lines_width: Number
   :param outer_lines_angle: angle of outer lines in degrees. Must be between -45 and 45 degrees.
   :type outer_lines_angle: Number
   :param target_lines_length: length of target lines in degrees visual angle
   :type target_lines_length: Number
   :param target_lines_width: line width of target lines in degrees visual angle
                              if 0 (default), set line width to 1 px
   :param target_distance: distance between target lines in degrees visual angle
   :type target_distance: Number
   :param intensity_outer_lines: intensity value(s) of outer lines
   :type intensity_outer_lines: Number or (Number, Number)
   :param intensity_target_lines: intensity value(s) of target lines
   :type intensity_target_lines: Number or (Number, Number)
   :param intensity_background: intensity value of background
   :type intensity_background: Number

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Ponzo, M. (1910).
       Intorno ad alcune illusioni nel campo delle sensazioni tattili,
       sull'illusione di Aristotele e fenomeni analoghi.
       Wilhelm Engelmann.




 