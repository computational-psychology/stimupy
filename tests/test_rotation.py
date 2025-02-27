# %% [markdown]
# # Test the rotation of the rectangle
# specifically that multiple rotated rectangles are approximately aligned

# %%
import numpy as np

from stimupy.components import combine_masks, shapes
from stimupy.utils.plotting import plot_stim

# %%
rect_A = shapes.rectangle(
    visual_size=(15, 15),
    ppd=10,
    rectangle_size=(4, 4),
    rectangle_position=(3, 3),
    rotation=30,
    intensity_rectangle=0.5,
)
plot_stim(rect_A)

# %%
rect_B = shapes.rectangle(
    visual_size=(15, 15),
    ppd=10,
    rectangle_size=(3, 3),
    rectangle_position=(3, 3),
    rotation=30,
    intensity_rectangle=0.5,
)
plot_stim(rect_B)

# %% Combine by adding the images
new_img = rect_A["img"] + rect_B["img"]
combined_stim = {"img": new_img, "visual_size": rect_A["visual_size"], "ppd": rect_A["ppd"]}

plot_stim(combined_stim)

# %% [markdown]
# One thing to note, is that the two rectangles don't perfectly align...
# This is because the rotation in pixel space is necessarily discrete.
#
# The misaligned is easier to see if we create new masks for the two regions in the combined stim.

# %%
mask_union = np.logical_and(rect_A["rectangle_mask"], rect_B["rectangle_mask"])
mask_intersect = np.logical_xor(rect_A["rectangle_mask"], rect_B["rectangle_mask"])

combined_mask = combine_masks(mask_union, mask_intersect)
combined_stim = {
    "img": new_img,
    "mask": combined_mask,
    "visual_size": rect_A["visual_size"],
    "ppd": rect_A["ppd"],
}

plot_stim(combined_stim, mask=True)
