
dungeon
=======


.. image:: /_static/generated_stimuli/papers.domijan2015.dungeon.png
   :alt: dungeon stimulus example
   :align: center
   :width: 400px






.. py:function:: stimupy.papers.domijan2015.dungeon(visual_size=VSIZES['dungeon'], ppd=PPD, shape=SHAPES['dungeon'])


   Dungeon illusion, Domijan (2015) Fig 6A

   :param visual_size: visual size [height, width] in degrees, default: (11, 22)
   :type visual_size: Sequence[Number, Number], Number, or None
   :param ppd: pixels per degree [vertical, horizontal], default: 10
   :type ppd: Sequence[Number, Number], Number, or None
   :param shape: shape [height, width] in pixels, default: (110, 220)
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




 