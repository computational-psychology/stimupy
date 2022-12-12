import itertools

import numpy as np

from stimuli.components.frame import frames as frames_component


__all__ = [
    "frames",
    "bullseye",
]

def frames(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(0.0, 1.0),
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
    intensity_bars : Sequence[float, ...]
        intensity value for each bar, by default [1.0, 0.0].
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities
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
    stim = frames_component(
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


def bullseye(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(0.0, 1.0),
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
    intensity_bars : Sequence[float, ...]
        intensity value for each bar, by default [1.0, 0.0].
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities
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

    stim = frames(
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


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {
        "Frames": frames(visual_size=10, ppd=10, frequency=0.5, target_indices=(1, 3)),
        "Bullseye": bullseye(visual_size=10, ppd=10, frequency=0.5),
    }
    plot_stimuli(stims, mask=True, save=None)