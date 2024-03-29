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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/bullseyes.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Bullseyes
{py:mod}`stimupy.stimuli.bullseyes`



## Circular
{py:func}`stimupy.stimuli.bullseyes.circular`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import circular

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

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_clip, w_mask])
b_target = iw.HBox([w_tint])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_bullseye(
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
    intensity_target=None,
):
    try:
        stim = circular(
            visual_size=(height, width),
            ppd=ppd,
            frequency=frequency,
            phase_shift=phase_shift,
            intensity_rings=(int1, int2),
            intensity_background=intensity_background,
            origin=origin,
            clip=clip,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_bullseye,
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
    },
)

# Show
display(ui, out)
```

## Circular bullseye, generalized
{py:func}`stimupy.stimuli.bullseyes.circular_generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import circular_generalized

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
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'ring_mask'], description="add mask")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius1, w_radius2, w_radius3])
b_intensities = iw.HBox([w_int1, w_int2, w_int3, w_int_back])
b_target = iw.HBox([w_tint])
b_add = iw.HBox([w_ori, w_rot, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_circular_generalized(
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
    rotation=0.0,
):
    try:
        stim = circular_generalized(
            visual_size=(height, width),
            ppd=ppd,
            radii=(radius1, radius2, radius3),
            intensity_rings=(int1, int2, int3),
            intensity_background=intensity_background,
            origin=origin,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_circular_generalized,
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
        "intensity_target": w_tint,
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```



## Circular, Two-sided
{py:func}`stimupy.stimuli.bullseyes.circular_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import circular_two_sided

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

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="left target int")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="right target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_add = iw.HBox([w_ori, w_mask])
b_target = iw.HBox([w_tint_l, w_tint_r])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_two_sided_bullseye(
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
    intensity_target_l=None,
    intensity_target_r=None,
):
    try:
        stim = circular_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            frequency=frequency,
            phase_shift=phase_shift,
            intensity_rings=((int1, int2),(int2, int1)),
            intensity_background=intensity_background,
            origin=origin,
            intensity_target=(intensity_target_l, intensity_target_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_two_sided_bullseye,
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
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
    },
)

# Show
display(ui, out)
```

## Rectangular
{py:func}`stimupy.stimuli.bullseyes.rectangular`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import rectangular

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
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_clip = iw.ToggleButton(value=False, disabled=False, description="clip")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tint])
b_add = iw.HBox([w_ori, w_rot, w_clip, w_mask])
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
    intensity_target=None,
    rotation=0.0,
):
    try:
        stim = rectangular(
            visual_size=(height, width),
            ppd=ppd,
            frequency=frequency,
            phase_shift=phase_shift,
            intensity_frames=(int1, int2),
            intensity_background=intensity_background,
            origin=origin,
            clip=clip,
            intensity_target=intensity_target,
            rotation=rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

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
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```

## Bullseye-generalized
{py:func}`stimupy.stimuli.bullseyes.rectangular_generalized`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import rectangular_generalized

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
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_radius1, w_radius2, w_radius3])
b_intensities = iw.HBox([w_int1, w_int2, w_int3, w_int_back])
b_target = iw.HBox([w_tint])
b_add = iw.HBox([w_ori, w_rot, w_mask])
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
    rotation=0.0,
):
    try:
        stim = rectangular_generalized(
            visual_size=(height, width),
            ppd=ppd,
            radii=(radius1, radius2, radius3),
            intensity_frames=(int1, int2, int3),
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
        "intensity_target": w_tint,
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```

## Two-sided-bullseye
{py:func}`stimupy.stimuli.bullseyes.rectangular_two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.bullseyes import rectangular_two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int-ring1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int-ring2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'frame_mask'], description="add mask")

w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="left target int")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="right target int")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_phase])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tint_l, w_tint_r])
b_add = iw.HBox([w_rot, w_mask])
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
    intensity_target_l=None,
    intensity_target_r=None,
    rotation=0.0,
):
    try:
        stim = rectangular_two_sided(
            visual_size=(height, width),
            ppd=ppd,
            frequency=frequency,
            phase_shift=phase_shift,
            intensity_frames=((int1, int2),(int2, int1)),
            intensity_background=intensity_background,
            intensity_target=(intensity_target_l, intensity_target_r),
            rotation=rotation,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

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
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "rotation": w_rot,
    },
)

# Show
display(ui, out)
```
