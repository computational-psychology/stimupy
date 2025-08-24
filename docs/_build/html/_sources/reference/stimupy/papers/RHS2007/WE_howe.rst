
WE_howe
=======


.. image:: /_static/generated_stimuli/papers.RHS2007.WE_howe.png
   :alt: WE_howe stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.WE_howe(ppd=PPD, pad=True)


   Howe variation of White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1e.
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

   Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
       Oriented multiscale spatial ﬁltering and contrast normalization:
       a parsimonious model of brightness induction in a continuum
       of stimuli including White, Howe and simultaneous brightness contrast.
       Vision Research, 45, 607-615.
   Howe, P. D. L. (2001).
       A comment on the Anderson (1997), the Todorovic (1997),
       and the Ross and Pessoa (2000) explanations of White's eﬀect.
       Perception, 30, 1023-1026




 