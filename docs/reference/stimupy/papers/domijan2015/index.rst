



domijan2015
===========

.. py:module:: stimupy.papers.domijan2015


.. autoapi-nested-parse::

   Stimuli from Domijan (2015)

   This module reproduces all of the stimuli used by Domijan (2015)
   as they were provided to the model described in that paper.
   Since the stimulus sizes were only defined in pixel-space,
   there is some ambiguity with respect to the stimulus sizes in
   degrees visual angle.
   To help solve this ambiguity, we approximated a realistic resolution
   of the stimuli (ppd = 10) which is set as default value.
   However, because of the ambiguity, it is possible to change the
   stimulus sizes by providing at least two of the following: a shape
   (in pixels), a visual_size (in degrees) and/or a resolution (in ppd).

   Each stimulus is provided by a separate function,
   which can be listed using

       >>> import stimupy.papers.domijan2015
       >>> help(stimupy.papers.domijan2015)

   The output of each of these functions is a stimulus dictionary.

   For a visual representation of all the stimuli and their mask,
   simply run this module from the shell

       $ python -m stimuli.papers.domijan2015

   or from within python:

       >>> from stimupy.utils import plot_stimuli
       >>> from stimupy.papers import domijan2015
       >>> plot_stimuli(domijan2015.gen_all())

   .. rubric:: References

   Domijan, D. (2015).
       A neurocomputational account
       of the role of contour facilitation in brightness perception.
       Frontiers in Human Neuroscience, 9, 93.
       https://doi.org/10.3389/fnhum.2015.00093









































Functions
---------

.. autoapisummary::

   stimupy.papers.domijan2015.dungeon
   stimupy.papers.domijan2015.cube
   stimupy.papers.domijan2015.grating
   stimupy.papers.domijan2015.rings
   stimupy.papers.domijan2015.bullseye
   stimupy.papers.domijan2015.simultaneous_brightness_contrast
   stimupy.papers.domijan2015.white
   stimupy.papers.domijan2015.benary
   stimupy.papers.domijan2015.todorovic
   stimupy.papers.domijan2015.checkerboard_contrast_contrast
   stimupy.papers.domijan2015.checkerboard
   stimupy.papers.domijan2015.checkerboard_extended
   stimupy.papers.domijan2015.white_yazdanbakhsh
   stimupy.papers.domijan2015.white_anderson
   stimupy.papers.domijan2015.white_howe



.. base-gallery::
   :caption: stimupy.papers.domijan2015

   dungeon
   cube
   grating
   rings
   bullseye
   simultaneous_brightness_contrast
   white
   benary
   todorovic
   checkerboard_contrast_contrast
   checkerboard
   checkerboard_extended
   white_yazdanbakhsh
   white_anderson
   white_howe















  