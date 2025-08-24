
checkerboard_contrast_contrast
==============================


.. image:: /_static/generated_stimuli/papers.domijan2015.checkerboard_contrast_contrast.png
   :alt: checkerboard_contrast_contrast stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.domijan2015.checkerboard_contrast_contrast(visual_size=VSIZES['checkerboard_contrast_contrast'], ppd=PPD, shape=SHAPES['checkerboard_contrast_contrast'], pad=PAD)


   Checkerboard contrast-contrast effect, Domijan (2015) Fig 9B

   :param visual_size: visual size [height, width] in degrees, default: (8, 16)
   :type visual_size: Sequence[Number, Number], Number, or None
   :param ppd: pixels per degree [vertical, horizontal], default: 10
   :type ppd: Sequence[Number, Number], Number, or None
   :param shape: shape [height, width] in pixels, default: (80, 160)
   :type shape: Sequence[Number, Number], Number, or None
   :param pad: If True, include original padding (default: False)
   :type pad: bool

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093




 