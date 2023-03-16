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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/illusions/cubes.md)
 to get interactivity
```

# Illusions - Cubes
{py:mod}`stimupy.illusions.cubes`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Varying cells
{py:func}`stimupy.illusions.cubes.varying_cells`

```{code-cell} ipython3
from stimupy.illusions.cubes import varying_cells

# Define widgets
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cl1 = iw.FloatSlider(value=2, min=0, max=4, description="c1-length")
w_cl2 = iw.FloatSlider(value=2, min=0, max=4, description="c2-length")
w_cl3 = iw.FloatSlider(value=2, min=0, max=4, description="c3-length")
w_cl4 = iw.FloatSlider(value=2, min=0, max=4, description="c4-length")

w_ct = iw.FloatSlider(value=2, min=0, max=4, description="cell thickness")
w_cs = iw.FloatSlider(value=2, min=0, max=4, description="cell spacing")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cells")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")

w_tidx = iw.IntSlider(value=0, min=0, max=3, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'cell_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_ppd])
b_cell_lengths = iw.HBox([w_cl1, w_cl2, w_cl3, w_cl4])
b_cell_geom = iw.HBox([w_ct, w_cs])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_cell_lengths, b_cell_geom, b_intensities, b_target, b_add])

# Function for showing stim
def show_varying_cells(
    ppd=None,
    intensity1=None,
    intensity_background=None,
    target_indices=None,
    intensity_target=None,
    add_mask=False,
    cell_l1=None,
    cell_l2=None,
    cell_l3=None,
    cell_l4=None,
    cell_t=None,
    cell_s=None,
):
    stim = varying_cells(
        ppd=ppd,
        cell_lengths=(cell_l1, cell_l2, cell_l3, cell_l4),
        cell_thickness=cell_t,
        cell_spacing=cell_s,
        target_indices=target_indices,
        intensity_background=intensity_background,
        intensity_cells=intensity1,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_varying_cells,
    {
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
        "target_indices": w_tidx,
        "intensity_target": w_tint,
        "cell_l1": w_cl1,
        "cell_l2": w_cl2,
        "cell_l3": w_cl3,
        "cell_l4": w_cl4,
        "cell_t": w_ct,
        "cell_s": w_cs,
    },
)

# Show
display(ui, out)
```

## Cube
{py:func}`stimupy.illusions.cubes.cube`

```{code-cell} ipython3
from stimupy.illusions.cubes import cube

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cn = iw.IntSlider(value=4, min=1, max=8, description="n-cells")
w_ct = iw.FloatSlider(value=1, min=0, max=4, description="cell thickness")
w_cs = iw.FloatSlider(value=1, min=0, max=4, description="cell spacing")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cells")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")

w_tidx = iw.IntSlider(value=0, min=0, max=3, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'cell_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_cell_geom = iw.HBox([w_cn, w_ct, w_cs])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_cell_geom, b_intensities, b_target, b_add])

# Function for showing stim
def show_cube(
    height=None,
    width=None,
    ppd=None,
    intensity1=None,
    intensity_background=None,
    target_indices=None,
    intensity_target=None,
    add_mask=False,
    n_cells=None,
    cell_t=None,
    cell_s=None,
):
    stim = cube(
        visual_size=(height, width),
        ppd=ppd,
        n_cells=n_cells,
        cell_thickness=cell_t,
        cell_spacing=cell_s,
        target_indices=target_indices,
        intensity_background=intensity_background,
        intensity_cells=intensity1,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_cube,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
        "target_indices": w_tidx,
        "intensity_target": w_tint,
        "n_cells": w_cn,
        "cell_t": w_ct,
        "cell_s": w_cs,
    },
)

# Show
display(ui, out)
```
