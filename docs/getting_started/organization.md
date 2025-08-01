---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# How `stimupy` is organized

## High-level submodules

The `stimupy` library is organized into several high-level submodules, each reflecting a different aspect of visual stimulus generation. These include:

- **[Components](../reference/_api/stimupy.components)** — basic building blocks such as geometric shapes, gratings, Gaussians, and lines  
- **[Noises](../reference/_api/stimupy.noises)** — noise textures like binary, white, pink, brown, and narrowband noise  
- **[Stimuli](../reference/_api/stimupy.stimuli)** — complete visual stimuli such as Gabors, plaids, Mondrians, and various visual illusions (e.g., Simultaneous Brightness Contrast, White's illusion, Hermann grid, Ponzo illusion)  
- **[Papers](../reference/_api/stimupy.papers)** — published stimulus sets which are exact replications of stimuli described in specific papers (e.g., ModelFest)  
- **[Utils](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.utils.html)** — a variety of utility functions for stimulus import/export, manipulation (e.g., contrast, size, padding), exploration of parameter spaces, plotting, etc  

You can import entire submodules via, e.g.:
```
from stimupy import stimuli
```


## Low-level submodules (sub-submodules)

`stimupy` is further subdivided into many lower-level submodules. The structure of these submodules reflects scientific conventions and conceptual similarities rather than strict software engineering practices. This means that stimuli are grouped with others that *look similar* or are *conceptually related*, even if they don’t share underlying code (although these two criteria can overlap, of course).

All submodule names are pluralized — for example, [`sbcs`](sbcs) for **S**imultaneous **B**rightness **C**ontrast**S**, and [`cubes`](cubes) for **cube** illusion**s**. This naming avoids namespace conflicts:

- `from stimupy.stimuli import cubes` refers to the `cubes` **submodule** of `stimuli`
- `from stimupy.stimuli.cubes import cube` refers to a specific **function** of the sub-submodule `cubes`

Pluralized names also hint that a given category may contain multiple variations or implementations.


## Multiple Approaches to the Same Stimulus

All roads lead to Rome, and many ways lead to the same stimulus.

Many `stimupy` stimuli can be constructed in more than one way, reflecting different visual or geometric interpretations. For example, the Todorovic Illusion can be seen either as:

- a **rectangle occluded** by covers ([`todorovics.rectangle`](todorovics.rectangle)), or  
- a **cross-shaped** target with adjacent squares ([`todorovics.cross`](todorovics.cross))

For some parameters, these two views may produce visually identical images. However, when parameters change, their behaviors diverge — demonstrating how interpretation shapes construction.


```{code-cell}
---
mystnb:
  image:
    classes: shadow bg-primary
  figure:
    caption: |
      [`todorovics.cross()`](todorovics.cross) (left) and [`.rectangle()`](todorovics.rectangle) (right)
      can produce identical images (top) for some parameterizations,
      but have different behavior for others (bottom)
    name: fig_todorovics
---
from stimupy.stimuli import todorovics
from stimupy.utils import plot_stimuli

resolution = {"visual_size": 5, "ppd": 10}

stims = {
    "cross, covers_size=1" : todorovics.cross(**resolution,     cross_size=2,  cross_thickness=1, covers_size=1),
    "rect, covers_size=1"  : todorovics.rectangle(**resolution, target_size=2, covers_offset=1,   covers_size=1),
    "cross, covers_size=.5": todorovics.cross(**resolution,     cross_size=2,  cross_thickness=1, covers_size=0.5),
    "rect, covers_size=.5" : todorovics.rectangle(**resolution, target_size=2, covers_offset=1,   covers_size=0.5),
}

plot_stimuli(stims)
```

To explore how different functions behave, we recommend trying the interactive [demos](../reference/demos).


## The philosophy behind `components` vs. `stimuli`

You might ask: What’s the difference between a component and a stimulus?

Truthfully, the line is not always clear. Conceptually, every component could be used as a stimulus, and vice versa. However, the distinction reflects a guiding principle of `stimupy`s modularity:

- `components` can be considered as atomic elements — reusable functions that serve as building blocks across many different stimulus functions
- `stimuli` are typically higher-level constructs, often featuring target regions and providing target_masks for region-specific analysis or manipulation

This modular structure allows for easy addition of entirely new stimulus functions or stimulus variations.

But do not worry. If this differentiation is not useful to you, you can import all `components` directly via the `stimuli` namespace, such that:
```
from stimupy.stimuli import ponzos, shapes
```
This flexibility supports both modular use and simplified workflows.
