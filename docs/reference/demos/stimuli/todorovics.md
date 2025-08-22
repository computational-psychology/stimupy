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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/todorovics.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Todorovics
{py:mod}`stimupy.stimuli.todorovics`



## Rectangle generalized
{py:func}`stimupy.stimuli.todorovics.rectangle_generalized`

```{code-cell} ipython3
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

```{code-cell} ipython3
from stimupy.stimuli.todorovics import rectangle_generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangle_generalized
rectangle_generalized_params = RectangleGeneralizedParams()
disp = InteractiveStimDisplay(rectangle_generalized, rectangle_generalized_params)
disp.layout
```

## Cross generalized
{py:func}`stimupy.stimuli.todorovics.cross_generalized`

```{code-cell} ipython3
import param

class CrossGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_size_height = param.Number(default=4, bounds=(2, 8), step=0.1, doc="Cross height")
    cross_size_width = param.Number(default=4, bounds=(2, 8), step=0.1, doc="Cross width")
    cross_thickness = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Cross thickness")
    covers_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers height")
    covers_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers width")
    cover_x1 = param.Number(default=2, bounds=(0, 8), step=0.1, doc="Cover 1 X position")
    cover_y1 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 1 Y position")
    cover_x2 = param.Number(default=6, bounds=(0, 8), step=0.1, doc="Cover 2 X position")
    cover_y2 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 2 Y position")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": (self.cross_size_height, self.cross_size_width),
            "cross_thickness": self.cross_thickness,
            "covers_size": (self.covers_height, self.covers_width),
            "covers_x": (self.cover_x1, self.cover_x2),
            "covers_y": (self.cover_y1, self.cover_y2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.todorovics import cross_generalized
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

## Equal
{py:func}`stimupy.stimuli.todorovics.equal`

```{code-cell} ipython3
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

```{code-cell} ipython3
from stimupy.stimuli.todorovics import equal
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive equal
equal_params = EqualParams()
disp = InteractiveStimDisplay(equal, equal_params)
disp.layout
```
