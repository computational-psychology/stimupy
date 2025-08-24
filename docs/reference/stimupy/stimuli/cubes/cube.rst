
cube
====


.. image:: /_static/generated_stimuli/stimuli.cubes.cube.png
   :alt: cube stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/cubes/cube.html>`__





.. py:function:: stimupy.stimuli.cubes.cube(visual_size=None, ppd=None, shape=None, n_cells=None, target_indices=(), cell_thickness=None, cell_spacing=None, intensity_background=0.0, intensity_cells=1.0, intensity_target=0.5)


   Cube illusion (Agostini & Galmonte, 2002)

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param n_cells: the number of square cells (not counting background) per dimension
   :type n_cells: int
   :param target_indices: Target indices. Will be used on each side
   :type target_indices: Sequence
   :param cell_thickness: thickness of each cell in degrees
   :type cell_thickness: Number or None (default)
   :param cell_spacing: spacing between cells in degrees (height, width)
   :type cell_spacing: Sequence[Number, Number], Number or None (default)
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_cells: intensity value for grid cells
   :type intensity_cells: float
   :param intensity_target: intensity value for target
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Agostini, T., and Galmonte, A. (2002).
       Perceptual organization overcomes the effects of local surround
       in determining simultaneous lightness contrast.
       Psychol. Sci. 13, 89-93.
       https://doi.org/10.1111/1467-9280.00417
   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093




 