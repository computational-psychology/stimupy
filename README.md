# Stimupy

[![Documentation Status](https://readthedocs.org/projects/stimupy/badge/?version=latest)](https://stimupy.readthedocs.io/en/latest/?badge=latest)

`Stimupy` is a pure-Python package
for creating new and exiting visual stimuli
commonly used in the sudy of contrast, brightness/lightness,
and other aspects of visual perception.

## Core features:
Stimupy has been designed to generate stimuli from code,
so that they are reproducible, flexible, and easy.
- Stimuli available through stimupy are:
  - basic visual stimulus [components](stimupy/components/),
    such as basic shapes, gratings, Gaussians, Gabors
  - visual [noise](stimupy/noises/) textures, of different kinds,
  - and many different stimuli commonly referred to as [illusions](stimupy/illusions/)
    with some special regions of interest,
    such as Simultaneous Brightness Contrast, White's illusion,
    but also Hermann Grids, checkerboards, Ponzo illusion, etc.

- All these stimuli are fully parameterizable
  with interpretable parameters that are relevant to vision scientists
  (e.g. visual angle, spatial frequency, target placements).
  - This also makes it possible to explore stimulus parameter spaces
    which might reveal relations between formerly unconnected stimuli

- Stimuli are also composable/composed:
`illusions` tend to be composed from several `components`.

- Generated stimuli are output as a Python `dict`ionary,
containing the stimulus-image as a NumPy-array,
together with other useful stimulus-specific information
(e.g. (target) masks, sizes etc.).
    - Since Python dictionaries are mutable data structures (compared to objects),
      they allow the user to add additional information easily.
    - The image as NumPy-array (rather than, e.g., an OpenGL texture),
      makes these stimuli fully interoperablye using common NumPy tooling.

- In addition, we provide many [utils](stimupy/utils/) functions
  to apply common operations to either the images, or the full stimulus-`dict`s.

- Reuse of existing stimuli and stimulus sets should be a key aim,
  so also included are exact replications of stimuli previously published (e.g. ModelFest)
  as described in their respecive [papers](stimupy/papers/)

See the [documentation](https://stimupy.readthedocs.io/en/latest/) for more details

## Your stimulus (set) is not here?
Given the modular nature of the package,
any stimulus or stimulus set not currently available, can be easily added.
Open an [issue](https://github.com/computational-psychology/stimupy/issues/new)
and let us know what you'd like to see added.

If you want to contribute yourself, see [contributing](#contributing-to-stimupy)



## Installation

For now, `pip` can install directly from GitHub (the `main` branch)
GitHub repository
```python
pip install https://github.com/computational-psychology/stimupy/zipball/main
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

## Citing stimupy

## Contributing to stimupy
1. *Fork* the [GitHub repository](https://github.com/computational-psychology/stimupy/)
2. *Clone* the repository to your local machine
3. *Install* `stimupy` using the developer install: `pip install -e ".[dev]"`
4. *Edit* the code:
    - To contribute a stimulus set, add it to `stimupy/papers/`
    - To contribute a stimulus function, add it to the relevant directory
5. *Commit & Push* to your fork
6. *Pull request* from your fork to our repository