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

# How to create a stimulus

This tutorial introduces the basics of stimulus generation with **`stimupy`** and shows how to create your first stimulus.  
At its core, `stimupy` provides a large set of *functions* that each draw a specific (visual) component into a {py:class}`numpy.ndarray`.

```{tip}
You can launch this tutorial as an interactive Jupyter Notebook on Binder — see the Binder icon at the top of the page.
```

---


## Example 1: A Gabor

One of the most common stimuli in vision science is the **Gabor patch** — a sinusoidal grating enveloped by a Gaussian.

In `stimupy`, Gabors are implemented in the {py:mod}`stimupy.stimuli.gabors` module:

```{code-cell}
from stimupy.stimuli.gabors import gabor

stim = gabor(visual_size=4, ppd=50, sigma=0.5, frequency=4, rotation=45, phase_shift=0)
```

The resulting stimulus is stored in a Python {py:class}`dict` with:
- `"img"` — a {py:class}`numpy.ndarray` containing the stimulus image. The default range of pixel values is $[0,1]$.
- All the parameters used to generate the stimulus
- Space for any additional metadata you wish to add

Some relevant parameters for Gabors:
- **`visual_size`** — image size (degrees)
- **`ppd`** — pixels per degree (resolution)
- **`sigma`** — size of Gaussian envelope (degrees)
- **`frequency`** — cycles per degree
- **`rotation`** — orientation in degrees
- **`phase_shift`** — phase offset in degrees

```{code-cell}
print(stim.keys())
```


You can use `stimupy`s plotting routine to plot the stimulus:

```{code-cell}
from stimupy.utils import plot_stim

plot_stim(stim)
```

Since the stimulus {py:class}`dict` contains the stimulus as a {py:class}`numpy.ndarray`, you can alternatively use your preferred way of showing a {py:class}`numpy.ndarray` on the `stim["img"]` array, e.g. {py:func}`matplotlib.pyplot.imshow()`:

```{code-cell}
import matplotlib.pyplot as plt

plt.imshow(stim["img"], cmap="gray")
plt.show()
```


## Example 2: A rectangle

`stimupy` also provides basic geometric shapes, located in the {py:mod}`stimupy.components.shapes` module.

```{code-cell}
from stimupy.components import shapes

stim = shapes.rectangle(visual_size=(6,8), ppd=10, rectangle_size=(4,4))
plot_stim(stim)
```

You can modify, e.g.:
- **`rectangle_size`** — width × height (degrees)
- **`rectangle_position`** — position from top-left corner (degrees)
- **`intensity_rectangle`** — brightness of rectangle
- **`intensity_background`** — brightness of background

Example with different size and brightness:
```{code-cell}
stim = shapes.rectangle(
    visual_size=(6,8),
    ppd=10,
    rectangle_size=(4,2),
    rectangle_position=(1,2),
    intensity_rectangle=.7
)
plot_stim(stim)
```

---


## Example 3: White noise

Another classic stimulus is **white noise** — an array of random pixel intensities.  
White noise is provided in {py:mod}`stimupy.noises.whites`:

```{code-cell}
from stimupy.noises.whites import white

stim = white(visual_size=4, ppd=50)
plot_stim(stim)
```

---

## Stimulus parameters

All `stimupy` stimulus-functions require and take multiple arguments. These control, for example:

- **Image size & resolution**
  - `visual_size`, `ppd`, or `shape` (pixels)
  - for more information, see our Topic Guide on [](../user_guide/resolution)
- **Stimulus-specific geometry**
  - e.g., `sigma`, `frequency` for Gabor
  - e.g., `rectangle_size` for rectangles
- **Photometric properties**
  - e.g., `intensity_rectangle` for rectangles
  - all `stimupy` stimuli by default are in the range [0, 1]

You can check a function's parameters in the [function reference](../reference/api) or via Python's `help()`:

```{code-cell}
:tags: [output_scroll]
help(gabor)
```

---

## Summary

A `stimupy` stimulus is:
1. A Python {py:class}`dict`
2. Containing `"img"` as a {py:class}`numpy.ndarray`
3. Including all parameters used to generate it

**Advantages**:
- Self-contained and reproducible
- Compatible with any NumPy-based workflow
- Easy to save, plot, and share

**Keep in mind**:
- Once created, parameters can be modified by the user — `stimupy` does not enforce post-creation validation. Handle with care.
