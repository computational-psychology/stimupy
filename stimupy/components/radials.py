import itertools

import numpy as np

from stimupy.components import image_base, mask_regions
from stimupy.utils import resolution

__all__ = [
    "disc",
    "ring",
    "annulus",
    "rings",
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
    stim = mask_regions(
        distance_metric="radial",
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


def rings(
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
        raise ValueError("rings() missing argument 'radii' which is not 'None'")

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

    if not isinstance(radii, (int, float)):
        if np.diff(radii).min() < 0:
            raise ValueError("radii need to monotonically increase")
    else:
        radii = (radii,)
    if isinstance(intensity_rings, (int, float)):
        ints = (intensity_rings,)
    else:
        ints = intensity_rings

    # Get masks for rings
    params = mask_rings(radii=radii, shape=shape, visual_size=visual_size, ppd=ppd, origin=origin)
    shape = params["shape"]

    # Draw rings
    base = image_base(shape=shape, visual_size=visual_size, origin=origin)
    distances = base["radial"]

    img = np.ones(shape) * intensity_background
    ints = [*itertools.islice(itertools.cycle(ints), len(radii))]
    for radius, intensity in zip(reversed(radii), reversed(ints)):
        img[distances < radius] = intensity

    # Assemble output
    params["intensity_rings"] = intensity_rings
    params["radii"] = radii
    params["intensity_background"] = intensity_background
    return {"img": img, **params}


def disc(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    intensity_disc=1.0,
    intensity_background=0.0,
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
        intensity value of background, by default 0.0
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
    stim["radius"] = radius
    stim["intensity_disc"] = intensity_disc
    del stim["radii"], stim["intensity_rings"]
    return stim


def ring(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_ring=1.0,
    intensity_background=0.0,
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
        intensity value of background, by default 0.0
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

    stim = rings(
        radii=radii,
        intensity_rings=[intensity_background, intensity_ring],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        origin=origin,
    )
    stim["ring_mask"] = np.where(stim["ring_mask"] == 2, 1, 0)
    stim["intensity_ring"] = intensity_ring
    return stim


annulus = ring


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
        "radials_disc": disc(**default_params, radius=3),
        "radials_rings": rings(**default_params, radii=(1, 2, 3)),
        "radials_ring": ring(**default_params, radii=(1, 2)),
        "radials_annulus": annulus(**default_params, radii=(1, 2)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
