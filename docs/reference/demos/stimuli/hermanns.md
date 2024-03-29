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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/hermanns.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Hermanns
{py:mod}`stimupy.stimuli.hermanns`



## Grid
{py:func}`stimupy.stimuli.hermanns.grid`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.hermanns import grid

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_eheight = iw.FloatSlider(value=1, min=0.1, max=2, description="element-height")
w_ewidth = iw.FloatSlider(value=1, min=0.1, max=2, description="element-width")
w_ethick = iw.FloatSlider(value=0.1, min=0.1, max=1, description="element-thickness")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int grid")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_eheight, w_ewidth, w_ethick])
b_intensities = iw.HBox([w_int1, w_int_back])
ui = iw.VBox([b_im_size, b_geometry, b_intensities])

# Function for showing stim
def show_grid(
    height=None,
    width=None,
    ppd=None,
    eheight=None,
    ewidth=None,
    ethick=None,
    int_grid=None,
    int_back=None,
):
    try:
        stim = grid(
            visual_size=(height, width),
            ppd=ppd,
            element_size=(eheight, ewidth, ethick),
            intensity_background=int_back,
            intensity_grid=int_grid,
        )
        plot_stim(stim, mask=False)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_grid,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "eheight": w_eheight,
        "ewidth": w_ewidth,
        "ethick": w_ethick,
        "int_grid": w_int1,
        "int_back": w_int_back,
    },
)

# Show
display(ui, out)
```
