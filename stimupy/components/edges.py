import copy

import numpy as np

from stimupy.components import gaussians, image_base

__all__ = [
    "step",
    "gaussian",
    "cornsweet",
]


def step(
    visual_size=None,
    ppd=None,
    shape=None,
    rotation=0.0,
    intensity_edges=(0.0, 1.0),
):
    """Draw a central step edge

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0
    intensity_edges : (float, float)
        intensity values of edges (default: (0., 1.))

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the each lobes (key: "edge_mask"),
        and additional keys containing stimulus parameters
    """
    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="corner",
    )

    img = np.ones(shape) * intensity_edges[0]
    img = np.where(base["oblique"] < base["oblique"].mean(), img, intensity_edges[1])
    mask = np.ones(shape)
    mask = np.where(base["oblique"] < base["oblique"].mean(), mask, 2)

    stim = {
        "img": img,
        "edge_mask": mask.astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "rotation": rotation,
        "intensity_edges": intensity_edges,
    }

    return stim


def gaussian(
    visual_size=None,
    ppd=None,
    shape=None,
    sigma=None,
    rotation=0.0,
    intensity_edges=(0.0, 1.0),
    intensity_background=0.5,
):
    """Draw a central step edge with a Gaussian envelop

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    sigma : float or (float, float)
        sigma of Gaussian in degree visual angle (y, x)
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0
    intensity_edges : (float, float)
        intensity values of edges (default: (0., 1.))
    intensity_background : float
        intensity value of background, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the each lobes (key: "edge_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("gaussian_edge() missing argument 'sigma' which is not 'None'")

    stim = step(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        intensity_edges=intensity_edges,
    )

    window = gaussians.gaussian(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        sigma=sigma,
    )

    img = stim["img"] - intensity_background
    img = img * window["img"] + intensity_background
    stim["img"] = img
    stim["sigma"] = sigma
    stim["intensity_background"] = intensity_background
    stim["gaussian_mask"] = window["gaussian_mask"]
    return stim


def cornsweet(
    visual_size=None,
    ppd=None,
    shape=None,
    ramp_width=None,
    rotation=0.0,
    intensity_edges=(0.0, 1.0),
    intensity_plateau=0.5,
    exponent=2.75,
):
    """Draw rectangular Cornsweet edge stimulus.
    The 2D luminance profile of the stimulus is defined as
    Left side:
    v = vtarget + (1 - X / w) ** a * (intensity_max-vtarget) for the ramp and v = vtarget beyond.
    Right side:
    v = vtarget - (1 - X / w) ** a * (intensity_min-vtarget) for the ramp and v = vtarget beyond.
    X is the distance to the edge, w is the width of the ramp, a is a variable
    determining the steepness of the ramp, vtarget is the luminance of the targets and
    intensity_max/intensity_min are the max/min luminances.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    ramp_width : float
        width of luminance ramp in degrees of visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0
    intensity_edges : (float, float)
        intensity of edges
    intensity_plateau : float
        intensity value of plateau
    exponent : float
        determines steepness of ramp (default is 2.75. 1 would be linear)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the each lobes (key: "edge_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Boyaci, H., Fang, F., Murray, S.O., Kersten, D. (2007).
        Responses to lightness variations in early human visual cortex.
        Current Biology 17, 989-993.
        https://doi.org/10.1016/j.cub.2007.05.005
    Cornsweet, T. (1970).
        Visual perception. Academic press.
        https://doi.org/10.1016/B978-0-12-189750-5.X5001-5
    """
    if ramp_width is None:
        raise ValueError("cornsweet_edge() missing argument 'ramp_width' which is not 'None'")

    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="mean",
    )

    if ramp_width > max(base["visual_size"]) / 2:
        raise ValueError("ramp_width is too large")

    dist = np.round(base["oblique"] / ramp_width, 6)
    d1 = copy.deepcopy(dist)
    d2 = copy.deepcopy(dist) * (-1)
    d1[d1 < 0] = -1
    d1[d1 > 1] = 1
    d2[d2 < 0] = -1
    d2[d2 > 1] = 1

    # Create ramp profiles individually for left and right side
    profile1 = (1.0 - d1) ** exponent * (
        intensity_edges[0] - intensity_plateau
    ) + intensity_plateau
    profile2 = (1.0 - d2) ** exponent * (
        intensity_edges[1] - intensity_plateau
    ) + intensity_plateau
    img = np.where(d1 == -1, 0, profile1) + np.where(d2 == -1, 0, profile2)
    mask = np.where(d1 == -1, 0, 2) + np.where(d2 == -1, 0, 1)
    mask[mask == 3] = 1

    stim = {
        "img": img,
        "edge_mask": mask.astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "intensity_edges": intensity_edges,
        "intensity_plateau": intensity_plateau,
        "ramp_width": ramp_width,
        "rotation": rotation,
        "exponent": exponent,
        "d1": d1,
        "d2": d2,
    }

    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 10,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "edges_step": step(**default_params),
        "edges_gaussian": gaussian(**default_params, sigma=3),
        "edges_cornsweet": cornsweet(**default_params, ramp_width=3),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
