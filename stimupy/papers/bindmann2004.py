"""Stimuli from Bindmann & Chubb (2004)
https://doi.org/10.1016/S0042-6989(03)00430-9

This module reproduces most of the stimuli used by Bindmann & Chubb (2004) as
they were described in that paper.

Each stimulus is provided by a separate function,
a full list can be found as stimupy.papers.bindmann2004.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/bindmann2004.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimupy.papers.bindmann2004 import *

References
-----------
Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
"""

import copy
import warnings

import numpy as np

from stimupy import bullseyes
from stimupy.utils.contrast_conversions import adapt_intensity_range_dict
from stimupy.utils.pad import pad_dict_by_visual_size

__all__ = [
    "bullseye_thin_gw45_gb31",
    "bullseye_thin_gw45_gb38",
    "bullseye_thin_gw45_gb45",
    "bullseye_thin_gw45_gb52",
    "bullseye_thin_gw45_gb59",
    "bullseye_thin_gw60_gb46",
    "bullseye_thin_gw60_gb53",
    "bullseye_thin_gw60_gb60",
    "bullseye_thin_gw60_gb67",
    "bullseye_thin_gw60_gb74",
    "bullseye_thin_gw75_gb61",
    "bullseye_thin_gw75_gb68",
    "bullseye_thin_gw75_gb75",
    "bullseye_thin_gw75_gb82",
    "bullseye_thin_gw75_gb89",
    "bullseye_thick_gw45_gb31",
    "bullseye_thick_gw45_gb38",
    "bullseye_thick_gw45_gb45",
    "bullseye_thick_gw45_gb52",
    "bullseye_thick_gw45_gb59",
    "bullseye_thick_gw60_gb46",
    "bullseye_thick_gw60_gb53",
    "bullseye_thick_gw60_gb60",
    "bullseye_thick_gw60_gb67",
    "bullseye_thick_gw60_gb74",
    "bullseye_thick_gw75_gb61",
    "bullseye_thick_gw75_gb68",
    "bullseye_thick_gw75_gb75",
    "bullseye_thick_gw75_gb82",
    "bullseye_thick_gw75_gb89",
]

# The authors say that they used a 15" Sony Trinitron monitor. We found the
# following specs online
monitor_height_px = 1024
monitor_width_px = 768
monitor_height_cm = 40.0
monitor_width_cm = 30.0
distance_cm = 132  # provided in the paper
ppcm = monitor_height_cm / monitor_height_px
PPD = int(np.tan(np.pi / 180.0 / 2.0) * 2.0 * distance_cm / ppcm)

TARGET_SIZE = 0.608
INTENSITY_BLACK = 1
INTENSITY_WHITE = 118
INTENSITY_BACKGROUND = 60
PAD1 = ((0, 1.2), (0, 2.7))
PAD2 = ((1.2, 0), (2.7, 0))
ORIGIN = "mean"


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating bindmann2004.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func(ppd=ppd)

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def resolve_target_size(target_size=TARGET_SIZE, ppd=PPD):
    target_size_old = copy.deepcopy(target_size)
    target_size = np.round(target_size / 2 * ppd) / ppd * 2

    if target_size_old != target_size:
        warnings.warn(
            f"Rounding target_size because of ppd; {target_size_old} -> {target_size}. "
            "This might also affect stimulus size."
        )
    return target_size


def resolve_band_width(band_width, ppd=PPD):
    band_width_old = copy.deepcopy(band_width)
    band_width = np.round(band_width * ppd) / ppd

    if band_width_old != band_width:
        warnings.warn(
            f"Rounding band_width because of ppd; {band_width_old} -> {band_width}. "
            "This might also affect stimulus size."
        )
    return band_width


def bullseye_thin_gw45_gb31(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 31 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
        Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=31.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw45_gb38(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 38 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=38.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw45_gb45(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 45 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=45.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw45_gb52(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 52 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=52.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw45_gb59(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 59 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=59.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw60_gb46(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 46 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=46.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw60_gb53(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 53 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=53.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw60_gb60(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 60 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=60.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw60_gb67(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 67 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=67.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw60_gb74(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 74 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=74.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw75_gb61(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 61 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=61.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw75_gb68(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 68 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=68.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw75_gb75(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 75 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=75.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw75_gb82(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 82 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=82.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thin_gw75_gb89(ppd=PPD):
    """Bullseye thin display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.122 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 89 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.122, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=89.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw45_gb31(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 31 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=31.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw45_gb38(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 38 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=38.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw45_gb45(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 45 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=45.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw45_gb52(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 52 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=52.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw45_gb59(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 45 & 59 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=45.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=59.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw60_gb46(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 46 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=46.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw60_gb53(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 53 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=53.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw60_gb60(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 60 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=60.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw60_gb67(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 67 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=67.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw60_gb74(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 60 & 74 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=60.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=74.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw75_gb61(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 61 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=61.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw75_gb68(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 68 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=68.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw75_gb75(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 75 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=75.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw75_gb82(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 82 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=82.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


def bullseye_thick_gw75_gb89(ppd=PPD):
    """Bullseye thick display from Bindmann & Chubb (2004)
    Target size: 0.608 x 0.608 deg
    Band widths: 0.243 deg
    Target distance (center to center): 1.2 x 2.7 deg
    Target luminances: 75 & 89 cd2/m

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindmann, D. & Chubb, C. (2004). Brightness assimilation in bullseye displays.
    Vision Research, 44 (3), 309-319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    target_size_half = resolve_target_size(ppd=ppd) / 2
    band_width = resolve_band_width(0.243, ppd=ppd)
    radii = np.linspace(target_size_half, target_size_half + band_width * 4, 5)

    params = {
        "shape": (target_size_half + band_width * 4) * 2 * ppd - 1,
        "ppd": ppd,
        "radii": radii,
        "origin": ORIGIN,
    }

    stim1 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_BLACK, INTENSITY_WHITE),
        intensity_target=75.0,
    )
    stim2 = bullseyes.rectangular_generalized(
        **params,
        intensity_frames=(INTENSITY_WHITE, INTENSITY_BLACK),
        intensity_target=89.0,
    )

    # Pad
    stim1 = pad_dict_by_visual_size(stim1, PAD1, ppd, pad_value=INTENSITY_BACKGROUND)
    stim2 = pad_dict_by_visual_size(stim2, PAD2, ppd, pad_value=INTENSITY_BACKGROUND)

    # Update dict keys
    stim1["img"] = np.where(stim2["pad_mask"] == 0, stim2["img"], stim1["img"])
    stim1["target_mask"] = np.where(stim2["target_mask"], 2, stim1["target_mask"])
    stim1["frame_mask2"] = stim2["frame_mask"]
    stim1["pad_mask2"] = stim2["pad_mask"]
    stim1["original_range"] = (INTENSITY_BLACK, INTENSITY_WHITE)

    # Adapt range between 0 and 1
    stim = adapt_intensity_range_dict(stim1)
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
