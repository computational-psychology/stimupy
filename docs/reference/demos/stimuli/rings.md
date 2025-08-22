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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/rings.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Rings
{py:mod}`stimupy.stimuli.rings`



## Circular
{py:func}`stimupy.stimuli.rings.circular`

```{code-cell} ipython3
import param

class CircularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=2, bounds=(0, 10), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin position")
    clip = param.Boolean(default=False, doc="Clip")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx,),
            "intensity_target": self.intensity_target,
            "origin": self.origin,
            "clip": self.clip,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import circular
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

## Circular, generalized
{py:func}`stimupy.stimuli.rings.circular_generalized`

```{code-cell} ipython3
import param

class CircularGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Radius 1")
    radius2 = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Radius 2")
    radius3 = param.Number(default=3.0, bounds=(0.1, 5), step=0.1, doc="Radius 3")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Intensity 3")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=1, bounds=(1, 4), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin position")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_rings": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx,),
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import circular_generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular_generalized
circular_generalized_params = CircularGeneralizedParams()
disp = InteractiveStimDisplay(circular_generalized, circular_generalized_params)
disp.layout
```

## Two-sided rings
{py:func}`stimupy.stimuli.rings.circular_two_sided`

```{code-cell} ipython3
import param

class CircularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=2, bounds=(0, 10), doc="Target index")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin position")
    clip = param.Boolean(default=False, doc="Clip")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": ((self.intensity1, self.intensity2), (self.intensity2, self.intensity1)),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx, self.target_idx),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "origin": self.origin,
            "clip": self.clip,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import circular_two_sided
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

## Rectangular
{py:func}`stimupy.stimuli.rings.rectangular`

```{code-cell} ipython3
import param

class RectangularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=1, bounds=(0, 10), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin position")
    clip = param.Boolean(default=False, doc="Clip")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "target_indices": self.target_idx,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
            "clip": self.clip,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import rectangular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular
rectangular_params = RectangularParams()
disp = InteractiveStimDisplay(rectangular, rectangular_params)
disp.layout
```

## Rectangular, generalized
{py:func}`stimupy.stimuli.rings.rectangular_generalized`

```{code-cell} ipython3
import param

class RectangularGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Radius 1")
    radius2 = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Radius 2")
    radius3 = param.Number(default=3.0, bounds=(0.1, 5), step=0.1, doc="Radius 3")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Intensity 3")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=1, bounds=(1, 4), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin position")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_frames": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "target_indices": self.target_idx,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
            "rotation": self.rotation,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import rectangular_generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular_generalized
rectangular_generalized_params = RectangularGeneralizedParams()
disp = InteractiveStimDisplay(rectangular_generalized, rectangular_generalized_params)
disp.layout
```

## Two-sided-rings
{py:func}`stimupy.stimuli.rings.rectangular_two_sided`

```{code-cell} ipython3
import param

class RectangularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 40), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=1, bounds=(0, 10), doc="Target index")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    clip = param.Boolean(default=False, doc="Clip")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": ((self.intensity1, self.intensity2), (self.intensity2, self.intensity1)),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx, self.target_idx),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "clip": self.clip,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.rings import rectangular_two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular_two_sided
rectangular_two_sided_params = RectangularTwoSidedParams()
disp = InteractiveStimDisplay(rectangular_two_sided, rectangular_two_sided_params)
disp.layout
```