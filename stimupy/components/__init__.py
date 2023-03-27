import itertools

import numpy as np

from stimupy.components import *  # angulars, edges, frames, gaussians, lines, radials, shapes, waves
from stimupy.utils import resolution

__all__ = [
    "overview",
    "plot_overview",
    "image_base",
    "draw_regions",
    "mask_elements",
    "overview",
    "angulars",
    "radials",
    "edges",
    "frames",
    "gaussians",
    "lines",
    "shapes",
    "waves",
]


def image_base(visual_size=None, shape=None, ppd=None, rotation=0.0, origin="mean"):
    """Create coordinate-arrays to serve as image base for drawing

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rotation : float, optional
        rotation (in degrees) counterclockwise from 3 o'clock, by default 0.0
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with keys:
        "visual_size", "ppd" : resolved from input arguments,
        "x", "y" : single axes
        "horizontal", "vertical" : numpy.ndarray of shape, with distance from origin,
        in deg. visual angle, at each pixel
        "oblique" : numpy.ndarray of shape, with oblique distance from origin,
        in deg. visual angle, at each pixel
        "radial" : numpyn.ndarray of shape, with radius from origin,
        in deg. visual angle, at each pixel
        "angular" : numpy.ndarray of shape, with angle relative to 3 o'clock,
        in rad, at each pixel
        "rectilinear" : numpy.ndarray of shape, with rectilinear/cityblock/Manhattan distance from origin,
        in deg. visual angle, at each pixel
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Set origin
    if origin == "corner":
        x = np.linspace(0, visual_size.width, shape.width)
        y = np.linspace(0, visual_size.height, shape.height)
    elif origin == "mean":
        vrange = (visual_size.height / 2, visual_size.width / 2)
        x = np.linspace(-vrange[1], vrange[1], shape.width)
        y = np.linspace(-vrange[0], vrange[0], shape.height)
    elif origin == "center":
        vrange = (visual_size.height / 2, visual_size.width / 2)
        x = np.linspace(-vrange[1], vrange[1], shape.width, endpoint=False)
        y = np.linspace(-vrange[0], vrange[0], shape.height, endpoint=False)
    else:
        raise ValueError("origin can only be be corner, mean or center")

    # Linear distance image bases
    xx, yy = np.meshgrid(x, y)

    # Rectilinear distance (frames)
    rectilinear = np.maximum(np.abs(xx), np.abs(yy))

    # Radial distance
    radial = np.sqrt(xx**2 + yy**2)

    # Angular distance
    angular = np.arctan2(xx, yy)
    angular -= np.deg2rad(rotation + 90)
    angular %= 2 * np.pi

    # Oblique
    alpha = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]
    oblique = alpha[0] * xx + alpha[1] * yy

    if origin == "corner":
        oblique = oblique - oblique.min()

    return {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rotation": rotation,
        "x": x,
        "y": y,
        "horizontal": xx,
        "vertical": yy,
        "oblique": oblique,
        "rectilinear": rectilinear,
        "radial": radial,
        "angular": angular,
    }


def mask_elements(
    distance_metric,
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    rotation=0.0,
    origin=None,
):
    """Generate mask with integer indices for consecutive elements

    Parameters
    ----------
    distance_metric : any of keys in stimupy.components.image_base()
        which dimension to mask over
    edges : Sequence[Number]
        upper-limit of each consecutive elements
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    origin : Sequence[Number, Number], Number, or None (default)
        placement of origin [height,width from topleft] to calculate distances from.
        If None, set to center of visual_size

    Returns
    -------
    dict[str, Any]
        mask with integer index for each angular segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Set up coordinates
    base = image_base(
        shape=shape, visual_size=visual_size, ppd=ppd, rotation=rotation, origin=origin
    )
    distances = base[distance_metric]
    distances = np.round(distances, 8)
    
    if isinstance(edges, (int, float)):
        edges = (edges,)

    # Mark elements with integer idx-value
    mask = np.zeros(base["shape"], dtype=int)
    for idx, edge in zip(reversed(range(len(edges))), reversed(edges)):
        mask[distances <= edge] = int(idx + 1)

    # Assemble output
    return {
        "mask": mask,
        "edges": edges,
        "distance_metric": distance_metric,
        "rotation": base["rotation"],
        "shape": base["shape"],
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "distances": distances,
        "origin": origin,
    }


def draw_regions(mask, intensities, intensity_background=0.5):
    """Draw image with intensities for components in mask

    Parameters
    ----------
    mask : numpy.ndarray
        image-array with integer-indices for each region to draw
    intensities : Sequence[float, ...]
        intensity value for each masked region.
        Can specify as many intensities as number of masked regions;
        If fewer intensities are passed than masked regions, cycles through intensities
    intensity_background : float, optional
        intensity value of background, by default 0.5

    Returns
    -------
    numpy.ndarray
        image-array, same shape as mask, with intensity assigned to each masked region
    """

    # Create background
    img = np.ones(mask.shape) * intensity_background

    # Get mask indices
    mask_idcs = np.unique(mask[mask > 0])
    
    if isinstance(intensities, (float, int)):
        intensities = (intensities,)

    # Assign intensities to masked regions
    ints = [*itertools.islice(itertools.cycle(intensities), len(mask_idcs))]
    for frame_idx, intensity in zip(mask_idcs, ints):
        img = np.where(mask == frame_idx, intensity, img)

    return img


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    stimuli = {}
    for stimmodule_name in __all__:
        if stimmodule_name in [
            "overview",
            "plot_overview",
            "draw_regions",
            "image_base",
            "mask_elements",
        ]:
            continue

        print(f"Generating stimuli from {stimmodule_name}")
        # Get a reference to the actual module
        stimmodule = globals()[stimmodule_name]
        try:
            stims = stimmodule.overview()

            # Accumulate
            stimuli.update(stims)
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stimuli


def plot_overview(mask=False, save=None, units="deg"):
    """Plot overview of examples in this module (and submodules)

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim

    """
    from stimupy.utils import plot_stimuli

    stims = overview(skip=True)
    plot_stimuli(stims, mask=mask, units=units, save=save)


if __name__ == "__main__":
    plot_overview()
