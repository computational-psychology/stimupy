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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/mueller_lyers.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Mueller-Lyers
{py:mod}`stimupy.stimuli.mueller_lyers`



## Mueller-Lyer
{py:func}`stimupy.stimuli.mueller_lyers.mueller_lyer`

```{code-cell} ipython3
import param

class MuellerLyerParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_lines_length = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Outer line length")
    outer_lines_angle = param.Number(default=45, bounds=(-180, 180), step=1, doc="Outer line angle")
    line_width = param.Number(default=0, bounds=(0, 0.5), step=0.01, doc="Line width")
    target_length = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="Target length")
    intensity_outer_lines = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Outer lines intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_lines_length": self.outer_lines_length,
            "outer_lines_angle": self.outer_lines_angle,
            "line_width": self.line_width,
            "target_length": self.target_length,
            "intensity_outer_lines": self.intensity_outer_lines,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.mueller_lyers import mueller_lyer
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive mueller_lyer
mueller_lyer_params = MuellerLyerParams()
disp = InteractiveStimDisplay(mueller_lyer, mueller_lyer_params)
disp.layout
```

## Two-sided
{py:func}`stimupy.stimuli.mueller_lyers.two_sided`

```{code-cell} ipython3
import param

class TwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_lines_length = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Outer line length")
    outer_lines_angle = param.Number(default=45, bounds=(-180, 180), step=1, doc="Outer line angle")
    line_width = param.Number(default=0, bounds=(0, 0.5), step=0.01, doc="Line width")
    target_length = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="Target length")
    intensity_outer_lines = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Outer lines intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_lines_length": self.outer_lines_length,
            "outer_lines_angle": self.outer_lines_angle,
            "line_width": self.line_width,
            "target_length": self.target_length,
            "intensity_outer_lines": self.intensity_outer_lines,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.mueller_lyers import two_sided
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive two_sided
two_sided_params = TwoSidedParams()
disp = InteractiveStimDisplay(two_sided, two_sided_params)
disp.layout
```
