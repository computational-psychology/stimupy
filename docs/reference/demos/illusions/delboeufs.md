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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/illusions/delboeufs.md)
 to get interactivity
```

# Illusions - Delboeufs
{py:mod}`stimupy.illusions.delboeufs`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Delboeuf
{py:func}`stimupy.illusions.delboeufs.delboeuf`

```{code-cell} ipython3
from stimupy.illusions.delboeufs import delboeuf

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outr = iw.FloatSlider(value=4, min=0.5, max=8, description="outer radius [deg]")
w_outw = iw.FloatSlider(value=0, min=0, max=2, description="outer line width [deg]")

w_int1 = iw.FloatSlider(value=0, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=1., min=0, max=1, description="int background")

w_tr = iw.FloatSlider(value=2.5, min=0, max=5, description="target radius [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="int target")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outr, w_outw])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tr, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_delboeuf(
    height=None,
    width=None,
    ppd=None,
    outer_radius=None,
    outer_line_width=None,
    target_radius=None,
    intensity_outer_line=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
):
    stim = delboeuf(
        visual_size=(height, width),
        ppd=ppd,
        outer_radius=outer_radius,
        outer_line_width=outer_line_width,
        target_radius=target_radius,
        intensity_outer_line=intensity_outer_line,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_delboeuf,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_radius": w_outr,
        "outer_line_width": w_outw,
        "target_radius": w_tr,
        "intensity_target": w_tint,
        "intensity_background": w_int_back,
        "intensity_outer_line": w_int1,
    },
)

# Show
display(ui, out)
```

## Two-sided
{py:func}`stimupy.illusions.delboeufs.two_sided`

```{code-cell} ipython3
from stimupy.illusions.delboeufs import two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outr1 = iw.FloatSlider(value=4, min=0.5, max=8, description="outer radius1 [deg]")
w_outr2 = iw.FloatSlider(value=2.5, min=0.5, max=8, description="outer radius2 [deg]")
w_outw = iw.FloatSlider(value=0, min=0, max=2, description="outer line width [deg]")

w_int1 = iw.FloatSlider(value=0, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=1., min=0, max=1, description="int background")

w_tr = iw.FloatSlider(value=2., min=0, max=4, description="target radius [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="int target")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outr1, w_outr2, w_outw])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tr, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_two_sided(
    height=None,
    width=None,
    ppd=None,
    outer_radius1=None,
    outer_radius2=None,
    outer_line_width=None,
    target_radius=None,
    intensity_outer_line=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
):
    stim = two_sided(
        visual_size=(height, width),
        ppd=ppd,
        outer_radii=(outer_radius1, outer_radius2),
        outer_line_width=outer_line_width,
        target_radius=target_radius,
        intensity_outer_line=intensity_outer_line,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_radius1": w_outr1,
        "outer_radius2": w_outr2,
        "outer_line_width": w_outw,
        "target_radius": w_tr,
        "intensity_target": w_tint,
        "intensity_background": w_int_back,
        "intensity_outer_line": w_int1,
    },
)

# Show
display(ui, out)
```
