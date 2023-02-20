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

```{code-cell}
:tags: [remove-cell]
from myst_nb import glue
import numpy as np
```

# A first stimulus

Here you will be introduced to the basics of `stimupy`,
and create your first stimulus through this package.
At its core, `stimupy` provides a large number of functions
that each draw some kind of (visual) component in a `numpy.ndarray`.

```{tip} Launch on Binder
This page can also be launched as an interactive Jupyter Notebook on Binder -- see icon at top
```

## Basic shapes

The most basic stimuli that `stimupy` provides, are basic geometric shapes.
These can be found in `stimupy.components.shapes`.

```{code-cell}
from stimupy.components import shapes
```
```{code-cell}
:tags: [hide-input]
print(f"Available basic shapes: {shapes.__all__}")
```

Each of these is a separate function
that takes in parameters specifying the geometry of the shape.
Let's take a look at one of these:

```{code-cell}
:tags: [hide-input]
help(shapes.rectangle)
```

This function creates an image, and draws a rectangle inside it.
Everywhere the rectangle isn't, is considered the "background".

The arguments consist of three main categories:

- image size & resolution:
  - `visual_size` (height, width) of the whole image, in degrees visual angle
  - pixels per degree (`ppd`) of visual angle
  - `shape` in pixels
  - because these are three are inter-dependent, only two out of 3 need to be specified
    (see [resolution guide](../topic_guides/resolution) for more information)
- component geometry:
  - `rectangle_size` in degrees visual angle
  - `rectangle_position`, as distance from top-left corner, in degrees visual angle
- intensity ("photometric"):
  - in this case: `intensity_rectangle` and `intensity_background`
  - all `stimupy` stimuli by default are in the range [0, 1]

```{code-cell}
stim = shapes.rectangle(visual_size=(6,8), ppd=10, rectangle_size=(4,4))
```
```{code-cell}
:tags: [remove-cell]
glue('type', type(stim))
glue('keys',stim.keys())
glue('imgtype',type(stim["img"]))
```

This is output is a {glue:}`type`, with {glue:}`keys`.

The generated stimulus image is also in this output {glue:}`type`, under the key `"img"`.
As you can see, this output also contains all of the parameters for the component,
including those for which default values were used.
Thus, this output is self-documenting:
all the necessary information to produce this stimulus are in the stimulus.

The `"img"` is a {glue:}`imgtype`,
where each entry in this array corresponds to a pixel in the image.
Thus, the `shape` of the array is the (specified) `shape` in pixels of the image.

```{code-cell}
:tags: [hide-input]
print(f'"img" is a {type(stim["img"])}, of shape {stim["img"].shape}')
print(f'stim["shape"] is {stim["shape"]}')
```

The values of the entries represent the pixel intensities,
by default in range $[0,1]$.

To visualize the stimulus,
you can use your preferred way of showing a `numpy.ndarray`
(e.g. `matplotlib.pyplot.imshow()`)
on the `stim["img"]` array.

```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
plt.imshow(stim["img"])
plt.show()
```

For convenience, however, `stimupy` provides a `.utils.plot_stim()` function:

```{code-cell}
from stimupy.utils import plot_stim

plot_stim(stim)
plt.show()
```

Let's change some different parameters:

```{code-cell}
stim = shapes.rectangle(visual_size=(6,8), ppd=10,
                        rectangle_size=(4,2), rectangle_position=(1,2),
                        intensity_rectangle=.7, intensity_background=.5)

plot_stim(stim)
plt.show()
```

or another shape:

```{code-cell}
ellipse = shapes.ellipse(visual_size=(6,8), ppd=10,
                        radius=(2,1),
                        intensity_ellipse=1, intensity_background=.5)

plot_stim(ellipse)
plt.show()
```

## Masked regions, and composition

Another key in the stimulus-{glue:}`type` not addressed yet, is the `"shape_mask"`.
This too is a {glue:}`imgtype`, with the same shape as `"img"`
(i.e., each entry corresponds to a pixel in `"img"`).
However, rather than the values here being any floating point pixel-intensities
(default in range $[0, 1]$),
the `"shape_mask"` contains integer-values.
Each integer-value corresponds to a geometric region of interest.
For basic shapes like these there are only two such regions:
the background (mask value: `0`), and the shape itself (mask value: `1`).
These can be used to *mask* the regions: all pixels with value `1` belong to the shape.

We can visualize these as well, overlayed as colorcoding on top of the stimulus:
```{code-cell}
plot_stim(stim, mask='shape_mask')
plt.show()
```

A simple use for these masks is to change the intensities in an image:
```{code-cell}
# Change intensity of rectangle to .4; leave rest of image as is:
stim["img"] = np.where(stim["shape_mask"]==1, .4, stim["img"])

plot_stim(stim)
plt.show()
```

In a given mask, a pixel can only belong to a single region.
A stimulus can have multiple different masks, each for different sets of regions.

### Composition

Another use of region masking
is to compose more complicated stimuli
from basic components.

```{code-cell}
# Create a new stimulus, i.e., a new dict
composition = {}

# Copy over the two masks
composition["rectangle_mask"] = stim["shape_mask"]
composition["ellipse_mask"] = ellipse["shape_mask"]

# Logically combine masks: rectangle mask, except where ellipse mask:
composition["anti_join_mask"] = (composition["rectangle_mask"] == 1) & (~(composition["ellipse_mask"]==1))

# Create image
composition["img"] = np.where(composition["anti_join_mask"], 1, .5)

plot_stim(composition)
plt.show()
```
and we can even display each of the different masks:
```{code-cell}
:tags: [hide-input]
plt.subplot(1,3,1)
plot_stim(composition, mask="rectangle_mask")
plt.subplot(1,3,2)
plot_stim(composition, mask="ellipse_mask")
plt.subplot(1,3,3)
plot_stim(composition, mask="anti_join_mask")
plt.show()
```


This highlights the core design principle of `stimupy`-stimuli:
at their simplest structure, it is a plain Python {glue:}`type`
containing a {glue:}`imgtype` as the `"img"` key.
The advantages of this are:
1. the actual image can easily be integrated in existing codebases:
   - save to file using `numpy.save()`, `matplotlib.save()`, or `Pillow`
   - manipulate using any `numpy`-based code
   - TODO: import in PsychoPy (?)
2. anything that is compliant with this basic structure
   can use (some of) `stimupy` tooling,
   e.g., `plot_stim()`
3. since Python `dict`s are mutable, you as user can add, create, remove, rename
   any of the keys and values.

The main disadvantages, is that there are no controls or guarantees
*after* a stimulus is created,
for the accuracy of any of its fields,
since the user can change values.