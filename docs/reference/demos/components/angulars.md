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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/angulars.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Components - Angulars
{py:mod}`stimupy.components.angulars`



## Wedge
{py:func}`stimupy.components.angulars.wedge`

```{code-cell} ipython3
import param

class WedgeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")
    
    # Wedge geometry parameters
    angle = param.Integer(default=45, bounds=(1, 90), doc="Wedge angle in degrees")
    radius = param.Number(default=3, bounds=(1, 6), step=0.1, doc="Outer radius in degrees")
    inner_radius = param.Number(default=0, bounds=(0, 3), step=0.1, doc="Inner radius in degrees")
    
    # Intensity parameters
    intensity_wedge = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Wedge intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    
    # Additional parameters
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "angle": self.angle,
            "radius": self.radius,
            "rotation": self.rotation,
            "inner_radius": self.inner_radius,
            "intensity_wedge": self.intensity_wedge,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.angulars import wedge
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive wedge
wedge_params = WedgeParams()
disp = InteractiveStimDisplay(wedge, wedge_params)
disp.layout
```

## Segments
{py:func}`stimupy.components.angulars.segments`

```{code-cell} ipython3
import param

class SegmentsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")
    
    # Segment angles
    angle1 = param.Integer(default=45, bounds=(1, 90), doc="Angle 1 in degrees")
    angle2 = param.Integer(default=90, bounds=(1, 180), doc="Angle 2 in degrees")
    angle3 = param.Integer(default=135, bounds=(1, 360), doc="Angle 3 in degrees")
    
    # Intensity parameters
    intensity1 = param.Number(default=0.2, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Intensity 3")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    
    # Additional parameters
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "angles": (self.angle1, self.angle2, self.angle3),
            "rotation": self.rotation,
            "intensity_segments": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.angulars import segments
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive segments
segments_params = SegmentsParams()
disp = InteractiveStimDisplay(segments, segments_params)
disp.layout
```
