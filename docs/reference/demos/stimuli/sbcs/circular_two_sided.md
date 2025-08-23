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

# Circular, Two sided
{py:func}`stimupy.stimuli.sbcs.circular_two_sided`

```{code-cell} ipython3
import param

class CircularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius")
    target_radius_right = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius")
    surround_radius_left = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius")
    surround_radius_right = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    intensity_surround_left = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity")
    intensity_surround_right = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.sbcs import circular_two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circular_two_sided
circular_two_sided_params = CircularTwoSidedParams()
disp = InteractiveStimDisplay(circular_two_sided, circular_two_sided_params)
disp.layout
```
