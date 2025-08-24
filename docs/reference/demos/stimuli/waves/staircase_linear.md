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

# Staircase, linear
{py:func}`stimupy.stimuli.waves.staircase_linear`

```{pyodide}
:skip-embed:

import param

class StaircaseLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    origin = param.Selector(default="corner", objects=["mean", "corner", "center"], doc="Origin")
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "origin": self.origin,
            "period": self.period,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.waves import staircase_linear
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase_linear
staircase_linear_params = StaircaseLinearParams()
disp = InteractiveStimDisplay(staircase_linear, staircase_linear_params)
disp.layout
```
