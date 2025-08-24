
todorovic_out
=============


.. image:: /_static/generated_stimuli/papers.RHS2007.todorovic_out.png
   :alt: todorovic_out stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.todorovic_out(ppd=PPD, pad=True)


   Todorovic stimulus - out as shown in Robinson, Hammon, & de Sa (2007) Fig 1t.
   Stimulus size: 13x31 deg
   Target size: 9.4x9.4 deg

   (note: in RHS2007, it says 8.7x8.7 deg, however that does not match with Fig 1t)

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
   Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
       Lightness and junctions: variations on White's display.
       Investigative Ophthalmology and Visual Science (Supplement), 39, S159.




 