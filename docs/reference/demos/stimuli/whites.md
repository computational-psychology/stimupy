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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/whites.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Stimuli - Whites
{py:mod}`stimupy.stimuli.whites`



## Generalized
{py:func}`stimupy.stimuli.whites.generalized`

```{code-cell} ipython3
import param

class GeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    target_indices = param.List(default=[1], doc="Target indices")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_center_offsets = param.Number(default=0, bounds=(-5, 5), step=0.1, doc="Target center offsets")
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
            "target_center_offsets": self.target_center_offsets,
            "target_heights": self.target_heights,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import generalized
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive generalized
generalized_params = GeneralizedParams()
disp = InteractiveStimDisplay(generalized, generalized_params)
disp.layout
```

## White
{py:func}`stimupy.stimuli.whites.white`

```{code-cell} ipython3
import param

class WhiteParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    target_indices = param.List(default=[1], doc="Target indices")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
            "target_heights": self.target_heights,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import white
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive white
white_params = WhiteParams()
disp = InteractiveStimDisplay(white, white_params)
disp.layout
```

## White, two-rows
{py:func}`stimupy.stimuli.whites.white_two_rows`

```{code-cell} ipython3
import param

class WhiteTwoRowsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[1], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_heights": self.target_heights,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import white_two_rows
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive white_two_rows
white_two_rows_params = WhiteTwoRowsParams()
disp = InteractiveStimDisplay(white_two_rows, white_two_rows_params)
disp.layout
```

## Anderson
{py:func}`stimupy.stimuli.whites.anderson`

```{code-cell} ipython3
import param

class AndersonParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[2], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_height = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target height")
    intensity_stripes_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low stripe intensity")
    intensity_stripes_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High stripe intensity")
    stripe_center_offset = param.Number(default=2, bounds=(-5, 5), step=0.1, doc="Stripe center offset")
    stripe_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Stripe height")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_height": self.target_height,
            "intensity_stripes": (self.intensity_stripes_low, self.intensity_stripes_high),
            "stripe_center_offset": self.stripe_center_offset,
            "stripe_height": self.stripe_height,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import anderson
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive anderson
anderson_params = AndersonParams()
disp = InteractiveStimDisplay(anderson, anderson_params)
disp.layout
```

## Howe
{py:func}`stimupy.stimuli.whites.howe`

```{code-cell} ipython3
import param

class HoweParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[2], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_height = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target height")
    intensity_stripes_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low stripe intensity")
    intensity_stripes_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High stripe intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_height": self.target_height,
            "intensity_stripes": (self.intensity_stripes_low, self.intensity_stripes_high),
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import howe
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive howe
howe_params = HoweParams()
disp = InteractiveStimDisplay(howe, howe_params)
disp.layout
```

## Yazdanbakhsh
{py:func}`stimupy.stimuli.whites.yazdanbakhsh`

```{code-cell} ipython3
import param

class YazdanbakhshParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    n_bars = param.Integer(default=10, bounds=(4, 20), doc="Number of bars")
    target_indices_top = param.List(default=[2], doc="Top target indices")
    target_indices_bottom = param.List(default=[-3], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_heights = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target heights")
    gap_size = param.Number(default=0.5, bounds=(0, 2), step=0.1, doc="Gap size")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "n_bars": self.n_bars,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_heights": self.target_heights,
            "gap_size": self.gap_size,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import yazdanbakhsh
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive yazdanbakhsh
yazdanbakhsh_params = YazdanbakhshParams()
disp = InteractiveStimDisplay(yazdanbakhsh, yazdanbakhsh_params)
disp.layout
```

## Radial
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

## Angular
{py:func}`stimupy.stimuli.whites.angular`

```{code-cell} ipython3
import param

class AngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=32, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=16, bounds=(4, 20), step=1, doc="Angular frequency")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_segments_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low segment intensity")
    intensity_segments_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High segment intensity")
    target_indices = param.List(default=[2], doc="Target indices")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity")
    target_width = param.Number(default=1.0, bounds=(0, 90), step=1, doc="Target width in degrees", allow_None=True)
    target_center = param.Number(default=3, bounds=(0, 10), step=0.1, doc="Target center radius", allow_None=True)

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity_segments_low, self.intensity_segments_high),
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
            "target_width": self.target_width,
            "target_center": self.target_center,
        }
```

```{code-cell} ipython3
from stimupy.stimuli.whites import angular
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive angular
angular_params = AngularParams()
disp = InteractiveStimDisplay(angular, angular_params)
disp.layout
```

## Wedding-cake
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
