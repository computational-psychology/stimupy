
cube
====


.. image:: /_static/generated_stimuli/papers.domijan2015.cube.png
   :alt: cube stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.domijan2015.cube(visual_size=VSIZES['cube'], ppd=PPD, shape=SHAPES['cube'])


   Cube illusion, Domijan (2015) Fig 6B

   :param visual_size: visual size [height, width] in degrees, default: (10, 20)
   :type visual_size: Sequence[Number, Number], Number, or None
   :param ppd: pixels per degree [vertical, horizontal], default: 10
   :type ppd: Sequence[Number, Number], Number, or None
   :param shape: shape [height, width] in pixels, default: (100, 200)
   :type shape: Sequence[Number, Number], Number, or None

   :returns: dict with the stimulus (key: "img") and target mask (key: "target_mask")
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093




 