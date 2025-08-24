



RHS2007
=======

.. py:module:: stimupy.papers.RHS2007


.. autoapi-nested-parse::

   Stimuli from Robinson, Hammon & de Sa (2007)

   This module reproduces all of the stimuli used by Robinson,
   Hammon & de Sa (2007)
   as they were provided to the model described in that paper.

   Each stimulus is provided by a separate function,
   which can be listed using

       >>> import stimupy.papers.RHS2007
       >>> help(stimupy.papers.RHS2007)

   The output of each of these functions is a stimulus dictionary.

   For a visual representation of all the stimuli and their mask,
   simply run this module from the shell

       $ python -m stimuli.papers.RHS2007

   or from within python

       >>> from stimupy.utils import plot_stimuli
       >>> from stimupy.papers import RHS2007
       >>> plot_stimuli(RHS2007.gen_all())

   .. rubric:: References

   Robinson, A. E., Hammon, P. S., & de Sa, V. R. (2007).
       Explaining brightness illusions
       using spatial filtering and local response normalization.
       Vision Research, 47(12), 1631-1644.
       https://doi.org/10.1016/j.visres.2007.02.017









































Functions
---------

.. autoapisummary::

   stimupy.papers.RHS2007.WE_thick
   stimupy.papers.RHS2007.WE_thin_wide
   stimupy.papers.RHS2007.WE_dual
   stimupy.papers.RHS2007.WE_anderson
   stimupy.papers.RHS2007.WE_howe
   stimupy.papers.RHS2007.WE_zigzag
   stimupy.papers.RHS2007.WE_radial_thick_small
   stimupy.papers.RHS2007.WE_radial_thick
   stimupy.papers.RHS2007.WE_radial_thin_small
   stimupy.papers.RHS2007.WE_radial_thin
   stimupy.papers.RHS2007.WE_circular1
   stimupy.papers.RHS2007.WE_circular05
   stimupy.papers.RHS2007.WE_circular025
   stimupy.papers.RHS2007.grating_induction
   stimupy.papers.RHS2007.sbc_large
   stimupy.papers.RHS2007.sbc_small
   stimupy.papers.RHS2007.todorovic_equal
   stimupy.papers.RHS2007.todorovic_in_large
   stimupy.papers.RHS2007.todorovic_in_small
   stimupy.papers.RHS2007.todorovic_out
   stimupy.papers.RHS2007.checkerboard_016
   stimupy.papers.RHS2007.checkerboard_094
   stimupy.papers.RHS2007.checkerboard_21
   stimupy.papers.RHS2007.corrugated_mondrian
   stimupy.papers.RHS2007.benary_cross
   stimupy.papers.RHS2007.todorovic_benary1_2
   stimupy.papers.RHS2007.todorovic_benary3_4
   stimupy.papers.RHS2007.todorovic_benary1_2_3_4
   stimupy.papers.RHS2007.bullseye_thin
   stimupy.papers.RHS2007.bullseye_thick



.. base-gallery::
   :caption: stimupy.papers.RHS2007

   WE_thick
   WE_thin_wide
   WE_dual
   WE_anderson
   WE_howe
   WE_zigzag
   WE_radial_thick_small
   WE_radial_thick
   WE_radial_thin_small
   WE_radial_thin
   WE_circular1
   WE_circular05
   WE_circular025
   grating_induction
   sbc_large
   sbc_small
   todorovic_equal
   todorovic_in_large
   todorovic_in_small
   todorovic_out
   checkerboard_016
   checkerboard_094
   checkerboard_21
   corrugated_mondrian
   benary_cross
   todorovic_benary1_2
   todorovic_benary3_4
   todorovic_benary1_2_3_4
   bullseye_thin
   bullseye_thick















  