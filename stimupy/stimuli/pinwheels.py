import itertools

import numpy as np

from stimupy.components.angulars import pinwheel as pinwheel_shape
from stimupy.components.shapes import ring as ring_shape
from stimupy.utils import resolution

__all__ = [
    "pinwheel",
]


def pinwheel(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0.0,
    target_indices=None,
    target_width=None,
    target_center=None,
    intensity_segments=(1.0, 0.0),
    intensity_background=0.5,
    intensity_target=0.5,
    origin="mean",
):
    """Pinwheel / radial White stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    shape : Sequence[int, int], int, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        angular frequency of angular grating, in cycles per angular degree
    n_segments : int, or None (default)
        number of segments
    segment_width : Number, or None (default)
        angular width of a single segment, in degrees
    rotation : float, optional
        rotation (in degrees) of pinwheel segments away
        counterclockwise from 3 o'clock, by default 0.0
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    target_width : float, or Sequence[float, ...], optional
        target width (outer - inner radius) in deg visual angle, by default 1.0
        Can specify as many target_widths as target_indices;
        if fewer widths are passed than indices, cycles through intensities
    target_center : float, or Sequence[float, ...], optional
        center (radius) in deg visual angle where each target will be placed
        within its segment, by default 1.0.
        Can specify as many centers as target_indices;
        if fewer centers are passed than indices, cycles through intensities
    intensity_segments : Sequence[float, ...]
        intensity value for each segment, by default (1.0, 0.0).
        Can specify as many intensities as n_segments;
        If fewer intensities are passed than n_segments, cycles through intensities
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
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Robinson, A. E., Hammon, P. S., & de Sa, V. R. (2007).
        Explaining brightness illusions
        using spatial filtering and local response normalization.
        Vision Research, 47(12), 1631-1644.
        https://doi.org/10.1016/j.visres.2007.02.017
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Radial grating
    stim = pinwheel_shape(
        radius=np.min(visual_size) / 2,
        frequency=frequency,
        n_segments=n_segments,
        segment_width=segment_width,
        rotation=rotation,
        intensity_segments=intensity_segments,
        intensity_background=intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        origin=origin,
        inner_radius=0,
    )
    if target_center is None:
        target_center = stim["radius"] / 2

    # Place target(s)
    if isinstance(target_indices, (int)):
        target_indices = [
            target_indices,
        ]
    if isinstance(target_center, (int, float)):
        target_center = [
            target_center,
        ]
    if isinstance(target_width, (int, float)):
        target_width = [
            target_width,
        ]
    if isinstance(intensity_target, (int, float)):
        intensity_target = [
            intensity_target,
        ]

    # Initiate target mask
    target_mask = np.zeros_like(stim["wedge_mask"])

    if target_indices is not None:
        if target_width is None:
            raise ValueError("pinwheel() missing argument 'target_width' which is not 'None'")

        target_center = itertools.cycle(target_center)
        target_width = itertools.cycle(target_width)
        intensity_target = itertools.cycle(intensity_target)

        for target_idx, (segment_idx, center, width, intensity) in enumerate(
            zip(target_indices, target_center, target_width, intensity_target)
        ):
            # Draw ring
            inner_radius = center - (width / 2)
            outer_radius = center + (width / 2)
            if inner_radius < 0 or outer_radius > np.min(visual_size) / 2:
                raise ValueError("target does not fully with into pinwheel")
            ring_stim = ring_shape(
                radii=[inner_radius, outer_radius],
                intensity_ring=intensity,
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                shape=stim["shape"],
            )
            condition1 = stim["wedge_mask"] == segment_idx
            condition2 = ring_stim["ring_mask"] == 1
            target_mask = np.where(condition1 & condition2, target_idx + 1, target_mask)
            stim["img"] = np.where(target_mask == (target_idx + 1), intensity, stim["img"])
    stim["target_mask"] = target_mask
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
        "pinwheel": pinwheel(**default_params, n_segments=10, target_width=1, target_indices=3),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)