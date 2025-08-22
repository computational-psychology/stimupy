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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/angulars.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Pinwheels
{py:mod}`stimupy.stimuli.pinwheels`



## Pinwheel
{py:func}`stimupy.stimuli.pinwheels.pinwheel`

```{code-cell} ipython3
import param

class PinwheelParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    n_segments = param.Integer(default=6, bounds=(2, 12), doc="Number of segments")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=3, bounds=(0, 12), doc="Target index")
    target_width = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Target width")
    target_center = param.Number(default=2.5, bounds=(0.5, 5), step=0.1, doc="Target center radius")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin position")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_segments": self.n_segments,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx,),
            "target_width": self.target_width,
            "target_center": self.target_center,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.pinwheels import pinwheel
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive pinwheel
pinwheel_params = PinwheelParams()
disp = InteractiveStimDisplay(pinwheel, pinwheel_params)
disp.layout
```
