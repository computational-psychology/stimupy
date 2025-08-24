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

# Dipole
{py:func}`stimupy.components.lines.dipole`

```{pyodide}
:skip-embed:

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

```{pyodide}
:skip-embed:

from stimupy.components.lines import dipole
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive dipole
dipole_params = DipoleParams()
disp = InteractiveStimDisplay(dipole, dipole_params)
disp.layout
```
