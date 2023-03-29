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

# Composing stimuli, composed stimuli

## Masked regions

Another key in the stimulus-`dict` not addressed yet, is the `"mask"`.
This too is a `numpy.ndarray`, with the same shape as `"img"`
(i.e., each entry corresponds to a pixel in `"img"`).

However, rather than the values here being any floating point pixel-intensities
(default in range $[0, 1]$),
the `"mask"` contains integer-values.
Each integer-value corresponds to a geometric region of interest.
For basic shapes like these there are only two such regions:
the background (mask value: `0`), and the shape itself (mask value: `1`).
These can be used to *mask* the regions: all pixels with value `1` belong to the shape.

We can visualize these as well,
overlayed as colorcoding on top of the stimulus:
```{code-cell}
plot_stim(stim, mask='shape_mask')
plt.show()
```

## Composition

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

## Composed stimuli

TODO: example going from `disc` to multiple `ring`s


## Using masks to alter the simulus after creation

Another use for `_mask`s is to change the intensities in an image:
```{code-cell}
# Change intensity of rectangle to .4; leave rest of image as is:
stim["img"] = np.where(stim["shape_mask"]==1, .4, stim["img"])

plot_stim(stim)
plt.show()
```

In a given mask, a pixel can only belong to a single region.
A stimulus can have multiple different masks, each for different sets of regions.