---
title: 'PyStim: A Python stimulus creation package for vision science'
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
 - name: Science of Intelligence, Technische Universitaet Berlin, Germany
   index: 1
 - name: Computational Psychology, Technische Universitaet Berlin, Germany
   index: 2
date: 25 December 2022
bibliography: bibliography.bib
---


# Summary

[PyStim](change) is a Python package for creating visual stimuli which are commonly used to study the human visual system.
These include basic shapes, a variety of gratings, different noises and other relevant visual phenomena (e.g. checkerboards, Cornsweet stimulus, White stimulus).

The main purpose of [PyStim](change) is to support vision science by providing a large, openly-available and flexible battery of relevant visual stimuli.
Its key feature is that all stimulus-functions are highly parameterized with parameters that vision scientists care about, such as visual angle, spatial frequency, or target placements to name a few.
[PyStim](change) is designed in a modular fashion, i.e. more complex stimuli are composed of less complex stimuli.
The output of all stimulus functions is a dictionary which contains the stimulus-array but also other potentially useful information such as (target) masks, sizes and other stimulus-specificities.
Using dictionaries is useful because it allows for any additional information (including stimulus specificities or experimental data) to be added.

Given the flexibility of the stimulus functions, [PyStim](change) can be used to re-create many stimuli that have been used in prior vision research or create entirely new stimuli.
This is particularly useful to built stimulus benchmarks which can be easily accessed by the community.
As a second key feature, [PyStim](change) therefore provides a selection of stimulus sets (e.g. ModelFest) as they have been used in the original manuscripts including their experimental findings.
Given the modular nature of the package, any stimulus or stimulus set that is currently not available can be easily added in the future.

Finally, [PyStim](change) allows for exploration of parameter spaces underlying the individual stimulus functions.
This can support both experimental as well as theoretical work in vision science.
As such, exploring parameter spaces can in itself provide insights into the kind of stimuli we use in vision science, e.g. by revealing how certain stimuli are connected or by exploring their edge cases.
On the other hand, the exploration of certain parameter spaces along a single or multiple dimensions can be directly mapped to research questions that we want to study in our field.

Building blocks of [PyStim](change):

- Stimulus components containing basic shapes, gratings, and Gaussians ([components](link))
- Different kinds of noise which are commonly used for noise-masking experiments ([noise](link))
- Visual illusions containing a variety of stimuli commonly referred to as illusions such as White's stimulus, the Hermann grid and many more ([illusions](link))
- Stimulus sets as used in the original research, including ModelFest and stimuli from lightness research ([papers](link))
- Many utility functions, e.g. for manipulating (e.g. contrast, size), importing, exporting or plotting stimuli ([utils](link))
- Demonstrations of all stimulus functions using (interactive) Jupyter Notebooks ([demos](link))
- Elaborate test cases ([tests](link))


# Statement of Need

Visual stimuli are one of the core concepts to elucidate the mechanisms underlying visual processing.
Though not complete, there are types of stimuli which are commonly used.
Despite their relevance, there is little software (but see related software) which supports the creation of many stimuli parameterized in a way which is targeted towards vision science.
Hence, most vision research requires to implement stimuli from scratch.
Depending on the complexity of these stimuli, this endeavor can be time-consuming, prone to error and can make comparison with other research harder.
This is where [PyStim](change) comes into place.

[PyStim](change) is an openly-available Python package for creating a multitude of visual stimuli in a parameterized way and is targeted towards the needs of vision science.
It can be easily downloaded and installed via github and pip.
Using [PyStim](change) can improve the consistency and accessibility of visual stimuli in the field, while helping to avoid bugs.
Given its modular and application-oriented nature, [PyStim](change) supports the use and design of visual stimuli for studying visual perception.
This is particularly useful because varying stimuli along one or multiple of the provided dimensions can be directly mapped to certain experimental designs.

Another challenge in some vision disciplines is the need for benchmark datasets [@carney1999, @murray2021].
These are particularly relevant to test the validity of vision models, hence support the understanding of visual mechanisms.
The usefulness of benchmarks have been shown in spatial vision with the ModelFest dataset [@carney1999, @carney2000] but also in various applications of computer vision including object recognition [@deng2009] or object segmentation [@martin2001].
However, visual stimuli from previous vision research are not always accessible and the creation of visual stimuli can be challenging.
Therefore, creating and agreeing on a benchmark dataset is not trivial.
To support this process and facilitate the accessibility of previously used stimuli, [PyStim](change) provides a collection of stimulus sets (including ModelFest) as they have been used in the original manuscripts.
Hence, entire stimulus sets (including experimental findings) can be accessed via a single line of code.

Finally, due to its high degree of parameterizability, [PyStim](change) allows for extensive explorations of stimulus spaces.
This can be useful for vision experiments because varying stimuli along one or multiple dimensions can be mapped to certain experimental designs.
Moreover, this feature can also guide theoretical work because it allows to find so-called maximally-differentiable stimuli [@wang2008].
The basic idea of maximum differentiation is to analyze model predictions for systematically varied stimuli to find the ones which differentiate best between models.
Like this, the number of stimuli tested experimentally can be reduced to the most relevant stimuli.
Since collecting (human) data is resourceful, maximal differentiation is a useful method to reduce theoretically large stimulus parameter spaces to a testable number of stimuli.

Key features of [PyStim](change):

- modular, open-source and unifying software for creating many visual stimuli,
- functions tailored towards the needs of vision science,
- highly parameterized stimulus functions with many use-cases,
- easily accessible stimulus sets from previous vision research,
- application-oriented documentation using (interactive) Jupyter Notebooks,
- flexible design which facilitates future development.


# Projects Using the Software

As stimulus creation is relevant for many vision science projects, stimulus functions which are part of [PyStim](change) or a pre-release version of the software have been used in almost all of the work of our laboratory within the last two years.
Some of [PyStim](change)'s noise functions have been used to generate the narrowband noise masks of varying center frequency in [@schmittwilken2022b].
A pre-release version was used in multiple conference contributions in which we ... (joris vss 2021) [@vincent2021], in which we compared existing models of human brightness perception on a large battery of brightness stimuli [@schmittwilken2022a], in which we (joris ecvp 2022) [@vincent2022], and in which we studied human edge processing with Cornsweet stimuli in various kinds of noise (white, pink, brown, several narrowband noises) [@schmittwilken2022c].
All these stimuli were created with [PyStim](change) or functions that are included in the software.
Moreover, we are using [PyStim](change) in ongoing work in our laboratory and in many student projects.


# Related Software

Since the creation of visual stimuli is a central topic in vision sciences, there exist some software which fulfills partial or related needs as [PyStim](change).
These are

- Psychtoolbox [@brainard1997],
- Psychopy [@peirce2019],
- Pyllusion [@makowski2021].

Vision experiments require profound control over the hardware at hand for precise stimulus display.
In their essence, Psychtoolbox and Psychopy support this process by interfacing between the computer hardware and Matlab (Psychtoolbox) and Python (Psychopy).
Hence, Pychtoolbox and Psychopy facilitate hardware control for vision experimentation via Matlab and Python.
Though their main focus is on hardware control, Psychtoolbox and Psychopy also provide functions for generating stimuli.
These include lines, basic shapes, gratings and Gaussian noise, as well as some dynamic displays and sound.

Other recent software which recognized the need for unified and automatized stimulus creation is Pyllusion.
Pyllusion is a framework to generate optical illusions systematically using parameters which are relevant for vision experimentation (e.g. illusion strength).
This parametric approach of Pyllusion is in spirit very similar to [PyStim](change).

Besides, there exist no software to access existing stimulus sets in vision science.
The two most common practices are to re-implement the stimuli in an idiosyncratic fashion or to import static stimulus files (image or data files; see e.g. @carney1999, @murray2020).

Within [PyStim](change), we combined and extended these software features and practices to unify and support stimulus creation and accessibility.
Compared to existing software, it contains a wide variety of visual stimuli which are all highly parameterizable and tailored towards vision science, and it can be used to access whole stimulus sets from previous vision research within a single line of code.
On top of that, the output dictionaries of the stimulus functions can store useful stimulus information , such as (target) masks and experimental data if applicable.
This is useful for comparing experimental findings and for developing and testing models of human vision.


# Future Work

In theory, there is an infinite number of stimuli which are or could be interesting in the future of vision research.
Hence, [PyStim](change) will by default remain under active development.
In future versions, we want to add more visual stimuli and more stimulus sets - particularly dynamic stimuli which are currently not included.
Finally, we want to foster the development of stimulus benchmarks in vision science which will be added to [PyStim](change).


# Acknowledgements

Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany's Excellence Strategy -EXC 2002/1 "Science of Intelligence"- project number 390523135 and individual grants MA 5127/4-1 and 5-1 to M. Maertens

# References

<div id="refs"></div>

\pagebreak
\appendix




