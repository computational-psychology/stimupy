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

# Two-sided-rings
{py:func}`stimupy.stimuli.rings.rectangular_two_sided`

```{pyodide}
:skip-embed:

import param

class RectangularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 40), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_idx = param.Integer(default=1, bounds=(0, 10), doc="Target index")
    intensity_target_left = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity")
    intensity_target_right = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity")
    clip = param.Boolean(default=False, doc="Clip")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": ((self.intensity1, self.intensity2), (self.intensity2, self.intensity1)),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx, self.target_idx),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "clip": self.clip,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.rings import rectangular_two_sided
# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[3] / "_static")))from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangular_two_sided
rectangular_two_sided_params = RectangularTwoSidedParams()
disp = InteractiveStimDisplay(rectangular_two_sided, rectangular_two_sided_params)
disp.layout
```
