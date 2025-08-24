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

# Mondrian
{py:func}`stimupy.stimuli.mondrians.mondrian`

```{pyodide}
:skip-embed:

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

```{pyodide}
:skip-embed:

from stimupy.stimuli.mondrians import mondrian
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive mondrian
mondrian_params = MondrianParams()
disp = InteractiveStimDisplay(mondrian, mondrian_params)
disp.layout
```
