import itertools

import numpy as np

from stimupy.components import frames as frames_component
from stimupy.utils import resolution, stack_dicts

__all__ = [
    "rings",
    "rings_generalized",
    "two_sided_rings",
    "bullseye",
    "bullseye_generalized",
    "two_sided_bullseye",
]


def rings(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, ...]
        intensity value for each bar, by default (1.0, 0.0).
        Can specify as many intensities as n_frames;
        If fewer intensities are passed than n_frames, cycles through intensities
    target_indices : int, or Sequence[int, ...]
        indices frames where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Frames component
    stim = frames_component.grating(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        period=period,
        intensity_frames=intensity_frames,
    )

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

    # Update and return stimulus
    stim["target_mask"] = targets_mask.astype(int)
    return stim


def two_sided_rings(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, ...]
        intensity value for each bar, by default (1.0, 0.0).
        Can specify as many intensities as n_frames;
        If fewer intensities are passed than n_frames, cycles through intensities
    target_indices : int, or Sequence[int, ...]
        indices frames where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = rings(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames,
        target_indices=target_indices,
    )

    stim2 = rings(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames[::-1],
        target_indices=target_indices,
    )

    stim = stack_dicts(stim1, stim2)
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def rings_generalized(
    frame_radii,
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
):
    """Draw sequential set of square frames with specified radii and targets

    Parameters
    ----------
    frame_radii : Sequence[Number]
        radii of each frame, in degrees visual angle
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as number of frame_widths;
        If fewer intensities are passed than frame_widhts, cycles through intensities
    intensity_background : float, optional
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

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """

    # Frames component
    stim = frames_component.frames(
        frame_radii=frame_radii,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        origin=origin,
    )

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

    # Update and return stimulus
    stim["target_mask"] = targets_mask
    return stim


def bullseye(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
):
    """Square "bullseye", i.e., set of rings with target in center

    Essentially frames(target_indices=1)

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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as n_franes;
        If fewer intensities are passed than n_frames, cycles through intensities
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

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
    """

    stim = rings(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        period=period,
        intensity_frames=intensity_frames,
        target_indices=1,
        intensity_target=intensity_target,
    )
    return stim


def bullseye_generalized(
    frame_radii,
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    intensity_target=0.5,
    origin="mean",
):
    """Draw sequential set of square frames with specified radii with central target

    Parameters
    ----------
    frame_radii : Sequence[Number]
        radii of each frame, in degrees visual angle
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as number of frame_widths;
        If fewer intensities are passed than frame_widhts, cycles through intensities
    intensity_background : float, optional
        intensity value of background, by default 0.5
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    stim = rings_generalized(
        frame_radii=frame_radii,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        target_indices=1,
        intensity_target=intensity_target,
        origin=origin,
    )
    return stim


def two_sided_bullseye(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    intensity_target=0.5,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Two-sided square "bullseye", i.e., set of rings with target in center

    Essentially frames(target_indices=1)

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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as n_franes;
        If fewer intensities are passed than n_frames, cycles through intensities
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

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
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = bullseye(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames,
    )

    stim2 = bullseye(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames[::-1],
    )

    stim = stack_dicts(stim1, stim2)
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    p1 = {
        "frame_radii": (1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5),
        "visual_size": 10,
        "ppd": 10,
    }

    stims = {
        "rings": rings(visual_size=10, ppd=10, frequency=0.5, target_indices=(1, 3)),
        "rings_generalized": rings_generalized(**p1, target_indices=(1, 3)),
        "two_sided_rings": two_sided_rings(
            visual_size=10, ppd=10, frequency=1, target_indices=(1, 3)
        ),
        "bullseye": bullseye(visual_size=10, ppd=10, frequency=0.5),
        "bullseye_generalized": bullseye_generalized(**p1),
        "two_sided_bullseye": two_sided_bullseye(visual_size=10, ppd=10, frequency=1),
    }
    plot_stimuli(stims, mask=True, save=None)
