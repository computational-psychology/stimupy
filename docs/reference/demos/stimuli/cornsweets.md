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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/cornsweets.md)
 to get interactivity
```

# Stimuli - Cornsweets
{py:mod}`stimupy.stimuli.cornsweets`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Cornsweet
{py:func}`stimupy.stimuli.cornsweets.cornsweet`

```{code-cell} ipython3
from stimupy.stimuli.cornsweets import cornsweet

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_rwid = iw.FloatSlider(value=2, min=0, max=5, description="ramp width [deg]")
w_exp = iw.FloatSlider(value=2.75, min=0.5, max=5, description="exponent")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="int plateau")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'edge_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_rwid, w_exp, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_cornsweet(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    intensity1=None,
    intensity2=None,
    intensity_plateau=None,
    ramp_width=None,
    exponent=None,
    add_mask=False,
):
    stim = cornsweet(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        intensity_edges=(intensity1, intensity2),
        intensity_plateau=intensity_plateau,
        ramp_width=ramp_width,
        exponent=exponent,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_cornsweet,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_plateau": w_int_back,
        "ramp_width": w_rwid,
        "exponent": w_exp,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
