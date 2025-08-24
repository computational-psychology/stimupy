import itertools
import logging

import numpy as np

from stimupy.components import draw_regions
from stimupy.stimuli import *  # noqa: F403

# Get module level logger
logger = logging.getLogger("stimupy.stimuli")


__all__ = [
    "mask_targets",
    "place_targets",
    "overview",
    "plot_overview",
    "benarys",  # noqa: F405
    "bullseyes",  # noqa: F405
    "checkerboards",  # noqa: F405
    "cornsweets",  # noqa: F405
    "cubes",  # noqa: F405
    "delboeufs",  # noqa: F405
    "dungeons",  # noqa: F405
    "edges",  # noqa: F405
    "gabors",  # noqa: F405
    "gratings",  # noqa: F405
    "hermanns",  # noqa: F405
    "mondrians",  # noqa: F405
    "mueller_lyers",  # noqa: F405
    "plaids",  # noqa: F405
    "ponzos",  # noqa: F405
    "rings",  # noqa: F405
    "sbcs",  # noqa: F405
    "todorovics",  # noqa: F405
    "waves",  # noqa: F405
    "wedding_cakes",  # noqa: F405
    "whites",  # noqa: F405
]


def mask_targets(element_mask, target_indices):
    """Indicate elements as targets

    Creates a new target_mask from a mask of elements (e.g., grating bars, rings, frames, etc.),
    by indexing these elements.

    Parameters
    ----------
    element_mask : numpy.ndarray
        mask with integer values for different elements / regions in a stimulus
    target_indices : Sequence[int] or int
        index or indices of elements to be designated as targets.
        Index 0 should always refer to background region.
        Indices can be negative, which results in "counting backwards"
        from the highest index in element_mask.

    Returns
    -------
    numpy.ndarray
        target mask, with integer values indicating target regions,
        in order that they appear in target_indices

    Raises
    ------
    ValueError
        if a target_idx is greater than any value in the element_mask
    """
    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (int, float)):
        target_indices = [
            target_indices,
        ]

    target_mask = np.zeros_like(element_mask)
    for target_idx, element_idx in enumerate(target_indices):
        if element_idx < 0:
            element_idx = int(element_mask.max()) + element_idx

        if element_idx > element_mask.max():
            raise ValueError("target_idx is outside stimulus")
        target_mask = np.where(element_mask == element_idx, target_idx + 1, target_mask)

    return target_mask


def place_targets(stim, element_mask_key, target_indices, intensity_target=0.5):
    """Place targets in stimulus

    Turns image regions/elements defined by element_mask_key
    and indicated by target_indices, into targets.
    Targets are defined in a new target_mask, and drawn into image with intensity_target.

    Parameters
    ----------
    stim : dict[str, Any]
        stimulus dictionary, with at least an "img" key, and mask indicated by element_mask_key
    element_mask_key : str
        key of the mask in stim-dict indicating image "elements"/regions
    target_indices : Sequence[int] or int
        index or indices of elements to be designated as targets
    intensity_target : float, optional
        intensity value for target, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") with targets placed,
        mask with integer index for the target (key: "target_mask")

    See also
    --------
        mask_targets, draw_regions
    """
    stim["target_mask"] = mask_targets(
        element_mask=stim[element_mask_key], target_indices=target_indices
    )

    if isinstance(intensity_target, (int, float)):
        intensity_target = [
            intensity_target,
        ]
    intensity_target = itertools.cycle(intensity_target)

    stim["img"] = np.where(
        stim["target_mask"],
        draw_regions(
            mask=stim["target_mask"], intensities=intensity_target, intensity_background=0.0
        ),
        stim["img"],
    )
    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target

    return stim


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    stimuli = {}
    for stimmodule_name in __all__:
        if stimmodule_name in ["overview", "plot_overview", "mask_targets", "place_targets"]:
            continue

        logger.info(f"Generating stimuli from {stimmodule_name}")
        # Get a reference to the actual module
        stimmodule = globals()[stimmodule_name]

        try:
            stims = stimmodule.overview()

            # Accumulate
            stimuli.update(stims)
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            logger.info("-- not implemented")
            pass

    return stimuli


def plot_overview(mask=False, save=None, units="deg"):
    """Plot overview of examples in this module (and submodules)

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim

    """
    from stimupy.utils import plot_stimuli

    stims = overview(skip=True)
    plot_stimuli(stims, mask=mask, units=units, save=save)


if __name__ == "__main__":
    # Log to console at INFO level
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    plot_overview()
