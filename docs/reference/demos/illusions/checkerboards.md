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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/illusions/checkerboards.md)
 to get interactivity
```

# Illusions - Checkerboards
{py:mod}`stimupy.illusions.checkerboards`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Checkerboard
{py:func}`stimupy.illusions.checkerboards.checkerboard`

```{code-cell} ipython3
from stimupy.illusions.checkerboards import checkerboard

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq1 = iw.FloatSlider(value=1, min=0, max=3, description="frequency1 [cpd]")
w_freq2 = iw.FloatSlider(value=1, min=0, max=3, description="frequency2 [cpd]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")

w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round check width")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'checker_mask', 'grating_mask', 'grating_mask2'], description="add mask")

w_tidxx = iw.IntSlider(value=0, min=0, max=10, description="target x-idx")
w_tidxy = iw.IntSlider(value=0, min=0, max=10, description="target y-idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")
w_text = iw.ToggleButton(value=False, disabled=False, description="extend target")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq1, w_freq2, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_period, w_round, w_mask])
b_target = iw.HBox([w_tidxx, w_tidxy, w_tint, w_text])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_checkerboard(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    frequency1=None,
    frequency2=None,
    period=None,
    intensity1=None,
    intensity2=None,
    add_mask=False,
    round_phase_width=False,
    target_x=None,
    target_y=None,
    intensity_target=None,
    extend_targets=False,
):

    stim = checkerboard(
        visual_size=(height, width),
        ppd=ppd,
        frequency=(frequency1, frequency2),
        period=period,
        rotation=rotation,
        intensity_checks=(intensity1, intensity2),
        round_phase_width=round_phase_width,
        target_indices=((target_y, target_x),),
        intensity_target=intensity_target,
        extend_targets=extend_targets,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_checkerboard,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency1": w_freq1,
        "frequency2": w_freq2,
        "period": w_period,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "round_phase_width": w_round,
        "add_mask": w_mask,
        "target_y": w_tidxy,
        "target_x": w_tidxx,
        "intensity_target": w_tint,
        "extend_targets": w_text,
    },
)

# Show
display(ui, out)
```

## Contrast-contrast
{py:func}`stimupy.illusions.checkerboards.contrast_contrast`

```{code-cell} ipython3
from stimupy.illusions.checkerboards import contrast_contrast

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq1 = iw.FloatSlider(value=1, min=0, max=3, description="frequency1 [cpd]")
w_freq2 = iw.FloatSlider(value=1, min=0, max=3, description="frequency2 [cpd]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")

w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round check width")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'checker_mask', 'grating_mask', 'grating_mask2'], description="add mask")

w_tidxy = iw.IntSlider(value=5, min=0, max=10, description="target height")
w_tidxx = iw.IntSlider(value=5, min=0, max=10, description="target width")
w_ttau = iw.FloatSlider(value=0.5, min=0, max=1, description="tau")
w_talpha = iw.FloatSlider(value=0.5, min=0, max=1, description="alpha")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq1, w_freq2, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_period, w_round, w_mask])
b_target = iw.HBox([w_tidxy, w_tidxx, w_ttau, w_talpha])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_contrast_contrast(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    frequency1=None,
    frequency2=None,
    period=None,
    intensity1=None,
    intensity2=None,
    add_mask=False,
    round_phase_width=False,
    target_x=None,
    target_y=None,
    alpha=None,
    tau=False,
):

    stim = contrast_contrast(
        visual_size=(height, width),
        ppd=ppd,
        frequency=(frequency1, frequency2),
        period=period,
        rotation=rotation,
        intensity_checks=(intensity1, intensity2),
        round_phase_width=round_phase_width,
        target_shape=(target_y, target_x),
        alpha=alpha,
        tau=tau,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_contrast_contrast,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency1": w_freq1,
        "frequency2": w_freq2,
        "period": w_period,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "round_phase_width": w_round,
        "add_mask": w_mask,
        "target_y": w_tidxy,
        "target_x": w_tidxx,
        "alpha": w_talpha,
        "tau": w_ttau,
    },
)

# Show
display(ui, out)
```
