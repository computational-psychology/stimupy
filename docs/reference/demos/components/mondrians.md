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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/mondrians.md)
 to get interactivity
```

# Components - Mondrians
{py:mod}`stimupy.components.mondrians`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Mondrians
{py:func}`stimupy.components.mondrians.mondrians`

```{code-cell} ipython3
from stimupy.components.mondrians import mondrians

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
w_x2 = iw.FloatSlider(value=4, min=0, max=10, description="x2")
w_y2 = iw.FloatSlider(value=4, min=0, max=10, description="y2")
w_h2 = iw.FloatSlider(value=3, min=0, max=6, description="height2")
w_w2 = iw.FloatSlider(value=3, min=0, max=6, description="width2")
w_int2 = iw.FloatSlider(value=0.6, min=0, max=1, description="int2")

# Mondrian 3
w_x3 = iw.FloatSlider(value=4, min=0, max=10, description="x3")
w_y3 = iw.FloatSlider(value=4, min=0, max=10, description="y3")
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
def show_mondrians(
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

    stim = mondrians(
        visual_size=(height, width),
        ppd=ppd,
        mondrian_positions=((y1, x1), (y2, x2), (y3, x3)),
        mondrian_sizes=((h1, w1), (h2, w2), (h3, w3)),
        mondrian_intensities=(int1, int2, int3),
        intensity_background=intensity_background,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_mondrians,
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
