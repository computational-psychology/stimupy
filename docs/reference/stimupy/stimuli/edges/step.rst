
step
====


.. image:: /_static/generated_stimuli/stimuli.edges.step.png
   :alt: step stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/edges/step.html>`__





.. py:function:: stimupy.stimuli.edges.step(visual_size=None, ppd=None, shape=None, rotation=0.0, intensity_edges=(0.0, 1.0))


   Draw a central step edge

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional
   :param intensity_edges: intensity values of edges (default: (0., 1.))
   :type intensity_edges: (float, float)

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the each lobes (key: "edge_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]




 