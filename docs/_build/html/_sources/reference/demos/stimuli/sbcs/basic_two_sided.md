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

# Basic, Two sided
{py:func}`stimupy.stimuli.sbcs.basic_two_sided`

```{pyodide}
:skip-embed:

import param

class BasicTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_background_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left background intensity")
    intensity_background_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_background": (self.intensity_background_left, self.intensity_background_right),
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.sbcs import basic_two_sided
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive basic_two_sided
basic_two_sided_params = BasicTwoSidedParams()
disp = InteractiveStimDisplay(basic_two_sided, basic_two_sided_params)
disp.layout
```
