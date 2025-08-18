import itertools

import numpy as np

from stimupy.components import combine_masks, draw_regions
from stimupy.components.shapes import circle
from stimupy.components.shapes import ring as ring_shape
from stimupy.stimuli import mask_targets, waves

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
    target_indices=(),
    target_width=None,
    target_center=None,
    intensity_segments=(0.0, 1.0),
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
        rotation (in degrees), counterclockwise, by default 0.0
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

    # Draw angular grating
    stim = waves.square_angular(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        segment_width=segment_width,
        n_segments=n_segments,
        period="ignore",
        rotation=rotation,
        origin=origin,
        intensity_segments=intensity_segments,
    )

    # Mask to circular aperture
    radius = min(stim["visual_size"]) / 2
    stim["circle_mask"] = circle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=radius,
        origin=origin,
    )["circle_mask"]
    stim["segment_mask"] = np.where(stim["circle_mask"], stim["segment_mask"], 0)
    stim["img"] = np.where(stim["circle_mask"], stim["img"], intensity_background)
    stim["intensity_background"] = intensity_background

    # Target segment mask
    if isinstance(target_indices, (int, float)):
        target_indices = (target_indices,)
    target_segment_mask = mask_targets(
        element_mask=stim["grating_mask"], target_indices=target_indices
    )
    stim["target_indices"] = target_indices

    # Mask ring regions
    if target_center is None:
        target_center = radius / 2
    if isinstance(target_center, (int, float)):
        target_center = (target_center,)
    stim["target_center"] = target_center
    target_center = tuple(itertools.islice(itertools.cycle(target_center), len(target_indices)))

    if target_width is None:
        raise ValueError("pinwheel() missing argument 'target_width' which is not 'None'")
    if isinstance(target_width, (int, float)):
        target_width = (target_width,)
    stim["target_width"] = target_width
    target_width = tuple(itertools.islice(itertools.cycle(target_width), len(target_indices)))

    target_ring_masks = []
    for target_idx, (center, width) in enumerate(zip(target_center, target_width)):
        # Draw ring
        inner_radius = center - (width / 2)
        outer_radius = center + (width / 2)
        if inner_radius < 0 or outer_radius > np.min(visual_size) / 2:
            raise ValueError("target does not fully fit into pinwheel")
        ring = ring_shape(
            radii=[inner_radius, outer_radius],
            intensity_ring=target_idx,
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            shape=stim["shape"],
        )
        target_ring_masks.append(ring["ring_mask"])

    # Combine segment & ring masks
    target_masks = []
    for target_idx, ring_mask in enumerate(target_ring_masks):
        # Find where ring intesects with target segment
        target_mask = (target_segment_mask == target_idx + 1) & ring_mask
        target_masks.append(target_mask)

    # Combine target masks
    if len(target_masks) > 0:
        target_mask = combine_masks(*target_masks)
    else:
        target_mask = np.zeros_like(stim["img"])
    stim["target_mask"] = target_mask.astype(int)

    # Draw target(s)
    stim["img"] = np.where(
        target_mask, draw_regions(mask=target_mask, intensities=intensity_target), stim["img"]
    )
    stim["intensity_target"] = intensity_target

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
        "ppd": 32,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "pinwheel": pinwheel(**default_params, n_segments=10, target_width=2, target_indices=3),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
