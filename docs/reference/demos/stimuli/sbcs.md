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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/sbcs.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - SBCs (Simultaneous Brightness Contrast)
{py:mod}`stimupy.stimuli.sbcs`



## Generalized
{py:func}`stimupy.stimuli.sbcs.generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.IntSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.IntSlider(value=3, min=1, max=6, description="target width [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_t_posx = iw.FloatSlider(value=3.0, min=0, max=10.0, description="horz. position")
w_t_posy = iw.FloatSlider(value=3.0, min=0, max=10.0, description="vert. position")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width, w_rot])
b_post = iw.HBox([w_t_posx, w_t_posy])
b_intensities = iw.HBox([w_tint, w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_post, b_intensities, b_add])

# Function for showing stim
def show_generalized(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    target_x=None,
    target_y=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
    rotation=0.0,
):
    try:
        stim = generalized(
            visual_size=(height, width),
            ppd=ppd,
            target_size=(target_height,target_width),
            target_position=(target_y,target_x),
            intensity_background=intensity_background,
            intensity_target=intensity_target,
            rotation=rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_generalized,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "target_x": w_t_posx,
        "target_y": w_t_posy,
        "intensity_background": w_int_back,
        "intensity_target": w_tint,
        "add_mask": w_mask,
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```

## Basic
{py:func}`stimupy.stimuli.sbcs.basic`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import basic

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.IntSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.IntSlider(value=3, min=1, max=6, description="target width [deg]")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width])
b_intensities = iw.HBox([w_tint, w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_intensities, b_add])

# Function for showing stim
def show_basic(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = basic(
            visual_size=(height, width),
            ppd=ppd,
            target_size=(target_height,target_width),
            intensity_background=intensity_background,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_basic,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "intensity_background": w_int_back,
        "intensity_target": w_tint,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Square
{py:func}`stimupy.stimuli.sbcs.square`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import square

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_radius_target = iw.FloatSlider(value=1, min=0, max=2, description="target radius [deg]")
w_radius_surround = iw.FloatSlider(value=2, min=1, max=3, description="surround radius [deg]")

w_int_surround = iw.FloatSlider(value=1, min=0, max=1, description="int surround")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="center", options=['mean', 'corner', 'center'], description="origin")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius_target, w_radius_surround])
b_intensities = iw.HBox([w_int_surround, w_int_back])
b_target = iw.HBox([w_tint])
b_add = iw.HBox([w_ori, w_rot, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_square(
    height=None,
    width=None,
    ppd=None,
    target_radius=None,
    surround_radius=None,
    intensity_surround=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
    intensity_target=None,
    rotation=0.0,
):
    try:
        stim = square(
            visual_size=(height, width),
            ppd=ppd,
            target_radius=target_radius,
            surround_radius=surround_radius,
            intensity_surround=intensity_surround,
            intensity_background=intensity_background,
            origin=origin,
            intensity_target=intensity_target,
            rotation=rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_square,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_radius": w_radius_target,
        "surround_radius": w_radius_surround,
        "intensity_surround": w_int_surround,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
        "intensity_target": w_tint,
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```


## Circular
{py:func}`stimupy.stimuli.sbcs.circular`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import circular

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_radius_target = iw.FloatSlider(value=1, min=0, max=2, description="target radius [deg]")
w_radius_surround = iw.FloatSlider(value=2, min=1, max=3, description="surround radius [deg]")

w_int_surround = iw.FloatSlider(value=1, min=0, max=1, description="int surround")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="center", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'ring_mask'], description="add mask")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius_target, w_radius_surround])
b_intensities = iw.HBox([w_int_surround, w_int_back])
b_target = iw.HBox([w_tint])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_circular(
    height=None,
    width=None,
    ppd=None,
    target_radius=None,
    surround_radius=None,
    intensity_surround=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
    intensity_target=None,
):
    try:
        stim = circular(
            visual_size=(height, width),
            ppd=ppd,
            target_radius=target_radius,
            surround_radius=surround_radius,
            intensity_surround=intensity_surround,
            intensity_background=intensity_background,
            origin=origin,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_circular,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_radius": w_radius_target,
        "surround_radius": w_radius_surround,
        "intensity_surround": w_int_surround,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Basic, Two sided
{py:func}`stimupy.stimuli.sbcs.basic_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import basic_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.IntSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.IntSlider(value=3, min=1, max=6, description="target width [deg]")

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target left")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target right")
w_int_back_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left background")
w_int_back_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right background")


w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width])
b_intensities = iw.HBox([w_tint_l, w_tint_r, w_int_back_l, w_int_back_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_intensities, b_add])

# Function for showing stim
def show_two_sided(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    intensity_background_l=None,
    intensity_background_r=None,
    intensity_target_l=None,
    intensity_target_r=None,
    add_mask=False,
):
    try:
        stim = basic_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_size=((target_height,target_width),(target_height,target_width)),
            intensity_background=(intensity_background_l, intensity_background_r),
            intensity_target=(intensity_target_l, intensity_target_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "intensity_background_l": w_int_back_l,
        "intensity_background_r": w_int_back_r,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Generalized, Two sided
{py:func}`stimupy.stimuli.sbcs.generalized_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import generalized_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height_l = iw.IntSlider(value=3, min=1, max=6, description="target height left [deg]")
w_t_width_l = iw.IntSlider(value=3, min=1, max=6, description="target width right [deg]")
w_t_height_r = iw.IntSlider(value=3, min=1, max=6, description="target height left [deg]")
w_t_width_r = iw.IntSlider(value=3, min=1, max=6, description="target width right [deg]")

w_t_y_l = iw.FloatSlider(value=5.0, min=0.0, max=20, description="y left target [deg]")
w_t_x_l = iw.FloatSlider(value=5.0, min=0.0, max=20, description="x left target [deg]") 
w_t_y_r = iw.FloatSlider(value=3.0, min=0.0, max=20, description="y right target [deg]")
w_t_x_r = iw.FloatSlider(value=3.0, min=0.0, max=20, description="x right target [deg]")

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target left")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target right")
w_int_back_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left background")
w_int_back_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right background")


w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size_l = iw.HBox([w_t_height_l, w_t_width_l])
b_t_size_r = iw.HBox([w_t_height_r, w_t_width_r])
b_t_pos_l = iw.HBox([w_t_y_l, w_t_x_l])
b_t_pos_r = iw.HBox([w_t_y_r, w_t_x_r])
b_intensities_l = iw.HBox([w_tint_l, w_int_back_l])
b_intensities_r = iw.HBox([w_tint_r, w_int_back_r])

b_left = iw.VBox([b_t_size_l, b_t_pos_l, b_intensities_l])
b_right = iw.VBox([b_t_size_r, b_t_pos_r, b_intensities_r])

b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_left, b_right, b_add])

# Function for showing stim
def show_gen_two_sided(
    height=None,
    width=None,
    ppd=None,
    target_height_l=None,
    target_width_l=None,
    target_height_r=None,
    target_width_r=None,
    target_pos_x_l=None,
    target_pos_y_l=None,
    target_pos_x_r=None,
    target_pos_y_r=None,
    intensity_background_l=None,
    intensity_background_r=None,
    intensity_target_l=None,
    intensity_target_r=None,
    add_mask=False,
):
    try:
        stim = generalized_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_size=((target_height_l,target_width_l),(target_height_r,target_width_r)),
            target_position=((target_pos_y_l, target_pos_x_l), (target_pos_y_r, target_pos_x_r)),
            intensity_background=(intensity_background_l, intensity_background_r),
            intensity_target=(intensity_target_l, intensity_target_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_gen_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height_l": w_t_height_l,
        "target_width_l": w_t_width_l,
        "target_height_r": w_t_height_r,
        "target_width_r": w_t_width_r,
        "target_pos_x_l": w_t_x_l,
        "target_pos_y_l": w_t_y_l,
        "target_pos_x_r": w_t_x_r,
        "target_pos_y_r": w_t_y_r,
        "intensity_background_l": w_int_back_l,
        "intensity_background_r": w_int_back_r,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Square, Two sided
{py:func}`stimupy.stimuli.sbcs.square_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import square_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_radius_l = iw.IntSlider(value=1, min=1, max=6, description="target radius left [deg]")
w_t_radius_r = iw.IntSlider(value=1, min=1, max=6, description="target radius right [deg]")
w_radius_surround_l = iw.IntSlider(value=2, min=1, max=6, description="surround radius left [deg]")
w_radius_surround_r = iw.IntSlider(value=2, min=1, max=6, description="surround radius right [deg]")

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target left")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target right")
w_int_surround_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left surround")
w_int_surround_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right surround")
w_int_background = iw.FloatSlider(value=.5, min=0, max=1, description="intenisty background")

w_rot_l = iw.FloatSlider(value=0, min=0, max=360, description="rotation left [deg]")
w_rot_r = iw.FloatSlider(value=0, min=0, max=360, description="rotation right [deg]")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_radius_l, w_t_radius_l])
b_s_size = iw.HBox([w_radius_surround_l, w_radius_surround_r])
b_intensities = iw.HBox([w_tint_l, w_tint_r, w_int_back_l, w_int_back_r])
b_add = iw.HBox([w_rot_l, w_rot_r, w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_s_size, b_intensities, b_add])

# Function for showing stim
def show_square_two_sided(
    height=None,
    width=None,
    ppd=None,
    target_radius_l=None,
    target_radius_r=None,
    surround_radius_l=None,
    surround_radius_r=None,
    intensity_surround_l=None,
    intensity_surround_r=None,
    intensity_target_l=None,
    intensity_target_r=None,
    intensity_background=None,
    add_mask=False,
    rotation_l=None,
    rotation_r=None,
):
    try:
        stim = square_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_radius=(target_radius_l,target_radius_r),
            surround_radius=(surround_radius_l, surround_radius_r),
            intensity_surround=(intensity_surround_l, intensity_surround_r),
            intensity_target=(intensity_target_l, intensity_target_r),
            intensity_background=intensity_background,
            rotation=(rotation_l, rotation_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_square_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_radius_l": w_t_radius_l,
        "target_radius_r": w_t_radius_r,
        "surround_radius_l": w_radius_surround_l,
        "surround_radius_r": w_radius_surround_r,
        "intensity_surround_l": w_int_surround_l,
        "intensity_surround_r": w_int_surround_r,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "intensity_background": w_int_background,
        "rotation_l": w_rot_l,
        "rotation_r": w_rot_r,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Circular, Two sided
{py:func}`stimupy.stimuli.sbcs.circular_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import circular_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_radius_l = iw.IntSlider(value=1, min=1, max=6, description="target radius left [deg]")
w_t_radius_r = iw.IntSlider(value=1, min=1, max=6, description="target radius right [deg]")
w_radius_surround_l = iw.IntSlider(value=2, min=1, max=6, description="surround radius left [deg]")
w_radius_surround_r = iw.IntSlider(value=2, min=1, max=6, description="surround radius right [deg]")

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target left")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target right")
w_int_surround_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left surround")
w_int_surround_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right surround")
w_int_background = iw.FloatSlider(value=.5, min=0, max=1, description="intenisty background")


w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_radius_l, w_t_radius_l])
b_s_size = iw.HBox([w_radius_surround_l, w_radius_surround_r])
b_intensities = iw.HBox([w_tint_l, w_tint_r, w_int_back_l, w_int_back_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_s_size, b_intensities, b_add])

# Function for showing stim
def show_circular_two_sided(
    height=None,
    width=None,
    ppd=None,
    target_radius_l=None,
    target_radius_r=None,
    surround_radius_l=None,
    surround_radius_r=None,
    intensity_surround_l=None,
    intensity_surround_r=None,
    intensity_target_l=None,
    intensity_target_r=None,
    intensity_background=None,
    add_mask=False,
):
    try:
        stim = circular_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_radius=(target_radius_l,target_radius_r),
            surround_radius=(surround_radius_l, surround_radius_r),
            intensity_surround=(intensity_surround_l, intensity_surround_r),
            intensity_target=(intensity_target_l, intensity_target_r),
            intensity_background=intensity_background,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_circular_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_radius_l": w_t_radius_l,
        "target_radius_r": w_t_radius_r,
        "surround_radius_l": w_radius_surround_l,
        "surround_radius_r": w_radius_surround_r,
        "intensity_surround_l": w_int_surround_l,
        "intensity_surround_r": w_int_surround_r,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "intensity_background": w_int_background,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```


## With dots
{py:func}`stimupy.stimuli.sbcs.with_dots`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import with_dots

# Define widgets
w_height = iw.IntSlider(value=15, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=15, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.FloatSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.FloatSlider(value=3, min=1, max=6, description="target width [deg]")

w_ndotsy = iw.IntSlider(value=5, min=1, max=10, description="n dots y")
w_ndotsx = iw.IntSlider(value=5, min=1, max=10, description="n dots x")
w_dotradius = iw.FloatSlider(value=.5, min=0.1, max=6.0, description="dot radius")
w_dotdist = iw.FloatSlider(value=0.25, min=0.1, max=3.0, description="dot distance")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_idots = iw.FloatSlider(value=1.0, min=0., max=1.0, description="intensity dots")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width, w_rot])
b_ndots = iw.HBox([w_ndotsy, w_ndotsx])
b_dotsize = iw.HBox([w_dotradius, w_dotdist])
b_intensities = iw.HBox([w_tint, w_int_back, w_idots])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_ndots, b_dotsize, b_intensities, b_add])

# Function for showing stim
def show_with_dots(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    ndotsy=None,
    ndotsx=None,
    dot_radius=None,
    dot_distance=None,
    intensity_background=None,
    intensity_target=None,
    intensity_dots=None,
    add_mask=False,
):
    try:
        stim = with_dots(
            visual_size=(height, width),
            ppd=ppd,
            target_shape=(target_height, target_width),
            n_dots=(ndotsy, ndotsx),
            dot_radius=dot_radius,
            distance=dot_distance,
            intensity_background=intensity_background,
            intensity_target=intensity_target,
            intensity_dots=intensity_dots,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_with_dots,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "ndotsy": w_ndotsy,
        "ndotsx": w_ndotsx,
        "dot_radius": w_dotradius,
        "dot_distance": w_dotdist,
        "intensity_background": w_int_back,
        "intensity_target": w_tint,
        "intensity_dots": w_idots,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## With dots, two sided
{py:func}`stimupy.stimuli.sbcs.with_dots_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import with_dots_two_sided

# Define widgets
w_height = iw.IntSlider(value=15, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=15, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.FloatSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.FloatSlider(value=3, min=1, max=6, description="target width [deg]")

w_ndotsy = iw.IntSlider(value=5, min=1, max=10, description="n dots y")
w_ndotsx = iw.IntSlider(value=5, min=1, max=10, description="n dots x")
w_dotradius = iw.FloatSlider(value=.5, min=0.1, max=6.0, description="dot radius")
w_dotdist = iw.FloatSlider(value=0.25, min=0.1, max=3.0, description="dot distance")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_idots_l = iw.FloatSlider(value=1.0, min=0., max=1.0, description="intensity left dots")
w_idots_r = iw.FloatSlider(value=0.0, min=0., max=1.0, description="intensity right dots")
w_int_back_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left background")
w_int_back_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right background")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width, w_rot])
b_ndots = iw.HBox([w_ndotsy, w_ndotsx])
b_dotsize = iw.HBox([w_dotradius, w_dotdist])
b_intensities = iw.HBox([w_tint, w_int_back_l, w_int_back_r, w_idots_l, w_idots_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_ndots, b_dotsize, b_intensities, b_add])

# Function for showing stim
def show_two_sided_with_dots(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    ndotsy=None,
    ndotsx=None,
    dot_radius=None,
    dot_distance=None,
    intensity_background_l=None,
    intensity_background_r=None,
    intensity_target=None,
    intensity_dots_l=None,
    intensity_dots_r=None,
    add_mask=False,
):
    try:
        stim = with_dots_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_shape=(target_height, target_width),
            n_dots=(ndotsy, ndotsx),
            dot_radius=dot_radius,
            distance=dot_distance,
            intensity_background=(intensity_background_l, intensity_background_r),
            intensity_target=intensity_target,
            intensity_dots=(intensity_dots_l, intensity_dots_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_two_sided_with_dots,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "ndotsy": w_ndotsy,
        "ndotsx": w_ndotsx,
        "dot_radius": w_dotradius,
        "dot_distance": w_dotdist,
        "intensity_background_l": w_int_back_l,
        "intensity_background_r": w_int_back_r,
        "intensity_target": w_tint,
        "intensity_dots_l": w_idots_l,
        "intensity_dots_r": w_idots_r,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Dotted
{py:func}`stimupy.stimuli.sbcs.dotted`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import dotted

# Define widgets
w_height = iw.IntSlider(value=15, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=15, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.FloatSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.FloatSlider(value=3, min=1, max=6, description="target width [deg]")

w_ndotsy = iw.IntSlider(value=5, min=1, max=10, description="n dots y")
w_ndotsx = iw.IntSlider(value=5, min=1, max=10, description="n dots x")
w_dotradius = iw.FloatSlider(value=.5, min=0.1, max=6.0, description="dot radius")
w_dotdist = iw.FloatSlider(value=0.25, min=0.1, max=3.0, description="dot distance")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_idots = iw.FloatSlider(value=1.0, min=0., max=1.0, description="intensity dots")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width, w_rot])
b_ndots = iw.HBox([w_ndotsy, w_ndotsx])
b_dotsize = iw.HBox([w_dotradius, w_dotdist])
b_intensities = iw.HBox([w_tint, w_int_back, w_idots])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_ndots, b_dotsize, b_intensities, b_add])

# Function for showing stim
def show_dotted(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    ndotsy=None,
    ndotsx=None,
    dot_radius=None,
    dot_distance=None,
    intensity_background=None,
    intensity_target=None,
    intensity_dots=None,
    add_mask=False,
):
    try:
        stim = dotted(
            visual_size=(height, width),
            ppd=ppd,
            target_shape=(target_height, target_width),
            n_dots=(ndotsy, ndotsx),
            dot_radius=dot_radius,
            distance=dot_distance,
            intensity_background=intensity_background,
            intensity_target=intensity_target,
            intensity_dots=intensity_dots,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_dotted,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "ndotsy": w_ndotsy,
        "ndotsx": w_ndotsx,
        "dot_radius": w_dotradius,
        "dot_distance": w_dotdist,
        "intensity_background": w_int_back,
        "intensity_target": w_tint,
        "intensity_dots": w_idots,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Dotted, two sided
{py:func}`stimupy.stimuli.sbcs.dotted_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.sbcs import dotted_two_sided

# Define widgets
w_height = iw.IntSlider(value=15, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=15, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.IntSlider(value=3, min=1, max=6, description="target height [deg]")
w_t_width = iw.IntSlider(value=3, min=1, max=6, description="target width [deg]")

w_ndotsy = iw.IntSlider(value=5, min=1, max=10, description="n dots y")
w_ndotsx = iw.IntSlider(value=5, min=1, max=10, description="n dots x")
w_dotradius = iw.FloatSlider(value=.5, min=0.1, max=6.0, description="dot radius")
w_dotdist = iw.FloatSlider(value=0.25, min=0.1, max=3.0, description="dot distance")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity target")
w_idots_l = iw.FloatSlider(value=1.0, min=0., max=1.0, description="intensity left dots")
w_idots_r = iw.FloatSlider(value=0.0, min=0., max=1.0, description="intensity right dots")
w_int_back_l = iw.FloatSlider(value=0., min=0, max=1, description="intensity left background")
w_int_back_r = iw.FloatSlider(value=1., min=0, max=1, description="intensity right background")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")


# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_t_size = iw.HBox([w_t_height, w_t_width, w_rot])
b_ndots = iw.HBox([w_ndotsy, w_ndotsx])
b_dotsize = iw.HBox([w_dotradius, w_dotdist])
b_intensities = iw.HBox([w_tint, w_int_back_l, w_int_back_r, w_idots_l, w_idots_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_t_size, b_ndots, b_dotsize, b_intensities, b_add])

# Function for showing stim
def show_two_sided_dotted(
    height=None,
    width=None,
    ppd=None,
    target_height=None,
    target_width=None,
    ndotsy=None,
    ndotsx=None,
    dot_radius=None,
    dot_distance=None,
    intensity_background_l=None,
    intensity_background_r=None,
    intensity_target=None,
    intensity_dots_l=None,
    intensity_dots_r=None,
    add_mask=False,
):
    try:
        stim = dotted_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            target_shape=(target_height, target_width),
            n_dots=(ndotsy, ndotsx),
            dot_radius=dot_radius,
            distance=dot_distance,
            intensity_background=(intensity_background_l, intensity_background_r),
            intensity_target=intensity_target,
            intensity_dots=(intensity_dots_l, intensity_dots_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_two_sided_dotted,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "target_height": w_t_height,
        "target_width": w_t_width,
        "ndotsy": w_ndotsy,
        "ndotsx": w_ndotsx,
        "dot_radius": w_dotradius,
        "dot_distance": w_dotdist,
        "intensity_background_l": w_int_back_l,
        "intensity_background_r": w_int_back_r,
        "intensity_target": w_tint,
        "intensity_dots_l": w_idots_l,
        "intensity_dots_r": w_idots_r,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
