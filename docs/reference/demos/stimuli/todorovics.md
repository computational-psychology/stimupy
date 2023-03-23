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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/todorovics.md)
 to get interactivity
```

# Stimuli - Todorovics
{py:mod}`stimupy.stimuli.todorovics`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Rectangle generalized
{py:func}`stimupy.stimuli.todorovics.rectangle_generalized`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import rectangle_generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=2, min=0, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=0, max=4, description="target width [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_tx = iw.FloatSlider(value=4, min=0, max=8, description="target x [deg]")
w_ty = iw.FloatSlider(value=4, min=0, max=8, description="target y [deg]")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint = iw.FloatSlider(value=1, min=0, max=1, description="cover int")

w_c1x = iw.FloatSlider(value=2, min=0, max=8, description="cover1 x [deg]")
w_c1y = iw.FloatSlider(value=2, min=0, max=8, description="cover1 y [deg]")

w_c2x = iw.FloatSlider(value=6, min=0, max=8, description="cover2 x [deg]")
w_c2y = iw.FloatSlider(value=6, min=0, max=8, description="cover2 y [deg]")

w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tint])
b_tpos = iw.HBox([w_tx, w_ty])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint])
b_c1pos = iw.HBox([w_c1x, w_c1y])
b_c2pos = iw.HBox([w_c2x, w_c2y])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_tpos, b_csize, b_c1pos, b_c2pos, b_intensities, b_add])

# Function for showing stim
def show_rectangle_generalized(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tx=None,
    ty=None,
    cheight=None,
    cwidth=None,
    cint=None,
    c1x=None,
    c1y=None,
    c2x=None,
    c2y=None,
    intback=None,
    add_mask=False,
):
    stim = rectangle_generalized(
        visual_size=(height, width),
        ppd=ppd,
        target_size=(theight, twidth),
        target_position=(ty, tx),
        covers_size=(cheight, cwidth),
        covers_x=(c1x, c2x),
        covers_y=(c1y, c2y),
        intensity_background=intback,
        intensity_target=tint,
        intensity_covers=cint,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rectangle_generalized,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tx": w_tx,
        "ty": w_ty,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint": w_cint,
        "c1x": w_c1x,
        "c2x": w_c2x,
        "c1y": w_c1y,
        "c2y": w_c2y,
        "intback": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Rectangle
{py:func}`stimupy.stimuli.todorovics.rectangle`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import rectangle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=2, min=0, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=0, max=4, description="target width [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_tx = iw.FloatSlider(value=4, min=0, max=8, description="target x [deg]")
w_ty = iw.FloatSlider(value=4, min=0, max=8, description="target y [deg]")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint = iw.FloatSlider(value=1, min=0, max=1, description="cover int")

w_coffx = iw.FloatSlider(value=2, min=0, max=8, description="cover offset x [deg]")
w_coffy = iw.FloatSlider(value=2, min=0, max=8, description="cover offset y [deg]")

w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tint])
b_tpos = iw.HBox([w_tx, w_ty])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint])
b_c1pos = iw.HBox([w_coffx, w_coffy])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_tpos, b_csize, b_c1pos, b_intensities, b_add])

# Function for showing stim
def show_rectangle(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tx=None,
    ty=None,
    cheight=None,
    cwidth=None,
    cint=None,
    coffx=None,
    coffy=None,
    intback=None,
    add_mask=False,
):
    stim = rectangle(
        visual_size=(height, width),
        ppd=ppd,
        target_size=(theight, twidth),
        target_position=(ty, tx),
        covers_size=(cheight, cwidth),
        covers_offset=(coffy, coffx),
        intensity_background=intback,
        intensity_target=tint,
        intensity_covers=cint,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rectangle,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tx": w_tx,
        "ty": w_ty,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint": w_cint,
        "coffx": w_coffx,
        "coffy": w_coffy,
        "intback": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Rectangle, two-sided
{py:func}`stimupy.stimuli.todorovics.two_sided_rectangle`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import two_sided_rectangle

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=2, min=0, max=4, description="target height [deg]")
w_twidth = iw.FloatSlider(value=2, min=0, max=4, description="target width [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint1 = iw.FloatSlider(value=1, min=0, max=1, description="cover1 int")
w_cint2 = iw.FloatSlider(value=0, min=0, max=1, description="cover2 int")

w_coffx = iw.FloatSlider(value=2, min=0, max=8, description="cover offset x [deg]")
w_coffy = iw.FloatSlider(value=2, min=0, max=8, description="cover offset y [deg]")

w_int_back1 = iw.FloatSlider(value=0., min=0, max=1, description="int back1")
w_int_back2 = iw.FloatSlider(value=1., min=0, max=1, description="int back2")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tint])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint1, w_cint2])
b_c1pos = iw.HBox([w_coffx, w_coffy])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_c1pos, b_intensities, b_add])

# Function for showing stim
def show_two_sided_rectangle(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    cheight=None,
    cwidth=None,
    cint1=None,
    cint2=None,
    coffx=None,
    coffy=None,
    intback1=None,
    intback2=None,
    add_mask=False,
):
    stim = two_sided_rectangle(
        visual_size=(height, width),
        ppd=ppd,
        target_size=(theight, twidth),
        covers_size=(cheight, cwidth),
        covers_offset=(coffy, coffx),
        intensity_backgrounds=(intback1, intback2),
        intensity_target=tint,
        intensity_covers=(cint1, cint2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_two_sided_rectangle,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint1": w_cint1,
        "cint2": w_cint2,
        "coffx": w_coffx,
        "coffy": w_coffy,
        "intback1": w_int_back1,
        "intback2": w_int_back2,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross generalized
{py:func}`stimupy.stimuli.todorovics.cross_generalized`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import cross_generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=4, min=0, max=8, description="cross height [deg]")
w_twidth = iw.FloatSlider(value=4, min=0, max=8, description="cross width [deg]")
w_tthick = iw.FloatSlider(value=2, min=0, max=4, description="cross thickness [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="cross int")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint = iw.FloatSlider(value=1, min=0, max=1, description="cover int")

w_c1x = iw.FloatSlider(value=2, min=0, max=8, description="cover1 x [deg]")
w_c1y = iw.FloatSlider(value=2, min=0, max=8, description="cover1 y [deg]")

w_c2x = iw.FloatSlider(value=6, min=0, max=8, description="cover2 x [deg]")
w_c2y = iw.FloatSlider(value=6, min=0, max=8, description="cover2 y [deg]")

w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tthick, w_tint])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint])
b_c1pos = iw.HBox([w_c1x, w_c1y])
b_c2pos = iw.HBox([w_c2x, w_c2y])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_c1pos, b_c2pos, b_intensities, b_add])

# Function for showing stim
def show_cross_generalized(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tthick=None,
    cheight=None,
    cwidth=None,
    cint=None,
    c1x=None,
    c1y=None,
    c2x=None,
    c2y=None,
    intback=None,
    add_mask=False,
):
    stim = cross_generalized(
        visual_size=(height, width),
        ppd=ppd,
        cross_size=(theight, twidth),
        cross_thickness=tthick,
        covers_size=(cheight, cwidth),
        covers_x=(c1x, c2x),
        covers_y=(c1y, c2y),
        intensity_background=intback,
        intensity_target=tint,
        intensity_covers=cint,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_cross_generalized,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tthick": w_tthick,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint": w_cint,
        "c1x": w_c1x,
        "c2x": w_c2x,
        "c1y": w_c1y,
        "c2y": w_c2y,
        "intback": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross
{py:func}`stimupy.stimuli.todorovics.cross`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import cross

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=4, min=0, max=8, description="cross height [deg]")
w_twidth = iw.FloatSlider(value=4, min=0, max=8, description="cross width [deg]")
w_tthick = iw.FloatSlider(value=2, min=0, max=4, description="cross thickness [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="cross int")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint = iw.FloatSlider(value=1, min=0, max=1, description="cover int")

w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tthick, w_tint])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_intensities, b_add])

# Function for showing stim
def show_cross(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tthick=None,
    cheight=None,
    cwidth=None,
    cint=None,
    intback=None,
    add_mask=False,
):
    stim = cross(
        visual_size=(height, width),
        ppd=ppd,
        cross_size=(theight, twidth),
        cross_thickness=tthick,
        covers_size=(cheight, cwidth),
        intensity_background=intback,
        intensity_target=tint,
        intensity_covers=cint,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_cross,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tthick": w_tthick,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint": w_cint,
        "intback": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cross, two-sided
{py:func}`stimupy.stimuli.todorovics.two_sided_cross`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import two_sided_cross

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=4, min=0, max=8, description="cross height [deg]")
w_twidth = iw.FloatSlider(value=4, min=0, max=8, description="cross width [deg]")
w_tthick = iw.FloatSlider(value=2, min=0, max=4, description="cross thickness [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="cross int")

w_cheight = iw.FloatSlider(value=2, min=0, max=4, description="cover height [deg]")
w_cwidth = iw.FloatSlider(value=2, min=0, max=4, description="cover width [deg]")
w_cint1 = iw.FloatSlider(value=1, min=0, max=1, description="cover int1")
w_cint2 = iw.FloatSlider(value=0, min=0, max=1, description="cover int2")

w_int_back1 = iw.FloatSlider(value=0., min=0, max=1, description="int back1")
w_int_back2 = iw.FloatSlider(value=1., min=0, max=1, description="int back12")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tthick, w_tint])
b_csize = iw.HBox([w_cheight, w_cwidth, w_cint1, w_cint2])
b_intensities = iw.HBox([w_int_back1, w_int_back2])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_intensities, b_add])

# Function for showing stim
def show_two_sided_cross(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tthick=None,
    cheight=None,
    cwidth=None,
    cint1=None,
    cint2=None,
    intback1=None,
    intback2=None,
    add_mask=False,
):
    stim = two_sided_cross(
        visual_size=(height, width),
        ppd=ppd,
        cross_size=(theight, twidth),
        cross_thickness=tthick,
        covers_size=(cheight, cwidth),
        intensity_backgrounds=(intback1, intback2),
        intensity_target=tint,
        intensity_covers=(cint1, cint2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_two_sided_cross,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tthick": w_tthick,
        "cheight": w_cheight,
        "cwidth": w_cwidth,
        "cint1": w_cint1,
        "cint2": w_cint2,
        "intback1": w_int_back1,
        "intback2": w_int_back2,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Equal
{py:func}`stimupy.stimuli.todorovics.equal`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import equal

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=4, min=0, max=8, description="cross height [deg]")
w_twidth = iw.FloatSlider(value=4, min=0, max=8, description="cross width [deg]")
w_tthick = iw.FloatSlider(value=2, min=0, max=4, description="cross thickness [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="cross int")

w_cint = iw.FloatSlider(value=1, min=0, max=1, description="cover int")

w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tthick, w_tint])
b_csize = iw.HBox([w_cint])
b_intensities = iw.HBox([w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_intensities, b_add])

# Function for showing stim
def show_equal(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tthick=None,
    cint=None,
    intback=None,
    add_mask=False,
):
    stim = equal(
        visual_size=(height, width),
        ppd=ppd,
        cross_size=(theight, twidth),
        cross_thickness=tthick,
        intensity_background=intback,
        intensity_target=tint,
        intensity_covers=cint,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_equal,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tthick": w_tthick,
        "cint": w_cint,
        "intback": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Equal, two-sided
{py:func}`stimupy.stimuli.todorovics.two_sided_equal`

```{code-cell} ipython3
from stimupy.stimuli.todorovics import two_sided_equal

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_theight = iw.FloatSlider(value=4, min=0, max=8, description="cross height [deg]")
w_twidth = iw.FloatSlider(value=4, min=0, max=8, description="cross width [deg]")
w_tthick = iw.FloatSlider(value=2, min=0, max=4, description="cross thickness [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="cross int")

w_cint1 = iw.FloatSlider(value=1, min=0, max=1, description="cover1 int")
w_cint2 = iw.FloatSlider(value=0, min=0, max=1, description="cover2 int")

w_int_back1 = iw.FloatSlider(value=0., min=0, max=1, description="int back1")
w_int_back2 = iw.FloatSlider(value=1., min=0, max=1, description="int back2")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_tsize = iw.HBox([w_theight, w_twidth, w_tthick, w_tint])
b_csize = iw.HBox([w_cint1, w_cint2])
b_intensities = iw.HBox([w_int_back1, w_int_back2])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_tsize, b_csize, b_intensities, b_add])

# Function for showing stim
def show_two_sided_equal(
    height=None,
    width=None,
    ppd=None,
    theight=None,
    twidth=None,
    tint=None,
    tthick=None,
    cint1=None,
    cint2=None,
    intback1=None,
    intback2=None,
    add_mask=False,
):
    stim = two_sided_equal(
        visual_size=(height, width),
        ppd=ppd,
        cross_size=(theight, twidth),
        cross_thickness=tthick,
        intensity_backgrounds=(intback1, intback2),
        intensity_target=tint,
        intensity_covers=(cint1, cint2),
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_two_sided_equal,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "theight": w_theight,
        "twidth": w_twidth,
        "tint": w_tint,
        "tthick": w_tthick,
        "cint1": w_cint1,
        "intback1": w_int_back1,
        "cint2": w_cint2,
        "intback2": w_int_back2,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
