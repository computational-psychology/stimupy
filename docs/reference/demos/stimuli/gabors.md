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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/gabors.md)
 to get interactivity
```

# Stimuli - Gabors
{py:mod}`stimupy.stimuli.gabors`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```


## Gabor
{py:func}`stimupy.stimuli.gabors.gabor`

```{code-cell} ipython3
from stimupy.stimuli.gabors import gabor

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_sigma = iw.FloatSlider(value=2, min=0, max=4, description="sigma [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase, w_rot, w_sigma])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_gabor(
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
):
    stim = gabor(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        frequency=frequency,
        phase_shift=phase_shift,
        sigma=sigma,
        intensities=(int1, int2),
        origin=origin,
        period=period,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_gabor,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "sigma": w_sigma,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```