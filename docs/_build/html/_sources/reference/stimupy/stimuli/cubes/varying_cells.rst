
varying_cells
=============


.. image:: /_static/generated_stimuli/stimuli.cubes.varying_cells.png
   :alt: varying_cells stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/cubes/varying_cells.html>`__





.. py:function:: stimupy.stimuli.cubes.varying_cells(ppd=None, cell_lengths=None, cell_thickness=None, cell_spacing=None, target_indices=(), intensity_background=0.0, intensity_cells=1.0, intensity_target=0.5)


   Cube stimulus (Agostini & Galmonte, 2002) with flexible cell lengths.

   :param ppd: pixels per degree (visual angle)
   :type ppd: Number or None (default)
   :param cell_lengths: lengths of individual cells in degrees
   :type cell_lengths: Sequence[Number, ...], Number of None (default)
   :param cell_thickness: thickness of each cell in degrees
   :type cell_thickness: Number or None (default)
   :param cell_spacing: spacing between cells in degrees
   :type cell_spacing: Number or None (default)
   :param target_indices: target indices; will be used on each side
   :type target_indices: Sequence or None
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




 