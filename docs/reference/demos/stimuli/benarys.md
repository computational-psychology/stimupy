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

```{tip}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/benarys.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Benary's cross
{py:mod}`stimupy.stimuli.benarys`



## Cross, generalized
{py:func}`stimupy.stimuli.benarys.cross_generalized`

```{code-cell} ipython3
import param

class CrossGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_height = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_width = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_type = param.Selector(default="r", objects=['r', 't'], doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    target_y = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_x = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="")
    intensity_background = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": (self.target_height, self.target_width),
            "target_type": self.target_type,
            "target_rotation": self.target_rotation,
            "target_x": self.target_x,
            "target_y": self.target_y,
            "intensity_background": self.intensity_background,
            "intensity_cross": self.intensity_cross,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.benarys import cross_generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross_generalized
cross_generalized_params = CrossGeneralizedParams()
disp = InteractiveStimDisplay(cross_generalized, cross_generalized_params)
disp.layout
```

## Cross, rectangles
{py:func}`stimupy.stimuli.benarys.cross_rectangles`

```{code-cell} ipython3
import param

class CrossRectanglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_height = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_width = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": (self.target_height, self.target_width),
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.benarys import cross_rectangles
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross_rectangles
cross_rectangles_params = CrossRectanglesParams()
disp = InteractiveStimDisplay(cross_rectangles, cross_rectangles_params)
disp.layout
```

## Cross triangles
{py:func}`stimupy.stimuli.benarys.cross_triangles`

```{code-cell} ipython3
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

```{code-cell} ipython3
from stimupy.stimuli.benarys import cross_triangles
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross_triangles
cross_triangles_params = CrossTrianglesParams()
disp = InteractiveStimDisplay(cross_triangles, cross_triangles_params)
disp.layout
```

## Todorovic triangles
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
