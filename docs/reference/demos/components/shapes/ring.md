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

# Ring
{py:func}`stimupy.components.shapes.ring`

```{code-cell} ipython3
import param

class RingParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=2, bounds=(1, 4), step=0.01, doc="")
    radius2 = param.Number(default=4, bounds=(3, 6), step=0.01, doc="")
    intensity_ring = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    add_mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2),
            "intensity_ring": self.intensity_ring,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import ring
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive ring
ring_params = RingParams()
disp = InteractiveStimDisplay(ring, ring_params)
disp.layout
```
