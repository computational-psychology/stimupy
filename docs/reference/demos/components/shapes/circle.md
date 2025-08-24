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

# Circle
{py:func}`stimupy.components.shapes.circle`

```{pyodide}
:skip-embed:

import param

class ShapeCircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(1, 6), step=0.1, doc="")
    intensity_circle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    restrict_size = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_circle": self.intensity_circle,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "restrict_size": self.restrict_size,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.shapes import circle
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive circle
circle_params = ShapeCircleParams()
disp = InteractiveStimDisplay(circle, circle_params)
disp.layout
```
