
grating_induction
=================


.. image:: /_static/generated_stimuli/papers.RHS2007.grating_induction.png
   :alt: grating_induction stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.grating_induction(ppd=PPD, pad=True)


   Grating induction as shown in Robinson, Hammon, & de Sa (2007) Fig 1n.
   Circle size: 12x16 deg
   Grating frequency: 0.25 cpd
   Target size: 1x16 deg

   :param ppd: Resolution of stimulus in pixels per degree. (default: 32)
   :type ppd: int
   :param pad: If True, include padding to 32x32 deg (default: True)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str

   .. rubric:: References

   Blakeslee, B., & McCourt, M. E. (1999).
       A multiscale spatial ﬁltering account
       of the White eﬀect, simultaneous brightness contrast and grating induction.
       Vision Research, 39, 4361-4377.
   McCourt, M. E. (1982).
       A spatial frequency dependent grating-induction effect.
       Vision Research, 22, 119-134.
       https://doi.org/10.1016/0042-6989(82)90173-0




 