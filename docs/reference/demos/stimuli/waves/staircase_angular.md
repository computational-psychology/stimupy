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

# Staircase, angular
{py:func}`stimupy.stimuli.waves.staircase_angular`

```{code-cell} ipython3
import param

class StaircaseAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8, bounds=(4, 20), step=1, doc="Frequency")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_segments_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low segment intensity")
    intensity_segments_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High segment intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity_segments_low, self.intensity_segments_high),
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import staircase_angular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase_angular
staircase_angular_params = StaircaseAngularParams()
disp = InteractiveStimDisplay(staircase_angular, staircase_angular_params)
disp.layout
```
