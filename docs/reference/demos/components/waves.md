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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/waves.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Components - Waves
{py:mod}`stimupy.components.waves`



## Sinewave
{py:func}`stimupy.components.waves.sine`

```{code-cell} ipython3
import param

class SineParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    distance_metric = param.Selector(default="horizontal", objects=['horizontal','vertical','oblique','radial','rectilinear','angular'], doc="")
    frequency = param.Number(default=1, bounds=(0, 2), step=0.01, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    rotation = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    intensity_min = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="center", objects=['mean', 'corner', 'center'], doc="")
    period = param.Selector(default="ignore", objects=['ignore', 'even', 'odd', 'either'], doc="")
    round_phase_width = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "distance_metric": self.distance_metric,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
            "period": self.period,
            "round_phase_width": self.round_phase_width,
        }
```

```{code-cell} ipython3
from stimupy.components.waves import sine
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine
sine_params = SineParams()
disp = InteractiveStimDisplay(sine, sine_params)
disp.layout
```

## Squarewave
{py:func}`stimupy.components.waves.square`

```{code-cell} ipython3
import param

class SquareParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    distance_metric = param.Selector(default="horizontal", objects=['horizontal','vertical','oblique','radial','rectilinear','angular'], doc="")
    frequency = param.Number(default=1, bounds=(0, 2), step=0.01, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    rotation = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    intensity_min = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="center", objects=['mean', 'corner', 'center'], doc="")
    period = param.Selector(default="ignore", objects=['ignore', 'even', 'odd', 'either'], doc="")
    round_phase_width = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "distance_metric": self.distance_metric,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
            "period": self.period,
            "round_phase_width": self.round_phase_width,
        }
```

```{code-cell} ipython3
from stimupy.components.waves import square
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square
square_params = SquareParams()
disp = InteractiveStimDisplay(square, square_params)
disp.layout
```

## Staircase
{py:func}`stimupy.components.waves.staircase`

```{code-cell} ipython3
import param

class StaircaseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    distance_metric = param.Selector(default="horizontal", objects=['horizontal','vertical','oblique','radial','rectilinear','angular'], doc="")
    frequency = param.Number(default=1, bounds=(0, 4), step=0.01, doc="")
    rotation = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    intensity_min = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="center", objects=['mean', 'corner', 'center'], doc="")
    period = param.Selector(default="ignore", objects=['ignore', 'even', 'odd', 'either'], doc="")
    round_phase_width = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "distance_metric": self.distance_metric,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
            "period": self.period,
            "round_phase_width": self.round_phase_width,
        }
```

```{code-cell} ipython3
from stimupy.components.waves import staircase
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase
staircase_params = StaircaseParams()
disp = InteractiveStimDisplay(staircase, staircase_params)
disp.layout
```

## Bessel
{py:func}`stimupy.components.waves.bessel`

```{code-cell} ipython3
import param

class BesselParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.01, doc="")
    order = param.Integer(default=0, bounds=(0, 5), doc="")
    intensity_center = param.Number(default=1, bounds=(0, 1), step=0.01, doc="")
    intensity_outer = param.Number(default=0, bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "order": self.order,
            "intensities": (self.intensity_center, self.intensity_outer),
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.waves import bessel
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive bessel
bessel_params = BesselParams()
disp = InteractiveStimDisplay(bessel, bessel_params)
disp.layout
```
