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

# Basic
{py:func}`stimupy.stimuli.sbcs.basic`

```{pyodide}
:skip-embed:

import param

class BasicParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.sbcs import basic
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive basic
basic_params = BasicParams()
disp = InteractiveStimDisplay(basic, basic_params)
disp.layout
```
