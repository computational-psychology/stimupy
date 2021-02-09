# Stimuli

Contains submodules for
- creating different stimuli used in lightness perception ([lightness](src/lightness/README.md))
- creating different brightness illusions ([illusions](src/illusions/README.md))
- creating 2D patterns or renderings of 3D checkerboards with transparent 
layers covering part of the image ([transparency](src/transparency/README.md))
- various functions that calculate contrast metrics ([contrast_metrics](src/contrest_metrics/README.md))
- some helper functions for padding, resizing, computing Munsell values, and
converting pixel values to degrees of visual angle ([utils](src/utils/README.md#utils))
- (creating different random and deterministic textures ([texture](src/texture/README.md)) [yet to be fixed])

For details, please refer to the source directory (src/), the respective subdirectories and the docstrings.

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

Then run `python setup.py install` at the root of the repository.

The repository may then be removed again.

To update to a newer version, run `python setup.py install --force`.

## Importing
To use in your own code, import the modules. See READMEs in src/ for example usages.
```python
from stimuli import lightness
from stimuli import illusions
from stimuli.transparency import TextureFactory
from stimuli.transparency import CheckerboardFactory
from stimuli import contrast_metrics as cm
from stimuli import utils
```
