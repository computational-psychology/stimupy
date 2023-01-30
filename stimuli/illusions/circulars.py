import itertools
from copy import deepcopy
import numpy as np

from stimuli.components.circulars import grating

__all__ = [
    "rings",
    "bullseye",
]


def rings(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    target_indices=None,
    intensity_target=0.5,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
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
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
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
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Hong, S. W., and Shevell, S. K. (2004). Brightness contrast and assimilation from patterned
        inducing backgrounds. Vision Research, 44, 35–43. https://doi.org/10.1016/j.visres.2003.07.010
    Howe, P. D. L. (2005). White's effect: removing the junctions but preserving the
        strength of the illusion. Perception, 34, 557–564. https://doi.org/10.1068/p5414
    """

    # Get stim
    stim = grating(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        intensity_background=intensity_background,
        intensity_rings=intensity_rings,
        shape=shape,
        origin=origin,
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
        intensity_rings=intensities,
        intensity_background=intensity_background,
        shape=shape,
        origin=origin,
    )

    # Update mask to only be targets
    stim["rings"] = deepcopy(stim["ring_mask"])
    mask = np.zeros(stim["shape"])
    for i, ring_idx in enumerate(target_indices):
        mask = np.where(stim["ring_mask"] == ring_idx+1, i+1, 0)
    stim["target_mask"] = mask.astype(int)
    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target

    return stim


def bullseye(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    intensity_target=0.5,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
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
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
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
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Bindman, D., & Chubb, C. (2004). Brightness assimilation in Bullseye displays.
        Vision Research, 44, 309–319. https://doi.org/10.1016/S0042-6989(03)00430-9
    Hong, S. W., and Shevell, S. K. (2004). Brightness contrast and assimilation from patterned
        inducing backgrounds. Vision Research, 44, 35–43. https://doi.org/10.1016/j.visres.2003.07.010
    Howe, P. D. L. (2005). White's effect: removing the junctions but preserving the
        strength of the illusion. Perception, 34, 557–564. https://doi.org/10.1068/p5414
    """
    stim = rings(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=0,
        origin=origin,
    )
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {
        "Circular Whites": rings(visual_size=(8, 8), ppd=32, frequency=1.0),
        "Circular Bullseye": bullseye(visual_size=(8, 8), ppd=32, frequency=1.0),
    }

    plot_stimuli(stims, mask=True, save=None)
