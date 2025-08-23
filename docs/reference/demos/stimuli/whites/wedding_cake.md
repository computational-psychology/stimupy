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

# Wedding-cake
{py:func}`stimupy.stimuli.whites.wedding_cake`

```{code-cell} ipython3
import param

class WeddingCakeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_size_height = param.Number(default=4, bounds=(1, 8), step=0.1, doc="L height")
    L_size_width = param.Number(default=3, bounds=(1, 6), step=0.1, doc="L width")
    L_size_thickness = param.Number(default=1, bounds=(0.5, 3), step=0.1, doc="L thickness")
    target_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Target height")
    target_indices1_y1 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 Y1 index")
    target_indices1_x1 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 X1 index")
    target_indices1_y2 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 Y2 index")
    target_indices1_x2 = param.Integer(default=1, bounds=(0, 5), doc="Target 1 X2 index")
    target_indices2_y1 = param.Integer(default=2, bounds=(0, 5), doc="Target 2 Y1 index")
    target_indices2_x1 = param.Integer(default=-1, bounds=(-5, 5), doc="Target 2 X1 index")
    target_indices2_y2 = param.Integer(default=2, bounds=(0, 5), doc="Target 2 Y2 index")
    target_indices2_x2 = param.Integer(default=0, bounds=(-5, 5), doc="Target 2 X2 index")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_size": (self.L_size_height, self.L_size_width, self.L_size_thickness),
            "target_height": self.target_height,
            "target_indices1": ((self.target_indices1_y1, self.target_indices1_x1), (self.target_indices1_y2, self.target_indices1_x2)),
            "target_indices2": ((self.target_indices2_y1, self.target_indices2_x1), (self.target_indices2_y2, self.target_indices2_x2)),
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import wedding_cake
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive wedding_cake
wedding_cake_params = WeddingCakeParams()
disp = InteractiveStimDisplay(wedding_cake, wedding_cake_params)
disp.layout
```
