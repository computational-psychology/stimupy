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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/dev_docs?urlpath=tree/docs/reference/demos/components/circulars.md)
 to get interactivity
```

# Components - Circulars
{py:mod}`stimupy.components.circulars`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Disc
{py:func}`stimupy.components.circulars.disc`

```{code-cell} ipython3
from stimupy.components.circulars import disc

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
{py:func}`stimupy.components.circulars.annulus`

```{code-cell} ipython3
from stimupy.components.circulars import annulus

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
{py:func}`stimupy.components.circulars.ring`

```{code-cell} ipython3
from stimupy.components.circulars import ring

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

## Disc and rings
{py:func}`stimupy.components.circulars.disc_and_rings`

```{code-cell} ipython3
from stimupy.components.circulars import disc_and_rings

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
def show_disc_and_rings(
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
    stim = disc_and_rings(
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
    show_disc_and_rings,
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

## Sine-wave
{py:func}`stimupy.components.circulars.sine_wave`

```{code-cell} ipython3
from stimupy.components.circulars import sine_wave

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_clip = iw.ToggleButton(value=False, disabled=False, description="clip")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_clip, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_sine_wave(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    intensity_background=None,
    origin=None,
    clip=False,
    add_mask=False,
):
    stim = sine_wave(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_rings=(int1, int2),
        intensity_background=intensity_background,
        origin=origin,
        clip=clip,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_sine_wave,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "clip": w_clip,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Square-wave
{py:func}`stimupy.components.circulars.square_wave`

```{code-cell} ipython3
from stimupy.components.circulars import square_wave

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_clip = iw.ToggleButton(value=False, disabled=False, description="clip")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_clip, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_square_wave(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    intensity_background=None,
    origin=None,
    clip=False,
    add_mask=False,
):
    stim = square_wave(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_rings=(int1, int2),
        intensity_background=intensity_background,
        origin=origin,
        clip=clip,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_square_wave,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "clip": w_clip,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Bessel
{py:func}`stimupy.components.circulars.bessel`

```{code-cell} ipython3
from stimupy.components.circulars import bessel

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_order = iw.IntSlider(value=0, min=0, max=5, description="order")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_order])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_bessel(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    order=None,
    int1=None,
    int2=None,
    origin=None,
    add_mask=False,
):
    stim = bessel(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        order=order,
        intensity_rings=(int1, int2),
        origin=origin,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_bessel,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "frequency": w_freq,
        "order": w_order,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
