
cornsweet
=========


.. image:: /_static/generated_stimuli/stimuli.edges.cornsweet.png
   :alt: cornsweet stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/edges/cornsweet.html>`__





.. py:function:: stimupy.stimuli.edges.cornsweet(visual_size=None, ppd=None, shape=None, ramp_width=None, rotation=0.0, intensity_edges=(0.0, 1.0), intensity_plateau=0.5, exponent=2.75)


   Draw rectangular Cornsweet edge stimulus.
   The 2D luminance profile of the stimulus is defined as
   Left side:
   v = vtarget + (1 - X / w) ** a * (intensity_max-vtarget) for the ramp and v = vtarget beyond.
   Right side:
   v = vtarget - (1 - X / w) ** a * (intensity_min-vtarget) for the ramp and v = vtarget beyond.
   X is the distance to the edge, w is the width of the ramp, a is a variable
   determining the steepness of the ramp, vtarget is the luminance of the targets and
   intensity_max/intensity_min are the max/min luminances.

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param ramp_width: width of luminance ramp in degrees of visual angle
   :type ramp_width: float
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0
   :type rotation: float, optional
   :param intensity_edges: intensity of edges
   :type intensity_edges: (float, float)
   :param intensity_plateau: intensity value of plateau
   :type intensity_plateau: float
   :param exponent: determines steepness of ramp (default is 2.75. 1 would be linear)
   :type exponent: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for the each lobes (key: "edge_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Boyaci, H., Fang, F., Murray, S.O., Kersten, D. (2007).
       Responses to lightness variations in early human visual cortex.
       Current Biology 17, 989-993.
       https://doi.org/10.1016/j.cub.2007.05.005
   Cornsweet, T. (1970).
       Visual perception. Academic press.
       https://doi.org/10.1016/B978-0-12-189750-5.X5001-5




 