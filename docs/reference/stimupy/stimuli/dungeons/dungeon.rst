
dungeon
=======


.. image:: /_static/generated_stimuli/stimuli.dungeons.dungeon.png
   :alt: dungeon stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/dungeons/dungeon.html>`__





.. py:function:: stimupy.stimuli.dungeons.dungeon(visual_size=None, ppd=None, shape=None, cell_size=None, n_cells=None, target_radius=1, intensity_background=0.0, intensity_grid=1.0, intensity_target=0.5)


   Dungeon stimulus (Bressan, 2001) with diamond target.

   :param visual_size: visual size [height, width] of grating, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of grating, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param cell_size: size of individual cell (height, width)
   :type cell_size: Sequence[Number, Number], Number, or None (default)
   :param n_cells: the number of square cells (not counting background) per dimension
   :type n_cells: Sequence[Number, Number], Number, or None (default)
   :param target_radius: the "Manhattan radius" of the diamond target in # cells
   :type target_radius: int
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_grid: intensity value for grid cells
   :type intensity_grid: float
   :param intensity_target: intensity value for target
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Bressan, P. (2001).
       Explaining lightness illusions.
       Perception, 30(9), 1031-1046.
       https://doi.org/10.1068/p3109
   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093




 