from stimupy.components.frames import frames
from stimupy.components.radials import rings
from stimupy.stimuli import place_targets
from stimupy.stimuli.waves import square_radial as circular
from stimupy.stimuli.waves import square_rectilinear as rectangular
from stimupy.utils import make_two_sided

__all__ = [
    "circular",
    "circular_generalized",
    "circular_two_sided",
    "rectangular",
    "rectangular_generalized",
    "rectangular_two_sided",
]


def circular_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_rings=(0.0, 1.0),
    intensity_background=0.5,
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
):
    """Sequential set of circular rings with specified radii and targets

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number] or None (default)
        radii of each ring, in degrees visual angle
    intensity_rings : Sequence[float, float]
        intensities of rings, by default (1.0, 0.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    target_indices : int, or Sequence[int, ...]
        indices rings where targets will be placed
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
        mask with integer index for each ring (key: "target_mask"),
        and additional keys containing stimulus parameters
    """

    # Rings component
    stim = rings(
        radii=radii,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        origin=origin,
    )

    # Place target(s)
    stim = place_targets(
        stim=stim,
        element_mask_key="ring_mask",
        target_indices=target_indices,
        intensity_target=intensity_target,
    )

    return stim


circular_two_sided = make_two_sided(
    circular, two_sided_params=("intensity_rings", "intensity_target", "target_indices")
)


def rectangular_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(0.0, 1.0),
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
        rotation (in degrees), counterclockwise, by default 0.0 (horizontal)


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

    # Place target(s)
    stim = place_targets(
        stim=stim,
        element_mask_key="frame_mask",
        target_indices=target_indices,
        intensity_target=intensity_target,
    )

    return stim


rectangular_two_sided = make_two_sided(
    rectangular, two_sided_params=("intensity_frames", "intensity_target", "target_indices")
)


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
        "rings_circular": circular(**default_params, frequency=1.0),
        "rings_circular_with_targets": circular(**default_params, frequency=1.0, target_indices=3),
        "rings_circular_clipped": circular(**default_params, frequency=1.0, clip=True),
        "rings_circular_2sided": circular_two_sided(**default_params, frequency=1.0, intensity_rings=((0.0, 1.0), (1.0, 0.0)), clip=True, target_indices=2),

        "rings_rectangular": rectangular(**default_params, frequency=1.0),
        "rings_rectangular_with_targets": rectangular(**default_params, frequency=1.0, target_indices=3),
        "rings_rectangular_clipped": rectangular(**default_params, frequency=1.0, clip=True),
        "rings_rectangular_2sided": rectangular_two_sided(**default_params, frequency=1.0, intensity_frames=((0.0, 1.0), (1.0, 0.0)), clip=True, target_indices=2),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
