
bullseye_thick
==============


.. image:: /_static/generated_stimuli/papers.RHS2007.bullseye_thick.png
   :alt: bullseye_thick stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.bullseye_thick(ppd=PPD, pad=True)


   Bullseye stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1bb.
   Target size: 0.608x0.608 deg
   Ring widths: 0.243 deg

   :param ppd: Resolution of stimulus in pixels per degree. (default: 32)
   :type ppd: int
   :param pad: If True, include padding to 32x32 deg (default: True)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str

   .. rubric:: References

   Bindman, D., & Chubb, C. (2004).
       Brightness assimilation in bullseye displays.
       Vision Research, 44, 309-319.
       https://doi.org/10.1016/S0042-6989(03)00430-9




 