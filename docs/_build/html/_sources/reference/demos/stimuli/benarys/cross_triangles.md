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

# Cross triangles
{py:func}`stimupy.stimuli.benarys.cross_triangles`

```{pyodide}
:skip-embed:

import param

class CrossTrianglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": self.target_size,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.benarys import cross_triangles
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross_triangles
cross_triangles_params = CrossTrianglesParams()
disp = InteractiveStimDisplay(cross_triangles, cross_triangles_params)
disp.layout
```
