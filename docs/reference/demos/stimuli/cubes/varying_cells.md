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

# Varying cells
{py:func}`stimupy.stimuli.cubes.varying_cells`

```{pyodide}
:skip-embed:

import param

class VaryingCellsParams(param.Parameterized):
    # Image parameters
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cell_length1 = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    cell_length2 = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    cell_length3 = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    cell_length4 = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    cell_thickness = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    cell_spacing = param.Number(default=2, bounds=(0, 4), step=0.1, doc="")
    intensity_cells = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "ppd": self.ppd,
            "cell_lengths": [self.cell_length1, self.cell_length2, self.cell_length3, self.cell_length4],
            "cell_thickness": self.cell_thickness,
            "cell_spacing": self.cell_spacing,
            "intensity_cells": self.intensity_cells,
            "intensity_background": self.intensity_background,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.cubes import varying_cells
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive varying_cells
varying_cells_params = VaryingCellsParams()
disp = InteractiveStimDisplay(varying_cells, varying_cells_params)
disp.layout
```
