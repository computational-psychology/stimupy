



white1981
=========

.. py:module:: stimupy.papers.white1981


.. autoapi-nested-parse::

   Stimuli from White (1981)

   This module reproduces most of the stimuli used by White (1981)
   as they were described in that paper.

   Each stimulus is provided by a separate function,
   which can be listed using

       >>> import stimupy.papers.white1981
       >>> help(stimupy.papers.white1981)

   The output of each of these functions is a stimulus dictionary.

   For a visual representation of all the stimuli and their mask,
   simply run this module from the shell

       $ python -m stimuli.papers.white1981

   or from within python

       >>> from stimupy.utils import plot_stimuli
       >>> from stimupy.papers import white1981
       >>> plot_stimuli(white1981.gen_all())

   .. rubric:: References

   White, M. (1981).
       The effect of the nature of the surround on the perceived lightness
       of grey bars within square-wave test grating.
       Perception, 10, 215-230.
       https://doi.org/10.1068/p100215









































Functions
---------

.. autoapisummary::

   stimupy.papers.white1981.square_white
   stimupy.papers.white1981.square_black
   stimupy.papers.white1981.grating_white_white
   stimupy.papers.white1981.grating_white_black
   stimupy.papers.white1981.grating_black_white
   stimupy.papers.white1981.grating_black_black
   stimupy.papers.white1981.grating_white_in
   stimupy.papers.white1981.grating_black_in
   stimupy.papers.white1981.grating_white_out
   stimupy.papers.white1981.grating_black_out
   stimupy.papers.white1981.grating_white_orthogonal
   stimupy.papers.white1981.grating_black_orthogonal



.. base-gallery::
   :caption: stimupy.papers.white1981

   square_white
   square_black
   grating_white_white
   grating_white_black
   grating_black_white
   grating_black_black
   grating_white_in
   grating_black_in
   grating_white_out
   grating_black_out
   grating_white_orthogonal
   grating_black_orthogonal















  