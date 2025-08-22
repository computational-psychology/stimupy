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

# Todorovic triangles
{py:func}`stimupy.stimuli.benarys.todorovic_triangles`

```{code-cell} ipython3
import param


class TodorovicTrianglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_width = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_width": self.L_width,
            "target_size": self.target_size,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.benarys import todorovic_triangles
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive todorovic_triangles
todorovic_triangles_params = TodorovicTrianglesParams()
disp = InteractiveStimDisplay(todorovic_triangles, todorovic_triangles_params)
disp.layout
```
