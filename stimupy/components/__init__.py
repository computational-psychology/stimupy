import itertools

import numpy as np

from stimupy.utils import resolution

__all__ = [
    "image_base",
    "draw_regions",
    "mask_elements",
    "overview",
    "angulars",
    "checkerboards",
    "circulars",
    "edges",
    "frames",
    "gaussians",
    "gratings",
    "lines",
    "shapes",
    "waves"
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
        "rotated" : numpy.ndarray of shape, with rotated distance from origin,
        in deg. visual angle, at each pixel
        "radial" : numpyn.ndarray of shape, with radius from origin,
        in deg. visual angle, at each pixel
        "angular" : numpy.ndarray of shape, with angle relative to 3 o'clock,
        in rad, at each pixel
        "cityblock" : numpy.ndarray of shape, with cityblock distance from origin,
        in deg. visual angle ,at each pixel
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

    # City-block distance (frames)
    cityblock = np.maximum(np.abs(xx), np.abs(yy))

    # Radial distance
    radial = np.sqrt(xx**2 + yy**2)

    # Angular distance
    angular = np.arctan2(xx, yy)
    angular -= np.deg2rad(rotation + 90)
    angular %= 2 * np.pi

    # Rotated
    alpha = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]
    rotated = alpha[0] * xx + alpha[1] * yy

    if origin == "corner":
        rotated = rotated - rotated.min()

    return {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rotation": rotation,
        "x": x,
        "y": y,
        "horizontal": xx,
        "vertical": yy,
        "rotated": rotated,
        "cityblock": cityblock,
        "radial": radial,
        "angular": angular,
    }


def mask_elements(
    orientation,
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
    orientation : any of keys in stimupy.components.image_base()
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
    distances = base[orientation]
    distances = np.round(distances, 8)

    # Mark elements with integer idx-value
    mask = np.zeros(base["shape"], dtype=int)
    for idx, edge in zip(reversed(range(len(edges))), reversed(edges)):
        mask[distances <= edge] = int(idx + 1)

    # Assemble output
    return {
        "mask": mask,
        "edges": edges,
        "orientation": orientation,
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

    # Assign intensities to masked regions
    ints = [*itertools.islice(itertools.cycle(intensities), len(mask_idcs))]
    for frame_idx, intensity in zip(mask_idcs, ints):
        img = np.where(mask == frame_idx, intensity, img)

    return img


from . import (
    angulars,
    checkerboards,
    circulars,
    edges,
    frames,
    gaussians,
    gratings,
    lines,
    shapes,
    waves,
)


def create_overview():
    """
    Create dictionary with examples from all stimulus-components

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """

    p = {
        "visual_size": 10,
        "ppd": 20,
    }

    # fmt: off
    stims = {
        # angulars
        "wedge": angulars.wedge(**p, width=30, radius=3),
        "angular_grating": angulars.grating(**p, n_segments=8),
        "pinwheel": angulars.pinwheel(**p, n_segments=8, radius=3),
        # checkerboards
        "checkerboard_v1": checkerboards.checkerboard(**p, board_shape=(10, 10)),
        "checkerboard_v2": checkerboards.checkerboard(**p, board_shape=(10, 10), rotation=45),
        "checkerboard_v3": checkerboards.checkerboard(**p, frequency=1),
        "checkerboard_v4": checkerboards.checkerboard(**p, frequency=1, rotation=45),
        # circulars
        "disc_and_rings": circulars.disc_and_rings(**p, radii=[1, 2, 3]),
        "disc": circulars.disc(**p, radius=3),
        "ring": circulars.ring(**p, radii=(1, 3)),
        "annulus (=ring)": circulars.annulus(**p, radii=(1, 3)),
        "bessel": circulars.bessel(**p, frequency=1),
        "circular_sine_wave": circulars.sine_wave(**p, frequency=0.5),
        "circular_square_wave": circulars.square_wave(**p, frequency=0.5),
        # edges
        "step_edge": edges.step_edge(**p),
        "gaussian_edge": edges.gaussian_edge(**p, sigma=1.5),
        "cornsweet_edge": edges.cornsweet_edge(**p, ramp_width=3),
        # frames
        "frames": frames.frames(**p, radii=(1, 2, 3)),
        "frames_sine_wave": frames.sine_wave(**p, frequency=0.5),
        "frames_square_wave": frames.square_wave(**p, frequency=0.5),
        # gaussians
        "gaussian": gaussians.gaussian(**p, sigma=(1, 2)),
        # gratings
        "square_wave": gratings.square_wave(**p, frequency=1),
        "square_wave2": gratings.square_wave(**p, frequency=1, rotation=45),
        "sine_wave": gratings.sine_wave(**p, frequency=1),
        "staircase": gratings.staircase(**p, n_bars=8),
        # lines
        "line": lines.line(**p, line_length=3),
        "dipole": lines.dipole(**p, line_length=3, line_gap=0.5),
        "line_circle": lines.circle(**p, radius=3),
        # shapes
        "rectangle": shapes.rectangle(**p, rectangle_size=3),
        "triangle": shapes.triangle(**p, triangle_size=3),
        "cross": shapes.cross(**p, cross_size=3, cross_thickness=0.5),
        "parallelogram": shapes.parallelogram(**p, parallelogram_size=(3, 3, 1)),
        "ellipse": shapes.ellipse(**p, radius=(2, 3)),
        "shape_wedge": shapes.wedge(**p, width=30, radius=3),
        "shape_annulus": shapes.annulus(**p, radii=(1, 3)),
        "shape_ring": shapes.ring(**p, radii=(1, 3)),
        "shape_disc": shapes.disc(**p, radius=3),
    }
    # fmt: on

    return stims


def overview(mask=False, save=None, extent_key="shape"):
    """
    Plot overview with examples from all stimulus-components

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    extent_key : str, optional
        Key to extent which will be used for plotting.
        Default is "shape", using the image size in pixels as extent.

    """
    from stimupy.utils import plot_stimuli

    stims = create_overview()

    # Plotting
    plot_stimuli(stims, mask=mask, save=save, extent_key=extent_key)
