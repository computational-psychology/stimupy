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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/angulars.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Pinwheels
{py:mod}`stimupy.stimuli.pinwheels`



## Pinwheel
{py:func}`stimupy.stimuli.pinwheels.pinwheel`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.pinwheels import pinwheel

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_nseg = iw.IntSlider(value=6, min=2, max=12, description="n_segments")
w_rot = iw.IntSlider(value=0, min=0, max=360, description="rotation [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int1")
w_int2 = iw.FloatSlider(value=0., min=0, max=1, description="int2")
w_int_back = iw.FloatSlider(value=0.5, min=0, max=1, description="int background")

w_tidx = iw.IntSlider(value=3, min=0, max=6, description="target idx")
w_twidth = iw.FloatSlider(value=2.5, min=0, max=5, description="target width")
w_tcent = iw.FloatSlider(value=2.5, min=0, max=5, description="target center")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_ori = iw.Dropdown(value="mean", options=['mean', 'corner', 'center'], description="origin")
w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'wedge_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_nseg, w_rot])
b_intensities = iw.HBox([w_int1, w_int2, w_int_back])
b_target = iw.HBox([w_tidx, w_twidth, w_tcent, w_tint])
b_add = iw.HBox([w_ori, w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_pinwheel(
    height=None,
    width=None,
    ppd=None,
    n_segments=None,
    rotation=None,
    intensity1=None,
    intensity2=None,
    intensity_background=None,
    target_indices=None,
    target_width=None,
    target_center=None,
    intensity_target=None,
    origin=None,
    add_mask=False,
):
    try:
        stim = pinwheel(
            visual_size=(height, width),
            ppd=ppd,
            rotation=rotation,
            n_segments=n_segments,
            intensity_segments=(intensity1, intensity2),
            intensity_background=intensity_background,
            origin=origin,
            target_indices=target_indices,
            target_width=target_width,
            target_center=target_center,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_pinwheel,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "n_segments": w_nseg,
        "rotation": w_rot,
        "intensity1": w_int1,
        "intensity2": w_int2,
        "intensity_background": w_int_back,
        "origin": w_ori,
        "add_mask": w_mask,
        "target_indices": w_tidx,
        "target_width": w_twidth,
        "target_center": w_tcent,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```
