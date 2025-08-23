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

# Dungeon
{py:func}`stimupy.stimuli.dungeons.dungeon`

```{code-cell} ipython3
import param

class DungeonParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Grid geometry parameters
    n_cells1 = param.Integer(default=5, bounds=(2, 10), doc="Number of cells 1")
    n_cells2 = param.Integer(default=5, bounds=(2, 10), doc="Number of cells 2")
    
    # Intensity parameters
    intensity_grid = param.Number(default=1, bounds=(0, 1), step=0.01, doc="Grid intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    
    # Target parameters
    target_radius = param.Integer(default=1, bounds=(0, 3), doc="Target radius")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    
    # Additional parameters
    add_mask = param.Selector(default=None, objects=[None, "target_mask"], doc="Add mask")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_cells": (self.n_cells1, self.n_cells2),
            "intensity_grid": self.intensity_grid,
            "intensity_background": self.intensity_background,
            "target_radius": self.target_radius,
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.dungeons import dungeon
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive dungeon
dungeon_params = DungeonParams()
disp = InteractiveStimDisplay(dungeon, dungeon_params)
disp.layout
```
