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

# Radial
{py:func}`stimupy.stimuli.whites.radial`

```{code-cell} ipython3
import param

class RadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_rings_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low ring intensity")
    intensity_rings_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High ring intensity")
    target_indices = param.List(default=[1], doc="Target indices")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity_rings_low, self.intensity_rings_high),
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import radial
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive radial
radial_params = RadialParams()
disp = InteractiveStimDisplay(radial, radial_params)
disp.layout
```