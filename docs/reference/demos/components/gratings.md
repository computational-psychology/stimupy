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

```{important}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/gratings.md)
 to get interactivity
```

# Components - Gratings
{py:mod}`stimupy.components.gratings`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Sine-wave
{py:func}`stimupy.components.gratings.sine_wave`

```{code-cell} ipython3
from stimupy.components.gratings import sine_wave

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_sine_wave(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    origin=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    stim = sine_wave(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        round_phase_width=round_phase_width,
        period=period,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_sine_wave,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Square-wave
{py:func}`stimupy.components.gratings.square_wave`

```{code-cell} ipython3
from stimupy.components.gratings import square_wave

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_square_wave(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    origin=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    stim = square_wave(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        round_phase_width=round_phase_width,
        period=period,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_square_wave,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Staircase
{py:func}`stimupy.components.gratings.staircase`

```{code-cell} ipython3
from stimupy.components.gratings import staircase

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=0.5, min=0, max=2, description="frequency [cpd]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_staircase(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    int1=None,
    int2=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    stim = staircase(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        intensity_bars=(int1, int2),
        round_phase_width=round_phase_width,
        period=period,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_staircase,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency": w_freq,
        "int1": w_int1,
        "int2": w_int2,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
