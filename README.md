# Stimupy

Contains submodules for
- drawing basic visual stimulus components ([components](stimupy/components/))
- creating different (brightness) illusions ([illusions](stimupy/illusions/))
- replicating illusions in certain published papers  ([papers](stimupy/papers/))
converting pixel values to degrees of visual angle ([utils](stimupy/utils/))

For details, please refer to the source directory (stimupy/),
the respective subdirectories and the docstrings.

## Dependencies
- Required: numpy, scipy, matplotlib


## Installation
First clone the repository via 

```shell script
git clone https://github.com/computational-psychology/stimuli.git
```

Then run `pip install .` at the root of the repository.
The repository may then be removed again.

To install in developer/editable mode: `pip install -e .` at the root directory.
This makes changes to files immediately usable,
rather than having to reinstall the package after every change.

## Importing
To use in your own code, import (from) the modules.
```python
from stimupy import components
from stimupy import illusions
from stimupy import papers
from stimupy import utils
```
