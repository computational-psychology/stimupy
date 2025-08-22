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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/waves.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Waves
{py:mod}`stimupy.stimuli.waves`


## Sine, linear
{py:func}`stimupy.stimuli.waves.sine_linear`

```{code-cell} ipython3
import param

class SineLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensities_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low intensity")
    intensities_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High intensity")
    origin = param.Selector(default="corner", objects=["mean", "corner", "center"], doc="Origin")
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensities": (self.intensities_low, self.intensities_high),
            "origin": self.origin,
            "period": self.period,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import sine_linear
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine_linear
sine_linear_params = SineLinearParams()
disp = InteractiveStimDisplay(sine_linear, sine_linear_params)
disp.layout
```

## Square, linear
{py:func}`stimupy.stimuli.waves.square_linear`

```{code-cell} ipython3
import param

class SquareLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    origin = param.Selector(default="corner", objects=["mean", "corner", "center"], doc="Origin")
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "origin": self.origin,
            "period": self.period,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import square_linear
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_linear
square_linear_params = SquareLinearParams()
disp = InteractiveStimDisplay(square_linear, square_linear_params)
disp.layout
```

## Staircase, linear
{py:func}`stimupy.stimuli.waves.staircase_linear`

```{code-cell} ipython3
import param

class StaircaseLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    origin = param.Selector(default="corner", objects=["mean", "corner", "center"], doc="Origin")
    period = param.Selector(default="ignore", objects=["ignore", "even", "odd", "either"], doc="Period")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "origin": self.origin,
            "period": self.period,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import staircase_linear
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase_linear
staircase_linear_params = StaircaseLinearParams()
disp = InteractiveStimDisplay(staircase_linear, staircase_linear_params)
disp.layout
```

## Sine, radial
{py:func}`stimupy.stimuli.waves.sine_radial`

```{code-cell} ipython3
import param

class SineRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensities_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low intensity")
    intensities_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High intensity")
    clip = param.Boolean(default=False, doc="Clip stimulus")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensities": (self.intensities_low, self.intensities_high),
            "clip": self.clip,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import sine_radial
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive sine_radial
sine_radial_params = SineRadialParams()
disp = InteractiveStimDisplay(sine_radial, sine_radial_params)
disp.layout
```

## Square, radial
{py:func}`stimupy.stimuli.waves.square_radial`

```{code-cell} ipython3
import param

class SquareRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_rings_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low ring intensity")
    intensity_rings_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High ring intensity")
    clip = param.Boolean(default=False, doc="Clip stimulus")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_rings": (self.intensity_rings_low, self.intensity_rings_high),
            "clip": self.clip,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import square_radial
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_radial
square_radial_params = SquareRadialParams()
disp = InteractiveStimDisplay(square_radial, square_radial_params)
disp.layout
```

## Staircase, radial
{py:func}`stimupy.stimuli.waves.staircase_radial`

```{code-cell} ipython3
import param

class StaircaseRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_rings_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low ring intensity")
    intensity_rings_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High ring intensity")
    clip = param.Boolean(default=False, doc="Clip stimulus")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_rings": (self.intensity_rings_low, self.intensity_rings_high),
            "clip": self.clip,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import staircase_radial
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase_radial
staircase_radial_params = StaircaseRadialParams()
disp = InteractiveStimDisplay(staircase_radial, staircase_radial_params)
disp.layout
```

## Square, angular
{py:func}`stimupy.stimuli.waves.square_angular`

```{code-cell} ipython3
import param

class SquareAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8, bounds=(4, 20), step=1, doc="Frequency")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_segments_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low segment intensity")
    intensity_segments_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High segment intensity")
    origin = param.Selector(default="mean", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity_segments_low, self.intensity_segments_high),
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import square_angular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive square_angular
square_angular_params = SquareAngularParams()
disp = InteractiveStimDisplay(square_angular, square_angular_params)
disp.layout
```

## Staircase, angular
{py:func}`stimupy.stimuli.waves.staircase_angular`

```{code-cell} ipython3
import param

class StaircaseAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8, bounds=(4, 20), step=1, doc="Frequency")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_segments_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low segment intensity")
    intensity_segments_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High segment intensity")
    origin = param.Selector(default="center", objects=["mean", "corner", "center"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity_segments_low, self.intensity_segments_high),
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.waves import staircase_angular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive staircase_angular
staircase_angular_params = StaircaseAngularParams()
disp = InteractiveStimDisplay(staircase_angular, staircase_angular_params)
disp.layout
```
