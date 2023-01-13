import itertools

import numpy as np

from stimuli.components import frame as frames_component

__all__ = [
    "frames_stimulus",
    "frames_generalized",
    "bullseye_stimulus",
    "bullseye_generalized",
]


def frames_stimulus(
    shape=None,
    visual_size=None,
    ppd=None,
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
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
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
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Frames component
    stim = frames_component.square_wave(
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
    targets_mask = np.zeros_like(stim["mask"])
    for target_idx, (bar_idx, intensity) in enumerate(zip(target_indices, intensity_target)):
        targets_mask = np.where(stim["mask"] == bar_idx, target_idx + 1, targets_mask)
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])

    # Update and return stimulus
    stim["bars_mask"] = stim["mask"]
    stim["mask"] = targets_mask

    return stim


def frames_generalized(
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
        mask with integer index for each frame (key: "mask"),
        and additional keys containing stimulus parameters
    """
    # if visual_size is None and shape is None:
    #     visual_size = sum(frame_radii)*2
    
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
    targets_mask = np.zeros_like(stim["mask"])
    for target_idx, (bar_idx, intensity) in enumerate(zip(target_indices, intensity_target)):
        targets_mask = np.where(stim["mask"] == bar_idx, target_idx + 1, targets_mask)
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])

    # Update and return stimulus
    stim["bars_mask"] = stim["mask"]
    stim["mask"] = targets_mask

    return stim


def bullseye_stimulus(
    shape=None,
    visual_size=None,
    ppd=None,
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
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
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
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Bindman, D., & Chubb, C. (2004). Brightness assimilation in Bullseye displays.
        Vision Research, 44, 309–319. https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    stim = frames_stimulus(
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
        mask with integer index for each frame (key: "mask"),
        and additional keys containing stimulus parameters
    """
    stim = frames_generalized(
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


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    p1 = {
        "frame_radii": (1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5),
        "visual_size": 10,
        "ppd": 10,
        }

    stims = {
        "Frames": frames_stimulus(visual_size=10, ppd=10, frequency=0.5, target_indices=(1, 3)),
        "Frames generalized": frames_generalized(**p1, target_indices=(1, 3)),
        "Bullseye": bullseye_stimulus(visual_size=10, ppd=10, frequency=0.5),
        "Bullseye generalized": bullseye_generalized(**p1),
    }
    plot_stimuli(stims, mask=True, save=None)
