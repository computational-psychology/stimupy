import itertools
from copy import deepcopy

import numpy as np

from stimuli.components.circular import circular_grating
from stimuli.utils import degrees_to_pixels, pad_to_visual_size, resize_array


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
    stim = circular_grating(
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
    stim = circular_grating(
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


def radial_white(
    visual_size=(10, 12),
    ppd=20,
    n_segments=8,
    rotate=3 * np.pi,
    target_width=2.5,
    target_center=2.5,
    target_indices=(0, 1, 2, 3, 4),
    intensity_slices=(1.0, 0.0),
    intensity_background=0.3,
    intensity_target=0.5,
    ssf=1,
):
    """
    Radial White stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    n_segments : int
        number of cycles in stimulus (= half number of slices)
    rotate : float
        orientation of circle in radians
    target_width : float
        target width given the slice shape in deg
    target_center : float
        target center within slice in deg
    target_indices : int or (int, )
        indices of target slices
    intensity_slices : (float, float)
        intensity values of slices
    intensity_background : float
        intensity value of target discs
    intensity_target : float
        intensity value of target discs
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing if >1. Default is 1.
          Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    ----------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    shape_px = degrees_to_pixels(np.minimum(visual_size[0], visual_size[1]), ppd) * ssf
    x = np.arange(-int(shape_px / 2), int(shape_px / 2))
    img = np.ones([shape_px, shape_px]) * intensity_background
    mask = np.zeros([shape_px, shape_px])
    rotate = rotate % (2 * np.pi)

    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)
    if not isinstance(n_segments, (float, int)):
        raise ValueError("n_segments should be a single float or int")
    if not n_segments % 2 == 0:
        raise ValueError("n_segments should be even-numbered")
    if not isinstance(target_width, (float, int)):
        raise ValueError("target_width should be a single float or int")
    if not isinstance(target_center, (float, int)):
        raise ValueError("target_center should be a single float or int")
    if (target_center - target_width / 2) * ppd < 0 or (
        target_center + target_width / 2
    ) * ppd > shape_px / 2:
        raise ValueError("Warning: targets do not fully fit into stimulus")
    if not isinstance(rotate, (float, int)):
        raise ValueError("rotate should be a single float or int")
    if len(intensity_slices) != 2:
        raise ValueError("vdiscs needs to be a tuple of two floats")

    # Create circle (i.e. radial part)
    yy, xx = np.meshgrid(x, x)
    radial = np.sqrt(yy**2.0 + xx**2.0)
    radial[radial > x.max()] = 0
    radial[int(shape_px / 2), int(shape_px / 2)] = 1

    tradial = np.copy(radial)
    tradial[tradial < ppd * (target_center - target_width / 2)] = 0
    tradial[tradial > ppd * (target_center + target_width / 2)] = 0

    # Calculate angular part
    angular = np.arctan2(yy, xx)
    angular = angular - angular.min() + rotate
    angular[angular > 2 * np.pi] -= 2 * np.pi
    angular[angular == 0] = 0.0001

    # Divide circle in nparts:
    theta = np.linspace(0, 2 * np.pi, n_segments + 1)
    theta[theta > 2 * np.pi] -= 2 * np.pi
    for i in range(n_segments):
        ang = np.copy(angular)
        ang[angular <= theta[i]] = 0
        ang[angular > theta[i + 1]] = 0
        indices = ang * radial
        tindices = ang * tradial
        img[indices != 0] = intensity_slices[i % 2]

        if i in target_indices:
            img[tindices != 0] = intensity_target
            mask[tindices != 0] = target_indices.index(i) + 1

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2
    mask = np.dot(sampler, np.dot(mask, sampler.T)) / ssf**2

    # Pad to desired size
    img = pad_to_visual_size(
        img=img, visual_size=visual_size, ppd=ppd, pad_value=intensity_background
    )
    mask = pad_to_visual_size(img=mask, visual_size=visual_size, ppd=ppd, pad_value=0)

    # Target masks should only cover areas where target intensity is exactly vtarget
    cond = (img != intensity_target) & (mask != 0)
    mask[cond] = 0

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "n_segments": n_segments,
        "rotate": rotate,
        "target_width": target_width,
        "target_center": target_center,
        "intensity_slices": intensity_slices,
        "intensity_background": intensity_background,
        "intensity_target": intensity_target,
        "target_indices": target_indices,
        "ssf": ssf,
    }

    return {"img": img, "mask": mask, **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "Circular Whites": circular_white(visual_size=(8, 8), ppd=32, frequency=1.0),
        "Circular Bullseye": circular_bullseye(visual_size=(8, 8), ppd=32, frequency=1.0),
        "Radial white": radial_white(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
