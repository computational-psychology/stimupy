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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/plaids.md)
 to get interactivity
```

# Stimuli - Plaids
{py:mod}`stimupy.stimuli.plaids`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Plaid
{py:func}`stimupy.stimuli.plaids.plaid`

```{code-cell} ipython3
from stimupy.stimuli.plaids import plaid

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.Dropdown(value=False, options=[False, 'gaussian_mask', 'grating_mask', 'grating_mask2'], description="add mask")

w_sigma = iw.FloatSlider(value=2, min=0, max=4, description="sigma [deg]")
w_weight1 = iw.FloatSlider(value=1, min=0, max=1, description="weight1")
w_weight2 = iw.FloatSlider(value=1, min=0, max=1, description="weight2")

# Grating 1
w_freq1 = iw.FloatSlider(value=1, min=0, max=2, description="frequency1 [cpd]")
w_phase1 = iw.FloatSlider(value=0, min=0, max=360, description="phase shift1 [deg]")
w_rot1 = iw.FloatSlider(value=0, min=0, max=360, description="rotation1 [deg]")

w_int11 = iw.FloatSlider(value=1, min=0, max=1, description="int1-1")
w_int12 = iw.FloatSlider(value=0, min=0, max=1, description="int1_2")

# Grating 2
w_freq2 = iw.FloatSlider(value=1, min=0, max=2, description="frequency2 [cpd]")
w_phase2 = iw.FloatSlider(value=0, min=0, max=360, description="phase shift2 [deg]")
w_rot2 = iw.FloatSlider(value=90, min=0, max=360, description="rotation2 [deg]")

w_int21 = iw.FloatSlider(value=1, min=0, max=1, description="int2-1")
w_int22 = iw.FloatSlider(value=0, min=0, max=1, description="int2_2")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_weight = iw.HBox([w_sigma, w_weight1, w_weight2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])

b_geometry1 = iw.HBox([w_freq1, w_phase1, w_rot1])
b_intensities1 = iw.HBox([w_int11, w_int12])

b_geometry2 = iw.HBox([w_freq2, w_phase2, w_rot2])
b_intensities2 = iw.HBox([w_int21, w_int22])

ui = iw.VBox([b_im_size, b_weight, b_add, b_geometry1, b_intensities1, b_geometry2, b_intensities2])

# Function for showing stim
def show_plaid(
    height=None,
    width=None,
    ppd=None,
    sigma=None,
    weight1=None,
    weight2=None,
    rotation1=None,
    frequency1=None,
    phase_shift1=None,
    int11=None,
    int12=None,
    rotation2=None,
    frequency2=None,
    phase_shift2=None,
    int21=None,
    int22=None,
    origin=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    p_common = {
        "visual_size": (height, width),
        "ppd": ppd,
        "origin": origin,
        "round_phase_width": round_phase_width,
        "period": period,
        "distance_metric": "rotated",
    }
    
    p_grating1 = {
        "frequency": frequency1,
        "rotation": rotation1,
        "phase_shift": phase_shift1,
        "intensities": (int11, int12),
    }
    
    p_grating2 = {
        "frequency": frequency2,
        "rotation": rotation2,
        "phase_shift": phase_shift2,
        "intensities": (int21, int22),
    }

    stim = plaid(
        grating_parameters1={**p_common, **p_grating1},
        grating_parameters2={**p_common, **p_grating2},
        weight1=weight1,
        weight2=weight2,
        sigma=sigma,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_plaid,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "sigma": w_sigma,
        "weight1": w_weight1,
        "weight2": w_weight2,
        "rotation1": w_rot1,
        "frequency1": w_freq1,
        "phase_shift1": w_phase1,
        "int11": w_int11,
        "int12": w_int12,
        "rotation2": w_rot2,
        "frequency2": w_freq2,
        "phase_shift2": w_phase2,
        "int21": w_int21,
        "int22": w_int22,
        "origin": w_ori,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```