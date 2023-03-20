import itertools

import numpy as np

from stimupy.components import image_base, mask_elements, waves
from stimupy.utils import resolution
from stimupy.utils.utils import apply_bessel, round_to_vals

__all__ = [
    "disc_and_rings",
    "disc",
    "ring",
    "annulus",
    "bessel",
    "sine_wave",
    "square_wave",
]


def mask_rings(
    radii,
    visual_size=None,
    ppd=None,
    shape=None,
    origin="mean",
):
    """Generate mask with integer indices for rings

    Parameters
    ----------
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters

    Raises
    ------
    ValueError
        if largest radius does not fit in visual size
    """

    # no axes are None; check if fits
    if visual_size.height < np.max(radii) * 2 or visual_size.width < np.max(radii) * 2:
        raise ValueError(
            f"Largest radius {np.max(radii)} does not fit in visual size {visual_size}"
        )

    # Mark elements with integer idx-value
    stim = mask_elements(
        orientation="radial",
        edges=radii,
        rotation=0.0,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
    )
    stim["ring_mask"] = stim["mask"]
    del stim["mask"]
    return stim


def disc_and_rings(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_rings=(0, 1),
    intensity_background=0.5,
    origin="mean",
):
    """Draw a central solid disc with zero or more solid rings (annuli)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    intensity_rings : Sequence[Number, ...]
        intensity value for each ring, from inside to out.
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """
    if radii is None:
        raise ValueError("disc_and_rings() missing argument 'radii' which is not 'None'")

    # Try to resolve resolution;
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except resolution.TooManyUnknownsError:
        # Check visual_size
        visual_size = resolution.validate_visual_size(visual_size)

    if visual_size is None or visual_size == (None, None):
        # Two axes are None; make image large enought to fit
        visual_size = resolution.validate_visual_size(np.max(radii) * 2)
    elif None in visual_size:
        # one axis is None; make square
        visual_size = [x for x in visual_size if x is not None]
        visual_size = resolution.validate_visual_size(visual_size)

    if np.diff(radii).min() < 0:
        raise ValueError("radii need to monotonically increase")

    # Get masks for rings
    params = mask_rings(radii=radii, shape=shape, visual_size=visual_size, ppd=ppd, origin=origin)
    shape = params["shape"]

    # Draw rings
    base = image_base(shape=shape, visual_size=visual_size, origin=origin)
    distances = base["radial"]

    img = np.ones(shape) * intensity_background
    ints = [*itertools.islice(itertools.cycle(intensity_rings), len(radii))]
    for radius, intensity in zip(reversed(radii), reversed(ints)):
        img[distances < radius] = intensity

    # Assemble output
    params["intensity_rings"] = intensity_rings
    return {"img": img, **params}


def disc(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    intensity_disc=1.0,
    intensity_background=0.5,
    origin="mean",
):
    """Draw a central disc

    Essentially, `dics(radius)` is an alias for `ring(radii=[0, radius])`

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radius : Number
        outer radius of disc in degree visual angle
    intensity_disc : Number
        intensity value of disc, by default 1.0
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
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """
    if radius is None:
        raise ValueError("disc() missing argument 'radius' which is not 'None'")

    radius = np.array(radius)
    intensity = np.array(intensity_disc)

    if radius.size != 1:
        raise ValueError("Can only pass 1 radius")
    if intensity.size != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = ring(
        radii=np.insert(radius, 0, 0),
        intensity_ring=intensity,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        shape=shape,
        origin=origin,
    )
    return stim


def ring(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_ring=1.0,
    intensity_background=0.5,
    origin="mean",
):
    """Draw a ring (annulus)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number, Number]
        inner and outer radius of ring in degree visual angle
    intensity_ring : Number
        intensity value of ring, by default 1.0
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
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters

    Raises
    ------
    ValueError
        if passed in less/more than 2 radii (inner, outer)
    ValueError
        if passed in less/more than 1 intensity
    """
    if radii is None:
        raise ValueError("ring() missing argument 'radii' which is not 'None'")
    if len(radii) != 2:
        raise ValueError("Can only pass exactly 2 radii")
    if len([intensity_ring]) != 1:
        raise ValueError("Can only pass 1 intensity")

    if radii[1] is None:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
        radii[1] = np.max(visual_size) / 2

    if radii[1] < radii[0]:
        raise ValueError("first radius needs to be smaller than second radius")

    stim = disc_and_rings(
        radii=radii,
        intensity_rings=[intensity_background, intensity_ring],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        origin=origin,
    )
    stim["ring_mask"] = np.where(stim["ring_mask"] == 2, 1, 0)
    return stim


annulus = ring


def bessel(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    order=0,
    intensity_rings=(1.0, 0.0),
    origin="mean",
):
    """Draw a Bessel stimulus, i.e. draw circular rings following an nth order
    Bessel function of a given frequency.

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
    order : int
        n-th order Bessel function
    intensity_rings : (float, float)
        intensity values of rings, first value indicating center intensity
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        empty mask (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """

    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=0,
        origin=origin,
    )

    arr = base["radial"] * frequency * 2 * np.pi
    img = apply_bessel(arr, order=order)
    img = (img - img.min()) / (img.max() - img.min())
    img = img * (intensity_rings[0] - intensity_rings[1]) + intensity_rings[1]

    stim = {
        "img": img,
        "ring_mask": np.zeros(base["shape"]).astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "order": order,
        "frequency": frequency,
        "intensity_rings": intensity_rings,
    }
    return stim


def sine_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    phase_shift=0,
    intensity_rings=(0.0, 1.0),
    intensity_background=0.5,
    origin="mean",
    clip=False,
):
    """Draw a circular sine-wave grating over the whole image

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
    intensity_rings : Sequence[float, float]
        min and max intensity of sine-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    clip : Bool
        if True, clip stimulus to image size (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_rings, ring_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_rings', 'ring_width'"
        )

    sw = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_rings,
        phase_width=ring_width,
        period="ignore",
        rotation=0,
        phase_shift=phase_shift,
        intensities=intensity_rings,
        origin=origin,
        round_phase_width=False,
        base_type="radial",
    )

    if clip:
        csize = min(sw["visual_size"]) / 2.0
        circle = disc(
            visual_size=sw["visual_size"],
            ppd=sw["ppd"],
            radius=csize,
            origin=origin,
        )
        sw["img"] = np.where(circle["ring_mask"], sw["img"], intensity_background)
        sw["mask"] = np.where(circle["ring_mask"], sw["mask"], 0)

    # Create stimulus dict
    stim = {
        "img": sw["img"],
        "ring_mask": sw["mask"].astype(int),
        "visual_size": sw["visual_size"],
        "ppd": sw["ppd"],
        "shape": sw["shape"],
        "origin": origin,
        "frequency": sw["frequency"],
        "frame_width": sw["phase_width"],
        "n_frames": sw["n_phases"],
        "intensity_rings": intensity_rings,
    }
    return stim


def square_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    phase_shift=0,
    intensity_rings=(0.0, 1.0),
    intensity_background=0.5,
    origin="mean",
    clip=False,
):
    """Draw a circular square-wave grating over the whole image

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
    intensity_rings : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    clip : Bool
        if True, clip stimulus to image size (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """
    stim = sine_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        phase_shift=phase_shift,
        intensity_rings=intensity_rings,
        origin=origin,
        clip=False,
    )

    # Round sine-wave to create square wave
    stim["img"] = round_to_vals(stim["img"], intensity_rings)

    if clip:
        csize = min(stim["visual_size"]) / 2.0
        circle = disc(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            radius=csize,
            origin=origin,
        )
        stim["img"] = np.where(circle["ring_mask"], stim["img"], intensity_background)
        stim["ring_mask"] = np.where(circle["ring_mask"], stim["ring_mask"], 0).astype(int)
    return stim


if __name__ == "__main__":
    from stimupy.utils.plotting import plot_stimuli

    p = {
        "visual_size": (10, 20),
        "ppd": 50,
    }

    stims = {
        "disc": disc(**p, radius=3),
        "disc_and_rings": disc_and_rings(**p, radii=(1, 2, 3)),
        "ring": ring(**p, radii=(1, 2)),
        "bessel": bessel(**p, frequency=0.5),
        "sine_wave": sine_wave(**p, frequency=0.5),
        "square_wave": square_wave(**p, frequency=0.5),
    }

    plot_stimuli(stims, mask=True)
