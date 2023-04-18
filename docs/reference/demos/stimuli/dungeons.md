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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/stimuli/dungeons.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Jupyter Widgets extension (`ipywidgets`)](https://ipywidgets.readthedocs.io/en/latest/index.html).
```

# Stimuli - Dungeons
{py:mod}`stimupy.stimuli.dungeons`



## Dungeon
{py:func}`stimupy.stimuli.dungeons.dungeon`

```{code-cell} ipython3
import ipywidgets as iw
from stimupy.utils import plot_stim
from stimupy.stimuli.dungeons import dungeon

# Define widgets
w_height = iw.IntSlider(value=10, min=1, max=20, description="height [deg]")
w_width = iw.IntSlider(value=10, min=1, max=20, description="width [deg]")
w_ppd = iw.IntSlider(value=20, min=1, max=40, description="ppd")

w_ncell1 = iw.IntSlider(value=5, min=2, max=10, description="n_cells1")
w_ncell2 = iw.IntSlider(value=5, min=2, max=10, description="n_cells2")

w_int1 = iw.FloatSlider(value=1, min=0, max=1, description="int grid")
w_int_back = iw.FloatSlider(value=0., min=0, max=1, description="int background")

w_trad = iw.IntSlider(value=1, min=0, max=3, description="target radius")
w_tint = iw.FloatSlider(value=0.5, min=0, max=1, description="target int")

w_mask = iw.Dropdown(value=None, options=[None, 'target_mask'], description="add mask")

# Layout
b_im_size = iw.HBox([w_height, w_width, w_ppd])
b_geometry = iw.HBox([w_ncell1, w_ncell2])
b_intensities = iw.HBox([w_int1, w_int_back])
b_target = iw.HBox([w_trad, w_tint])
b_add = iw.HBox([w_mask])
ui = iw.VBox([b_im_size, b_geometry, b_intensities, b_target, b_add])

# Function for showing stim
def show_dungeon(
    height=None,
    width=None,
    ppd=None,
    n_cells1=None,
    n_cells2=None,
    intensity1=None,
    intensity_background=None,
    target_radius=None,
    intensity_target=None,
    add_mask=False,
):
    stim = dungeon(
        visual_size=(height, width),
        ppd=ppd,
        n_cells=(n_cells1, n_cells2),
        intensity_grid=intensity1,
        intensity_background=intensity_background,
        target_radius=target_radius,
        intensity_target=intensity_target,
    )
    plot_stim(stim, mask=add_mask)

# Set interactivity
out = iw.interactive_output(
    show_dungeon,
    {
        "height": w_height,
        "width": w_width,
        "ppd": w_ppd,
        "n_cells1": w_ncell1,
        "n_cells2": w_ncell2,
        "intensity1": w_int1,
        "intensity_background": w_int_back,
        "add_mask": w_mask,
        "target_radius": w_trad,
        "intensity_target": w_tint,
    },
)

# Show
display(ui, out)
```
