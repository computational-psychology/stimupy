---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{important}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=lab/tree/docs/reference/demos/components/shapes.md)
 to get interactivity
```

# Basic shapes
{py:mod}`stimupy.components.shapes`
```{code-cell}
:tags: [remove-cell]
import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Rectangle
{py:func}`stimupy.components.shapes.rectangle`
```{code-cell}
:tags: [hide-input]
from stimupy.components.shapes import rectangle

# Define widgets
w_height = iw.IntSlider(value=4, min=1, max=10, description="height [deg]")
w_width = iw.IntSlider(value=4, min=1, max=10, description="width [deg]")
w_ppd = iw.IntSlider(value=32, min=1, max=64, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")


w_rect_height = iw.IntSlider(value=2, min=1, max=10, description="height [deg]")
w_rect_width = iw.IntSlider(value=2, min=1, max=10, description="width [deg]")

w_rect_posx = iw.FloatSlider(value=0.0, min=-5.0, max=5.0, description="horz. position")
w_rect_posy = iw.FloatSlider(value=0.0, min=-5.0, max=5.0, description="vert. position")

w_intensities = iw.FloatRangeSlider(value=[0.0, 1.0], min=0.0, max=1.0, step=0.1, description="intensities")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_rect_size = iw.HBox([w_rect_height, w_rect_width])
b_post = iw.HBox([w_rect_posx, w_rect_posy])
b_intensities = iw.HBox([w_intensities])
ui = iw.VBox([b_im_size, b_rect_size, b_post, b_intensities])

# Function for showing stim
def show_rect(
    height=None,
    width=None,
    ppd=None,
    rect_height=None,
    rect_width=None,
    pos_x=0.0,
    pos_y=0.0,
    orientation='horizontal',
    intensities=(0.0, 1.0)
):
    stim = rectangle(
        visual_size=(height, width),
        ppd=ppd,
        rectangle_size=(rect_height, rect_width),
        rectangle_position=(pos_y, pos_x),
        intensity_rectangle=intensities[1],
        intensity_background=intensities[0]
    )
    plot_stim(stim, mask=False)

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
        "intensities": w_intensities,
    },
)

# Show
display(ui, out)
```

## Triangle
{py:func}`stimupy.components.shapes.triangle`
```{code-cell}
:tags: [hide-input]
from stimupy.components.shapes import triangle

# Define widgets
w_height = iw.IntSlider(value=4, min=1, max=10, description="height [deg]")
w_width = iw.IntSlider(value=4, min=1, max=10, description="width [deg]")
w_ppd = iw.IntSlider(value=32, min=1, max=64, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_t_height = iw.IntSlider(value=4, min=1, max=10, description="triangle height [deg]")
w_t_width = iw.IntSlider(value=4, min=1, max=10, description="triangle width [deg]")

w_intensities = iw.FloatRangeSlider(value=[0.0, 1.0], min=0.0, max=1.0, step=0.1, description="intensities")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_geometry = iw.HBox([w_t_height, w_t_width])
b_intensities = iw.HBox([w_intensities])
ui = iw.VBox([b_im_size, b_intensities])

# Function for showing stim
def show_triangle(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    triangle_height=None,
    triangle_width=None,
    intensities=(0.0, 1.0)
):
    stim = triangle(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        triangle_size=(triangle_height, triangle_width),
        intensity_triangle=intensities[1],
        intensity_background=intensities[0]
    )
    plot_stim(stim, mask=False)

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
        "intensities": w_intensities,
    },
)

# Show
display(ui, out)
```

## Cross
{py:func}`stimupy.components.shapes.cross`
```{code-cell}
:tags: [hide-input]
from stimupy.components.shapes import cross

# Define widgets
w_height = iw.IntSlider(value=4.0, min=1, max=10, description="heigh [deg]")
w_width = iw.IntSlider(value=4.0, min=1, max=10, description="width [deg]")
w_ppd = iw.IntSlider(value=32, min=1, max=64, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_c_height = iw.IntSlider(value=4, min=1, max=10, description="cross height [deg]")
w_c_width = iw.IntSlider(value=4, min=1, max=10, description="cross width [deg]")
w_cross_thick = iw.FloatSlider(value=0.5, min=0.0, max=5.0, description="thickness [deg]")
w_cross_ratio = iw.FloatSlider(value=1.0, min=0.0, max=5.0, description="horz. arm ratio")

w_intensities = iw.FloatRangeSlider(value=[0.0, 1.0], min=0.0, max=1.0, step=0.1, description="intensities")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_geometry = iw.HBox([w_c_height, w_c_width, w_cross_thick, w_cross_ratio])
b_intensities = iw.HBox([w_intensities])
ui = iw.VBox([b_im_size, b_geometry, b_intensities])

# Function for showing stim
def show_cross(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    cross_height=None,
    cross_width=None,
    thickness=None,
    ratio=1.0,
    intensities=(0.0, 1.0)
):
    stim = cross(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        cross_size=(cross_height, cross_width),
        cross_thickness=thickness,
        cross_arm_ratios=(ratio, ratio),
        intensity_cross=intensities[1],
        intensity_background=intensities[0]
    )
    plot_stim(stim, mask=False)

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
        "ratio": w_cross_ratio,
        "intensities": w_intensities,
    },
)

# Show
display(ui, out)
```

## Parallelogram
{py:func}`stimupy.components.shapes.parallelogram`
```{code-cell}
:tags: [hide-input]
from stimupy.components.shapes import parallelogram

# Define widgets
w_height = iw.IntSlider(value=5, min=1, max=10, description="heigh [deg]")
w_width = iw.IntSlider(value=5, min=1, max=10, description="width [deg]")
w_ppd = iw.IntSlider(value=32, min=1, max=64, description="ppd")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_p_height = iw.IntSlider(value=2, min=1, max=10, description="cross height [deg]")
w_p_width = iw.IntSlider(value=2, min=1, max=10, description="cross width [deg]")
w_p_depth = iw.FloatSlider(value=2.0, min=-3.0, max=3.0, description="depth [deg]")

w_intensities = iw.FloatRangeSlider(value=[0.0, 1.0], min=0.0, max=1.0, step=0.1, description="intensities")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd, w_rot])
b_geometry = iw.HBox([w_p_height, w_p_width, w_p_depth])
b_intensities = iw.HBox([w_intensities])
ui = iw.VBox([b_im_size, b_geometry, b_intensities])

# Function for showing stim
def show_parallelogram(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    p_height=None,
    p_width=None,
    p_depth=None,
    intensities=(0.0, 1.0)
):
    stim = parallelogram(
        visual_size=(height, width),
        ppd=ppd,
        rotation=rotation,
        parallelogram_size=(p_height, p_width, p_depth),
        intensity_parallelogram=intensities[1],
        intensity_background=intensities[0]
    )
    plot_stim(stim, mask=False)

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
        "intensities": w_intensities,
    },
)

# Show
display(ui, out)
```