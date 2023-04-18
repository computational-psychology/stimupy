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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/ponzos.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Ponzos
{py:mod}`stimupy.stimuli.ponzos`



## Ponzo
{py:func}`stimupy.stimuli.ponzos.ponzo`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.ponzos import ponzo

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outl = iw.FloatSlider(value=4, min=0.5, max=8, description="o-line length [deg]")
w_outw = iw.FloatSlider(value=0, min=0, max=2, description="o-line width [deg]")
w_outa = iw.IntSlider(value=15, min=-30, max=30, description="o-line angle [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int o-line")
w_tint = iw.FloatSlider(value=1, min=0, max=1, description="int t-line")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")

w_tl = iw.FloatSlider(value=4, min=0.5, max=8, description="t-line length [deg]")
w_tw = iw.FloatSlider(value=0, min=0, max=2, description="t-line width [deg]")
w_td = iw.FloatSlider(value=2, min=0, max=4, description="t-distance [deg]")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outl, w_outw, w_outa])
b_intensities = iw.HBox([w_int1, w_tint, w_int_back])
b_target = iw.HBox([w_tl, w_tw, w_td])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_ponzo(
    height=None,
    width=None,
    ppd=None,
    outer_lines_length=None,
    outer_lines_width=None,
    outer_lines_angle=None,
    target_lines_length=None,
    target_lines_width=None,
    target_distance=None,
    intensity_outer_lines=None,
    intensity_background=None,
    intensity_target_lines=None,
    add_mask=False,
):
    stim = ponzo(
        visual_size=(height, width),
        ppd=ppd,
        outer_lines_length=outer_lines_length,
        outer_lines_width=outer_lines_width,
        outer_lines_angle=outer_lines_angle,
        target_lines_length=target_lines_length,
        target_lines_width=target_lines_width,
        target_distance=target_distance,
        intensity_outer_lines=intensity_outer_lines,
        intensity_background=intensity_background,
        intensity_target_lines=intensity_target_lines,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_ponzo,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_lines_length": w_outl,
        "outer_lines_width": w_outw,
        "outer_lines_angle": w_outa,
        "target_lines_length": w_tl,
        "target_lines_width": w_tw,
        "target_distance": w_td,
        "intensity_target_lines": w_tint,
        "intensity_background": w_int_back,
        "intensity_outer_lines": w_int1,
    },
)

# Show
display(ui, out)
```
