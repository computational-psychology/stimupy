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

# Rectangular-generalized
{py:func}`stimupy.stimuli.bullseyes.rectangular_generalized`

```{pyodide}
:skip-embed:

import param

class RectangularGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1, bounds=(0, 2), step=0.1, doc="")
    radius2 = param.Number(default=2, bounds=(1, 3), step=0.1, doc="")
    radius3 = param.Number(default=3, bounds=(2, 4), step=0.1, doc="")
    intensity_frame1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_frame2 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="")
    intensity_frame3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="center", objects=['mean', 'corner', 'center'], doc="")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": [self.radius1, self.radius2, self.radius3],
            "intensity_frames": [self.intensity_frame1, self.intensity_frame2, self.intensity_frame3],
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "rotation": self.rotation,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.bullseyes import rectangular_generalized
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular_generalized
rectangular_generalized_params = RectangularGeneralizedParams()
disp = InteractiveStimDisplay(rectangular_generalized, rectangular_generalized_params)
disp.layout
```
