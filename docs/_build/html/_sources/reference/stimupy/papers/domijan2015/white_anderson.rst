
white_anderson
==============


.. image:: /_static/generated_stimuli/papers.domijan2015.white_anderson.png
   :alt: white_anderson stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.domijan2015.white_anderson(visual_size=VSIZES['white_anderson'], ppd=PPD, shape=SHAPES['white_anderson'], pad=PAD)


   Anderson variation of White stimulus, Domijan (2015) Fig 11B

   :param visual_size: visual size [height, width] in degrees, default: (10, 10)
   :type visual_size: Sequence[Number, Number], Number, or None
   :param ppd: pixels per degree [vertical, horizontal], default: 10
   :type ppd: Sequence[Number, Number], Number, or None
   :param shape: shape [height, width] in pixels, default: (100, 100)
   :type shape: Sequence[Number, Number], Number, or None
   :param pad: If True, include original padding (default: False)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Anderson, B. L. (2001).
       Contrasting theories of White's illusion.
       Perception, 30, 1499-1501.
   Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
       Oriented multiscale spatial ﬁltering and contrast normalization:
       a parsimonious model of brightness induction in a continuum
       of stimuli including White, Howe and simultaneous brightness contrast.
       Vision Research, 45, 607-615.
   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093




 