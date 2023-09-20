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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/delboeufs.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Delboeufs
{py:mod}`stimupy.stimuli.delboeufs`



## Delboeuf
{py:func}`stimupy.stimuli.delboeufs.delboeuf`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.delboeufs import delboeuf

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outr = iw.FloatSlider(value=4, min=0.5, max=8, description="outer radius [deg]")
w_outw = iw.FloatSlider(value=0, min=0, max=2, description="outer line width [deg]")

w_int1 = iw.FloatSlider(value=0, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=1., min=0, max=1, description="int background")

w_tr = iw.FloatSlider(value=2.5, min=0, max=5, description="target radius [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="int target")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outr, w_outw])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tr, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_delboeuf(
    height=None,
    width=None,
    ppd=None,
    outer_radius=None,
    outer_line_width=None,
    target_radius=None,
    intensity_outer_line=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = delboeuf(
            visual_size=(height, width),
            ppd=ppd,
            outer_radius=outer_radius,
            outer_line_width=outer_line_width,
            target_radius=target_radius,
            intensity_outer_line=intensity_outer_line,
            intensity_background=intensity_background,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_delboeuf,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_radius": w_outr,
        "outer_line_width": w_outw,
        "target_radius": w_tr,
        "intensity_target": w_tint,
        "intensity_background": w_int_back,
        "intensity_outer_line": w_int1,
    },
)

# Show
display(ui, out)
```

## Two-sided
{py:func}`stimupy.stimuli.delboeufs.two_sided`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.delboeufs import two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=20, min=1, max=40, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_out_rad_l = iw.FloatSlider(value=4, min=0.5, max=8, description="outer radius1 [deg]")
w_out_rad_r = iw.FloatSlider(value=2.5, min=0.5, max=8, description="outer radius2 [deg]")
w_outw = iw.FloatSlider(value=0, min=0, max=2, description="outer line width [deg]")

w_int1 = iw.FloatSlider(value=0, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=1., min=0, max=1, description="int background")

w_tr = iw.FloatSlider(value=2., min=0, max=4, description="target radius [deg]")
w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="int left target")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="int right target")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_out_rad_l, w_out_rad_r, w_outw])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tr, w_tint_l, w_tint_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_two_sided(
    height=None,
    width=None,
    ppd=None,
    outer_radius1=None,
    outer_radius2=None,
    outer_line_width=None,
    target_radius=None,
    intensity_outer_line=None,
    intensity_background=None,
    intensity_target_l=None,
    intensity_target_r=None,
    add_mask=False,
):
    try:
        stim = two_sided(
            visual_size=(height, width),
            ppd=ppd,
            outer_radius=(outer_radius1, outer_radius2),
            outer_line_width=outer_line_width,
            target_radius=target_radius,
            intensity_outer_line=intensity_outer_line,
            intensity_background=intensity_background,
            intensity_target=(intensity_target_l, intensity_target_r),
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_two_sided,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_radius_l": w_out_rad_l,
        "outer_radius_r": w_out_rad_r,
        "outer_line_width": w_outw,
        "target_radius": w_tr,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "intensity_background": w_int_back,
        "intensity_outer_line": w_int1,
    },
)

# Show
display(ui, out)
```
