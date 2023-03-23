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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/whites.md)
 to get interactivity
```

# Stimuli - Whites
{py:mod}`stimupy.stimuli.whites`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Generalized
{py:func}`stimupy.stimuli.whites.generalized`

```{code-cell} ipython3
from stimupy.stimuli.whites import generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_tidx = iw.IntSlider(value=1, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_toff = iw.FloatSlider(value=0, min=-5, max=5, description="target center offset [deg]")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-1, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_toff2 = iw.FloatSlider(value=0, min=-5, max=5, description="target2 center offset [deg]")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_target = iw.HBox([w_tidx, w_tint, w_toff, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_toff2, w_theights2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_target2, b_add])

# Function for showing stim
def show_generalized(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_center_offsets=None,
    target_heights=None,
    target_idx2=None,
    intensity_target2=None,
    target_center_offsets2=None,
    target_heights2=None,
):
    stim = generalized(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        period=period,
        target_indices=(target_idx, target_idx2),
        intensity_target=(intensity_target, intensity_target2),
        target_center_offsets=(target_center_offsets, target_center_offsets2),
        target_heights=(target_heights, target_heights2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_generalized,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_center_offsets": w_toff,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_center_offsets2": w_toff2,
        "target_heights2": w_theights2,
    },
)

# Show
display(ui, out)
```

## White
{py:func}`stimupy.stimuli.whites.white`

```{code-cell} ipython3
from stimupy.stimuli.whites import white

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_tidx = iw.IntSlider(value=1, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-1, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_target = iw.HBox([w_tidx, w_tint, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_theights2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_target2, b_add])

# Function for showing stim
def show_white(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_idx2=None,
    intensity_target2=None,
    target_heights=None,
    target_heights2=None,
):
    stim = white(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        period=period,
        target_indices=(target_idx, target_idx2),
        intensity_target=(intensity_target, intensity_target2),
        target_height=(target_heights, target_heights2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_white,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_heights2": w_theights2,
    },
)

# Show
display(ui, out)
```

## White, two-rows
{py:func}`stimupy.stimuli.whites.white_two_rows`

```{code-cell} ipython3
from stimupy.stimuli.whites import white_two_rows

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_toff = iw.FloatSlider(value=0, min=-5, max=5, description="target center offset [deg]")

w_tidx = iw.IntSlider(value=1, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-1, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_toff = w_toff
b_target = iw.HBox([w_tidx, w_tint, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_theights2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_toff, b_target, b_target2, b_add])

# Function for showing stim
def show_white_two_rows(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_center_offsets=None,
    target_heights=None,
    target_idx2=None,
    intensity_target2=None,
    target_heights2=None,
):
    stim = white_two_rows(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
        origin=origin,
        period=period,
        target_indices_top=target_idx,
        target_indices_bottom=target_idx2,
        intensity_target=(intensity_target, intensity_target2),
        target_center_offset=target_center_offsets,
        target_height=(target_heights, target_heights2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_white_two_rows,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_center_offsets": w_toff,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_heights2": w_theights2,
    },
)

# Show
display(ui, out)
```

## Anderson
{py:func}`stimupy.stimuli.whites.anderson`

```{code-cell} ipython3
from stimupy.stimuli.whites import anderson

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_toff = iw.FloatSlider(value=1.5, min=0, max=5, description="target center offset [deg]")

w_tidx = iw.IntSlider(value=5, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-4, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_sheight = iw.FloatSlider(value=1, min=0, max=5, description="stripe height [deg]")
w_soff = iw.FloatSlider(value=2, min=0, max=5, description="stripe center offset [deg]")
w_sint1 = iw.FloatSlider(value=1.0, min=0, max=1, description="stripe1 int")
w_sint2 = iw.FloatSlider(value=0.0, min=0, max=1, description="stripe2 int")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_toff = w_toff
b_target = iw.HBox([w_tidx, w_tint, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_theights2])
b_stripe = iw.HBox([w_sheight, w_soff, w_sint1, w_sint2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_toff, b_target, b_target2, b_stripe, b_add])

# Function for showing stim
def show_anderson(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_center_offsets=None,
    target_heights=None,
    target_idx2=None,
    intensity_target2=None,
    target_heights2=None,
    stripe_height=None,
    stripe_center_offset=None,
    stripe_int1=None,
    stripe_int2=None,
):
    stim = anderson(
        visual_size=(height, width),
        ppd=ppd,
#        rotation=rotation,
        frequency=frequency,
#        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
#        origin=origin,
        period=period,
        target_indices_top=target_idx,
        target_indices_bottom=target_idx2,
        intensity_target=(intensity_target, intensity_target2),
        target_center_offset=target_center_offsets,
        target_height=target_heights,
        stripe_height=stripe_height,
        stripe_center_offset=stripe_center_offset,
        intensity_stripes=(stripe_int1, stripe_int2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_anderson,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_center_offsets": w_toff,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_heights2": w_theights2,
        "stripe_height": w_sheight,
        "stripe_center_offset": w_soff,
        "stripe_int1": w_sint1,
        "stripe_int2": w_sint2,
    },
)

# Show
display(ui, out)
```

## Howe
{py:func}`stimupy.stimuli.whites.howe`

```{code-cell} ipython3
from stimupy.stimuli.whites import howe

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_toff = iw.FloatSlider(value=1.5, min=0, max=5, description="target center offset [deg]")

w_tidx = iw.IntSlider(value=5, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-4, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_sint1 = iw.FloatSlider(value=1.0, min=0, max=1, description="stripe1 int")
w_sint2 = iw.FloatSlider(value=0.0, min=0, max=1, description="stripe2 int")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_toff = w_toff
b_target = iw.HBox([w_tidx, w_tint, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_theights2])
b_stripe = iw.HBox([w_sint1, w_sint2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_toff, b_target, b_target2, b_stripe, b_add])

# Function for showing stim
def show_howe(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_center_offsets=None,
    target_heights=None,
    target_idx2=None,
    intensity_target2=None,
    target_heights2=None,
    stripe_int1=None,
    stripe_int2=None,
):
    stim = howe(
        visual_size=(height, width),
        ppd=ppd,
#        rotation=rotation,
        frequency=frequency,
#        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
#        origin=origin,
        period=period,
        target_indices_top=target_idx,
        target_indices_bottom=target_idx2,
        intensity_target=(intensity_target, intensity_target2),
        target_center_offset=target_center_offsets,
        target_height=target_heights,
        intensity_stripes=(stripe_int1, stripe_int2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_howe,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_center_offsets": w_toff,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_heights2": w_theights2,
        "stripe_int1": w_sint1,
        "stripe_int2": w_sint2,
    },
)

# Show
display(ui, out)
```

## Yazdanbakhsh
{py:func}`stimupy.stimuli.whites.yazdanbakhsh`

```{code-cell} ipython3
from stimupy.stimuli.whites import yazdanbakhsh

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_toff = iw.FloatSlider(value=1.5, min=0, max=5, description="target center offset [deg]")
w_gap = iw.FloatSlider(value=0.1, min=0, max=1, description="gap size [deg]")

w_tidx = iw.IntSlider(value=5, min=0, max=20, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_theights = iw.FloatSlider(value=1, min=0, max=5, description="target heights [deg]")

w_tidx2 = iw.IntSlider(value=-4, min=-20, max=0, description="target2 idx")
w_tint2 = iw.FloatSlider(value=0.5, min=0, max=1, description="target2 int")
w_theights2 = iw.FloatSlider(value=1, min=0, max=5, description="target2 heights [deg]")

w_sint1 = iw.FloatSlider(value=1.0, min=0, max=1, description="stripe1 int")
w_sint2 = iw.FloatSlider(value=0.0, min=0, max=1, description="stripe2 int")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_toff = iw.HBox([w_toff, w_gap])
b_target = iw.HBox([w_tidx, w_tint, w_theights])
b_target2 = iw.HBox([w_tidx2, w_tint2, w_theights2])
b_stripe = iw.HBox([w_sint1, w_sint2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_toff, b_target, b_target2, b_stripe, b_add])

# Function for showing stim
def show_yazdanbakhsh(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    sigma=None,
    int1=None,
    int2=None,
    origin=None,
    period=None,
    add_mask=False,
    target_idx=None,
    intensity_target=None,
    target_center_offsets=None,
    target_heights=None,
    target_idx2=None,
    intensity_target2=None,
    target_heights2=None,
    gap_size=None,
    stripe_int1=None,
    stripe_int2=None,
):
    stim = yazdanbakhsh(
        visual_size=(height, width),
        ppd=ppd,
#        rotation=rotation,
        frequency=frequency,
#        phase_shift=phase_shift,
        intensity_bars=(int1, int2),
#        origin=origin,
        period=period,
        target_indices_top=target_idx,
        target_indices_bottom=target_idx2,
        intensity_target=(intensity_target, intensity_target2),
        target_center_offset=target_center_offsets,
        target_height=target_heights,
        intensity_stripes=(stripe_int1, stripe_int2),
        gap_size=gap_size,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_yazdanbakhsh,
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
        "period": w_period,
        "add_mask": w_mask,
        "target_idx": w_tidx,
        "intensity_target": w_tint,
        "target_center_offsets": w_toff,
        "target_heights": w_theights,
        "target_idx2": w_tidx2,
        "intensity_target2": w_tint2,
        "target_heights2": w_theights2,
        "stripe_int1": w_sint1,
        "stripe_int2": w_sint2,
        "gap_size": w_gap,
    },
)

# Show
display(ui, out)
```

## Circular
{py:func}`stimupy.stimuli.whites.circular`

```{code-cell} ipython3
from stimupy.stimuli.whites import circular

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
w_clip = iw.ToggleButton(value=True, disabled=False, description="clip to aperature")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'grating_mask'], description="add mask")

w_tidx = iw.IntSlider(value=1, min=1, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_ori, w_period, w_round, w_clip, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_circular(
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
    clip=True,
):
    stim = circular(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_rings=(int1, int2),
        origin=origin,
        round_phase_width=round_phase_width,
        period=period,
        target_indices=target_indices,
        intensity_target=intensity_target,
        clip=clip,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_circular,
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
        "clip": w_clip,
    },
)

# Show
display(ui, out)
```

## Radial
{py:func}`stimupy.stimuli.whites.radial`

```{code-cell} ipython3
from stimupy.stimuli.whites import radial

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_nseg = iw.IntSlider(value=6, min=2, max=12, description="n_segments")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="int background")

w_tidx = iw.IntSlider(value=3, min=0, max=6, description="target idx")
w_twidth = iw.FloatSlider(value=2.5, min=0, max=5, description="target width")
w_tcent = iw.FloatSlider(value=2.5, min=0, max=5, description="target center")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'wedge_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_nseg, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tidx, w_twidth, w_tcent, w_tint])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_radial(
    height=None,
    width=None,
    ppd=None,
    n_segments=None,
    rotation=None,
    intensity1=None,
    intensity2=None,
    intensity_background=None,
    target_indices=None,
    target_width=None,
    target_center=None,
    intensity_target=None,
    origin=None,
    add_mask=False,
):
    stim = radial(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        n_segments=n_segments,
        intensity_segments=(intensity1, intensity2),
        intensity_background=intensity_background,
        origin=origin,
        target_indices=target_indices,
        target_width=target_width,
        target_center=target_center,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_radial,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "n_segments": w_nseg,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
        "target_indices": w_tidx,
        "target_width": w_twidth,
        "target_center": w_tcent,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Wedding-cake
{py:func}`stimupy.stimuli.whites.wedding_cake`

```{code-cell} ipython3
from stimupy.stimuli.whites import wedding_cake

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_Lheight = iw.FloatSlider(value=2, min=0, max=5, description="L-height [deg]")
w_Lwidth = iw.FloatSlider(value=2, min=0, max=5, description="L-width [deg]")
w_Lthick = iw.FloatSlider(value=0.5, min=0, max=2, description="L-thickness [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")

w_tidx11 = iw.IntSlider(value=0, min=0, max=5, description="target1 idx1")
w_tidx12 = iw.IntSlider(value=0, min=-5, max=5, description="target1 idx2")
w_tidx21 = iw.IntSlider(value=0, min=0, max=5, description="target1 idx1")
w_tidx22 = iw.IntSlider(value=0, min=-5, max=5, description="target2 idx2")

w_theight = iw.FloatSlider(value=0.5, min=0, max=2, description="target height [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_Lheight, w_Lwidth, w_Lthick])
b_intensities = iw.HBox([w_int1, w_int2])
b_target = iw.HBox([w_theight, w_tint])
b_target_idx = iw.HBox([w_tidx11, w_tidx12, w_tidx21, w_tidx22])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_target_idx, b_add])

# Function for showing stim
def show_wedding_cake(
    height=None,
    width=None,
    ppd=None,
    add_mask=False,
    L_height=None,
    L_width=None,
    L_thick=None,
    int1=None,
    int2=None,
    tidx11=None,
    tidx12=None,
    tidx21=None,
    tidx22=None,
    theight=None,
    int_target=None,
):
    stim = wedding_cake(
        visual_size=(height, width),
        ppd=ppd,
        L_size=(L_height, L_width, L_thick),
        target_height=theight,
        intensity_target=int_target,
        target_indices1=((tidx11, tidx12),),
        target_indices2=((tidx21, tidx22),),
        intensity_bars=(int1, int2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_wedding_cake,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "L_height": w_Lheight,
        "L_width": w_Lwidth,
        "L_thick": w_Lthick,
        "int1": w_int1,
        "int2": w_int2,
        "tidx11": w_tidx11,
        "tidx12": w_tidx12,
        "tidx21": w_tidx21,
        "tidx22": w_tidx22,
        "theight": w_theight,
        "int_target": w_tint,
        
    },
)

# Show
display(ui, out)
```
