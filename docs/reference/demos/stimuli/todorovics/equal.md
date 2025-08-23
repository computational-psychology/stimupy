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

# Equal
{py:func}`stimupy.stimuli.todorovics.equal`

```{pyodide}
:skip-embed:

import param

class EqualParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_size = param.Number(default=4.0, bounds=(2, 8), step=0.1, doc="Cross size", allow_None=True)
    cross_thickness = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Cross thickness", allow_None=True)
    cover_size = param.Number(default=1.5, bounds=(0.1, 2), step=0.1, doc="Cover size", allow_None=True)
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": self.cross_size,
            "cross_thickness": self.cross_thickness,
            "cover_size": self.cover_size,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.todorovics import equal
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive equal
equal_params = EqualParams()
disp = InteractiveStimDisplay(equal, equal_params)
disp.layout
```
