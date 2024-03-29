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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/waves.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Components - Waves
{py:mod}`stimupy.components.waves`



## Sinewave
{py:func}`stimupy.components.waves.sine`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.waves import sine

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_distance_metric = iw.Dropdown(value="horizontal", options=['horizontal','vertical','oblique','radial','rectilinear','angular'], description="distance_metric")
w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_distance_metric, w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_sine(
    height=None,
    width=None,
    ppd=None,
    distance_metric=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    origin=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    try:
        stim = sine(
            visual_size=(height, width),
            ppd=ppd,
            distance_metric=distance_metric,
            rotation=rotation,
            frequency=frequency,
            phase_shift=phase_shift,
            intensities=(int1, int2),
            origin=origin,
            round_phase_width=round_phase_width,
            period=period,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_sine,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "distance_metric": w_distance_metric,
        "rotation": w_rot,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Squarewave
{py:func}`stimupy.components.waves.square`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.waves import square

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_distance_metric = iw.Dropdown(value="horizontal", options=['horizontal','vertical','oblique','radial','rectilinear','angular'], description="distance_metric")
w_freq = iw.FloatSlider(value=1, min=0, max=2, description="frequency [cpd]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_distance_metric, w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_square(
    height=None,
    width=None,
    ppd=None,
    distance_metric=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    origin=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
):
    try:
        stim = square(
            visual_size=(height, width),
            ppd=ppd,
            distance_metric=distance_metric,
            rotation=rotation,
            frequency=frequency,
            phase_shift=phase_shift,
            intensities=(int1, int2),
            origin=origin,
            round_phase_width=round_phase_width,
            period=period,
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
        "distance_metric": w_distance_metric,
        "rotation": w_rot,
        "frequency": w_freq,
        "phase_shift": w_phase,
        "int1": w_int1,
        "int2": w_int2,
        "origin": w_ori,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Staircase
{py:func}`stimupy.components.waves.staircase`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.waves import staircase

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_distance_metric = iw.Dropdown(value="horizontal", options=['horizontal','vertical','oblique','radial','rectilinear','angular'], description="distance_metric")
w_freq = iw.FloatSlider(value=1, min=0, max=4, description="frequency [cpd / cpc]")
w_rot = iw.FloatSlider(value=0, min=0, max=360, description="rotation [deg]")
w_phase = iw.FloatSlider(value=0, min=0, max=360, description="phase shift [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0, min=0, max=1, description="int2")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_period = iw.Dropdown(value="ignore", options=['ignore', 'even', 'odd', 'either'], description="period")
w_round = iw.ToggleButton(value=False, disabled=False, description="round phase")
w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_distance_metric, w_freq, w_phase, w_rot])
b_intensities = iw.HBox([w_int1, w_int2])
b_add = iw.HBox([w_ori, w_period, w_round, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_add])

# Function for showing stim
def show_staircase(
    height=None,
    width=None,
    ppd=None,
    distance_metric=None,
    rotation=None,
    frequency=None,
    phase_shift=None,
    int1=None,
    int2=None,
    round_phase_width=False,
    period=None,
    add_mask=False,
    origin=None,
):
    try:
        stim = staircase(
            visual_size=(height, width),
            ppd=ppd,
            distance_metric=distance_metric,
            rotation=rotation,
            frequency=frequency,
            phase_shift=phase_shift,
            intensities=(int1, int2),
            round_phase_width=round_phase_width,
            period=period,
            origin=origin,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_staircase,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "distance_metric": w_distance_metric,
        "rotation": w_rot,
        "frequency": w_freq,
        "int1": w_int1,
        "int2": w_int2,
        "round_phase_width": w_round,
        "period": w_period,
        "add_mask": w_mask,
        "phase_shift": w_phase,
        "origin": w_ori,
    },
)

# Show
display(ui, out)
```

## Bessel
{py:func}`stimupy.components.waves.bessel`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.waves import bessel

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
    try:
        stim = bessel(
            visual_size=(height, width),
            ppd=ppd,
            frequency=frequency,
            order=order,
            intensities=(int1, int2),
            origin=origin,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

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
