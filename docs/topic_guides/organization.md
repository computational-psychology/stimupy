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
# How stimupy is organized

Broadly, `stimupy` functions currently fall into the following categories, which are also the toplevel submodules of `stimupy`:
- basic visual stimulus [components](../reference/_api/stimupy.components),
  such as basic shapes, wave gratings, Gaussians
- visual [noise](../reference/_api/stimupy.noises) textures, of different kinds,
- parameterized visual [stimuli](../reference/_api/stimupy.stimuli)
  - Gabors, plaids, edges,
  - a variety of so-called illusions 
   (e.g. Simultaneous Brightness Contrast, White's illusion, Hermann grid, Ponzo illusion), and many more
- exact replications of stimuli previously published (e.g. ModelFest)
  as described in their respecive [papers](../reference/_api/stimupy.papers)
- [utility functions](https://stimupy.readthedocs.io/en/latest/reference/_api/stimupy.utils.html)
  for stimulus import, export, manipulation (e.g. contrast, size), or plotting

## `components` vs. `stimuli`
::::{margin}
:::{note}
Some if not most `components` are also imported in `stimuli` for convenience,
such that 
```
from stimupy.stimuli import ponzos, shapes
```
will work easily.
:::
::::
In principle, every component can also be considered a stimulus:
it is some visual feature that can be drawn as an image.
The distinctions we make in `stimupy` are:
firstly, that the `components` underly (many) different stimuli,
and are "atomic" in a sense;
secondly, most/all `stimuli` have some concept of one or more *target*(s)
-- a region of special scientific interest.
Thus, most/all `stimuli` come with a `target_mask`
that indicate these targets.

## Submodules
Further subdividing the overall structure are lots of submodules.
These submodules are organized along scientific interest,
history, convention, etc., rather than engineering.
Thus, a you should find a stimulus in a submodule
with those stimuli *that is looks like* or *is related to*,
rather than with those stimuli that it shares components or code with
(although these two criteria can overlap, of course).

Moreover, the submodules all have pluralized names,
e.g., [`sbcs`](sbcs) for **S**imultaneous **B**rightness **C**ontrast**S**,
[`cubes`](cubes) for **Cube** illusion**S**.
This is in part to avoid namespace conflicts,
i.e. `from stimupy.stimuli import cubes` uniquely identifies the [`cubes`](cubes) *submodule*,
where `from stimupy.stimuli.cubes import cube` uniquely identifies the [`cubes.cube`](cubes.cube) *function*.
In addition, it also serves to indicate that for a given "stimulus",
there may be multiple functions, see next section.

## Multiple alternative stimulus functions

All roads lead to Rome,
and many ways lead to the same stimulus.
For lots of the stimuli provided by `stimupy`,
there are numerous different ways one can draw it.
Often, these different ways of drawing
are informed by the visual and geometric interpretation
of who is doing the drawing.

A good example of this is the Todorovic Illusion, which one can interpret as
having a [rectangular target](todorovics.rectangle) that is partially occluded by some "covers"
OR as having a [cross-shaped target](todorovics.cross) with adjoining squares.
For a single stimulus parameterization,
these two conceptions may produce perfectly identical images ([see fig, top](fig_todorovics)).
However, when changing parameters,
you would expect different *behavior* from the stimulus fuction
dependent on your conception/interpretation of the stimulus ([see fig, bottom](fig_todorovics)).

```{code-cell}
---
mystnb:
  image:
    classes: shadow bg-primary
  figure:
    caption: |
      [`todorovics.cross()`](todorovics.cross) (left) and [`.rectangle()`](todorovics.cross) (right)
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

The easiest way to find out how the different functions
differ in their behavior,
is to interactively explore their parameters using the [demos](../reference/demos).

Even for those stimuli for which we currently have only have one implementation,
(e.g., the [Ponzo illusion](ponzos))
we could see other alternatives,
and the modular structure of `stimupy` is designed to make additing these straightforward.

