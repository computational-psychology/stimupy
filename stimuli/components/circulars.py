import copy
import itertools
import warnings
import numpy as np
import scipy.special as sp

from stimuli.components import image_base, mask_elements, resolve_grating_params
from stimuli.utils import resolution

__all__ = [
    "disc_and_rings",
    "disc",
    "ring",
    "annulus",
    "grating",
    "bessel"
]


def resolve_circular_params(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
):
    """Resolve (if possible) spatial parameters for circular grating, i.e., set of rings

    Circular grating / rings component takes the regular resolution parameters
    (shape, ppd, visual_size). In addition, there has to be an additional specification
    of the number of rings, and their width. This can be done in two ways:
    a ring_width (in degrees) and n_rings, and/or by specifying the spatial frequency
    of a circular grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the rings and their widths.
    Thus, not all 6 parameters have to be specified, as long as the both the resolution
    and the distribution of rings can be resolved.

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

    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """

    # Resolve params
    shape = resolution.validate_shape(shape)
    ppd = resolution.validate_ppd(ppd)
    visual_size = resolution.validate_visual_size(visual_size)

    length = np.array(shape).min() / 2 if None not in shape else None
    ppd_1D = np.array(ppd).min() if None not in ppd else None
    visual_angle = np.array(visual_size).min() / 2 if None not in visual_size else None
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_rings,
        phase_width=ring_width,
        ppd=ppd_1D,
        frequency=frequency,
    )
    
    # Remove too large radii:
    if visual_angle is not None:
        if params["edges"][-1] > visual_angle:
            warnings.warn("Last ring does not perfecetly fit into image")
            params["edges"][-1] = visual_angle

    shape = resolution.validate_shape(params["length"] * 2)
    visual_size = resolution.validate_visual_size(params["visual_angle"] * 2)
    ppd = resolution.validate_ppd(params["ppd"])

    return {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "frequency": params["frequency"],
        "ring_width": params["phase_width"],
        "n_rings": n_rings,
        "radii": params["edges"],
    }


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
    ----------
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
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution;
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        # Check visual_size
        visual_size = resolution.validate_visual_size(visual_size)

    if visual_size is None or visual_size == (None, None):
        # Two axes are None; make image large enought to fit
        visual_size = resolution.validate_visual_size(np.max(radii) * 2)
    elif None in visual_size:
        # one axis is None; make square
        visual_size = [x for x in visual_size if x is not None]
        visual_size = resolution.validate_visual_size(visual_size)

    # Get masks for rings
    params = mask_rings(
        radii=radii,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin
        )
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
    intensity_discs=1.0,
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
    intensity_discs : Number
        intensity value of disc, by default 1.0
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """

    radius = np.array(radius)
    intensity = np.array(intensity_discs)

    if radius.size != 1:
        raise ValueError("Can only pass 1 radius")
    if intensity.size != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = ring(
        radii=np.insert(radius, 0, 0),
        intensity_rings=intensity,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        shape=shape,
        origin=origin,
    )
    stim["ring_mask"] = (stim["ring_mask"]/2).astype(int)
    return stim


def ring(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_rings=1.0,
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
    intensity_rings : Number
        intensity value of ring, by default 1.0
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
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

    if len(radii) != 2:
        raise ValueError("Can only pass exactly 2 radii")
    if len([intensity_rings]) != 1:
        raise ValueError("Can only pass 1 intensity")

    if radii[1] is None:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
        radii[1] = np.max(visual_size) / 2

    stim = disc_and_rings(
        radii=radii,
        intensity_rings=[intensity_background, intensity_rings],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        origin=origin,
    )
    return stim


annulus = ring


def grating(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Draw a circular grating, i.e., set of rings

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
    intensities : Sequence[Number, ...]
        intensity value for each ring, from inside to out, by default (1.0, 0.0).
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each ring (key: "ring_mask"),
        and additional keys containing stimulus parameters
    """
    
    # Resolve sizes
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except:
        pass

    # Resolve grating
    params = resolve_circular_params(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_rings=n_rings,
        ring_width=ring_width,
        )

    # Clean-up params for passing through
    stim_params = copy.deepcopy(params)
    stim_params.pop("n_rings", None)
    stim_params.pop("ring_width", None)
    stim_params.pop("frequency", None)
    if shape is not None:
        stim_params["shape"] = shape
    if visual_size is not None:
        stim_params["visual_size"] = visual_size

    # Draw stim
    stim = disc_and_rings(
        **stim_params,
        intensity_background=intensity_background,
        intensity_rings=intensity_rings,
        origin=origin,
    )

    # Assemble output
    return {**stim, **params}


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
    
    img = base["radial"] * frequency * 2 * np.pi
    img = sp.jv(order, img)
    img = (img - img.min()) / (img.max() - img.min())
    img = img * (intensity_rings[0] - intensity_rings[1]) + intensity_rings[1]

    stim = {
        "img": img,
        "ring_mask": np.zeros(shape).astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "order": order,
        "frequency": frequency,
        "intensity_rings": intensity_rings,
        }
    return stim
    

if __name__ == "__main__":
    from stimuli.utils.plotting import plot_stimuli
    
    p = {
        "visual_size": (10, 20),
        "ppd": 50,
        }
    
    stims = {
        "grating": grating(**p, frequency=2),
        "disc_and_rings": disc_and_rings(**p, radii=(1, 2, 3)),
        "ring": ring(**p, radii=(1, 2)),
        }
    
    plot_stimuli(stims, mask=False)
