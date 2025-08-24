



white1985
=========

.. py:module:: stimupy.papers.white1985


.. autoapi-nested-parse::

   Stimuli from White & White (1985)

   This module reproduces most of the stimuli used by White & White (1985)
   as they were described in that paper.

   Each stimulus is provided by a separate function,
   which can be listed using

       >>> import stimupy.papers.white1985
       >>> help(stimupy.papers.white1985)

   The output of each of these functions is a stimulus dictionary.

   For a visual representation of all the stimuli,
   simply run this module from the shell

       $ python -m stimuli.papers.white1985

   or from within python

       >>> from stimupy.utils import plot_stimuli
       >>> from stimupy.papers import white1985
       >>> plot_stimuli(white1985.gen_all())

   .. rubric:: References

   White, M. & White, T. (1985).
       Counterphase lightness induction.
       Vision Research, 25 (9), 1331-1335.
       https://doi.org/10.1016/0042-6989(85)90049-5









































Functions
---------

.. autoapisummary::

   stimupy.papers.white1985.wide_0phase
   stimupy.papers.white1985.wide_36phase
   stimupy.papers.white1985.wide_72phase
   stimupy.papers.white1985.wide_108phase
   stimupy.papers.white1985.wide_144phase
   stimupy.papers.white1985.wide_180phase
   stimupy.papers.white1985.square_0phase
   stimupy.papers.white1985.square_36phase
   stimupy.papers.white1985.square_72phase
   stimupy.papers.white1985.square_108phase
   stimupy.papers.white1985.square_144phase
   stimupy.papers.white1985.square_180phase



.. base-gallery::
   :caption: stimupy.papers.white1985

   wide_0phase
   wide_36phase
   wide_72phase
   wide_108phase
   wide_144phase
   wide_180phase
   square_0phase
   square_36phase
   square_72phase
   square_108phase
   square_144phase
   square_180phase















  