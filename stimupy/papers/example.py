"""Example paper module (citation information here)

This set only serves as an example / template
for how to set up a stimulus-set-module

Attributes
----------
__all__ (list of str): list of all stimulus-functions,
    these are exported by this module when executing
        >>> from stimupy.papers.example import *

References
----------
reference information here

"""

from stimupy.components import combine_masks, draw_regions, shapes

# Define original size resolution parameters
VISUAL_SIZE = (10, 12)
PPD = 10

__all__ = [
    "my_bullseye",
    "my_inverse_bullseye",
]


# Helper function:
def bullseye_geometry(ppd=PPD):
    """Helper function to create the bullseye geometry

    This function itself is not a stimulus,
    and will not be shown in `stimupy.papers.my_paper`

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)

    """
    # Create center (target) disc:
    disc = shapes.disc(
        visual_size=VISUAL_SIZE, ppd=ppd, radius=2, intensity_disc=0.5, intensity_background=0.5
    )

    # Create first ring, white:
    ring_1 = shapes.ring(
        visual_size=VISUAL_SIZE, ppd=ppd, radii=(2, 3), intensity_ring=1, intensity_background=0.5
    )

    # Create second ring, black:
    ring_2 = shapes.ring(
        visual_size=VISUAL_SIZE, ppd=ppd, radii=(3, 4), intensity_ring=0, intensity_background=0.5
    )

    bullseye_mask = combine_masks(disc["ring_mask"], ring_1["ring_mask"], ring_2["ring_mask"])

    return bullseye_mask


# New stimulus function:
def my_bullseye(ppd=PPD):
    """My bullseye stimulus: grey on white on black

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters

    """

    # Call geometry helper function
    bullseye_mask = bullseye_geometry(ppd=ppd)

    bullseye_img = draw_regions(
        mask=bullseye_mask, intensities=[0.5, 1, 0], intensity_background=0.5
    )

    # Package into stim-dict, adding parameter information
    stim = {
        "img": bullseye_img,
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "radii": (2, 3, 4),
        "intensities": (0.5, 1, 0),
        "intensity_background": 0.5,
    }

    # Output
    return stim


# Second stimulus function:
def my_inverse_bullseye(ppd=PPD):
    """My other bullseye stimulus: grey on black on white


    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters

    """

    # Call geometry helper function
    bullseye_mask = bullseye_geometry(ppd=ppd)

    bullseye_img = draw_regions(
        mask=bullseye_mask, intensities=[0.5, 0, 1], intensity_background=0.5
    )

    # Package into stim-dict, adding parameter information
    stim = {
        "img": bullseye_img,
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "radii": (2, 3, 4),
        "intensities": (0.5, 0, 1),
        "intensity_background": 0.5,
        "note": "Here is some additional information: I like this stimulus!",
    }

    # Output
    return stim
