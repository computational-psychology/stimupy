import itertools
from copy import deepcopy

import numpy as np

from stimuli.components.circular import grating


def circular_white(
    visual_size=None,
    ppd=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    target_indices=None,
    intensity_target=0.5,
    intensity_rings=[1.0, 0.0],
    intensity_background=0.5,
    supersampling=1,
    shape=None,
):
    """Circular grating, with one or more target rings

    Specification of the number of rings, and their width can be done in two ways:
    a ring_width (in degrees) and n_rings, and/or by specifying the spatial frequency
    of a circular grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the rings and their widths.
    Thus, not all 6 parameters (visual_size, ppd, shape, frequency, ring_width, n_rings)
    have to be specified, as long as both the resolution, and the distribution of rings,
    can be resolved.

    Note: all rings in a grating have the same width -- if more control is required
    see disc_and_rings

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of circular grating, in cycles per degree
    n_rings : int, or None (default)
        number of rings
    ring_width : Number, or None (default)
        width of a single ring, in degrees
    target_indices : int or Sequence[int, ] (optional)
        indices of target discs. If not specified, use middle ring (round down)
    intensity_target : float (optional)
        intensity value of target ring(s), by default 0.5
    intensity_rings : Sequence[Number, ...]
        intensity value for each ring, from inside to out, by default [1,0]
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 1.
        Warning: produces smoother circles but might introduce gradients that affect vision!
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Get stim
    stim = grating(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        intensity_background=intensity_background,
        intensities=intensity_rings,
        supersampling=supersampling,
        shape=shape,
    )

    # Add target intensity
    intensities = [*itertools.islice(itertools.cycle(intensity_rings), len(stim["radii"]))]
    if target_indices is None:
        target_indices = len(intensities) // 2
    try:
        for ring_idx in target_indices:
            intensities[ring_idx] = intensity_target
    except TypeError:
        intensities[target_indices] = intensity_target
        target_indices = [target_indices]

    # Redraw stim with target
    stim = grating(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        intensities=intensities,
        intensity_background=intensity_background,
        supersampling=supersampling,
        shape=shape,
    )

    # Update mask to only be targets
    stim["rings"] = deepcopy(stim["mask"])
    stim["mask"] = np.zeros_like(stim["rings"])
    for i, ring_idx in enumerate(target_indices):
        stim["mask"] = np.where(stim["rings"] == ring_idx + 1, i + 1, stim["mask"])

    # Target masks should only cover areas where target intensity is exactly vtarget
    cond = (stim["img"] != intensity_target) & (stim["mask"] != 0)
    stim["mask"][cond] = 0

    params = {
        "target_indices": target_indices,
        "intensity_target": intensity_target,
    }
    stim.update(params)

    return stim


def circular_bullseye(
    visual_size=None,
    ppd=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    intensity_target=0.5,
    intensity_rings=[1.0, 0.0],
    intensity_background=0.5,
    supersampling=1,
    shape=None,
):
    """Circular Bullseye stimulus

    Circular grating, where the target is the central disc.
    Alias for circular_white(target_indices=0,...)

    Specification of the number of rings, and their width can be done in two ways:
    a ring_width (in degrees) and n_rings, and/or by specifying the spatial frequency
    of a circular grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the rings and their widths.
    Thus, not all 6 parameters (visual_size, ppd, shape, frequency, ring_width, n_rings)
    have to be specified, as long as both the resolution, and the distribution of rings,
    can be resolved.

    Note: all rings in a grating have the same width -- if more control is required
    see disc_and_rings

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of circular grating, in cycles per degree
    n_rings : int, or None (default)
        number of rings
    ring_width : Number, or None (default)
        width of a single ring, in degrees
    intensity_target : float (optional)
        intensity value of target ring(s), by default 0.5
    intensity_rings : Sequence[Number, ...]
        intensity value for each ring, from inside to out, by default [1,0]
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 1.
        Warning: produces smoother circles but might introduce gradients that affect vision!
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """
    stim = circular_white(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=0,
        supersampling=supersampling,
        shape=shape,
    )
    return stim


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "Circular Whites": circular_white(visual_size=(8, 8), ppd=32, frequency=1.0),
        "Circular Bullseye": circular_bullseye(visual_size=(8, 8), ppd=32, frequency=1.0),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
