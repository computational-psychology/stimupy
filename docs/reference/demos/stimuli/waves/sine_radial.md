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

# Sine, radial
{py:func}`stimupy.stimuli.waves.sine_radial`

```{code-cell} ipython3
import param

class SineRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensities_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low intensity")
    intensities_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High intensity")
    clip = param.Boolean(default=False, doc="Clip stimulus")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensities": (self.intensities_low, self.intensities_high),
            "clip": self.clip,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import sine_radial
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine_radial
sine_radial_params = SineRadialParams()
disp = InteractiveStimDisplay(sine_radial, sine_radial_params)
disp.layout
```
