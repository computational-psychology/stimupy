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

# Corrugated Mondrian
{py:func}`stimupy.stimuli.mondrians.corrugated_mondrian`

```{pyodide}
:skip-embed:

import param

class CorrugatedMondrianParams(param.Parameterized):
    # Image size parameters
    height = param.Number(default=10, bounds=(1, 20), doc="Height of image in degrees")
    width = param.Number(default=10, bounds=(1, 20), doc="Width of image in degrees")
    ppd = param.Number(default=32, bounds=(1, 60), doc="Pixels per degree")
    
    # Grid parameters
    nrows = param.Integer(default=4, bounds=(1, 8), doc="Number of rows", allow_None=True)
    ncols = param.Integer(default=4, bounds=(1, 8), doc="Number of columns", allow_None=True)
    
    # Depth parameters
    depth1 = param.Number(default=1, bounds=(-2, 2), doc="Depth of row 1")
    depth2 = param.Number(default=0, bounds=(-2, 2), doc="Depth of row 2") 
    depth3 = param.Number(default=-1, bounds=(-2, 2), doc="Depth of row 3")
    depth4 = param.Number(default=0, bounds=(-2, 2), doc="Depth of row 4")
    
    # Target parameters
    target_idx1 = param.Integer(default=1, bounds=(0, 3), doc="Target row index 1")
    target_idx2 = param.Integer(default=1, bounds=(0, 3), doc="Target column index 1")
    target_idx3 = param.Integer(default=3, bounds=(0, 3), doc="Target row index 2")
    target_idx4 = param.Integer(default=1, bounds=(0, 3), doc="Target column index 2")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), doc="Target intensity", allow_None=True)
    
    # Background intensity
    intensity_background = param.Number(default=0.5, bounds=(0, 1), doc="Background intensity")
    
    def get_stimulus_params(self):
        import numpy as np
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "nrows": self.nrows,
            "ncols": self.ncols,
            "depths": (self.depth1, self.depth2, self.depth3, self.depth4),
            "intensities": np.random.rand(4, 4),
            "target_indices": ((self.target_idx1, self.target_idx2), (self.target_idx3, self.target_idx4)),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.mondrians import corrugated_mondrian
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive corrugated_mondrian
corrugated_mondrian_params = CorrugatedMondrianParams()
disp = InteractiveStimDisplay(corrugated_mondrian, corrugated_mondrian_params)
disp.layout
```
