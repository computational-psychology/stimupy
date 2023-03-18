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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/noises/naturals.md)
 to get interactivity
```

# Noises - Naturals
{py:mod}`stimupy.noises.naturals`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## One over f
{py:func}`stimupy.noises.naturals.one_over_f`

```{code-cell} ipython3
from stimupy.noises.naturals import one_over_f

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_exp = iw.FloatSlider(value=1., min=0., max=5, description="noise exponent")

w_int1 = iw.FloatSlider(value=0., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=1., min=0, max=1, description="intensity2")

w_pseudo = iw.ToggleButton(value=False, disabled=False, description="pseudo-noise")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, w_exp, b_intensities, w_pseudo])

# Function for showing stim
def show_one_over_f(
    height=None,
    width=None,
    ppd=None,
    exponent=None,
    intensity1=None,
    intensity2=None,
    pseudo_noise=False,
):

    stim = one_over_f(
        visual_size=(height, width),
        ppd=ppd,
        intensity_range=(intensity1, intensity2),
        exponent=exponent,
        pseudo_noise=pseudo_noise,
    )
    plot_stim(stim, mask=False)

# Set interactivity
out = iw.interactive_output(
    show_one_over_f,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "exponent": w_exp,
        "pseudo_noise": w_pseudo,
    },
)

# Show
display(ui, out)
```

## Pink
{py:func}`stimupy.noises.naturals.pink`

```{code-cell} ipython3
from stimupy.noises.naturals import pink

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_int1 = iw.FloatSlider(value=0., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=1., min=0, max=1, description="intensity2")

w_pseudo = iw.ToggleButton(value=False, disabled=False, description="pseudo-noise")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, b_intensities, w_pseudo])

# Function for showing stim
def show_pink(
    height=None,
    width=None,
    ppd=None,
    intensity1=None,
    intensity2=None,
    pseudo_noise=False,
):

    stim = pink(
        visual_size=(height, width),
        ppd=ppd,
        intensity_range=(intensity1, intensity2),
        pseudo_noise=pseudo_noise,
    )
    plot_stim(stim, mask=False)

# Set interactivity
out = iw.interactive_output(
    show_pink,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "pseudo_noise": w_pseudo,
    },
)

# Show
display(ui, out)
```

## Brown
{py:func}`stimupy.noises.naturals.brown`

```{code-cell} ipython3
from stimupy.noises.naturals import brown

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_int1 = iw.FloatSlider(value=0., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=1., min=0, max=1, description="intensity2")

w_pseudo = iw.ToggleButton(value=False, disabled=False, description="pseudo-noise")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, b_intensities, w_pseudo])

# Function for showing stim
def show_brown(
    height=None,
    width=None,
    ppd=None,
    intensity1=None,
    intensity2=None,
    pseudo_noise=False,
):

    stim = brown(
        visual_size=(height, width),
        ppd=ppd,
        intensity_range=(intensity1, intensity2),
        pseudo_noise=pseudo_noise,
    )
    plot_stim(stim, mask=False)

# Set interactivity
out = iw.interactive_output(
    show_brown,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "pseudo_noise": w_pseudo,
    },
)

# Show
display(ui, out)
```
