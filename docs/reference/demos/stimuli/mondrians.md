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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/mondrians.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Mondrians
{py:mod}`stimupy.stimuli.mondrians`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim


import numpy as np
import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Mondrian
{py:func}`stimupy.stimuli.mondrians.mondrian`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.mondrians import mondrian

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

# Mondrian 1
w_x1 = iw.FloatSlider(value=4, min=0, max=10, description="x1")
w_y1 = iw.FloatSlider(value=4, min=0, max=10, description="y1")
w_h1 = iw.FloatSlider(value=3, min=0, max=6, description="height1")
w_w1 = iw.FloatSlider(value=3, min=0, max=6, description="width1")
w_int1 = iw.FloatSlider(value=0.2, min=0, max=1, description="int1")

# Mondrian 2
w_x2 = iw.FloatSlider(value=2, min=0, max=10, description="x2")
w_y2 = iw.FloatSlider(value=2, min=0, max=10, description="y2")
w_h2 = iw.FloatSlider(value=3, min=0, max=6, description="height2")
w_w2 = iw.FloatSlider(value=3, min=0, max=6, description="width2")
w_int2 = iw.FloatSlider(value=0.6, min=0, max=1, description="int2")

# Mondrian 3
w_x3 = iw.FloatSlider(value=6, min=0, max=10, description="x3")
w_y3 = iw.FloatSlider(value=6, min=0, max=10, description="y3")
w_h3 = iw.FloatSlider(value=3, min=0, max=6, description="height3")
w_w3 = iw.FloatSlider(value=3, min=0, max=6, description="width3")
w_int3 = iw.FloatSlider(value=0.9, min=0, max=1, description="int3")

w_intback = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity_background")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_x = iw.HBox([w_x1, w_x2, w_x3])
b_y = iw.HBox([w_y1, w_y2, w_y3])
b_h = iw.HBox([w_h1, w_h2, w_h3])
b_w = iw.HBox([w_w1, w_w2, w_w3])
b_int = iw.HBox([w_int1, w_int2, w_int3])
b_add = iw.HBox([w_intback, w_mask])
ui = iw.VBox([b_im_size, b_x, b_y, b_h, b_w, b_int, b_add])

# Function for showing stim
def show_mondrian(
    height=None,
    width=None,
    ppd=None,
    intensity_background=None,
    x1=None,
    y1=None,
    h1=None,
    w1=None,
    int1=None,
    x2=None,
    y2=None,
    h2=None,
    w2=None,
    int2=None,
    x3=None,
    y3=None,
    h3=None,
    w3=None,
    int3=None,
    add_mask=False,
):
    try:
        stim = mondrian(
            visual_size=(height, width),
            ppd=ppd,
            positions=((y1, x1), (y2, x2), (y3, x3)),
            sizes=((h1, w1), (h2, w2), (h3, w3)),
            intensities=(int1, int2, int3),
            intensity_background=intensity_background,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_mondrian,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "x1": w_x1,
        "y1": w_y1,
        "h1": w_h1,
        "w1": w_w1,
        "int1": w_int1,
        "x2": w_x2,
        "y2": w_y2,
        "h2": w_h2,
        "w2": w_w2,
        "int2": w_int2,
        "x3": w_x3,
        "y3": w_y3,
        "h3": w_h3,
        "w3": w_w3,
        "int3": w_int3,
        "intensity_background": w_intback,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Corrugated Mondrian
{py:func}`stimupy.stimuli.mondrians.corrugated`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.mondrians import corrugated_mondrian

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=30, min=1, max=60, description="ppd")

w_mdepth1 = iw.FloatSlider(value=-2., min=-2, max=2, description="depth 1")
w_mdepth2 = iw.FloatSlider(value=0., min=-2, max=2, description="depth 2")
w_mdepth3 = iw.FloatSlider(value=2., min=-2, max=2, description="depth 3")

w_intback = iw.FloatSlider(value=0.5, min=0, max=1, description="int back")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'mondrian_mask'], description="add mask")

w_tidx1 = iw.IntSlider(value=1, min=0, max=10, description="target idx1")
w_tidx2 = iw.IntSlider(value=1, min=0, max=10, description="target idx2")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_depths = iw.HBox([w_mdepth1, w_mdepth2, w_mdepth3])
b_target = iw.HBox([w_tidx1, w_tidx2, w_tint])
b_add = iw.HBox([w_intback, w_mask])
ui = iw.VBox([b_im_size, b_depths, b_target, b_add])

# Function for showing stim
def show_corrugated_mondrian(
    height=None,
    width=None,
    ppd=None,
    intensity_background=None,
    add_mask=False,
    depth1=None,
    depth2=None,
    depth3=None,
    target_idx1=None,
    target_idx2=None,
    intensity_target=None,
):
    try:
        intensities = np.random.rand(3, 4)
        stim = corrugated_mondrian(
            visual_size=(height, width),
            ppd=ppd,
            depths=(depth1, depth2, depth3),
            intensities=intensities,
            intensity_background=intensity_background,
            intensity_target=intensity_target,
            target_indices=((target_idx1, target_idx2),),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_corrugated_mondrian,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity_background": w_intback,
        "add_mask": w_mask,
        "depth1": w_mdepth1,
        "depth2": w_mdepth2,
        "depth3": w_mdepth3,
        "target_idx1": w_tidx1,
        "target_idx2": w_tidx2,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```
