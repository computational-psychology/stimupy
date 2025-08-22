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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/plaids.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Plaids
{py:mod}`stimupy.stimuli.plaids`



## Gabors
{py:func}`stimupy.stimuli.plaids.gabors`

```{code-cell} ipython3
import param

class GaborsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    sigma = param.Number(default=2, bounds=(0.1, 4), step=0.1, doc="Sigma")
    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        gabor_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        gabor_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "gabor_parameters1": gabor_params1,
            "gabor_parameters2": gabor_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.plaids import gabors
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive gabors
gabors_params = GaborsParams()
disp = InteractiveStimDisplay(gabors, gabors_params)
disp.layout
```

## Sine waves
{py:func}`stimupy.stimuli.plaids.sine_waves`

```{code-cell} ipython3
import param

class SineWavesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        grating_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        grating_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "grating_parameters1": grating_params1,
            "grating_parameters2": grating_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.plaids import sine_waves
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine_waves
sine_waves_params = SineWavesParams()
disp = InteractiveStimDisplay(sine_waves, sine_waves_params)
disp.layout
```

## Square waves
{py:func}`stimupy.stimuli.plaids.square_waves`

```{code-cell} ipython3
import param

class SquareWavesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        grating_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        grating_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "grating_parameters1": grating_params1,
            "grating_parameters2": grating_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.plaids import square_waves
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_waves
square_waves_params = SquareWavesParams()
disp = InteractiveStimDisplay(square_waves, square_waves_params)
disp.layout
