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

# Sine waves
{py:func}`stimupy.stimuli.plaids.sine_waves`

```{pyodide}
:skip-embed:

import param

class SineWavesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        grating_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        grating_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "grating_parameters1": grating_params1,
            "grating_parameters2": grating_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.plaids import sine_waves
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine_waves
sine_waves_params = SineWavesParams()
disp = InteractiveStimDisplay(sine_waves, sine_waves_params)
disp.layout
```
