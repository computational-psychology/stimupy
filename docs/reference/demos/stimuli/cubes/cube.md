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

# Cube
{py:func}`stimupy.stimuli.cubes.cube`

```{pyodide}
:skip-embed:

import param

class CubeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    n_cells = param.Integer(default=4, bounds=(1, 8), doc="")
    cell_thickness = param.Number(default=1, bounds=(0, 4), step=0.1, doc="")
    cell_spacing = param.Number(default=1, bounds=(0, 4), step=0.1, doc="")
    intensity_cells = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    target_indices = param.Integer(default=0, bounds=(0, 3), doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_cells": self.n_cells,
            "cell_thickness": self.cell_thickness,
            "cell_spacing": self.cell_spacing,
            "intensity_cells": self.intensity_cells,
            "intensity_background": self.intensity_background,
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.cubes import cube
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cube
cube_params = CubeParams()
disp = InteractiveStimDisplay(cube, cube_params)
disp.layout
```