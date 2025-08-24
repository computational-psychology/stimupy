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

# Square, Two sided
{py:func}`stimupy.stimuli.sbcs.square_two_sided`

```{pyodide}
:skip-embed:

import param

class SquareTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius")
    target_radius_right = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius")
    surround_radius_left = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius")
    surround_radius_right = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius")
    rotation_left = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Left rotation in degrees")
    rotation_right = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Right rotation in degrees")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_surround_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity")
    intensity_surround_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "rotation": (self.rotation_left, self.rotation_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.sbcs import square_two_sided
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_two_sided
square_two_sided_params = SquareTwoSidedParams()
disp = InteractiveStimDisplay(square_two_sided, square_two_sided_params)
disp.layout
```
