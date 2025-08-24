
sbc_large
=========


.. image:: /_static/generated_stimuli/papers.RHS2007.sbc_large.png
   :alt: sbc_large stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.sbc_large(ppd=PPD, pad=True)


   Simultaneous brightness contrast as shown in Robinson, Hammon, & de Sa (2007) Fig 1o.
   Stimulus size: 13x31 deg
   Target sizes: 3x3 deg

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




 