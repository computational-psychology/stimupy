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

# Disc
{py:func}`stimupy.components.radials.disc`

```{pyodide}
:skip-embed:

import param

class DiscParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Disc geometry parameters
    radius = param.Number(default=3, bounds=(1, 6), step=0.1, doc="Radius in degrees")
    
    # Intensity parameters
    intensity_disc = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Disc intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    
    # Additional parameters
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_disc": self.intensity_disc,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.radials import disc
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive disc
disc_params = DiscParams()
disp = InteractiveStimDisplay(disc, disc_params)
disp.layout
```
