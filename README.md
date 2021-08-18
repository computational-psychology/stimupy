# Stimuli

Contains submodules for
- creating different brightness illusions ([illusions](stimuli/illusions/))
- replicating illusions in certain published papers  ([papers](stimuli/papers/))
- creating 2D patterns or renderings of 3D checkerboards with transparent 
layers covering part of the image ([transparency](stimuli/transparency/))
- various functions that calculate contrast metrics ([contrast_metrics](stimuli/contrest_metrics/))
- some helper functions for padding, resizing, computing Munsell values, and
converting pixel values to degrees of visual angle ([utils](stimuli/utils/))
- (creating different random and deterministic textures ([texture](stimuli/texture/)) [yet to be fixed])

For details, please refer to the source directory (stimuli/), the respective subdirectories and the docstrings.

## Dependencies
- Required: numpy, matplotlib, PIL
- Optional: 
    - [PovRay](http://www.povray.org/) (to render variegated checkerboards - submodule transparency.CheckerboardFactory])
    - rpy2 and R (to render textures with specific spatial properties - submodule texture)
 

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
To use in your own code, import the modules. See READMEs in stimuli/ for example usages.
```python
from stimuli import lightness
from stimuli import illusions
from stimuli.transparency import TextureFactory
from stimuli.transparency import CheckerboardFactory
from stimuli import contrast_metrics as cm
from stimuli import utils
```
