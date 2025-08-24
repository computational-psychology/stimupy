
benary_cross
============


.. image:: /_static/generated_stimuli/papers.RHS2007.benary_cross.png
   :alt: benary_cross stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.benary_cross(ppd=PPD, pad=True)


   Benarys cross as shown in Robinson, Hammon, & de Sa (2007) Fig 1y.

   :param ppd: Resolution of stimulus in pixels per degree. (default: 32)
   :type ppd: int
   :param pad: If True, include padding to 32x32 deg (default: True)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str

   .. rubric:: References

   Blakeslee, B., & McCourt, M. E. (2001).
       A multiscale spatial filtering account
       of the Wertheimer-Benary effect and the corrugated Mondrian.
       Vision Research, 41, 2487-2502.
   Benary, W. (1924).
       Beobachtungen zu einem Experiment über Helligkeitskontrast.
       Psychologische Forschung, 5, 131-142.
       https://doi.org/10.1007/BF00402398




 