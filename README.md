# Stimuli

Contains submodules for
- creating different stimuli used in lightness perception (lightness)
- creating 2D patterns or renderings of 3D checkerboards with transparent 
layers covering part of the image (transparency)
- creating different random and deterministic textures (texture)
- some helper functions for padding, resizing, computing Munsell values, and
converting pixel values to degrees of visual angle (utils)
- various functions that calculate contrast metrics (contrast_metrics)

For details, please refer to the source directory (src/), the respective subdirectories and the docstrings.

## Dependencies
- Required: numpy, matplotlib, PIL
- Optional: 
    - PovRay (to render variegated checkerboards - submodule transparency.CheckerboardFactory])
    - rpy2 and R (to render textures with specific spatial properties - submodule texture)
 

## Installation
First clone the repository via 

```python
git clone https://github.com/computational-psychology/stimuli.git
``` 

Then run `python setup.py install` at the root of the repository.

The repository may then be removed again.

## Importing
To use in your own code, import the modules. See READMEs in src/ for example usages.
```python
from stimuli.transparency import TextureFactory
from stimuli.transparency import CheckerboardFactory
#from stimuli import contrast_measures as cm
#from stimuli import utils
# (other modules are yet to be fixed)
```