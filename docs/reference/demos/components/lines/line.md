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

# Line
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
