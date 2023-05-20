import itertools

import numpy as np

from stimupy.components.frames import frames
from stimupy.stimuli.waves import square_radial as circular
from stimupy.stimuli.waves import square_rectilinear as rectangular
from stimupy.utils import resolution, stack_dicts

__all__ = [
    "circular",
    "circular_two_sided",
    "rectangular",
    "rectangular_generalized",
    "rectangular_two_sided",
]


def circular_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    phase_shift=0,
    target_indices=None,
    intensity_target=0.5,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Two-sided circular grating, with one or more target rings

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
    phase_shift : float
        phase shift of grating in degrees
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
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Hong, S. W., and Shevell, S. K. (2004).
        Brightness contrast and assimilation from patterned inducing backgrounds.
        Vision Research, 44, 35-43.
        https://doi.org/10.1016/j.visres.2003.07.010
    Howe, P. D. L. (2005).
        White's effect:
        removing the junctions but preserving the strength of the illusion.
        Perception, 34, 557-564.
        https://doi.org/10.1068/p5414
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = circular(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
        target_indices=target_indices,
        intensity_target=intensity_target,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        origin=origin,
        clip=True,
    )

    stim2 = circular(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
        target_indices=target_indices,
        intensity_target=intensity_target,
        intensity_rings=intensity_rings[::-1],
        intensity_background=intensity_background,
        origin=origin,
        clip=True,
    )

    stim = stack_dicts(stim1, stim2)
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    stim["intensity_background"] = intensity_background
    return stim


def rectangular_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    rotation=0.0,
):
    """Draw sequential set of square frames with specified radii and targets

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number] or None (default)
        radii of each frame, in degrees visual angle
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    target_indices : int, or Sequence[int, ...]
        indices frames where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)


    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """

    # Frames component
    stim = frames(
        radii=radii,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        origin=origin,
        rotation=rotation,
    )
    stim["intensity_target"] = intensity_target

    # Resolve target parameters
    if isinstance(target_indices, (int)):
        target_indices = [
            target_indices,
        ]
    if isinstance(intensity_target, (int, float)):
        intensity_target = [
            intensity_target,
        ]
    intensity_target = itertools.cycle(intensity_target)

    # Place target(s)
    targets_mask = np.zeros_like(stim["frame_mask"])
    for target_idx, (bar_idx, intensity) in enumerate(zip(target_indices, intensity_target)):
        targets_mask = np.where(stim["frame_mask"] == bar_idx, target_idx + 1, targets_mask)
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])
        if bar_idx > stim["frame_mask"].max():
            raise ValueError("target_idx is outside stimulus")

    # Update and return stimulus
    stim["target_mask"] = targets_mask
    stim["target_indices"] = target_indices
    return stim


def rectangular_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    phase_shift=0,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    rotation=0.0,
):
    """Draw set of square frames, with some frame(s) as target

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    phase_shift : float
        phase shift of grating in degrees
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    target_indices : int, or Sequence[int, ...]
        indices frames where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)


    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Domijan, D. (2015).
        A neurocomputational account
        of the role of contour facilitation in brightness perception.
        Frontiers in Human Neuroscience, 9, 93.
        https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = rectangular(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames,
        target_indices=target_indices,
        origin=origin,
        clip=True,
        intensity_background=intensity_background,
        rotation=rotation,
    )

    stim2 = rectangular(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames[::-1],
        target_indices=target_indices,
        origin=origin,
        clip=True,
        intensity_background=intensity_background,
        rotation=rotation,
    )

    stim = stack_dicts(stim1, stim2)
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": (10, 10),
        "ppd": 30,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "rings_circular": circular(**default_params, frequency=1.0),
        "rings_circular_with_targets": circular(**default_params, frequency=1.0, target_indices=3),
        "rings_circular_clipped": circular(**default_params, frequency=1.0, clip=True),
        "rings_circular_2sided": circular_two_sided(**default_params, frequency=1.0),

        "rings_rectangular": rectangular(**default_params, frequency=1.0),
        "rings_rectangular_with_targets": rectangular(**default_params, frequency=1.0, target_indices=3),
        "rings_rectangular_clipped": rectangular(**default_params, frequency=1.0, clip=True),
        "rings_rectangular_2sided": rectangular_two_sided(**default_params, frequency=1.0),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
