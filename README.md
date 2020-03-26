## Stimuli

Contains submodules for
- creating different lightness illusions (lightness)
- creating different textures (texture)
- creating 2D patterns or renderings of 3D checkerboards with transparent 
layers covering part of the image (transparency)
- some helper functions for padding, resizing, computing Munsell values, and
converting pixel values to degrees of visual angle (utils)
- various contrast measure functions (contrast_measures)

For details, please refer to the source directory and the respective subdirectories.

## Dependencies
- Required: numpy, matplotlib, PIL
- Optional: 
    - PovRay (transparency.CheckerboardFactory)
    - rpy2 (texture)
 

### Installation
First clone the repository via 

`git clone https://github.com/computational-psychology/stimuli.git`. 

Then run `python setup.py install` at the root of the repository.

The repository may then be removed again.

## Importing
```
from stimuli.transparency import TextureFactory
from stimuli.transparency import CheckerboardFactory
from stimuli import contrast_measures as cm
from stimuli import utils
# (other modules are yet to be fixed)
```