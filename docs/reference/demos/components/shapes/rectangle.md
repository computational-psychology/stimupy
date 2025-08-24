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

# Rectangle
{py:func}`stimupy.components.shapes.rectangle`

```{pyodide}
:skip-embed:

import param

class RectangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    rectangle_height = param.Integer(default=3, bounds=(1, 6), doc="")
    rectangle_width = param.Integer(default=3, bounds=(1, 6), doc="")
    rectangle_position_x = param.Number(default=3.0, bounds=(0, 10.0), step=0.01, doc="")
    rectangle_position_y = param.Number(default=3.0, bounds=(0, 10.0), step=0.01, doc="")
    intensity_rectangle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rectangle_size": (self.rectangle_height, self.rectangle_width),
            "rectangle_position": (self.rectangle_position_x, self.rectangle_position_y),
            "intensity_rectangle": self.intensity_rectangle,
            "intensity_background": self.intensity_background,
            "rotation": self.rotation,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.shapes import rectangle
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangle
rectangle_params = RectangleParams()
disp = InteractiveStimDisplay(rectangle, rectangle_params)
disp.layout
```
