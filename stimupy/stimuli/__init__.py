import numpy as np
from stimupy.stimuli import *

__all__ = [
    "mask_targets",
    "overview",
    "plot_overview",
    "benarys",
    "bullseyes",
    "checkerboards",
    "cornsweets",
    "cubes",
    "delboeufs",
    "dungeons",
    "edges",
    "gabors",
    "gratings",
    "hermanns",
    "mondrians",
    "mueller_lyers",
    "plaids",
    "ponzos",
    "rings",
    "sbcs",
    "todorovics",
    "waves",
    "wedding_cakes",
    "whites",
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


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    stimuli = {}
    for stimmodule_name in __all__:
        if stimmodule_name in ["overview", "plot_overview", "mask_targets"]:
            continue

        print(f"Generating stimuli from {stimmodule_name}")
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
            print("-- not implemented")
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
    plot_overview()
