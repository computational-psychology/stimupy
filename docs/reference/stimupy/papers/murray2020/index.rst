



murray2020
==========

.. py:module:: stimupy.papers.murray2020


.. autoapi-nested-parse::

   Stimuli from Murray (2020)

   This module reproduces most of the stimuli used by Murray (2020)
   as they were provided to the model described in that paper
   but normalized between 0 and 1.
   The stimuli are show in Fig 1 of the paper.
   NOTE that the Haze illusion (Fig 1m) is not provided.

   Each stimulus is provided by a separate function,
   which can be listed using

       >>> import stimupy.papers.murray2020
       >>> help(stimupy.papers.murray2020)

   The output of each of these functions is a stimulus dictionary.

   For a visual representation of all the stimuli and their mask,
   simply run this module from the shell

       $ python -m stimuli.papers.murray2020

   or from within python

       >>> from stimupy.utils import plot_stimuli
       >>> from stimupy.papers import murray2020
       >>> plot_stimuli(murray2020.gen_all())

   .. rubric:: References

   Murray, R. F. (2020).
       A model of lightness perception
       guided by probabilistic assumptions about lighting and reflectance.
       Journal of Vision, 20(7), 28.
       https://doi.org/10/gh57gf









































Functions
---------

.. autoapisummary::

   stimupy.papers.murray2020.argyle
   stimupy.papers.murray2020.argyle_control
   stimupy.papers.murray2020.argyle_long
   stimupy.papers.murray2020.snake
   stimupy.papers.murray2020.snake_control
   stimupy.papers.murray2020.koffka_adelson
   stimupy.papers.murray2020.koffka_broken
   stimupy.papers.murray2020.koffka_connected
   stimupy.papers.murray2020.checkassim
   stimupy.papers.murray2020.simcon
   stimupy.papers.murray2020.simcon_articulated
   stimupy.papers.murray2020.white



.. base-gallery::
   :caption: stimupy.papers.murray2020

   argyle
   argyle_control
   argyle_long
   snake
   snake_control
   koffka_adelson
   koffka_broken
   koffka_connected
   checkassim
   simcon
   simcon_articulated
   white















  