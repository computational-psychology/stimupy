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

# Wedge
{py:func}`stimupy.components.shapes.wedge`

```{pyodide}
:skip-embed:

import param

class ShapeWedgeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    angle = param.Number(default=45, bounds=(1, 360), step=1, doc="")
    radius = param.Number(default=4, bounds=(1, 8), step=0.1, doc="")
    inner_radius = param.Number(default=0, bounds=(0, 3), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_wedge = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "angle": self.angle,
            "radius": self.radius,
            "inner_radius": self.inner_radius,
            "rotation": self.rotation,
            "intensity_wedge": self.intensity_wedge,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.shapes import wedge
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive wedge
wedge_params = ShapeWedgeParams()
disp = InteractiveStimDisplay(wedge, wedge_params)
disp.layout
```
