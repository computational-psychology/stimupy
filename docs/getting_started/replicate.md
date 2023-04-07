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

# Replicate exact stimulus

Sometimes, you want to have an *exact copy*
of some existing stimulus.
Since `stimupy`s functions are highly parameterizable,
lots of variants of a stimulus can be created,
and thus specific existing parameterizations can be recreated.

For a large selection of the generic {py:mod}`stimupy.stimuli`,
there are specific parameterizations in the published literature.
Some of these are implement in stimupy as well,
under the corresponding {py:mod}`stimupy.papers`.

```{code-cell}
:tags: [hide-cell]
import matplotlib.pyplot as plt
from stimupy.utils import plot_stim
```

```{code-cell}
from stimupy.papers import RHS2007

stim = RHS2007.WE_thick()

plot_stim(stim)
plt.show()
```
Note that without *any* input arguments,
this will create the pixel-exact image as described in the original source.

## Adjusting resolution

The default version of the stimulus
may not be the right aspect ratio or resolution for your use.
For example, the {py:mod}`RHS2007 <stimupy.papers.RHS2007>` stimuli
are 32x32 degrees, at 32 pixels-per-degree, resulting in 1024x1024 pixels.
However, lets say your observer is seated at a distance that gives 24 pixels-per-degree.
These resolution parameters can be changed for the paper stimuli, keep the visual elements at the same *visual* size.
**Only** these resolution parameters can be changed;
the user cannot redefine the sizes of the visual elements.
```{code-cell}
stim = RHS2007.WE_thick(ppd=24)

plot_stim(stim)
plt.show()
```