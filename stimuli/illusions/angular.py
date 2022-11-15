import itertools

import numpy as np

from stimuli.components.angular import pinwheel
from stimuli.components.circular import ring


def radial_white(
    visual_size=None,
    ppd=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0,
    target_indices=[2, 5],
    target_width=1.0,
    target_center=1.0,
    intensities_segments=[1.0, 0.0],
    intensity_background=0.3,
    intensity_target=0.5,
    shape=None,
):
    """
    Radial White stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
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
    intensities_segments : Sequence[float, ...]
        intensity value for each segment, by default [1.0, 0.0]
        Can specify as many intensities as n_segments;
        If fewer intensities are passed than n_segments, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    shape : Sequence[int, int], int, or None (default)
        shape [height, width] of image, in pixels

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Radial grating
    stim = pinwheel(
        radius=np.max(visual_size) / 2,
        frequency=frequency,
        n_segments=n_segments,
        segment_width=segment_width,
        rotation=rotation,
        intensities=intensities_segments,
        intensity_background=intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
    )

    # Place target(s)
    if isinstance(target_indices, (int)):
        target_indices = [
            target_indices,
        ]
    if isinstance(target_center, (int, float)):
        target_center = [
            target_center,
        ]
    target_center = itertools.cycle(target_center)
    if isinstance(target_width, (int, float)):
        target_width = [
            target_width,
        ]
    target_width = itertools.cycle(target_width)
    if isinstance(intensity_target, (int, float)):
        intensity_target = [
            intensity_target,
        ]
    intensity_target = itertools.cycle(intensity_target)

    target_mask = np.zeros_like(stim["mask"])
    for target_idx, (segment_idx, center, width, intensity) in enumerate(
        zip(target_indices, target_center, target_width, intensity_target)
    ):
        # Draw ring
        inner_radius = center - (width / 2)
        outer_radius = center + (width / 2)
        ring_stim = ring(
            radii=[inner_radius, outer_radius],
            intensity=intensity,
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            shape=stim["shape"],
        )
        target_mask = np.where(
            (stim["mask"] == segment_idx) & (ring_stim["mask"] == 2), target_idx + 1, target_mask
        )
        stim["img"] = np.where(target_mask == (target_idx + 1), intensity, stim["img"])
    stim["mask"] = target_mask

    return stim


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "Radial white": radial_white(visual_size=(8, 8), ppd=32, n_segments=8),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
