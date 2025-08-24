
WE_dual
=======


.. image:: /_static/generated_stimuli/papers.RHS2007.WE_dual.png
   :alt: WE_dual stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.WE_dual(ppd=PPD, pad=True)


   Dual White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1c.
   Grating sizes: 6x8 deg
   Grating frequency: 0.5 cpd
   Target size: 2x1 deg

   :param ppd: Resolution of stimulus in pixels per degree. (default: 32)
   :type ppd: int
   :param pad: If True, include padding to 32x32 deg (default: True)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict of str




 