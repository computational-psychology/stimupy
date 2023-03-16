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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/gaussians.md)
 to get interactivity
```

# Components - Gaussians
{py:mod}`stimupy.components.gaussians`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Gaussian
{py:func}`stimupy.components.gaussians.gaussian`

```{code-cell} ipython3
from stimupy.components.gaussians import gaussian

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_sig1 = iw.FloatSlider(value=1, min=0, max=3, description="sigma1 [deg]")
w_sig2 = iw.FloatSlider(value=1, min=0, max=3, description="sigma2 [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity max")

w_ori = iw.Dropdown(value="center", options=['center', 'mean', 'corner'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_sig1, w_sig2, w_rot])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, w_int1, b_add])

# Function for showing stim
def show_gaussian(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    sigma1=None,
    sigma2=None,
    origin=None,
    intensity_max=None,
    add_mask=False,
):

    stim = gaussian(
        visual_size=(height, width),
        ppd=ppd,
        sigma=(sigma1, sigma2),
        origin=origin,
        rotation=rotation,
        intensity_max=intensity_max,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_gaussian,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "sigma1": w_sig1,
        "sigma2": w_sig2,
        "origin": w_ori,
        "intensity_max": w_int1,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
