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

# Exploring an illusion

The geometric components in [`stimupy.components`](../reference/api/stimupy.components)
form the basic building blocks for all stimuli implement in `stimupy`.
More complex stimuli can be composed using the functions that generate components.
Included in `stimupy` is a large set of functionst to generate more complex stimuli,
which we term [`illusions`](../reference/api/stimupy.illusions).

## Simultaneous Brightness Contrast (SBC)

```{code-cell}
:tags: [hide-cell]
import matplotlib.pyplot as plt
from stimupy.utils import plot_stim
```

```{code-cell}
from stimupy.illusions import sbcs

stim = sbcs.basic(visual_size=(6,8), ppd=10, target_size=(2,2))

plot_stim(stim)
plt.show()
```

As you can see, this is not (much) more than:
```{code-cell}
from stimupy.components.shapes import rectangle

component = rectangle(visual_size=(6,8), ppd=10, rectangle_size=(2,2), intensity_background=0.0, intensity_rectangle=0.5)

plot_stim(component)
plt.show()
```

However, some of the stimulus parameters have different names in `illusions`.
In particular, **all** `illusions` have the concept of a `target` region(s):
image regions that are of some particular scientific interest in this stimulus.
For an SBC stimulus, this would be the rectangular path.
Thus, the `sbcs.basic` function takes a
- `target_size`, compared to `rectangle_size`
- `intensity_target`, rather than an `intensity_rectangle` (with a default intermediate value of `0.5`)
In addition, the output stimulus contains a `target_mask`,
which masks the pixels of the target region.

Let's look at a more realistic example:
```{code-cell}
two_sided_stim = sbcs.two_sided(visual_size=(6,8), ppd=10, target_size=(2,2))

plot_stim(two_sided_stim)
plt.show()
```
Now we have a true SBC display:
two separate image regions, with different background intensities,
and physically identical patches embedded in these regions.
Both patches are part of the same `target_mask`,
although with different integer-indices:
```{code-cell}
plot_stim(two_sided_stim, mask='target_mask')
plt.show()
```
and they are controlled by the same `intensity_target` argument.
The `intensity_backgrounds` can also be specified at creation:
```{code-cell}
two_sided_stim = sbcs.two_sided(visual_size=(6,8), ppd=10, target_size=(2,2),
intensity_backgrounds=(.25,.75))

plot_stim(two_sided_stim)
plt.show()
```

## White's illusion
```{code-cell}
from stimupy.illusions import whites

stim_whites = whites.white_two_rows(
    visual_size=(10,12),
    ppd=10,
    n_bars=6,
    target_height=2,
    target_indices_top=(2,4),
    target_indices_bottom=(3,5),
    target_center_offset=3,
    )

plot_stim(stim_whites)
plt.show()

```