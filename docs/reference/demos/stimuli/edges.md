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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/edges.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Edges
{py:mod}`stimupy.stimuli.edges`



## Step edge
{py:func}`stimupy.stimuli.edges.step`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.edges import step

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, w_rot, b_intensities, w_mask])

# Function for showing stim
def show_step_edge(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    intensity1=None,
    intensity2=None,
    add_mask=False,
):
    try:
        stim = step(
            visual_size=(height, width),
            ppd=ppd,
            rotation=rotation,
            intensity_edges=(intensity1, intensity2),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_step_edge,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Gaussian edge
{py:func}`stimupy.stimuli.edges.gaussian`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.edges import gaussian

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_sigma = iw.FloatSlider(value=2., min=0, max=4, description="sigma")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_mask = iw.Dropdown(value=None, options=[None, 'gaussian_mask', 'edge_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_sigma, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_gaussian_edge(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    sigma=None,
    intensity1=None,
    intensity2=None,
    intensity_background=None,
    add_mask=False,
):
    try:
        stim = gaussian(
            visual_size=(height, width),
            ppd=ppd,
            sigma=sigma,
            rotation=rotation,
            intensity_edges=(intensity1, intensity2),
            intensity_background=intensity_background,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_gaussian_edge,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "sigma": w_sigma,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```

## Cornsweet edge
{py:func}`stimupy.stimuli.edges.cornsweet`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.edges import cornsweet

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_ramp = iw.FloatSlider(value=2., min=0, max=4, description="ramp width [deg]")
w_exp = iw.FloatSlider(value=1., min=0, max=3, description="exponent")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="intensity2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="intensity background")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_ramp, w_exp, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_mask])

# Function for showing stim
def show_cornsweet_edge(
    height=None,
    width=None,
    ppd=None,
    rotation=0,
    ramp_width=None,
    exponent=None,
    intensity1=None,
    intensity2=None,
    intensity_plateau=None,
    add_mask=False,
):
    try:
        stim = cornsweet(
            visual_size=(height, width),
            ppd=ppd,
            ramp_width=ramp_width,
            exponent=exponent,
            rotation=rotation,
            intensity_edges=(intensity1, intensity2),
            intensity_plateau=intensity_plateau,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_cornsweet_edge,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "ramp_width": w_ramp,
        "exponent": w_exp,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_plateau": w_int_back,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```
