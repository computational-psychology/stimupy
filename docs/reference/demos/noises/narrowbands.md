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

```{tip}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/noises/narrowbands.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Noises - Narrowbands
{py:mod}`stimupy.noises.narrowbands`



## Narrowband
{py:func}`stimupy.noises.narrowbands.narrowband`

```{code-cell} ipython3
import param

class NarrowbandParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    center_frequency = param.Number(default=5., bounds=(0.1, 12), step=0.1, doc="")
    bandwidth = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="")
    intensity_min = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1., bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "center_frequency": self.center_frequency,
            "bandwidth": self.bandwidth,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }
```

```{code-cell} ipython3
from stimupy.noises.narrowbands import narrowband
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive narrowband
narrowband_params = NarrowbandParams()
disp = InteractiveStimDisplay(narrowband, narrowband_params)
disp.layout
```
