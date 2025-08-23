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

# Gaussian
{py:func}`stimupy.components.gaussians.gaussian`

```{code-cell} ipython3
import param

class GaussianParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Gaussian parameters
    sigma1 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Sigma 1 in degrees")
    sigma2 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Sigma 2 in degrees")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")
    
    # Intensity parameters
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    
    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": (self.sigma1, self.sigma2),
            "origin": self.origin,
            "rotation": self.rotation,
            "intensity_max": self.intensity_max,
        }
```

```{code-cell} ipython3
from stimupy.components.gaussians import gaussian
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive gaussian
gaussian_params = GaussianParams()
disp = InteractiveStimDisplay(gaussian, gaussian_params)
disp.layout
```
