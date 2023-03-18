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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/noises/narrowbands.md)
 to get interactivity
```

# Noises - Narrowbands
{py:mod}`stimupy.noises.narrowbands`

```{code-cell} ipython3
:tags: [remove-cell]

import IPython
import ipywidgets as iw
from stimupy.utils import plot_stim
```

## Narrowband
{py:func}`stimupy.noises.narrowbands.narrowband`

```{code-cell} ipython3
from stimupy.noises.narrowbands import narrowband

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_freq = iw.FloatSlider(value=5., min=0.1, max=12, description="center frequency [deg]")
w_band = iw.FloatSlider(value=1, min=0.1, max=2, description="bandwidth [octaves]")

w_int1 = iw.FloatSlider(value=0., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=1., min=0, max=1, description="intensity2")

w_pseudo = iw.ToggleButton(value=False, disabled=False, description="pseudo-noise")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_freq, w_band])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, w_pseudo])

# Function for showing stim
def show_narrowband(
    height=None,
    width=None,
    ppd=None,
    frequency=None,
    bandwidth=None,
    intensity1=None,
    intensity2=None,
    pseudo_noise=False,
):

    stim = narrowband(
        visual_size=(height, width),
        ppd=ppd,
        intensity_range=(intensity1, intensity2),
        center_frequency=frequency,
        bandwidth=bandwidth,
        pseudo_noise=pseudo_noise,
    )
    plot_stim(stim, mask=False)

# Set interactivity
out = iw.interactive_output(
    show_narrowband,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "frequency": w_freq,
        "bandwidth": w_band,
        "pseudo_noise": w_pseudo,
    },
)

# Show
display(ui, out)
```
