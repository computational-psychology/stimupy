
checkerboard
============


.. image:: /_static/generated_stimuli/stimuli.checkerboards.checkerboard.png
   :alt: checkerboard stimulus example
   :align: center
   :width: 400px



.. centered:: You can find an interactive version of this example `here <../../../demos/stimuli/checkerboards/checkerboard.html>`__





.. py:function:: stimupy.stimuli.checkerboards.checkerboard(visual_size=None, ppd=None, shape=None, frequency=None, board_shape=None, check_visual_size=None, target_indices=(), extend_targets=False, period='ignore', rotation=0.0, intensity_checks=(0.0, 1.0), intensity_target=0.5, round_phase_width=True)


   Checkerboard assimilation effect

   High-contrast checkerboard, with intermediate targets embedded in it.
   Target brightness assimilates to direct surround, rather than contrast with it.

   These kinds of checkerboard displays are described by De Valois & De Valois (1988),
   and the brightness effect of it by Blakeslee & McCourt (2004).

   :param visual_size: visual size of the total board [height, width] in degrees
   :type visual_size: Sequence[Number, Number], Number, or None (default)
   :param ppd: pixels per degree [vertical, horizontal]
   :type ppd: Sequence[Number, Number], Number, or None (default)
   :param shape: shape [height, width] in pixels
   :type shape: Sequence[Number, Number], Number, or None (default)
   :param frequency: frequency of checkerboard in [y, x] in cpd
   :type frequency: Sequence[Number, Number], Number, or None (default)
   :param board_shape: number of checks in [height, width] of checkerboard
   :type board_shape: Sequence[Number, Number], Number, or None (default)
   :param check_visual_size: visual size of a single check [height, width] in degrees
   :type check_visual_size: Sequence[Number, Number], Number, or None (default)
   :param target_indices: target indices (row, column of checkerboard), by default None
   :type target_indices: Sequence[(Number, Number),...], optional
   :param extend_targets: if true, extends the targets by 1 check in all 4 directions, by default False
   :type extend_targets: bool, optional
   :param period: ensure whether the grating has "even" number of phases, "odd"
                  number of phases, either or whether not to round the number of
                  phases ("ignore")
   :type period: "even", "odd", "either" or "ignore" (default)
   :param rotation: rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
   :type rotation: float, optional
   :param intensity_checks: intensity values of checks, by default (0.0, 1.0)
   :type intensity_checks: Sequence[float, float]
   :param round_phase_width: if True, round width of bars given resolution (default: True)
   :type round_phase_width: Bool

   :returns: dict with the stimulus (key: "img"),
             mask with integer index for each target (key: "target_mask"),
             and additional keys containing stimulus parameters
   :rtype: dict[str, Any]

   .. rubric:: References

   Blakeslee, B., & McCourt, M. E. (2004).
       A unified theory of brightness contrast and assimilation
       incorporating oriented multiscale spatial filtering and contrast normalization.
       Vision Research, 44(21), 2483-2503.
       https://doi.org/10/fmcx5p
   De Valois, R. L., & De Valois, K. K. (1988).
       Spatial Vision. Oxford University Press.




 