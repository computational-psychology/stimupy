
square_36phase
==============


.. image:: /_static/generated_stimuli/papers.white1985.square_36phase.png
   :alt: square_36phase stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.white1985.square_36phase(ppd=PPD)


   A square-wave grating with four squares that are 36 deg out-of-phase as
   shown in White & White (1985), Fig. 3
   Stimulus size: 3.5 x 3.5 deg
   Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
   Grating frequency: 3.5 cpd

   :param ppd: Resolution of stimulus in pixels per degree.
   :type ppd: int

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str

   .. rubric:: References

   White, M. & White, T. (1985).
       Counterphase lightness induction.
       Vision Research, 25 (9), 1331-1335.
       https://doi.org/10.1016/0042-6989(85)90049-5




 