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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/mondrians.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Mondrians
{py:mod}`stimupy.stimuli.mondrians`

## Mondrian
{py:func}`stimupy.stimuli.mondrians.mondrian`

```{code-cell} ipython3
import param

class MondrianParams(param.Parameterized):
    # Image size parameters
    height = param.Number(default=10, bounds=(1, 20), doc="Height of image in degrees")
    width = param.Number(default=10, bounds=(1, 20), doc="Width of image in degrees") 
    ppd = param.Number(default=32, bounds=(1, 60), doc="Pixels per degree")
    
    # Mondrian positions (y, x coordinates)
    pos1_y = param.Number(default=0, bounds=(0, 10), doc="Y position of mondrian 1")
    pos1_x = param.Number(default=0, bounds=(0, 10), doc="X position of mondrian 1")
    pos2_y = param.Number(default=8, bounds=(0, 10), doc="Y position of mondrian 2")
    pos2_x = param.Number(default=4, bounds=(0, 10), doc="X position of mondrian 2")
    pos3_y = param.Number(default=1, bounds=(0, 10), doc="Y position of mondrian 3")
    pos3_x = param.Number(default=6, bounds=(0, 10), doc="X position of mondrian 3")
    
    # Mondrian sizes (height, width, depth)
    size1_h = param.Number(default=3, bounds=(0.5, 8), doc="Height of mondrian 1")
    size1_w = param.Number(default=4, bounds=(0.5, 8), doc="Width of mondrian 1")
    size1_d = param.Number(default=1, bounds=(-2, 2), doc="Depth of mondrian 1")
    size2_h = param.Number(default=2, bounds=(0.5, 8), doc="Height of mondrian 2")
    size2_w = param.Number(default=2, bounds=(0.5, 8), doc="Width of mondrian 2")
    size2_d = param.Number(default=0, bounds=(-2, 2), doc="Depth of mondrian 2")
    size3_h = param.Number(default=5, bounds=(0.5, 8), doc="Height of mondrian 3")
    size3_w = param.Number(default=4, bounds=(0.5, 8), doc="Width of mondrian 3")
    size3_d = param.Number(default=-1, bounds=(-2, 2), doc="Depth of mondrian 3")
    
    # Intensities
    intensity1 = param.Number(default=0.2, bounds=(0, 1), doc="Intensity of mondrian 1")
    intensity2 = param.Number(default=0.6, bounds=(0, 1), doc="Intensity of mondrian 2") 
    intensity3 = param.Number(default=0.9, bounds=(0, 1), doc="Intensity of mondrian 3")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), doc="Background intensity")
    
    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "positions": ((self.pos1_y, self.pos1_x), (self.pos2_y, self.pos2_x), (self.pos3_y, self.pos3_x)),
            "sizes": ((self.size1_h, self.size1_w, self.size1_d), (self.size2_h, self.size2_w, self.size2_d), (self.size3_h, self.size3_w, self.size3_d)),
            "intensities": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.mondrians import mondrian
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive mondrian
mondrian_params = MondrianParams()
disp = InteractiveStimDisplay(mondrian, mondrian_params)
disp.layout
```

## Corrugated Mondrian
{py:func}`stimupy.stimuli.mondrians.corrugated_mondrian`

```{code-cell} ipython3
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

```{code-cell} ipython3
from stimupy.stimuli.mondrians import corrugated_mondrian
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive corrugated_mondrian
corrugated_mondrian_params = CorrugatedMondrianParams()
disp = InteractiveStimDisplay(corrugated_mondrian, corrugated_mondrian_params)
disp.layout
```
