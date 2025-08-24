
grid
====


.. image:: /_static/generated_stimuli/stimuli.hermanns.grid.png
   :alt: grid stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/hermanns/grid.html>`__





.. py:function:: stimupy.stimuli.hermanns.grid(visual_size=None, ppd=None, shape=None, element_size=None, intensity_background=0.0, intensity_grid=1.0)


   Hermann's (1870) grid

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param element_size: height, width and thickness of individual elements in degree visual angle
   :type element_size: (float, float, float)
   :param intensity_background: value of background
   :type intensity_background: float
   :param intensity_grid: value of grid
   :type intensity_grid: float

   :returns: dict with the stimulus (key: "img"),
             empty mask (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Hermann L (1870).
       Eine Erscheinung simultanen Contrastes".
       Pflügers Archiv für die gesamte Physiologie. 3: 13-15.
       https://doi.org/10.1007/BF01855743




 