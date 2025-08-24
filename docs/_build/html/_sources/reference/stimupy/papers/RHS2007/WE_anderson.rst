
WE_anderson
===========


.. image:: /_static/generated_stimuli/papers.RHS2007.WE_anderson.png
   :alt: WE_anderson stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.WE_anderson(ppd=PPD, pad=True)


   Anderson variation of White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1d.
   Grating size: 16x16 deg
   Grating frequency: 0.5 cpd
   Target size: 3.2x1 deg

   :param ppd: Resolution of stimulus in pixels per degree. (default: 32)
   :type ppd: int
   :param pad: If True, include padding to 32x32 deg (default: True)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str

   .. rubric:: References

   Anderson, B. L. (2001).
       Contrasting theories of White's illusion. Perception, 30, 1499-1501
   Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
       Oriented multiscale spatial ﬁltering and contrast normalization:
       a parsimonious model of brightness induction in a continuum of stimuli
       including White, Howe and simultaneous brightness contrast.
       Vision Research, 45, 607-615.




 