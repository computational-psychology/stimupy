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

# With dots
{py:func}`stimupy.stimuli.sbcs.with_dots`

```{pyodide}
:skip-embed:

import param

class WithDotsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=15, bounds=(10, 20), doc="Height in degrees")
    width = param.Integer(default=15, bounds=(10, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    n_dots_y = param.Integer(default=5, bounds=(2, 10), doc="Number of dots Y")
    n_dots_x = param.Integer(default=5, bounds=(2, 10), doc="Number of dots X")
    dot_radius = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Dot radius")
    distance = param.Number(default=0.25, bounds=(0.1, 1), step=0.05, doc="Distance between dots")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_dots = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Dots intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "n_dots": (self.n_dots_y, self.n_dots_x),
            "dot_radius": self.dot_radius,
            "distance": self.distance,
            "intensity_background": self.intensity_background,
            "intensity_dots": self.intensity_dots,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.sbcs import with_dots
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive with_dots
with_dots_params = WithDotsParams()
disp = InteractiveStimDisplay(with_dots, with_dots_params)
disp.layout
```
