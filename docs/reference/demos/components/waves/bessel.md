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

# Bessel
{py:func}`stimupy.components.waves.bessel`

```{code-cell} ipython3
import param

class BesselParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.01, doc="")
    order = param.Integer(default=0, bounds=(0, 5), doc="")
    intensity_center = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    intensity_outer = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "order": self.order,
            "intensities": (self.intensity_center, self.intensity_outer),
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.waves import bessel
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive bessel
bessel_params = BesselParams()
disp = InteractiveStimDisplay(bessel, bessel_params)
disp.layout
```
