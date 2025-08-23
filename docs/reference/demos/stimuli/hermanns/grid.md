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

# Grid
{py:func}`stimupy.stimuli.hermanns.grid`

```{code-cell} ipython3
import param

class HermannParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Element geometry parameters
    element_height = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Element height")
    element_width = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Element width")
    element_thickness = param.Number(default=0.1, bounds=(0.1, 1), step=0.1, doc="Element thickness")
    
    # Intensity parameters
    intensity_grid = param.Number(default=1, bounds=(0, 1), step=0.01, doc="Grid intensity")
    intensity_background = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "element_size": (self.element_height, self.element_width, self.element_thickness),
            "intensity_background": self.intensity_background,
            "intensity_grid": self.intensity_grid,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.hermanns import grid
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive hermann grid
hermann_params = HermannParams()
disp = InteractiveStimDisplay(grid, hermann_params)
disp.layout
```
