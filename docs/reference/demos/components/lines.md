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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/lines.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Components - Lines
{py:mod}`stimupy.components.lines`



## Line
{py:func}`stimupy.components.lines.line`

```{code-cell} ipython3
import param

class LineParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    line_length = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    line_position_x = param.Number(default=3.0, bounds=(-10, 10.0), step=0.01, doc="")
    line_position_y = param.Number(default=3.0, bounds=(-10, 10.0), step=0.01, doc="")
    intensity_line = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="corner", objects=['corner', 'center', 'mean'], doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "line_length": self.line_length,
            "line_width": self.line_width,
            "rotation": self.rotation,
            "line_position": (self.line_position_y, self.line_position_x),
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.lines import line
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive line
line_params = LineParams()
disp = InteractiveStimDisplay(line, line_params)
disp.layout
```

## Dipole
{py:func}`stimupy.components.lines.dipole`

```{code-cell} ipython3
import param

class DipoleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    line_length = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    line_gap = param.Number(default=0.5, bounds=(0, 3), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_lines = param.Range(default=(0.0, 1.0), bounds=(0, 1), doc="Line intensity range (min, max)")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "line_length": self.line_length,
            "line_width": self.line_width,
            "line_gap": self.line_gap,
            "rotation": self.rotation,
            "intensity_lines": self.intensity_lines,
        }
```

```{code-cell} ipython3
from stimupy.components.lines import dipole
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive dipole
dipole_params = DipoleParams()
disp = InteractiveStimDisplay(dipole, dipole_params)
disp.layout
```

## Ellipse
{py:func}`stimupy.components.lines.ellipse`

```{code-cell} ipython3
import param

class EllipseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    radius2 = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1., bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": (self.radius1, self.radius2),
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.components.lines import ellipse
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive ellipse
ellipse_params = EllipseParams()
disp = InteractiveStimDisplay(ellipse, ellipse_params)
disp.layout
```

## Circle
{py:func}`stimupy.components.lines.circle`

```{code-cell} ipython3
import param

class CircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1., bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.components.lines import circle
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circle
circle_params = CircleParams()
disp = InteractiveStimDisplay(circle, circle_params)
disp.layout
```
