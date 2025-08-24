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

# Cross
{py:func}`stimupy.components.shapes.cross`

```{pyodide}
:skip-embed:

import param

class CrossParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_height = param.Integer(default=4, bounds=(1, 8), doc="")
    cross_width = param.Integer(default=4, bounds=(1, 8), doc="")
    cross_thickness_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="")
    cross_thickness_width = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="")
    cross_arm_ratio1 = param.Number(default=1.0, bounds=(0.1, 5.0), step=0.1, doc="")
    cross_arm_ratio2 = param.Number(default=1.0, bounds=(0.1, 5.0), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_cross = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": (self.cross_height, self.cross_width),
            "cross_thickness": (self.cross_thickness_height, self.cross_thickness_width),
            "cross_arm_ratios": (self.cross_arm_ratio1, self.cross_arm_ratio2),
            "rotation": self.rotation,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.components.shapes import cross
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross
cross_params = CrossParams()
disp = InteractiveStimDisplay(cross, cross_params)
disp.layout
```
