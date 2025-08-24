
delboeuf
========


.. image:: /_static/generated_stimuli/stimuli.delboeufs.delboeuf.png
   :alt: delboeuf stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/delboeufs/delboeuf.html>`__





.. py:function:: stimupy.stimuli.delboeufs.delboeuf(visual_size=None, ppd=None, shape=None, outer_radius=None, outer_line_width=0, target_radius=None, intensity_outer_line=0.0, intensity_target=0.0, intensity_background=1.0)


   Delboeuf's (1865) stimulus

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param outer_radius: radius of outer circle
   :type outer_radius: Number
   :param outer_line_width: line width of outer circle in degrees visual angle
                            if 0 (default), set line width to 1 px
   :type outer_line_width: Number
   :param target_radius: radius of target circle
   :type target_radius: Number
   :param intensity_outer_line: intensity value of outer circle line (default: 0)
   :type intensity_outer_line: Number
   :param intensity_target: intensity value of target (default: 0)
   :type intensity_target: Number
   :param intensity_background: intensity value of background (default: 1)
   :type intensity_background: Number

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Delboeuf, F. J. (1865).
       Note sur certaines illusions d'optique:
       Essai d'une théorie psychophysique de la maniere
       dont l'oeil apprécie les distances et les angles.
       Bulletins de l'Académie Royale des Sciences, Lettres et
       Beaux-arts de Belgique, 19, 195-216.




 