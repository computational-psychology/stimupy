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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/benarys.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Benary's cross
{py:mod}`stimupy.stimuli.benarys`



## Cross, generalized
{py:func}`stimupy.stimuli.benarys.cross_generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import cross_generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="cross thickness [deg]")

w_theight = iw.FloatSlider(value=2, min=1, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=1, max=4, description="target width [deg]")
w_ttype = iw.Dropdown(value="r", options=['r', 't'], description="target type")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_ty = iw.FloatSlider(value=2, min=1, max=4, description="target y [deg]")
w_tx = iw.FloatSlider(value=2, min=1, max=4, description="target x [deg]")
w_trot = iw.IntSlider(value=0, min=0, max=360, description="target rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'cross_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_theight, w_twidth, w_ttype, w_tint])
b_target2 = iw.HBox([w_ty, w_tx, w_trot])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_target2, b_add])

# Function for showing stim
def show_cross_generalized(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_height=None,
    target_width=None,
    target_type=None,
    intensity_target=None,
    target_x=None,
    target_y=None,
    target_rotation=None,
    add_mask=False,
):
    try:
        stim = cross_generalized(
            visual_size=(height, width),
            ppd=ppd,
            cross_thickness=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=(target_height, target_width),
            target_type=target_type,
            intensity_target=intensity_target,
            target_x=target_x,
            target_y=target_y,
            target_rotation=target_rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_cross_generalized,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_height": w_theight,
        "target_width": w_twidth,
        "target_type": w_ttype,
        "intensity_target": w_tint,
        "target_x": w_tx,
        "target_y": w_ty,
        "target_rotation": w_trot,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross, rectangles
{py:func}`stimupy.stimuli.benarys.cross_rectangles`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import cross_rectangles

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="cross thickness [deg]")

w_theight = iw.FloatSlider(value=2, min=1, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=1, max=4, description="target width [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'cross_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_theight, w_twidth, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_add])

# Function for showing stim
def show_cross_rectangles(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_height=None,
    target_width=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = cross_rectangles(
            visual_size=(height, width),
            ppd=ppd,
            cross_thickness=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=(target_height, target_width),
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_cross_rectangles,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_height": w_theight,
        "target_width": w_twidth,
        "intensity_target": w_tint,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross triangles
{py:func}`stimupy.stimuli.benarys.cross_triangles`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import cross_triangles

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="cross thickness [deg]")

w_tsize = iw.FloatSlider(value=2, min=1, max=4, description="target size [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'cross_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_tsize, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_add])

# Function for showing stim
def show_cross_triangles(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_size=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = cross_triangles(
            visual_size=(height, width),
            ppd=ppd,
            cross_thickness=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=target_size,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_cross_triangles,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_size": w_tsize,
        "intensity_target": w_tint,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Todorovic generalized
{py:func}`stimupy.stimuli.benarys.todorovic_generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import todorovic_generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="L width [deg]")

w_theight = iw.FloatSlider(value=2, min=1, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=1, max=4, description="target width [deg]")
w_ttype = iw.Dropdown(value="r", options=['r', 't'], description="target type")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_ty = iw.FloatSlider(value=2, min=1, max=4, description="target y [deg]")
w_tx = iw.FloatSlider(value=2, min=1, max=4, description="target x [deg]")
w_trot = iw.IntSlider(value=0, min=0, max=360, description="target rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'L_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_theight, w_twidth, w_ttype, w_tint])
b_target2 = iw.HBox([w_ty, w_tx, w_trot])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_target2, b_add])

# Function for showing stim
def show_todorovic_generalized(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_height=None,
    target_width=None,
    target_type=None,
    intensity_target=None,
    target_x=None,
    target_y=None,
    target_rotation=None,
    add_mask=False,
):
    try:
        stim = todorovic_generalized(
            visual_size=(height, width),
            ppd=ppd,
            L_width=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=(target_height, target_width),
            target_type=target_type,
            intensity_target=intensity_target,
            target_x=target_x,
            target_y=target_y,
            target_rotation=target_rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_todorovic_generalized,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_height": w_theight,
        "target_width": w_twidth,
        "target_type": w_ttype,
        "intensity_target": w_tint,
        "target_x": w_tx,
        "target_y": w_ty,
        "target_rotation": w_trot,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Todorovic rectangles
{py:func}`stimupy.stimuli.benarys.todorovic_rectangles`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import todorovic_rectangles

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="L width [deg]")

w_theight = iw.FloatSlider(value=2, min=1, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=1, max=4, description="target width [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'L_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_theight, w_twidth, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_add])

# Function for showing stim
def show_todorovic_rectangles(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_height=None,
    target_width=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = todorovic_rectangles(
            visual_size=(height, width),
            ppd=ppd,
            L_width=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=(target_height, target_width),
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_todorovic_rectangles,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_height": w_theight,
        "target_width": w_twidth,
        "intensity_target": w_tint,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Todorovic triangles
{py:func}`stimupy.stimuli.benarys.todorovic_triangles`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.benarys import todorovic_triangles

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_cthick = iw.FloatSlider(value=2, min=1, max=10, description="L width [deg]")

w_theight = iw.FloatSlider(value=2, min=1, max=4, description="target size [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int cross")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'L_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_cthick])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target1 = iw.HBox([w_theight, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target1, b_add])

# Function for showing stim
def show_todorovic_triangles(
    height=None,
    width=None,
    ppd=None,
    cross_thickness=None,
    intensity1=None,
    intensity_background=None,
    target_size=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = todorovic_triangles(
            visual_size=(height, width),
            ppd=ppd,
            L_width=cross_thickness,
            intensity_cross=intensity1,
            intensity_background=intensity_background,
            target_size=target_size,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_todorovic_triangles,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "cross_thickness": w_cthick,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "target_size": w_theight,
        "intensity_target": w_tint,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
