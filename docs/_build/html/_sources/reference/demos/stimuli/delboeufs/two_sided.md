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

# Delboeuf, two_sided
{py:func}`stimupy.stimuli.delboeufs.two_sided`

```{pyodide}
:skip-embed:

import param

class DelboeufTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="")
    target_radius_right = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="")
    outer_radius_left = param.Number(default=4, bounds=(0.5, 8), step=0.1, doc="")
    outer_radius_right = param.Number(default=4, bounds=(0.5, 8), step=0.1, doc="")
    outer_line_width_left = param.Number(default=0, bounds=(0, 2), step=0.1, doc="")
    outer_line_width_right = param.Number(default=0, bounds=(0, 2), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_outer_line = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius":( self.target_radius_left, self.target_radius_right),
            "outer_radius": (self.outer_radius_left, self.outer_radius_right),
            "outer_line_width": (self.outer_line_width_left, self.outer_line_width_right),
            "intensity_target": self.intensity_target,
            "intensity_outer_line": self.intensity_outer_line,
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.delboeufs import two_sided
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive two_sided
two_sided_params = DelboeufTwoSidedParams()
disp = InteractiveStimDisplay(two_sided, two_sided_params)
disp.layout
```
