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

# Staircase
{py:func}`stimupy.components.waves.staircase`

```{pyodide}
:skip-embed:

import param

class StaircaseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    distance_metric = param.Selector(default="horizontal", objects=['horizontal','vertical','oblique','radial','rectilinear','angular'], doc="")
    frequency = param.Number(default=1, bounds=(0, 4), step=0.01, doc="")
    rotation = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    intensity_min = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="center", objects=['mean', 'corner', 'center'], doc="")
    period = param.Selector(default="ignore", objects=['ignore', 'even', 'odd', 'either'], doc="")
    round_phase_width = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "distance_metric": self.distance_metric,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
            "period": self.period,
            "round_phase_width": self.round_phase_width,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.waves import staircase
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase
staircase_params = StaircaseParams()
disp = InteractiveStimDisplay(staircase, staircase_params)
disp.layout
```
