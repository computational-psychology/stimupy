import numpy as np


__all__ = [
    "cornsweet",
]

def cornsweet(
    visual_size=None,
    ppd=None,
    ramp_width=None,
    intensity_max=1.0,
    intensity_min=0.0,
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
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    ramp_width : float
        width of luminance ramp in degrees of visual angle
    intensity_max : float
        maximum intensity value
    intensity_min : float
        minimum intensity value
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
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if ramp_width > visual_size[1]/2:
        raise ValueError("ramp_width is too large")

    size = [int(visual_size[0] * ppd), int(visual_size[1] * ppd)]
    ramp_width = int(ramp_width * ppd)
    img = np.ones(size) * intensity_plateau
    mask = np.zeros(size)

    # Create ramp profiles individually for left and right side
    dist = np.arange(size[1] / 2.0)
    dist = dist / ramp_width
    dist[dist > 1.0] = 1.0
    profile1 = (1.0 - dist) ** exponent * (intensity_max - intensity_plateau)
    profile2 = (1.0 - dist) ** exponent * (intensity_min - intensity_plateau)
    img[:, : int(size[1] / 2.0)] += profile1[::-1]
    img[:, size[1] // 2 :] += profile2

    # Generate the target mask
    mask[:, 0 : int(size[1] / 2.0 - ramp_width - 1)] = 1
    mask[:, int(size[1] / 2.0 + ramp_width + 1) : :] = 2

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "intensity_max": intensity_max,
        "intensity_min": intensity_min,
        "intensity_plateau": intensity_plateau,
        "ramp_width": ramp_width,
        "exponent": exponent,
    }

    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stim

    stim = cornsweet(visual_size=10, ppd=10, ramp_width=3)
    plot_stim(stim, stim_name="Cornsweet illusion", mask=True, save=None)
