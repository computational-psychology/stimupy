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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/noises/binaries.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Noises - Binaries
{py:mod}`stimupy.noises.binaries`



## Binary
{py:func}`stimupy.noises.binaries.binary`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.noises.binaries import binary

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_int1 = iw.FloatSlider(value=0., min=0, max=1, description="intensity1")
w_int2 = iw.FloatSlider(value=1., min=0, max=1, description="intensity2")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_intensities = iw.HBox([w_int1, w_int2])
ui = iw.VBox([b_im_size, b_intensities])

# Function for showing stim
def show_binary(
    height=None,
    width=None,
    ppd=None,
    intensity1=None,
    intensity2=None,
):

    stim = binary(
        visual_size=(height, width),
        ppd=ppd,
        intensity_range=(intensity1, intensity2),
    )
    plot_stim(stim, mask=False)

# Set interactivity
out = iw.interactive_output(
    show_binary,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "intensity1": w_int1,
        "intensity2": w_int2,
    },
)

# Show
display(ui, out)
```
