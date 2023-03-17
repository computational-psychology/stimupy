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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/shapes.md)
 to get interactivity
```

# Components - Shapes
{py:mod}`stimupy.components.shapes`

```{code-cell} ipython3
:tags: [remove-cell]


import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Rectangle
{py:func}`stimupy.components.shapes.rectangle`

```{code-cell} ipython3
:tags: [hide-input]

from stimupy.components.shapes import rectangle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_rect_height = iw.IntSlider(value=3, min=1, max=6, description="rectangle height [deg]")
w_rect_width = iw.IntSlider(value=3, min=1, max=6, description="rectangle width [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_rect_posx = iw.FloatSlider(value=3.0, min=0, max=10.0, description="horz. position")
w_rect_posy = iw.FloatSlider(value=3.0, min=0, max=10.0, description="vert. position")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity rectangle")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_rect_size = iw.HBox([w_rect_height, w_rect_width, w_rot])
b_post = iw.HBox([w_rect_posx, w_rect_posy])
b_intensities = iw.HBox([w_int, w_int_back])
ui = iw.VBox([b_im_size, b_rect_size, b_post, b_intensities, w_mask])

# Function for showing stim
def show_rect(
    height=None,
    width=None,
    ppd=None,
    rect_height=None,
    rect_width=None,
    pos_x=None,
    pos_y=None,
    rotation=None,
    intensity_rectangle=None,
    intensity_background=None,
    add_mask=False,
):
    stim = rectangle(
        visual_size=(height, width),
        ppd=ppd,
        rectangle_size=(rect_height, rect_width),
        rectangle_position=(pos_y, pos_x),
        rotation=rotation,
        intensity_rectangle=intensity_rectangle,
        intensity_background=intensity_background,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rect,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rect_height": w_rect_height,
        "rect_width": w_rect_width,
        "pos_x": w_rect_posx,
        "pos_y": w_rect_posy,
        "rotation": w_rot,
        "intensity_rectangle": w_int,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Triangle
{py:func}`stimupy.components.shapes.triangle`

```{code-cell} ipython3
:tags: [hide-input]

from stimupy.components.shapes import triangle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_t_height = iw.FloatSlider(value=3, min=1, max=10, description="triangle height [deg]")
w_t_width = iw.FloatSlider(value=3, min=1, max=10, description="triangle width [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity triangle")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_corners = iw.ToggleButton(value=False, disabled=False, description="include corners")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_t_height, w_t_width, w_rot])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_corners, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_triangle(
    height=None,
    width=None,
    ppd=None,
    rotation=None,
    triangle_height=None,
    triangle_width=None,
    intensity_triangle=None,
    intensity_background=None,
    include_corners=None,
    add_mask=False,
):
    stim = triangle(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        triangle_size=(triangle_height, triangle_width),
        intensity_triangle=intensity_triangle,
        intensity_background=intensity_background,
        include_corners=include_corners,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_triangle,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "triangle_height": w_t_height,
        "triangle_width": w_t_width,
        "intensity_triangle": w_int,
        "intensity_background": w_int_back,
        "include_corners": w_corners,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross
{py:func}`stimupy.components.shapes.cross`

```{code-cell} ipython3
:tags: [hide-input]

from stimupy.components.shapes import cross

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_c_height = iw.IntSlider(value=3, min=1, max=6, description="cross height [deg]")
w_c_width = iw.IntSlider(value=3, min=1, max=6, description="cross width [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_cross_thick = iw.FloatSlider(value=1.5, min=0.0, max=3, description="thickness [deg]")
w_cross_ratio1 = iw.FloatSlider(value=1.0, min=0.0, max=5.0, description="cross ratio1")
w_cross_ratio2 = iw.FloatSlider(value=1.0, min=0.0, max=5.0, description="cross ratio2")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity cross")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_csize = iw.HBox([w_c_height, w_c_width, w_rot])
b_cratio = iw.HBox([w_cross_thick, w_cross_ratio1, w_cross_ratio2])
b_intensities = iw.HBox([w_int, w_int_back])
ui = iw.VBox([b_im_size, b_csize, b_cratio, b_intensities, w_mask])

# Function for showing stim
def show_cross(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    cross_height=None,
    cross_width=None,
    thickness=None,
    ratio1=None,
    ratio2=None,
    intensity_cross=None,
    intensity_background=None,
    add_mask=False,
):
    stim = cross(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        cross_size=(cross_height, cross_width),
        cross_thickness=thickness,
        cross_arm_ratios=(ratio1, ratio2),
        intensity_cross=intensity_cross,
        intensity_background=intensity_background,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_cross,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "cross_height": w_c_height,
        "cross_width": w_c_width,
        "thickness": w_cross_thick,
        "ratio1": w_cross_ratio1,
        "ratio2": w_cross_ratio2,
        "intensity_cross": w_int,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Parallelogram
{py:func}`stimupy.components.shapes.parallelogram`

```{code-cell} ipython3
:tags: [hide-input]

from stimupy.components.shapes import parallelogram

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_p_height = iw.IntSlider(value=3, min=1, max=6, description="p-height [deg]")
w_p_width = iw.IntSlider(value=3, min=1, max=6, description="p-width [deg]")
w_p_depth = iw.FloatSlider(value=1.0, min=-3.0, max=3.0, description="p-depth [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity p")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_p_height, w_p_width, w_p_depth, w_rot])
b_intensities = iw.HBox([w_int, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_parallelogram(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    p_height=None,
    p_width=None,
    p_depth=None,
    intensity_parallelogram=None,
    intensity_background=None,
    add_mask=False,
):
    stim = parallelogram(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        parallelogram_size=(p_height, p_width, p_depth),
        intensity_parallelogram=intensity_parallelogram,
        intensity_background=intensity_background,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_parallelogram,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "p_height": w_p_height,
        "p_width": w_p_width,
        "p_depth": w_p_depth,
        "intensity_parallelogram": w_int,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Ellipse
{py:func}`stimupy.components.shapes.ellipse`

```{code-cell} ipython3
from stimupy.components.shapes import ellipse

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_eheight = iw.IntSlider(value=3, min=1, max=6, description="radius 1 [deg]")
w_ewidth = iw.IntSlider(value=3, min=1, max=6, description="radius 2 [deg]")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity ellipse")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_eheight, w_ewidth, w_rot])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_ellipse(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    radius1=None,
    radius2=None,
    intensity_ellipse=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = ellipse(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        radius=(radius1, radius2),
        intensity_ellipse=intensity_ellipse,
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_ellipse,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "radius1": w_eheight,
        "radius2": w_ewidth,
        "intensity_ellipse": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Circle
{py:func}`stimupy.components.shapes.circle`

```{code-cell} ipython3
from stimupy.components.shapes import circle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_eheight = iw.IntSlider(value=3, min=1, max=6, description="radius [deg]")

w_int = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity circle")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, w_eheight, b_intensities, b_add])

# Function for showing stim
def show_circle(
    height=None,
    width=None,
    ppd=None,
    radius=None,
    intensity_circle=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
):
    stim = circle(
        visual_size=(height, width),
        ppd=ppd,
        radius=radius,
        intensity_circle=intensity_circle,
        intensity_background=intensity_background,
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_circle,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "radius": w_eheight,
        "intensity_circle": w_int,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Wedge
{py:func}`stimupy.components.shapes.wedge`

```{code-cell} ipython3
from stimupy.components.shapes import wedge

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

## Disc
{py:func}`stimupy.components.shapes.disc`

```{code-cell} ipython3
from stimupy.components.shapes import disc

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

## Annulus
{py:func}`stimupy.components.shapes.annulus`

```{code-cell} ipython3
from stimupy.components.shapes import annulus

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

## Ring
{py:func}`stimupy.components.shapes.ring`

```{code-cell} ipython3
from stimupy.components.shapes import ring

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
def show_ring(
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
    show_ring,
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
