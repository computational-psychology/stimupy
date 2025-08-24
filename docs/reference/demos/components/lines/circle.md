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
{py:func}`stimupy.components.lines.circle`

```{pyodide}
:skip-embed:

import param

class CircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1., bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.lines import circle
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive circle
circle_params = CircleParams()
disp = InteractiveStimDisplay(circle, circle_params)
disp.layout
```
