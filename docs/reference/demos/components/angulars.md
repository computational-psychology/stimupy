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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/angulars.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Components - Angulars
{py:mod}`stimupy.components.angulars`



## Wedge
{py:func}`stimupy.components.angulars.wedge`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.angulars import wedge

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_wwidth = iw.IntSlider(value=45, min=1, max=90, description="angle [deg]")

w_oradius = iw.FloatSlider(value=3, min=1, max=6, description="outer radius [deg]")
w_iradius = iw.FloatSlider(value=0, min=0, max=3, description="inner radius [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity wedge")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_angles = iw.HBox([w_wwidth])
b_geometry = iw.HBox([w_oradius, w_iradius])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_angles, b_geometry, b_intensities, b_add])

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
        angle=wwidth,
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

## Segments
{py:func}`stimupy.components.angulars.segments`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.angulars import segments

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_wwidth1 = iw.IntSlider(value=45, min=1, max=90, description="angle1 [deg]")
w_wwidth2 = iw.IntSlider(value=90, min=1, max=180, description="angle2 [deg]")
w_wwidth3 = iw.IntSlider(value=135, min=1, max=360, description="angle3 [deg]")

w_oradius = iw.FloatSlider(value=3, min=1, max=6, description="outer radius [deg]")
w_iradius = iw.FloatSlider(value=0, min=0, max=3, description="inner radius [deg]")

w_int1 = iw.FloatSlider(value=0.2, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0.5, min=0, max=1, description="int2")
w_int3 = iw.FloatSlider(value=0.8, min=0, max=1, description="int3")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity back")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_angles = iw.HBox([w_wwidth1, w_wwidth2, w_wwidth3])
b_intensities = iw.HBox([w_int1, w_int2, w_int3, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_angles, b_intensities, b_add])

# Function for showing stim
def show_segments(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    wwidth1=None,
    wwidth2=None,
    wwidth3=None,
    int1=None,
    int2=None,
    int3=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = segments(
        visual_size=(height, width),
        ppd=ppd,
        angles=(wwidth1, wwidth2, wwidth3),
        rotation=rotation,
        intensity_segments=(int1, int2, int3),
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_segments,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "wwidth1": w_wwidth1,
        "wwidth2": w_wwidth2,
        "wwidth3": w_wwidth3,
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
