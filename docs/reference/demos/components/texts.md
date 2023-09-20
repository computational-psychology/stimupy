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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/texts.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Components - Texts
{py:mod}`stimupy.components.texts`


## Text
{py:func}`stimupy.components.texts.text`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.components.texts import text

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_int = iw.FloatSlider(value=1., min=0, max=1, description="intensity line")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="intensity background")

w_text = iw.Textarea(value='Hello World', placeholder='Type something', description='text')
w_fontsize = iw.IntSlider(value=30, min=1, max=60, description="fontsize")
w_align = iw.Dropdown(value="center", options=['left', 'center', 'right'], description="align")
w_direction = iw.Dropdown(value="ltr", options=['ltr', 'rtl'], description="direction")

w_mask = iw.ToggleButton(value=False, disabled=False, description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_text = iw.HBox([w_text, w_fontsize, w_align, w_direction])
b_intensities = iw.HBox([w_int, w_int_back])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_text, b_intensities, b_add])

# Function for showing stim
def show_text(
    height=None,
    width=None,
    ppd=None,
    str_text=None,
    intensity_text=None,
    intensity_background=None,
    fontsize=None,
    align=None,
    direction=None,
    add_mask=False,
):
    try:
        stim = text(
            text=str_text,
            visual_size=(height, width),
            ppd=ppd,
            intensity_text=intensity_text,
            intensity_background=intensity_background,
            fontsize=fontsize,
            align=align,
            direction=direction,
        )
        plot_stim(stim, mask=add_mask)
    except Exception as e:
        raise ValueError(f"Invalid parameter combination: {e}") from None    

# Set interactivity
out = iw.interactive_output(
    show_text,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "str_text": w_text,
        "intensity_text": w_int,
        "intensity_background": w_int_back,
        "fontsize": w_fontsize,
        "align": w_align,
        "direction": w_direction,
        "add_mask": w_mask,
    },
)

# Show
display(ui, out)
```