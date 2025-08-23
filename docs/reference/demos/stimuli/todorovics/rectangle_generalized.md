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

# Rectangle generalized
{py:func}`stimupy.stimuli.todorovics.rectangle_generalized`

```{pyodide}
:skip-embed:

import param

class RectangleGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Target height")
    target_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Target width")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_x = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Target X position")
    target_y = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Target Y position")
    covers_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers height")
    covers_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers width")
    cover_x1 = param.Number(default=2, bounds=(0, 8), step=0.1, doc="Cover 1 X position")
    cover_y1 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 1 Y position")
    cover_x2 = param.Number(default=6, bounds=(0, 8), step=0.1, doc="Cover 2 X position")
    cover_y2 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 2 Y position")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "target_position": (self.target_y, self.target_x),
            "covers_size": (self.covers_height, self.covers_width),
            "covers_x": (self.cover_x1, self.cover_x2),
            "covers_y": (self.cover_y1, self.cover_y2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.todorovics import rectangle_generalized
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangle_generalized
rectangle_generalized_params = RectangleGeneralizedParams()
disp = InteractiveStimDisplay(rectangle_generalized, rectangle_generalized_params)
disp.layout
```
