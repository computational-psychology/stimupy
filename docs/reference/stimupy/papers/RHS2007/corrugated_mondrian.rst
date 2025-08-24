
corrugated_mondrian
===================


.. image:: /_static/generated_stimuli/papers.RHS2007.corrugated_mondrian.png
   :alt: corrugated_mondrian stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.RHS2007.corrugated_mondrian(ppd=PPD, pad=True)


   Corrugated Mondrians as shown in Robinson, Hammon, & de Sa (2007) Fig 1x.

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
   Adelson, E. H. (1993).
       Perceptual organization and the judgment of brightness.
       Science, 262, 2042-2044.
       https://doi.org/10.1126/science.8266102




 