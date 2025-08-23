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

```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Gabor
{py:func}`stimupy.stimuli.gabors.gabor`

```{code-cell} ipython3
import param

class GaborParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Gabor geometry parameters
    frequency = param.Number(default=1.0, bounds=(0, 2), step=0.1, doc="Frequency in cycles per degree")
    phase_shift = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    sigma = param.Number(default=2.0, bounds=(0, 4), step=0.1, doc="Gaussian envelope sigma")
    
    # Intensity parameters
    int1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    int2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    
    # Additional parameters
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "sigma": self.sigma,
            "intensities": (self.int1, self.int2),
            "origin": self.origin,
            "period": self.period,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.gabors import gabor
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive gabor
gabor_params = GaborParams()
disp = InteractiveStimDisplay(gabor, gabor_params)
disp.layout
```
