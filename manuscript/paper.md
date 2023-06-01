---
title: '`stimupy`: A Python package for creating stimuli in vision science'
tags:
  - Python package
  - vision science
  - stimulus creation
authors:
  - name: Lynn Schmittwilken
    orcid: 0000-0003-3621-9576
    equal-contrib: false
    corresponding: true
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Marianne Maertens
    equal-contrib: false
    affiliation: "1, 2"
  - name: Joris Vincent
    orcid: 0000-0001-6882-5584
    affiliation: 2
affiliations:
 - name: Science of Intelligence, Technische Universität Berlin, Germany
   index: 1
 - name: Computational Psychology, Technische Universität Berlin, Germany
   index: 2
date: 24 March 2023
bibliography: bibliography.bib
---


# Summary

Visual stimuli are at the heart of perception research.
They may come as visual illusions which demonstrate the striking differences
between the perceptual and physical world,
they may involve minuscule stimulus changes
which are used to probe the limits of visual sensitivity,
or they may be used to probe any other aspect of visual processing.
`stimupy` is a free and open-source Python package
which allows the user to create visual stimuli
of different complexity as they are commonly used in the study of visual perception
(\autoref{fig:overview}).

`stimupy` provides functions to generate:

- basic [components](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.components.html),
  including shapes, lines, gratings, checkerboards, and Gaussians
- different types of visual [noise](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.noises.html) textures
- visual [stimuli](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.stimuli.html)
  such as Gabors, plaids, edges, and a variety of so-called illusions
  (e.g., Simultaneous Brightness Contrast, White's illusion, Hermann grid, Ponzo illusion), and many more
- stimulus sets from prior research papers, providing exact stimulus recreations (e.g., ModelFest, @carney1999)
- [utility functions](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.utils.html)
  for stimulus import, export, manipulation (e.g., contrast, size), or plotting
- [documentation](https://stimupy.readthedocs.io/en/latest/index.html),
  including [interactive demonstrations](https://stimupy.readthedocs.io/en/latest/reference/demos.html) of stimulus functions
- unit and integration [tests](https://github.com/computational-psychology/stimupy/actions/workflows/test.yml)

`stimupy` has been designed to:

- generate (novel) visual stimuli in a reproducible, flexible, and easy way
- recreate exact stimuli as they have been used in prior vision research
- explore large parameter spaces to reveal relations between formerly unconnected stimuli
- provide classic stimulus sets (e.g., ModelFest),
  exactly as described in the original manuscripts (including experimental data)
- build new stimulus sets or benchmarks (e.g., for testing computational models),
  and easily add them to `stimupy`
- support vision science by providing a large, openly-available and flexible battery of relevant stimulus functions
- unify and automate stimulus creation

![A small fraction of the stimulus variety that ``stimupy`` can produce \label{fig:overview}](overview.png)


# State of the field
Creating visual stimuli is a central task in vision research.
To generate stimuli, it is common practice to
either write your own stimulus functions from scratch;
reuse existing code;
or import a static stimulus version from an image or data file
(see e.g., @carney1999, @murray2020).
The alternative to these idiosyncratic approaches
is to use existing software which provides more flexible stimulus functions.

We are currently aware of

- Psychtoolbox [@brainard1997],
- Psychopy [@peirce2019],
- Pyllusion [@makowski2021],
- OCTA [@OCTA].

Psychtoolbox and Psychopy both provide functions to generate a number of visual stimuli.
However, stimulus generation is integrated into their main purpose
which is to run psychophysical experiments.
The design focus of both Psychtoolbox and Psychopy has therefore been
to support the user to interface between computer hardware and MATLAB and Python,
respectively,
to enable temporal precision and high dynamic range stimulus delivery.

The design focus of `stimupy` is on stimulus creation.
This allows `stimupy` to include many more stimuli
than included in Psychtoolbox or Psychopy.
It also allows the user to interact with the stimulus arrays directly.
This makes it easy to manipulate the stimulus and use it
for other purposes than psychophysical experimentation
(e.g., computational modeling, visualization).
This also means that in order to present the stimuli on a computer monitor,
the user may still want to use Psychopy, Psychtoolbox
or another delivery system for hardware control.

Pyllusion is a Python package to generate a number of well-known illusions
such as the Müller-Lyer, Ponzo or Zöllner illusions, and more.
Pyllusion provides functions for each of these illusions using high-level parameters
(e.g., illusion strength).
The parametric approach of Pyllusion is similar in spirit to `stimupy`.
However, in Pyllusion each illusion-function stands alone:
it produces only that stimulus, and its arguments are unique to that stimulus.
In contrast, `stimupy` provides a unified interface to stimulus creation,
where many functions share the same —intuitive— parameters.
This makes it easier to explore parameters and to create novel stimuli.

OCTA is also a Python package to generate stimuli,
specifically grids of multiple elements that can be show regularity and variety
along various stimulus dimensions.
These stimuli are of particular use to studies on Gestalt vision,
aesthetics and complexity.
The parametric variation of stimulus dimensions
as well as the compositionality of displays
are features found in both OCTA and `stimupy`.
Both packages also have a strong focus on ease-of-use, replicability, and open science.
`stimupy` currently focuses on a different class of stimuli:
mainly displays used to study early and low-level visual processes,
as well as visual features such as brightness, contrast, and orientation.
Thus, OCTA and `stimupy` cover complementary usecases.

Another design decision that sets `stimupy` apart from existing software such as OCTA and Pyllusion,
is that all `stimupy` stimuli are generated as `NumPy`-arrays
representing pixel-based raster-graphics (NumPy, @harris2020).
This has several advantages over existing, vector-graphics or custom object-based approaches,
mainly that any standard array-manipulation tooling can be used to further process
a stimulus.

# Statement of Need

Many visual stimuli are used time and again.
Despite their relevance, there is no standard way of implementing stimuli
which considers function parameters in a way that is targeted towards vision science.
Hence, in practice, researchers implement their own stimuli from scratch
or are lucky enough to find some existing implementation online,
from colleagues or in the above mentioned software packages.
Depending on the complexity or specificity of the desired stimulus manipulation,
this endeavor is (1) time-consuming, (2) prone to error,
and (3) makes comparisons with other research difficult.
Hence, we developed `stimupy` to simplify, unify and automate visual stimulus generation 
while at the same time allowing the flexibility
to create entirely new stimuli and build stimulus benchmarks.

As far as we know `stimupy` is the only package that:

- contains a wide variety of visual stimuli, from simple geometric shapes to complex illusions
- includes ready-to-use replications of existing stimulus sets (e.g., ModelFest)
- makes it easy to create new stimuli because (1) stimulus functions
  use parameters which are familiar to vision scientists,
  and (2) it provides building blocks and masks which can be used to assemble more complicated geometries
- uses flexible output structures (NumPy arrays, and Python dictionaries)
  and hence makes it easy to interact with the stimulus arrays
  and store additional information
  (e.g., stimulus descriptions, stimulus masks, experimental data)
- is modular and therefore easy to extend with new stimulus functions,
  and new stimulus sets
- is hierarchical in a sense that more complex stimulus functions
  (e.g., visual illusions) use more basic stimulus functions (e.g., components)
- comes with application-oriented documentation, including interactive Jupyter Notebooks [@kluyver2016]

`stimupy` is a free and open-source Python package
which can be easily downloaded and installed via standard package managers,
or directly from its GitHub source.
We think that using `stimupy` will improve the consistency
and accessibility of visual stimuli while helping to avoid bugs.
A key feature in `stimupy` is that its functions are parameterized
with parameters that are relevant to vision scientists
(e.g., visual angle, spatial frequency, target placements).
Moreover, `stimupy` is designed in a modular fashion,
i.e. more complex stimuli are composed of less complex stimuli,
which supports the understanding of existing stimuli,
makes connections between stimuli explicit,
and facilitates the creation of novel stimuli.
The output of all stimulus functions is a dictionary
which contains the stimulus-image as a NumPy-array
together with other useful stimulus information
(e.g., masks, stimulus parameters, and experimental data).
Having the stimulus-image as a NumPy-array makes it easy to work
and interact with the stimulus,
e.g., using common NumPy tooling and/or utility functions provided by `stimupy`.
This is useful for manipulating the stimulus as well as for using the stimulus
for other purposes than psychophysical experimentation on a computer screen
(e.g., for visualizations or for computational modeling).
The main advantage of using dictionaries as function outputs is that
Python dictionaries are mutable data structures
which allow you to add additional information easily.
Taken together,
these design choices make `stimupy` a flexible and versatile Python package
which facilitates the (re)creation and use of visual stimuli for a variety of purposes.

Another important use case for `stimupy` is the evaluation of computational vision models.
A common strategy to validate computational vision models
is to test them with benchmark datasets; e.g. in spatial vision [@carney1999],
lightness perception [@murray2021], object recognition [@deng2009], or object segmentation [@martin2001].
However, visual stimuli from prior research are not always publicly available
and it is thus difficult and time-consuming
to test model performance on stimuli from prior research.
On top of that, creating and agreeing on benchmark datasets is a challenging task.
Hence, to support the accessibility of previously used stimuli
and encourage the creation of stimulus benchmarks,
`stimupy` provides a collection of existing stimulus sets (including ModelFest)
as they have been used in the original manuscripts.
Due to `stimupy`’s versatility, entire stimulus sets (including experimental findings)
can be accessed via a single line of code,
and more stimulus sets can be added at any point in time.

![Samples from a parameter space of a single ``stimupy`` stimulus function: \label{fig:stimspace}](stimspace.png)

`stimupy`'s high degree of parameterizability allows for extensive explorations
of stimulus parameter spaces (\autoref{fig:stimspace}).
On the one hand, this can be useful for vision experimentation
because varying stimuli along one or multiple dimensions
can be directly mapped to certain experimental designs and research questions.
On the other hand, this feature can also guide theoretical work because
among other things it allows to find so-called
maximally-differentiable stimuli [@wang2008].
The basic idea of maximum differentiation is to analyze model predictions
for systematically varied stimuli
to find the ones which differentiate best (maximally) between models.
Like this, the number of stimuli tested experimentally can be reduced to the most relevant stimuli.
Since collecting (human) data is resourceful,
maximal differentiation is a useful method
to reduce theoretically large stimulus parameter spaces to a testable number of stimuli.

Last but not least,
`stimupy` can be a useful aid in teaching contexts
because it provides students with a basic framework
in which they can design and interact with stimuli in a playful way.
Since `stimupy` is focused on stimulus creation rather than stimulus presentation,
a user can quickly generate complex and innovative stimuli
– even with beginner knowledge of Python.
The parameterized functions and the interactive documentation
allow for easy teaching and communication
of how various stimulus parameters affect perception.


# Projects Using the Software

As stimulus creation is relevant for many vision science projects,
stimulus functions which are part of `stimupy` or a pre-release version of the software
have been used in almost all of the work of our laboratory within the last two years.
Some of `stimupy`'s noise functions have been used to generate the narrowband noise masks of varying center frequency in [@schmittwilken2022b].
A pre-release version was used in multiple conference contributions
in which we compared structural elements between existing models of brightness perception [@vincent.maertens2021a];
in which we compared existing models of human brightness perception on a large battery of brightness stimuli [@schmittwilken2022a];
in which we evaluated how to quantitatively link output of computational models to human brightness perception data [@vincent.maertens2021];
in which we demonstrate that a family of computational models
fails to account for novel brightenss perception data [@vincent.maertens.ea2021; @aguilar.maertens.ea2022; @vincent.maertens.ea2022]
and in which we studied human edge processing with Cornsweet stimuli in various kinds of noise
(white, pink, brown, several narrowband noises) [@schmittwilken2022c].
All these stimuli were created with `stimupy` or functions that are included in the software.
Moreover, we are using `stimupy` in ongoing work in our laboratory and in many student projects.


# Future Work

In theory, there is an infinite number of stimuli which are or could be interesting in the future of vision research.
Hence, `stimupy` will by default remain under active development.
In future versions, we want to add more visual stimuli and more stimulus sets
-- particularly dynamic stimuli which are currently not included.
Finally, we want to foster the development of stimulus benchmarks in vision science which will be added to `stimupy`.


# Acknowledgements

Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)
under Germany's Excellence Strategy -EXC 2002/1 "Science of Intelligence"- project number 390523135
and individual grants MA 5127/4-1 and 5-1 to M. Maertens

# References

<div id="refs"></div>

\pagebreak
\appendix




