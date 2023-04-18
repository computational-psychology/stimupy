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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/lines.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Components - Lines
{py:mod}`stimupy.components.lines`



## Line
{py:func}`stimupy.components.lines.line`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.lines import line

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_len = iw.FloatSlider(value=3, min=0, max=6, description="line length [deg]")
w_lwidth = iw.FloatSlider(value=0, min=0, max=3, description="line width [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_posx = iw.FloatSlider(value=3.0, min=-10, max=10.0, description="x-position")
w_posy = iw.FloatSlider(value=3.0, min=-10, max=10.0, description="y-position")

w_int = iw.FloatSlider(value=1., min=0, max=1, description="intensity line")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="corner", options=['corner', 'center', 'mean'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_len, w_lwidth, w_rot])
b_pos = iw.HBox([w_posx, w_posy])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_pos, b_intensities, b_add])

# Function for showing stim
def show_line(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    line_length=None,
    line_width=None,
    xpos=None,
    ypos=None,
    intensity_line=None,
    intensity_background=None,
    add_mask=False,
    origin=None,
):
    try:
        stim = line(
            visual_size=(height, width),
            ppd=ppd,
            line_position=(ypos, xpos),
            line_length=line_length,
            line_width=line_width,
            rotation=rotation,
            intensity_line=intensity_line,
            intensity_background=intensity_background,
            origin=origin,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None    

# Set interactivity
out = iw.interactive_output(
    show_line,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "line_length": w_len,
        "line_width": w_lwidth,
        "xpos": w_posx,
        "ypos": w_posy,
        "intensity_line": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Dipole
{py:func}`stimupy.components.lines.dipole`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.lines import dipole

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_len = iw.FloatSlider(value=3, min=0, max=6, description="line length [deg]")
w_lwidth = iw.FloatSlider(value=0, min=0, max=3, description="line width [deg]")
w_gap = iw.FloatSlider(value=0.5, min=0, max=3, description="gap [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_len, w_lwidth, w_gap, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_dipole(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    line_length=None,
    line_width=None,
    line_gap=None,
    int1=None,
    int2=None,
    add_mask=False,
):
    try:
        stim = dipole(
            visual_size=(height, width),
            ppd=ppd,
            line_length=line_length,
            line_width=line_width,
            line_gap=line_gap,
            rotation=rotation,
            intensity_lines=(int1, int2),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_dipole,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "line_length": w_len,
        "line_width": w_lwidth,
        "line_gap": w_gap,
        "int1": w_int1,
        "int2": w_int2,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Ellipse
{py:func}`stimupy.components.lines.ellipse`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.lines import ellipse

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_rad1 = iw.FloatSlider(value=3, min=0, max=6, description="radius1 [deg]")
w_rad2 = iw.FloatSlider(value=3, min=0, max=6, description="radius2 [deg]")
w_lwidth = iw.FloatSlider(value=0, min=0, max=3, description="line width [deg]")

w_int = iw.FloatSlider(value=1., min=0, max=1, description="intensity line")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_rad1, w_rad2, w_lwidth])
b_intensities = iw.HBox([w_int, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_ellipse(
    height=None,
    width=None,
    ppd=None,
    rad1=None,
    rad2=None,
    line_width=None,
    intensity_line=None,
    intensity_background=None,
    add_mask=False,
):
    try:
        stim = ellipse(
            visual_size=(height, width),
            ppd=ppd,
            radius=(rad1, rad2),
            line_width=line_width,
            intensity_line=intensity_line,
            intensity_background=intensity_background,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_ellipse,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rad1": w_rad1,
        "rad2": w_rad2,
        "line_width": w_lwidth,
        "intensity_line": w_int,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Circle
{py:func}`stimupy.components.lines.circle`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.lines import circle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_rad = iw.FloatSlider(value=3, min=0, max=6, description="radius [deg]")
w_lwidth = iw.FloatSlider(value=0, min=0, max=3, description="line width [deg]")

w_int = iw.FloatSlider(value=1., min=0, max=1, description="intensity line")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_rad, w_lwidth])
b_intensities = iw.HBox([w_int, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_circle(
    height=None,
    width=None,
    ppd=None,
    radius=None,
    line_width=None,
    intensity_line=None,
    intensity_background=None,
    add_mask=False,
):
    try:
        stim = circle(
            visual_size=(height, width),
            ppd=ppd,
            radius=radius,
            line_width=line_width,
            intensity_line=intensity_line,
            intensity_background=intensity_background,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_circle,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius": w_rad,
        "line_width": w_lwidth,
        "intensity_line": w_int,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
