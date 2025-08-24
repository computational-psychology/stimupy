
contrast_contrast
=================


.. image:: /_static/generated_stimuli/stimuli.checkerboards.contrast_contrast.png
   :alt: contrast_contrast stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/checkerboards/contrast_contrast.html>`__





.. py:function:: stimupy.stimuli.checkerboards.contrast_contrast(visual_size=None, ppd=None, shape=None, frequency=None, board_shape=None, check_visual_size=None, target_shape=None, period='ignore', rotation=0.0, intensity_checks=(0.0, 1.0), tau=0.5, alpha=None, round_phase_width=True)


   Contrast-contrast effect on checkerboard with square transparency layer

   Checkerboard version of the contrast-contrast illusion (Chubb, Sperling, Solomon,
   1989), as used by Domijan (2015).

   :param shape: shape [height, width] in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param visual_size: visual size of the total board [height, width] in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param board_shape: number of checks in [height, width] of checkerboard
   :type board_shape: Sequence[Number, Number], Number, or None (default)
   :param check_visual_size: visual size of a single check [height, width] in degrees
   :type check_visual_size: Sequence[Number, Number], Number, or None (default)
   :param targets_shape: number of checks with transparency in y, x direction
   :type targets_shape: Sequence[Number, Number], Number, or None (default)
   :param intensity_low: intensity value of the dark checks, by default 0.0
   :type intensity_low: float, optional
   :param intensity_high: intensity value of the light checks, by default 1.0
   :type intensity_high: float, optional
   :param tau: tau of transparency (i.e. value of transparent medium), default 0.5
   :type tau: Number
   :param alpha: alpha of transparency (i.e. how transparent the medium is)
   :type alpha: Number or None (default)
   :param round_phase_width: if True, round width of bars given resolution (default: True)
   :type round_phase_width: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Chubb, C., Sperling, G., & Solomon, J. A. (1989).
       Texture interactions determine perceived contrast.
       Proc. Natl. Acad. Sci. USA, 5.
       https://doi.org/10.1073/pnas.86.23.9631
   Domijan, D. (2015).
       A Neurocomputational account of the role
       of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9(February), 1-16.
       https://doi.org/10/gh62x2




 