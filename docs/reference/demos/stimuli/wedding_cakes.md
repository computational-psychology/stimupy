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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/wedding_cakes.md)
 to get interactivity
```

# Stimuli - Wedding cakes
{py:mod}`stimupy.stimuli.wedding_cakes`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Wedding cake
{py:func}`stimupy.stimuli.wedding_cakes.wedding_cake`

```{code-cell} ipython3
from stimupy.stimuli.wedding_cakes import wedding_cake

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
