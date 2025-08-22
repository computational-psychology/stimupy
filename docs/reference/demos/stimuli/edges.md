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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/edges.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Edges
{py:mod}`stimupy.stimuli.edges`



## Step edge
{py:func}`stimupy.stimuli.edges.step`

```{code-cell} ipython3
import param

class StepParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
        }
```

```{code-cell} ipython3
from stimupy.stimuli.edges import step
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive step
step_params = StepParams()
disp = InteractiveStimDisplay(step, step_params)
disp.layout
```

## Gaussian edge
{py:func}`stimupy.stimuli.edges.gaussian`

```{code-cell} ipython3
import param

class GaussianParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    sigma = param.Number(default=2.0, bounds=(0.1, 4), step=0.1, doc="Sigma")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.edges import gaussian
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive gaussian
gaussian_params = GaussianParams()
disp = InteractiveStimDisplay(gaussian, gaussian_params)
disp.layout
```

## Cornsweet edge
{py:func}`stimupy.stimuli.edges.cornsweet`

```{code-cell} ipython3
import param

class CornweetParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    ramp_width = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Ramp width")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_plateau = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Plateau intensity")
    exponent = param.Number(default=2.75, bounds=(1, 5), step=0.1, doc="Exponent")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "ramp_width": self.ramp_width,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
            "intensity_plateau": self.intensity_plateau,
            "exponent": self.exponent,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.edges import cornsweet
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cornsweet
cornsweet_params = CornweetParams()
disp = InteractiveStimDisplay(cornsweet, cornsweet_params)
disp.layout
```
