from stimupy.stimuli import rings

__all__ = [
    "circular",
    "circular_two_sided",
    "rectangular",
    "rectangular_generalized",
    "rectangular_two_sided",
]


def circular(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    phase_shift=0,
    intensity_target=0.5,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
    clip=True,
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
    stim = rings.circular(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=0,
        origin=origin,
        clip=clip,
    )
    return stim


def circular_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    phase_shift=0,
    intensity_target=0.5,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Two-sided circular Bullseye stimulus

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
    Bindman, D., & Chubb, C. (2004).
        Brightness assimilation in bullseye displays.
        Vision Research, 44, 309-319.
        https://doi.org/10.1016/S0042-6989(03)00430-9
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

    stim = rings.circular_two_sided(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
        intensity_rings=intensity_rings,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=0,
        origin=origin,
    )
    return stim


def rectangular(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    rotation=0.0,
    phase_shift=0,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    intensity_target=0.5,
    origin="mean",
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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

    stim = rings.rectangular(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_frames=intensity_frames,
        target_indices=0,
        intensity_target=intensity_target,
        origin=origin,
        clip=clip,
        intensity_background=intensity_background,
    )
    return stim


def rectangular_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    rotation=0.0,
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
    radii : Sequence[Number] or None (default)
        radii of each frame, in degrees visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
    stim = rings.rectangular_generalized(
        radii=radii,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        target_indices=1,
        intensity_target=intensity_target,
        origin=origin,
    )
    return stim


def rectangular_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    rotation=0.0,
    phase_shift=0,
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        Bindman, D., & Chubb, C. (2004).
        Brightness assimilation in bullseye displays.
        Vision Research, 44, 309-319.
        https://doi.org/10.1016/S0042-6989(03)00430-9
    """

    stim = rings.rectangular_two_sided(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        target_indices=0,
        origin=origin,
    )
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
        "bullseyes_circular": circular(**default_params, frequency=1.0, clip=True),
        "bullseyes_circular_2sided": circular_two_sided(**default_params, frequency=1.0),
        "bullseyes_rectangular": rectangular(**default_params, frequency=1.0, clip=True),
        "bullseyes_rectangular_2sided": rectangular_two_sided(**default_params, frequency=1.0),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
