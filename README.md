# Stimupy

[![Documentation Status](https://readthedocs.org/projects/stimupy/badge/?version=latest)](https://stimupy.readthedocs.io/en/latest/?badge=latest)

Contains submodules for
- drawing basic visual stimulus components ([components](stimupy/components/))
- creating different (brightness) illusions ([illusions](stimupy/illusions/))
- replicating illusions in certain published papers  ([papers](stimupy/papers/))
converting pixel values to degrees of visual angle ([utils](stimupy/utils/))

For details, please refer to the source directory (stimupy/),
the respective subdirectories and the docstrings.


## Installation

Either install using `pip`:
```python
pip install 'stimupy @ https://github.com/computational-psychology/stimupy'
```

OR (for developers), install from source:
1. Clone the repository from GitHub (TUB):

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
- numpy
- scipy
- matplotlib
- Pillow
- pandas


## Importing
To use in your own code, `import` (from) the modules.
```python
from stimupy import components
from stimupy import noises
from stimupy import illusions
from stimupy import papers
from stimupy import utils
```
