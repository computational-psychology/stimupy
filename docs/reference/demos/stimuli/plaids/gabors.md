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

# Gabors
{py:func}`stimupy.stimuli.plaids.gabors`

```{pyodide}
:skip-embed:

import param

class GaborsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    sigma = param.Number(default=2, bounds=(0.1, 4), step=0.1, doc="Sigma")
    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        gabor_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        gabor_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "gabor_parameters1": gabor_params1,
            "gabor_parameters2": gabor_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.plaids import gabors
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive gabors
gabors_params = GaborsParams()
disp = InteractiveStimDisplay(gabors, gabors_params)
disp.layout
```
