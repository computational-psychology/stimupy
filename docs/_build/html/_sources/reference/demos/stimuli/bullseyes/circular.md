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

# Circular
{py:func}`stimupy.stimuli.bullseyes.circular`

```{pyodide}
:skip-embed:

import param

class CircularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="")
    intensity_ring1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_ring2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    clip = param.Boolean(default=False, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity_ring1, self.intensity_ring2),
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "clip": self.clip,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.bullseyes import circular
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular
circular_params = CircularParams()
disp = InteractiveStimDisplay(circular, circular_params)
disp.layout
```
