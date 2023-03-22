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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/mondrians.md)
 to get interactivity
```

# Stimuli - Mondrians
{py:mod}`stimupy.stimuli.mondrians`

```{code-cell} ipython3
:tags: [remove-cell]

import numpy as np
import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Corrugated Mondrians
{py:func}`stimupy.stimuli.mondrians.corrugated_mondrians`

```{code-cell} ipython3
from stimupy.stimuli.mondrians import corrugated_mondrians

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=30, min=1, max=60, description="ppd")

w_mdepth1 = iw.FloatSlider(value=-2., min=-2, max=2, description="mondrian depth 1")
w_mdepth2 = iw.FloatSlider(value=0., min=-2, max=2, description="mondrian depth 2")
w_mdepth3 = iw.FloatSlider(value=2., min=-2, max=2, description="mondrian depth 3")

w_intback = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity_background")
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
def show_corrugated_mondrians(
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
    intensities = np.random.rand(3, 4)

    stim = corrugated_mondrians(
        visual_size=(height, width),
        ppd=ppd,
        mondrian_depths=(depth1, depth2, depth3),
        mondrian_intensities=intensities,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=((target_idx1, target_idx2),),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_corrugated_mondrians,
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
