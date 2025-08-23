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

# Wedding cake
{py:func}`stimupy.stimuli.wedding_cakes.wedding_cake`

```{pyodide}
:skip-embed:

import param

class WeddingCakeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_height = param.Number(default=2, bounds=(1, 5), step=0.1, doc="L height")
    L_width = param.Number(default=2, bounds=(1, 5), step=0.1, doc="L width")
    L_thickness = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="L thickness")
    target_height = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Target height")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_size": (self.L_height, self.L_width, self.L_thickness),
            "target_height": self.target_height,
            "target_indices1": ((0, 0),),
            "target_indices2": ((0, 0),),
            "intensity_bars": (self.intensity1, self.intensity2),
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.wedding_cakes import wedding_cake
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive wedding_cake
wedding_cake_params = WeddingCakeParams()
disp = InteractiveStimDisplay(wedding_cake, wedding_cake_params)
disp.layout
```
