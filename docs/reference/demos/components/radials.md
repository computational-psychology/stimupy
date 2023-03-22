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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/radials.md)
 to get interactivity
```

# Components - Radials
{py:mod}`stimupy.components.radials`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Disc
{py:func}`stimupy.components.radials.disc`

```{code-cell} ipython3
from stimupy.components.radials import disc

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")
w_radius = iw.FloatSlider(value=3, min=1, max=6, description="radius [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity disc")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_radius])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_intensities, b_add])

# Function for showing stim
def show_disc(
    height=None,
    width=None,
    ppd=None,
    radius=None,
    intensity_disc=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = disc(
        visual_size=(height, width),
        ppd=ppd,
        radius=radius,
        intensity_disc=intensity_disc,
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_disc,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius": w_radius,
        "intensity_disc": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Annulus (/ Ring)
{py:func}`stimupy.components.radials.annulus`

```{code-cell} ipython3
from stimupy.components.radials import annulus

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_radius1 = iw.FloatSlider(value=2, min=1, max=4, description="radius1 [deg]")
w_radius2 = iw.FloatSlider(value=4, min=3, max=6, description="radius2 [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity ring")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius1, w_radius2])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_annulus(
    height=None,
    width=None,
    ppd=None,
    radius1=None,
    radius2=None,
    intensity_ring=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = annulus(
        visual_size=(height, width),
        ppd=ppd,
        radii=(radius1, radius2),
        intensity_ring=intensity_ring,
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_annulus,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius1": w_radius1,
        "radius2": w_radius2,
        "intensity_ring": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```


## Rings
{py:func}`stimupy.components.radials.rings`

```{code-cell} ipython3
from stimupy.components.radials import rings

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_radius1 = iw.FloatSlider(value=1, min=0, max=2, description="radius1 [deg]")
w_radius2 = iw.FloatSlider(value=2, min=1, max=3, description="radius2 [deg]")
w_radius3 = iw.FloatSlider(value=3, min=2, max=4, description="radius2 [deg]")

w_int1 = iw.FloatSlider(value=0.8, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0.5, min=0, max=1, description="int-ring2")
w_int3 = iw.FloatSlider(value=0.3, min=0, max=1, description="int-ring3")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius1, w_radius2, w_radius3])
b_intensities = iw.HBox([w_int1, w_int2, w_int3, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_rings(
    height=None,
    width=None,
    ppd=None,
    radius1=None,
    radius2=None,
    radius3=None,
    int1=None,
    int2=None,
    int3=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = rings(
        visual_size=(height, width),
        ppd=ppd,
        radii=(radius1, radius2, radius3),
        intensity_rings=(int1, int2, int3),
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rings,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius1": w_radius1,
        "radius2": w_radius2,
        "radius3": w_radius3,
        "int1": w_int1,
        "int2": w_int2,
        "int3": w_int3,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
