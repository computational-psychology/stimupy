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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/waves.md)
 to get interactivity
```

# Stimuli - Waves
{py:mod}`stimupy.stimuli.waves`

```{code-cell} ipython3
:tags: [remove-cell]

import numpy as np
import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Sine, linear

## Square, linear
{py:func}`stimupy.stimuli.waves.square_linear`

```{code-cell} ipython3
from stimupy.stimuli.waves import square_linear

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="corner", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'grating_mask'], description="add mask")

w_tidx = iw.IntSlider(value=1, min=1, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_square_linear(
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
    target_indices=None,
    intensity_target=None,
):
    stim = square_linear(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        round_phase_width=round_phase_width,
        period=period,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_square_linear,
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
        "target_indices": w_tidx,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Sine, radial

## Square, radial

## Sine, rectilinear

## Square, rectilinear

## Sine, angular

## Square, angular