# Stimupy

<p align=center>
A pure-Python package
for creating new and existing visual stimuli
commonly used in the study of contrast, brightness, lightness,
and other aspects of visual perception.
</p>

<p align=center>

[![JOSS Status](https://joss.theoj.org/papers/af54c793f6f4c02a4af6a8b5f6f57e9d/status.svg)](https://joss.theoj.org/papers/af54c793f6f4c02a4af6a8b5f6f57e9d)
[![PyPI version](https://img.shields.io/pypi/v/stimupy)](https://pypi.org/project/stimupy/)
[![Tests](https://github.com/computational-psychology/stimupy/actions/workflows/test.yml/badge.svg)](https://github.com/computational-psychology/stimupy/actions/workflows/test.yml)
[![Py versions](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/stimupy/badge/?version=latest)](https://stimupy.readthedocs.io/en/latest/?badge=latest)
</p>

<p align=center>
<img src=docs/logo.png width=400>
</p>

---
- documentation: https://stimupy.readthedocs.io/en/latest/
- source code: https://github.com/computational-psychology/stimupy
---

`stimupy` has been designed to:

- *generate* (novel) visual stimuli in a reproducible, flexible, and easy way
- *recreate* exact stimuli as they have been used in prior vision research 
- *explore* large parameter spaces to reveal relations between formerly unconnected stimuli
- *provide* classic stimulus sets (e.g. ModelFest),
  exactly as described in the original manuscripts (including experimental data)
- *build* new stimulus sets or benchmarks (e.g. for testing computational models),
  and easily add them to `stimupy`
- *support* vision science by providing a large, openly-available and flexible battery of relevant stimulus functions
- *unify* and *automate* stimulus creation
- be [**FAIR**](https://doi.org/10.1038/s41597-022-01710-x):
  **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable

---
## Core features:
Stimupy has been designed to generate stimuli from code,
so that they are reproducible, flexible, and easy.

- basic visual stimulus [components](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.components.html),
  such as basic shapes, wave gratings, Gaussians
- visual [noise](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.noises.html) textures, of different kinds,
- many different parameterized visual [stimuli](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.stimuli.html)
  - Gabors, plaids, edges,
  - a variety of so-called illusions 
   (e.g. Simultaneous Brightness Contrast, White's illusion, Hermann grid, Ponzo illusion), and many more

- exact replications of stimuli previously published (e.g. ModelFest)
  as described in their respecive [papers](stimupy/papers/)

- all stimuli are fully parameterizable
  - with interpretable parameters that are familiar and relevant to vision scientists
    (e.g. visual angle, spatial frequency, target placements).
  - This also makes it possible to explore stimulus parameter spaces
    which might reveal relations between formerly unconnected stimuli

- stimuli are composable/composed:
  - `stimuli` tend to be composed from several `components`,
  and these provided building blocks and masks
  can be used to assemble more complicated geometries

- flexible output structures
  - generated stimuli are Python `dict`ionary
    - mutable data structures (compared to objects),
      so they allow the user to add additional information easily
      (e.g. stimulus descriptions, stimulus masks, experimental data).
  - containing the stimulus-image as a NumPy-array,
    - makes images fully interoperable using common NumPy tooling
      (rather than, e.g., an OpenGL texture),
  - together with other useful stimulus-specific information
    (e.g. (target) masks, sizes etc.).

- modular and therefore easy to extend with new stimulus functions,
  and new stimulus sets
 
- [utility functions](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.utils.html)
  for stimulus import, export, manipulation (e.g. contrast, size), or plotting

- application-oriented documentation [documentation](https://stimupy.readthedocs.io/en/latest/index.html),
  including [interactive demonstrations](https://stimupy.readthedocs.io/en/latest/reference/demos.html) of stimulus functions

- unit and integration [tests](https://github.com/computational-psychology/stimupy/actions/workflows/test.yml)


See the [documentation](https://stimupy.readthedocs.io/en/latest/) for more details

![A small fraction of the stimulus variety that ``stimupy`` can produce \label{fig:overview}](manuscript/overview.png)

---

## Citing stimupy

## Your stimulus (set) is not here?
Given the modular nature of the package,
any stimulus or stimulus set not currently available, can be easily added.
Open an [issue](https://github.com/computational-psychology/stimupy/issues/new)
and let us know what you'd like to see added.

If you want to contribute yourself, see [contributing](https://stimupy.readthedocs.io/en/latest/contributing/contribute.html)


---
## Installation

`pip` can install `stimupy` directly PyPI:
```python
pip install stimupy
```

OR (for developers), install from source:
1. Clone the repository from GitHub:

    ```bash
    git clone git@github.com:computational-psychology/stimupy.git
    ```

2. `stimupy` can then be installed using pip.
    From top-level directory run:

    ```python
    pip install .
    ```

    to install to your local python library.

To install in developer/editable mode: `pip install -e .` at the root directory.
This makes changes to files immediately usable,
rather than having to reinstall the package after every change.

### Dependencies
Dependencies should be automatically installed (at least using `pip`).
`stimupy`s required dependencies are:
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [matplotlib](https://matplotlib.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)

