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

# Checkerboard
{py:func}`stimupy.stimuli.checkerboards.checkerboard`

```{pyodide}
:skip-embed:

import param

class CheckerboardParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Checkerboard geometry parameters
    frequency1 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Frequency 1 in cycles per degree")
    frequency2 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Frequency 2 in cycles per degree")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")
    
    # Intensity parameters
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    
    # Target parameters
    target_x = param.Integer(default=0, bounds=(0, 10), doc="Target x index")
    target_y = param.Integer(default=0, bounds=(0, 10), doc="Target y index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    extend_targets = param.Boolean(default=False, doc="Extend targets")
    
    # Additional parameters
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")
    round_phase_width = param.Boolean(default=False, doc="Round check width")
    add_mask = param.Selector(default=None, objects=[None, "target_mask", "checker_mask", "row_mask", "col_mask"], doc="Add mask")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": (self.frequency1, self.frequency2),
            "period": self.period,
            "rotation": self.rotation,
            "intensity_checks": (self.intensity1, self.intensity2),
            "round_phase_width": self.round_phase_width,
            "target_indices": ((self.target_y, self.target_x),),
            "intensity_target": self.intensity_target,
            "extend_targets": self.extend_targets,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.checkerboards import checkerboard
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive checkerboard
checkerboard_params = CheckerboardParams()
disp = InteractiveStimDisplay(checkerboard, checkerboard_params)
disp.layout
```
