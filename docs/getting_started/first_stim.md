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

# A first stimulus

Here you will be introduced to the basics of `stimupy`,
and create your first stimulus through this package.
At its core, `stimupy` provides a large number of *functions*
that each draw some kind of (visual) component in a {py:class}`numpy.ndarray`.

```{tip} Launch on Binder
This page can also be launched as an interactive Jupyter Notebook on Binder -- see icon at top
```

## Drawing a basic shape

The most basic stimuli that `stimupy` provides, are basic geometric shapes.
These functions can be found in the {py:mod}`stimupy.components.shapes` *module*.
To be able to access these,
we first have to *import* this module
into our current Python session:
```{code-cell}
from stimupy.components import shapes
```

`````{margin}
````{tip}
In some interactive Python interpreters,
such as IPython, or Jupyter Notebooks,
you can also see all contents of a module
by typing the (imported) module name
and pressing <TAB> to autocomplete:
```
>>> shapes.<TAB>
```
````
`````
This module contains the following functions:
```{code-cell}
:tags: [hide-input]
print(f"Available basic shapes: {shapes.__all__}")
```

Each of these `str`ings represents a separate function.
Let's take a look at one of them:
```{code-cell}
stim = shapes.rectangle(visual_size=(6,8), ppd=10, rectangle_size=(4,4))
```

This function creates an image, and draws a rectangle inside it.
Every pixel which is not part of the rectangle, is considered the "background".
It returns a {py:class}`dict`ionary,
mapping `str`ings as *keys*, to all kinds of *values*.

One of these values in in this output {py:class}`dict`,
is the generated stimulus image is under the key `"img"`.
This `"img"` is a {py:class}`numpy.ndarray`,
where each entry in this array corresponds to a pixel in the image.

To visualize the stimulus,
you can use your preferred way of showing a {py:class}`numpy.ndarray`
on the `stim["img"]` array,
e.g. {py:func}`matplotlib.pyplot.imshow()`:
```{code-cell}
:tags: [hide-input]
import matplotlib.pyplot as plt
plt.imshow(stim["img"])
plt.show()
```

For convenience, however, `stimupy` provides a {py:func}`.utils.plot_stim <stimupy.utils.plotting.plot_stim>` function:

```{code-cell}
from stimupy.utils import plot_stim

plot_stim(stim)
plt.show()
```

The values of the entries in the `"img"` {py:class}`numpy.ndarray` represent the pixel intensities,
by default in range $[0,1]$.

## Stimulus parameters
All `stimupy` stimulus-functions require and take multiple arguments.
To see what arguments a given function takes,
and what each of these arguments controls,
you can look at the (online) [function reference](../reference/api.md)
-- or access the function *docstring* from within Python:
```{code-cell}
help(shapes.rectangle)
```

The arguments consist of three main categories:
- image size & resolution:
  - `visual_size` (height, width) of the whole image, in degrees visual angle
  - pixels per degree (`ppd`) of visual angle
  - `shape` in pixels
  - because these three are inter-dependent, only two out of 3 need to be specified
    (see [resolution guide](../topic_guides/resolution) for more information)
- component geometry:
  - `rectangle_size` in degrees visual angle
  - `rectangle_position`, as distance from top-left corner, in degrees visual angle
- intensity ("photometric"):
  - in this case: `intensity_rectangle` and `intensity_background`
  - all `stimupy` stimuli by default are in the range [0, 1]

For these simple shapes, the arguments should be quite intuitive.
To change the geometry of the {py:func}`rectangle <stimupy.components.shapes.rectangle>`,
for example make it half its width,
we call the function with `rectangle_size=(4,2)`
(changed from `(4,4)`):
```{code-cell}
stim = shapes.rectangle(visual_size=(6,8), ppd=10,
                        rectangle_size=(4,2), rectangle_position=(1,2))

plot_stim(stim)
plt.show()
```

We can also change the `intensity` of the
{py:func}`rectangle <stimupy.components.shapes.rectangle>` that gets drawn:
```{code-cell}
stim = shapes.rectangle(visual_size=(6,8), ppd=10,
                        rectangle_size=(4,2), rectangle_position=(1,2),
                        intensity_rectangle=.7)

plot_stim(stim)
plt.show()
```


## Another shape
Let's look at another example shape -- {py:func}`disc <stimupy.components.shapes.disc>`:
```{code-cell}
help(shapes.disc)
```

Again, this function takes various arguments.
The resolution arguments are the same
(as they are for all `stimupy` components and stimul),
and the photometric `intensity` arguments are similar.
The component geometry arguments are of course different,
specific to the shape that the function provides.
```{code-cell}
disc = shapes.disc(visual_size=(6,8), ppd=10,
                        radius=2,
                        intensity_disc=1, intensity_background=.5)

plot_stim(disc)
plt.show()
```

## Stimulus parameters are part of output
When we take a closer look at the whole output {py:class}`dict`ionary,
we see that all of the input parameters to the function
are also there:
```
print(stim)
```
As you can see, this output also contains all of the parameters for the component,
both those that we specified (e.g., `visual_size`, `intensity_rectangle`),
but also those for which default values were used (e.g., `intensity_background`).
Thus, this output is self-documenting:
all the necessary information to produce this stimulus are in the stimulus-`dict`.

A nice feature of these {py:class}`dict`s is that you, the user,
can add any arbitrary (meta)data to them, after creating the stimulus.
For instance, we can add some label,
or a creation date:
```{code-cell}
stim["label"] = "A nice stimulus"
stim["date"] = "today"

print(stim)
```

## Summary
This tutorial highlights the core design principles of `stimupy`-stimuli.
At its simplest, a `stimupy`-stimulus is:

1. a plain Python {py:class}`dict`,
2. containing a {py:class}`numpy.ndarray` as the `"img"` key.
3. (produced by a stimulus or component function)

The advantages of this are:
1. the actual image can easily be integrated in existing codebases:
   - save to file using {py:func}`numpy.save`, {py:func}`matplotlib.pyplot.imsave`, or {py:mod}`PIL`
   - manipulate using any {py:mod}`numpy`-based code
   % TODO: import in PsychoPy (?)
2. anything that is compliant with this basic structure
   can use (some of) `stimupy` tooling,
   e.g., {py:func}`plot_stim <stimupy.utils.plotting.plot_stim>`, {py:mod}`exports <stimupy.utils.export>`, or  {py:mod}`contrast manipulations <stimupy.utils.contrast_conversions>` to name a few
3. since Python {py:class}`dict`s are *mutable*, you as user can add, create, remove, rename
   any of the keys and values.

The main disadvantage is that there are no controls or guarantees
*after* a stimulus is created
for the accuracy of any of its fields,
since the user can manually change values at any point in time.