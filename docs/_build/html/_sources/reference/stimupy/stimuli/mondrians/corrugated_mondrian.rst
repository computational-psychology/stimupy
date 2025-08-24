
corrugated_mondrian
===================


.. image:: /_static/generated_stimuli/stimuli.mondrians.corrugated_mondrian.png
   :alt: corrugated_mondrian stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/mondrians/corrugated_mondrian.html>`__





.. py:function:: stimupy.stimuli.mondrians.corrugated_mondrian(visual_size=None, ppd=None, shape=None, nrows=None, ncols=None, depths=0, intensities=(0, 1), target_indices=(), intensity_background=0.5, intensity_target=None)


   Corrugated Mondrian

   :param visual_size: visual size [height, width] of image, in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] of image, in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param depths: depth of Mondrian parallelograms per row
   :type depths: Sequence[Number, ... ], Number, or None (default)
   :param intensities: intensities of mondrians; as many tuples as there are rows and as many
                       numbers in each tuple as there are columns
   :type intensities: nested tuples
   :param target_indices: indices of targets; as many tuples as there are targets with (y, x) indices
   :type target_indices: nested tuples
   :param intensity_background: intensity value for background
   :type intensity_background: float
   :param intensity_target: target intensity. If None, use values defined in intensities
   :type intensity_target: float

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Adelson, E. H. (1993).
       Perceptual organization and the judgment of brightness.
       Science, 262, 2042-2044.
       https://doi.org/10.1126/science.8266102




 