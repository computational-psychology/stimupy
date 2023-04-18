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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/rings.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Rings
{py:mod}`stimupy.stimuli.rings`



## Circular
{py:func}`stimupy.stimuli.rings.circular`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.rings import circular

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="int background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_clip = iw.ToggleButton(value=False, disabled=False, description="clip")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'ring_mask'], description="add mask")

w_tidx = iw.IntSlider(value=2, min=0, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_clip, w_mask])
b_target = iw.HBox([w_tidx, w_tint])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_circular(
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
    target_indices=None,
    intensity_target=None,
):
    stim = circular(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_rings=(int1, int2),
        intensity_background=intensity_background,
        origin=origin,
        clip=clip,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_circular,
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
        "target_indices": w_tidx,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Two-sided rings
{py:func}`stimupy.stimuli.rings.circular_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.rings import circular_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="int background")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'ring_mask'], description="add mask")

w_tidx = iw.IntSlider(value=2, min=0, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
b_target = iw.HBox([w_tidx, w_tint])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_circular_two_sided(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    intensity_background=None,
    origin=None,
    add_mask=False,
    target_indices=None,
    intensity_target=None,
):
    stim = circular_two_sided(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_rings=(int1, int2),
        intensity_background=intensity_background,
        origin=origin,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_circular_two_sided,
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
        "add_mask": w_mask,
        "target_indices": w_tidx,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Rectangular
{py:func}`stimupy.stimuli.rings.rectangular`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.rings import rectangular

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="center", options=['mean', 'corner', 'center'], description="origin")
w_clip = iw.ToggleButton(value=False, disabled=False, description="clip")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tidx = iw.IntSlider(value=1, min=0, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_ori, w_clip, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_rectangular(
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
    target_indices=None,
    intensity_target=None,
):
    stim = rectangular(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_frames=(int1, int2),
        intensity_background=intensity_background,
        origin=origin,
        clip=clip,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rectangular,
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
        "intensity_target": w_tint,
        "target_indices": w_tidx,
    },
)

# Show
display(ui, out)
```

## Rectangular, generalized
{py:func}`stimupy.stimuli.rings.rectangular_generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.rings import rectangular_generalized

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_radius1 = iw.FloatSlider(value=1, min=0, max=2, description="radius1 [deg]")
w_radius2 = iw.FloatSlider(value=2, min=1, max=3, description="radius2 [deg]")
w_radius3 = iw.FloatSlider(value=3, min=2, max=4, description="radius2 [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0.3, min=0, max=1, description="int-ring2")
w_int3 = iw.FloatSlider(value=0.8, min=0, max=1, description="int-ring3")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_ori = iw.Dropdown(value="center", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tidx = iw.IntSlider(value=1, min=1, max=4, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius1, w_radius2, w_radius3])
b_intensities = iw.HBox([w_int1, w_int2, w_int3, w_int_back])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_rectangular_generalized(
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
    intensity_target=None,
    target_indices=None,
):
    stim = rectangular_generalized(
        visual_size=(height, width),
        ppd=ppd,
        radii=(radius1, radius2, radius3),
        intensity_frames=(int1, int2, int3),
        intensity_background=intensity_background,
        origin=origin,
        intensity_target=intensity_target,
        target_indices=target_indices,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rectangular_generalized,
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
        "target_indices": w_tidx,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```

## Two-sided-rings
{py:func}`stimupy.stimuli.rings.rectangular_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.rings import rectangular_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tidx = iw.IntSlider(value=1, min=0, max=10, description="target idx")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tidx, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_rectangular_two_sided(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    intensity_background=None,
    add_mask=False,
    target_indices=None,
    intensity_target=None,
):
    stim = rectangular_two_sided(
        visual_size=(height, width),
        ppd=ppd,
        frequency=frequency,
        phase_shift=phase_shift,
        intensity_frames=(int1, int2),
        intensity_background=intensity_background,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_rectangular_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
        "intensity_target": w_tint,
        "target_indices": w_tidx,
    },
)

# Show
display(ui, out)
```