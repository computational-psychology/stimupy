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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/angulars.md)
 to get interactivity
```

# Components - Angulars
{py:mod}`stimupy.components.angulars`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Wedge
{py:func}`stimupy.components.angulars.wedge`

```{code-cell} ipython3
from stimupy.components.angulars import wedge

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_wwidth = iw.IntSlider(value=45, min=1, max=90, description="width [deg]")
w_oradius = iw.FloatSlider(value=3, min=1, max=6, description="outer radius [deg]")
w_iradius = iw.FloatSlider(value=0, min=0, max=3, description="inner radius [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity wedge")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_wwidth, w_oradius, w_iradius, w_rot])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_wedge(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    wwidth=None,
    radius=None,
    inner_radius=None,
    intensity_wedge=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = wedge(
        visual_size=(height, width),
        ppd=ppd,
        width=wwidth,
        radius=radius,
        rotation=rotation,
        inner_radius=inner_radius,
        intensity_wedge=intensity_wedge,
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_wedge,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "wwidth": w_wwidth,
        "radius": w_oradius,
        "inner_radius": w_iradius,
        "intensity_wedge": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Grating
{py:func}`stimupy.components.angulars.grating`

```{code-cell} ipython3
from stimupy.components.angulars import grating

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_nseg = iw.IntSlider(value=6, min=2, max=12, description="n_segments")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_nseg, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_grating(
    height=None,
    width=None,
    ppd=None,
    n_segments=None,
    rotation=None,
    intensity1=None,
    intensity2=None,
    origin=None,
    add_mask=False,
):
    stim = grating(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        n_segments=n_segments,
        intensity_segments=(intensity1, intensity2),
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_grating,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "n_segments": w_nseg,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Pinwheel
{py:func}`stimupy.components.angulars.pinwheel`

```{code-cell} ipython3
from stimupy.components.angulars import pinwheel

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_oradius = iw.FloatSlider(value=4, min=2, max=6, description="outer radius [deg]")
w_iradius = iw.FloatSlider(value=0, min=0, max=3, description="inner radius [deg]")
w_nseg = iw.IntSlider(value=6, min=2, max=12, description="n_segments")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_oradius, w_iradius, w_nseg, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_pinwheel(
    height=None,
    width=None,
    ppd=None,
    radius=None,
    inner_radius=None,
    n_segments=None,
    rotation=None,
    intensity1=None,
    intensity2=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = pinwheel(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        radius=radius,
        n_segments=n_segments,
        intensity_segments=(intensity1, intensity2),
        intensity_background=intensity_background,
        inner_radius=inner_radius,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_pinwheel,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius": w_oradius,
        "inner_radius": w_iradius,
        "n_segments": w_nseg,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
