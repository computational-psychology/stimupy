---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{tip}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/sbcs.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - SBCs (Simultaneous Brightness Contrast)
{py:mod}`stimupy.stimuli.sbcs`



## Generalized
{py:func}`stimupy.stimuli.sbcs.generalized`

```{code-cell} ipython3
import param

class GeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    target_x = param.Number(default=3.0, bounds=(0, 10), step=0.1, doc="Target X position")
    target_y = param.Number(default=3.0, bounds=(0, 10), step=0.1, doc="Target Y position")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "target_position": (self.target_y, self.target_x),
            "rotation": self.rotation,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive generalized
generalized_params = GeneralizedParams()
disp = InteractiveStimDisplay(generalized, generalized_params)
disp.layout
```

## Basic
{py:func}`stimupy.stimuli.sbcs.basic`

```{code-cell} ipython3
import param

class BasicParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import basic
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive basic
basic_params = BasicParams()
disp = InteractiveStimDisplay(basic, basic_params)
disp.layout
```

## Square
{py:func}`stimupy.stimuli.sbcs.square`

```{code-cell} ipython3
import param

class SquareParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Target radius")
    surround_radius = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Surround radius")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_surround = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin position")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": self.target_radius,
            "surround_radius": self.surround_radius,
            "rotation": self.rotation,
            "intensity_surround": self.intensity_surround,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import square
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square
square_params = SquareParams()
disp = InteractiveStimDisplay(square, square_params)
disp.layout
```

## Circular
{py:func}`stimupy.stimuli.sbcs.circular`

```{code-cell} ipython3
import param

class CircularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Target radius")
    surround_radius = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Surround radius")
    intensity_surround = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin position")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": self.target_radius,
            "surround_radius": self.surround_radius,
            "intensity_surround": self.intensity_surround,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import circular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular
circular_params = CircularParams()
disp = InteractiveStimDisplay(circular, circular_params)
disp.layout
```

## Basic, Two sided
{py:func}`stimupy.stimuli.sbcs.basic_two_sided`

```{code-cell} ipython3
import param

class BasicTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_background_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left background intensity")
    intensity_background_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_background": (self.intensity_background_left, self.intensity_background_right),
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import basic_two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive basic_two_sided
basic_two_sided_params = BasicTwoSidedParams()
disp = InteractiveStimDisplay(basic_two_sided, basic_two_sided_params)
disp.layout
```

## Square, Two sided
{py:func}`stimupy.stimuli.sbcs.square_two_sided`

```{code-cell} ipython3
import param

class SquareTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius")
    target_radius_right = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius")
    surround_radius_left = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius")
    surround_radius_right = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius")
    rotation_left = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Left rotation in degrees")
    rotation_right = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Right rotation in degrees")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_surround_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity")
    intensity_surround_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "rotation": (self.rotation_left, self.rotation_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import square_two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_two_sided
square_two_sided_params = SquareTwoSidedParams()
disp = InteractiveStimDisplay(square_two_sided, square_two_sided_params)
disp.layout
```

## Circular, Two sided
{py:func}`stimupy.stimuli.sbcs.circular_two_sided`

```{code-cell} ipython3
import param

class CircularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius")
    target_radius_right = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius")
    surround_radius_left = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius")
    surround_radius_right = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_surround_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity")
    intensity_surround_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import circular_two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular_two_sided
circular_two_sided_params = CircularTwoSidedParams()
disp = InteractiveStimDisplay(circular_two_sided, circular_two_sided_params)
disp.layout
```

## With dots
{py:func}`stimupy.stimuli.sbcs.with_dots`

```{code-cell} ipython3
import param

class WithDotsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=15, bounds=(10, 20), doc="Height in degrees")
    width = param.Integer(default=15, bounds=(10, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    n_dots_y = param.Integer(default=5, bounds=(2, 10), doc="Number of dots Y")
    n_dots_x = param.Integer(default=5, bounds=(2, 10), doc="Number of dots X")
    dot_radius = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Dot radius")
    distance = param.Number(default=0.25, bounds=(0.1, 1), step=0.05, doc="Distance between dots")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_dots = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Dots intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_dots": (self.n_dots_y, self.n_dots_x),
            "dot_radius": self.dot_radius,
            "distance": self.distance,
            "target_shape": (self.target_height, self.target_width),
            "intensity_background": self.intensity_background,
            "intensity_dots": self.intensity_dots,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import with_dots
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive with_dots
with_dots_params = WithDotsParams()
disp = InteractiveStimDisplay(with_dots, with_dots_params)
disp.layout
```

## Dotted
{py:func}`stimupy.stimuli.sbcs.dotted`

```{code-cell} ipython3
import param

class DottedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=15, bounds=(10, 20), doc="Height in degrees")
    width = param.Integer(default=15, bounds=(10, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    n_dots_y = param.Integer(default=5, bounds=(2, 10), doc="Number of dots Y")
    n_dots_x = param.Integer(default=5, bounds=(2, 10), doc="Number of dots X")
    dot_radius = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Dot radius")
    distance = param.Number(default=0.25, bounds=(0.1, 1), step=0.05, doc="Distance between dots")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_dots = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Dots intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_dots": (self.n_dots_y, self.n_dots_x),
            "dot_radius": self.dot_radius,
            "distance": self.distance,
            "target_shape": (self.target_height, self.target_width),
            "intensity_background": self.intensity_background,
            "intensity_dots": self.intensity_dots,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import dotted
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive dotted
dotted_params = DottedParams()
disp = InteractiveStimDisplay(dotted, dotted_params)
disp.layout
```
