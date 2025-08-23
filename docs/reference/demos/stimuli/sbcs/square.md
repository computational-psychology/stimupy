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

# Square
{py:func}`stimupy.stimuli.sbcs.square`

```{code-cell} ipython3
import param

class SquareParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Target radius")
    surround_radius = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Surround radius")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
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
            "rotation": self.rotation,
            "intensity_surround": self.intensity_surround,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import square
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square
square_params = SquareParams()
disp = InteractiveStimDisplay(square, square_params)
disp.layout
```
