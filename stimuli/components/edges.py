import numpy as np

from stimuli.components import gaussians
from stimuli.components import image_base
from stimuli.utils import resolution

__all__ = [
    "step_edge",
    "gaussian_edge",
    "cornsweet_edge",
]


def step_edge(
    visual_size=None,
    ppd=None,
    shape=None,
    rotation=0.,
    intensity_edges=(0.0, 1.0),
):
    # Resolve resolutions
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin=None,
        )
    
    img = np.ones(shape) * intensity_edges[0]
    img = np.where(base["rotated"] < base["rotated"].mean(), img, intensity_edges[1])
    mask = np.ones(shape)
    mask = np.where(base["rotated"] < base["rotated"].mean(), mask, 2)
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "rotation": rotation,
        "intensity_edges": intensity_edges,
        }
    
    return stim


def gaussian_edge(
    visual_size=None,
    ppd=None,
    shape=None,
    sigma=None,
    rotation=0.,
    intensity_edges=(0.0, 1.0),
    intensity_background=0.5,
):
    stim = step_edge(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        intensity_edges=(0.0, 1.0),
        )
    
    window = gaussians.gaussian(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        sigma=sigma,
        )
    
    img = stim["img"] - intensity_background
    img = img * window["img"] + intensity_background
    mask = stim["mask"] * window["img"]
    stim["img"] = img
    stim["mask"] = mask.astype(int)
    stim["sigma"] = sigma
    stim["intensity_background"] = intensity_background
    return stim


def cornsweet_edge(
    visual_size=None,
    ppd=None,
    shape=None,
    ramp_width=None,
    intensity_edges=(0.0, 1.0),
    intensity_plateau=0.5,
    exponent=2.75,
):
    """
    Create a matrix containing a rectangular Cornsweet edge stimulus.
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
    intensity_edges : (float, float)
        intensity of edges
    intensity_plateau : float
        intensity value of plateau
    exponent : float
        determines steepness of ramp (default is 2.75. 1 would be linear)

    Returns
    -------
    Dictionary with img: ndarray (2D) and mask

    References
    ----------
    Boyaci, H., Fang, F., Murray, S.O., Kersten, D. (2007). Responses to lightness
        variations in early human visual cortex. Current Biology 17, 989-993.
        https://doi.org/10.1016/j.cub.2007.05.005
    Cornsweet, T. (1970). Visual perception. Academic press.
        https://doi.org/10.1016/B978-0-12-189750-5.X5001-5
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)    
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")
    if ramp_width > visual_size[1]/2:
        raise ValueError("ramp_width is too large")

    ramp_width_px = int(ramp_width * ppd[1])
    img = np.ones(shape) * intensity_plateau
    mask = np.zeros(shape)

    # Create ramp profiles individually for left and right side
    dist = np.arange(shape[1] / 2.0)
    dist = dist / ramp_width_px
    dist[dist > 1.0] = 1.0
    profile1 = (1.0 - dist) ** exponent * (intensity_edges[0] - intensity_plateau)
    profile2 = (1.0 - dist) ** exponent * (intensity_edges[1] - intensity_plateau)
    img[:, : int(shape[1] / 2.0)] += profile1[::-1]
    img[:, shape[1] // 2 :] += profile2

    # Generate the edge mask
    mask[:, int(shape[1] / 2.0 - ramp_width_px - 1) : int(shape[1] / 2.0)] = 1
    mask[:, int(shape[1] / 2.0) : int(shape[1] / 2.0 + ramp_width_px + 1)] = 2

    stim = {
        "img": img,
        "edge_mask": mask.astype(int),
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "intensity_edges": intensity_edges,
        "intensity_plateau": intensity_plateau,
        "ramp_width": ramp_width,
        "exponent": exponent,
    }

    return stim