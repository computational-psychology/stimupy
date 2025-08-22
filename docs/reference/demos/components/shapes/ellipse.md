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

# Ellipse
{py:func}`stimupy.components.shapes.ellipse`

```{code-cell} ipython3
import param

class ShapeEllipseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius_height = param.Number(default=3, bounds=(1, 6), step=0.1, doc="")
    radius_width = param.Number(default=4, bounds=(1, 6), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_ellipse = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    restrict_size = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": (self.radius_height, self.radius_width),
            "rotation": self.rotation,
            "intensity_ellipse": self.intensity_ellipse,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "restrict_size": self.restrict_size,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import ellipse
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive ellipse
ellipse_params = ShapeEllipseParams()
disp = InteractiveStimDisplay(ellipse, ellipse_params)
disp.layout
```
