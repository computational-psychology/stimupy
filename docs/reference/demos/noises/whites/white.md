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

# White
{py:func}`stimupy.noises.whites.white`

```{pyodide}
:skip-embed:

import param

class WhiteParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    intensity_min = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1., bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }
```

```{pyodide}
:skip-embed:

from stimupy.noises.whites import white
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive white
white_params = WhiteParams()
disp = InteractiveStimDisplay(white, white_params)
disp.layout
```
