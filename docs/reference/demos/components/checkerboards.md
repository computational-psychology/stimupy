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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/checkerboards.md)
 to get interactivity
```

# Components - Checkerboards
{py:mod}`stimupy.components.checkerboards`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Checkerboard
{py:func}`stimupy.components.checkerboards.checkerboard`

```{code-cell} ipython3
from stimupy.components.checkerboards import checkerboard

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq1 = iw.FloatSlider(value=1, min=0, max=3, description="frequency1 [cpd]")
w_freq2 = iw.FloatSlider(value=1, min=0, max=3, description="frequency2 [cpd]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")

w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round check width")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq1, w_freq2, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

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
):

    stim = checkerboard(
        visual_size=(height, width),
        ppd=ppd,
        frequency=(frequency1, frequency2),
        period=period,
        rotation=rotation,
        intensity_checks=(intensity1, intensity2),
        round_phase_width=round_phase_width,
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
    },
)

# Show
display(ui, out)
```
