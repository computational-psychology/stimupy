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

# Rings
{py:func}`stimupy.components.radials.rings`

```{pyodide}
:skip-embed:

import param

class RingsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1, bounds=(0, 2), step=0.01, doc="")
    radius2 = param.Number(default=2, bounds=(1, 3), step=0.01, doc="")
    radius3 = param.Number(default=3, bounds=(2, 4), step=0.01, doc="")
    intensity_1 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="")
    intensity_2 = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_3 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_rings": (self.intensity_1, self.intensity_2, self.intensity_3),
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.radials import rings
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rings
rings_params = RingsParams()
disp = InteractiveStimDisplay(rings, rings_params)
disp.layout
```
