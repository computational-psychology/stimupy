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

# Rectangular, Two-sided
{py:func}`stimupy.stimuli.bullseyes.rectangular_two_sided`

```{pyodide}
:skip-embed:

import param

class RectangularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 40), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="")
    intensity_frame1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_frame2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": ((self.intensity_frame1, self.intensity_frame2), (self.intensity_frame2, self.intensity_frame1)),
            "intensity_background": self.intensity_background,
            "rotation": self.rotation,
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.bullseyes import rectangular_two_sided
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular_two_sided
rectangular_two_sided_params = RectangularTwoSidedParams()
disp = InteractiveStimDisplay(rectangular_two_sided, rectangular_two_sided_params)
disp.layout
```
