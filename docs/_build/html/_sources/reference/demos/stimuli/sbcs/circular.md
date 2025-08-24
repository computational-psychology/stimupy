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
{py:func}`stimupy.stimuli.sbcs.circular`

```{pyodide}
:skip-embed:

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

```{pyodide}
:skip-embed:

from stimupy.stimuli.sbcs import circular
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular
circular_params = CircularParams()
disp = InteractiveStimDisplay(circular, circular_params)
disp.layout
```
