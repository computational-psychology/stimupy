
mueller_lyer
============


.. image:: /_static/generated_stimuli/stimuli.mueller_lyers.mueller_lyer.png
   :alt: mueller_lyer stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/mueller_lyers/mueller_lyer.html>`__





.. py:function:: stimupy.stimuli.mueller_lyers.mueller_lyer(visual_size=None, ppd=None, shape=None, outer_lines_length=None, outer_lines_angle=45, target_length=None, line_width=0, intensity_outer_lines=1.0, intensity_target=0.5, intensity_background=0.0)


   Mueller-Lyer's (1896) illusion

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param outer_lines_length: length of outer lines in degrees visual angle
   :type outer_lines_length: Number
   :param outer_lines_angle: angle of outer lines in degrees, by default 45. Must be between -180 and 180 degrees.
   :type outer_lines_angle: Number (optional)
   :param target_length: length of target line in degrees visual angle
   :type target_length: Number
   :param line_width: line width in degrees visual angle; if 0 (default), line width is 1 px
   :type line_width: Number (optional)
   :param intensity_outer_lines: intensity value of outer lines, by default 0.01
   :type intensity_outer_lines: Number (optional)
   :param intensity_target: intensity value of target line, by default 0.5
   :type intensity_target: Number (optional)
   :param intensity_background: intensity value of background, by default 0.0
   :type intensity_background: Number (optional)

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Mueller-Lyer, F. (1896).
       Zur Lehre von den optischen Taeuschungen.
       Ueber Kontrast und Konfluxion.
       Zeitschrift fuer Psychologie und Physiologie der Sinnesorgane, IX, 1-16.




 