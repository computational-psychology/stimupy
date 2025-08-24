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

# Triangle
{py:func}`stimupy.components.shapes.triangle`

```{pyodide}
:skip-embed:

import param

class TriangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    triangle_height = param.Number(default=3, bounds=(1, 10), step=0.01, doc="")
    triangle_width = param.Number(default=3, bounds=(1, 10), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_triangle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    include_corners = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "triangle_size": (self.triangle_height, self.triangle_width),
            "rotation": self.rotation,
            "intensity_triangle": self.intensity_triangle,
            "intensity_background": self.intensity_background,
            "include_corners": self.include_corners,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.shapes import triangle
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive triangle
triangle_params = TriangleParams()
disp = InteractiveStimDisplay(triangle, triangle_params)
disp.layout
```
