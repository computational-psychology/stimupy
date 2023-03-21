from stimupy.utils import resolution, stack_dicts
from stimupy.waves import square_radial

__all__ = ["circular", "circular_two_sided"]


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
    stim = square_radial(
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

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = circular(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
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
        intensity_target=intensity_target,
        intensity_rings=intensity_rings[::-1],
        intensity_background=intensity_background,
        origin=origin,
        clip=True,
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
        "circular": circular(**default_params, frequency=1.0, clip=True),
        "circular, two sided": circular_two_sided(**default_params, frequency=1.0),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)
