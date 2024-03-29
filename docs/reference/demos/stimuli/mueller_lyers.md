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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/mueller_lyers.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Mueller-Lyers
{py:mod}`stimupy.stimuli.mueller_lyers`



## Mueller-Lyer
{py:func}`stimupy.stimuli.mueller_lyers.mueller_lyer`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.mueller_lyers import mueller_lyer

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outl = iw.FloatSlider(value=1, min=0.1, max=2, description="o-line length [deg]")
w_outa = iw.IntSlider(value=45, min=-180, max=180, description="o-line angle [deg]")
w_w = iw.FloatSlider(value=0, min=0, max=0.5, description="o-line width [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_tl = iw.FloatSlider(value=2.5, min=0, max=5, description="target length [deg]")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="int target")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outl, w_outa, w_w])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tl, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_mueller_lyer(
    height=None,
    width=None,
    ppd=None,
    outer_lines_length=None,
    line_width=None,
    outer_lines_angle=None,
    target_length=None,
    intensity_outer_line=None,
    intensity_background=None,
    intensity_target=None,
    add_mask=False,
):
    try:
        stim = mueller_lyer(
            visual_size=(height, width),
            ppd=ppd,
            outer_lines_length=outer_lines_length,
            outer_lines_angle=outer_lines_angle,
            line_width=line_width,
            target_length=target_length,
            intensity_outer_lines=intensity_outer_line,
            intensity_background=intensity_background,
            intensity_target=intensity_target,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None

# Set interactivity
out = iw.interactive_output(
    show_mueller_lyer,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "add_mask": w_mask,
        "outer_lines_length": w_outl,
        "line_width": w_w,
        "outer_lines_angle": w_outa,
        "target_length": w_tl,
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
from stimupy.stimuli.mueller_lyers import two_sided

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_outl = iw.FloatSlider(value=1, min=0.1, max=2, description="o-line length [deg]")
w_outa_l = iw.IntSlider(value=45, min=-180, max=180, description="o-line angle left [deg]")
w_outa_r = iw.IntSlider(value=45, min=-180, max=180, description="o-line angle right [deg]")

w_w = iw.FloatSlider(value=0, min=0, max=0.5, description="o-line width [deg]")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int line")
w_int_back = iw.FloatSlider(value=0, min=0, max=1, description="int background")

w_tl_l = iw.FloatSlider(value=2.5, min=0, max=5, description="target length left [deg]")
w_tl_r = iw.FloatSlider(value=2.5, min=0, max=5, description="target length right [deg]")
w_tint_l = iw.FloatSlider(value=0.5, min=0, max=1, description="int target left")
w_tint_r = iw.FloatSlider(value=0.5, min=0, max=1, description="int target right")


w_mask = iw.Dropdown(value=None, options=[None, 'target_mask', 'line_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_outl, w_outa_l, w_outa_r, w_w])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_tl_l, w_tl_r, w_tint_l, w_tint_r])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_two_sided(
    height=None,
    width=None,
    ppd=None,
    outer_lines_length=None,
    line_width=None,
    outer_lines_angle_l=None,
    outer_lines_angle_r=None,
    target_length_l=None,
    target_length_r=None,
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
            outer_lines_length=outer_lines_length,
            outer_lines_angle=(outer_lines_angle_l, outer_lines_angle_r),
            line_width=line_width,
            target_length=(target_length_l, target_length_r),
            intensity_outer_lines=intensity_outer_line,
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
        "outer_lines_length": w_outl,
        "line_width": w_w,
        "outer_lines_angle_l": w_outa_l,
        "outer_lines_angle_r": w_outa_r,
        "target_length_l": w_tl_l,
        "target_length_r": w_tl_r,
        "intensity_target_l": w_tint_l,
        "intensity_target_r": w_tint_r,
        "intensity_background": w_int_back,
        "intensity_outer_line": w_int1,
    },
)

# Show
display(ui, out)
```
