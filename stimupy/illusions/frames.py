import itertools

import numpy as np

from stimupy.components.frames import frames
from stimupy.utils import resolution, stack_dicts
from stimupy.waves import square_cityblock as rings

__all__ = [
    "rings",
    "rings_generalized",
    "bullseye",
    "bullseye_generalized",
    "two_sided_bullseye",
]


def rings_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    target_indices=(),
    intensity_target=0.5,
    origin="center",
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
        if bar_idx > stim["frame_mask"].max():
            raise ValueError("target_idx is outside stimulus")

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
    phase_shift=0,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    intensity_target=0.5,
    origin="center",
    clip=True,
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
    phase_shift : float
        phase shift of grating in degrees
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    clip : Bool
        if True, clip stimulus to image size (default: True)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bindman, D., & Chubb, C. (2004).
        Brightness assimilation in bullseye displays.
        Vision Research, 44, 309-319.
        https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    stim = rings(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
        intensity_frames=intensity_frames,
        target_indices=1,
        intensity_target=intensity_target,
        origin=origin,
        clip=clip,
        intensity_background=intensity_background,
    )
    return stim


def bullseye_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    intensity_target=0.5,
    origin="center",
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
    radii : Sequence[Number] or None (default)
        radii of each frame, in degrees visual angle
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
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
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    stim = rings_generalized(
        radii=radii,
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
    phase_shift=0,
    intensity_target=0.5,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
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
    phase_shift : float
        phase shift of grating in degrees
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
        Bindman, D., & Chubb, C. (2004).
        Brightness assimilation in bullseye displays.
        Vision Research, 44, 309-319.
        https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = bullseye(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
        intensity_target=intensity_target,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
    )

    stim2 = bullseye(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
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
        "radii": (1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5),
        "visual_size": 10,
        "ppd": 10,
    }

    stims = {
        "rings": rings(visual_size=10, ppd=10, frequency=0.5, target_indices=(1, 3)),
        "rings_generalized": rings_generalized(**p1, target_indices=(1, 3)),
        "bullseye": bullseye(visual_size=10, ppd=10, frequency=0.5),
        "bullseye_generalized": bullseye_generalized(**p1),
        "two_sided_bullseye": two_sided_bullseye(visual_size=10, ppd=10, frequency=1),
    }
    plot_stimuli(stims, mask=True, save=None)
