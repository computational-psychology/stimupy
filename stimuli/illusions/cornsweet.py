import numpy as np


def cornsweet(
    size=(10.0, 10.0),
    ppd=10.0,
    vmax=1.0,
    vmin=0.0,
    vtarget=0.5,
    ramp_width=2.0,
    exponent=2.75,
):
    """
    Create a matrix containing a rectangular Cornsweet edge stimulus.
    The 2D luminance profile of the stimulus is defined as
    Left side:
    v = vtarget + (1 - X / w) ** a * (vmax-vtarget) for the ramp and v = vtarget beyond.
    Right side:
    v = vtarget - (1 - X / w) ** a * (vmin-vtarget) for the ramp and v = vtarget beyond.
    X is the distance to the edge, w is the width of the ramp, a is a variable
    determining the steepness of the ramp, vtarget is the luminance of the targets and
    vmax/vmin are the max/min luminances.

    Parameters
    ----------
    size : tuple of 2 numbers
        size in degrees of visual angle
    ppd : float
        number of pixels in one degree of visual angle
    vmax : float
        maximum luminance value
    vmin : float
        minimum luminance value
    vtarget : float
        luminance value of targets (=plateaus)
    ramp_width : float
        width of luminance ramp in degrees of visual angle
    exponent : float
        determines steepness of ramp (default is 2.75. 1 would be linear)

    Returns
    -------
    Dictionary with img: ndarray (2D) and mask

    References
    ----------
    The formula and default values are adapted from Boyaci, H., Fang, F., Murray,
    S.O., Kersten, D. (2007). Responses to Lightness Variations in Early Human
    Visual Cortex. Current Biology 17, 989-993.
    """

    size = [int(size[0] * ppd), int(size[1] * ppd)]
    ramp_width = int(ramp_width * ppd)
    img = np.ones(size) * vtarget
    mask = np.zeros(size)

    # Create ramp profiles individually for left and right side
    dist = np.arange(size[1] / 2.0)
    dist = dist / ramp_width
    dist[dist > 1.0] = 1.0
    profile1 = (1.0 - dist) ** exponent * (vmax - vtarget)
    profile2 = (1.0 - dist) ** exponent * (vmin - vtarget)
    img[:, : int(size[1] / 2.0)] += profile1[::-1]
    img[:, size[1] // 2 :] += profile2

    # Generate the target mask
    mask[:, 0 : int(size[1] / 2.0 - ramp_width - 1)] = 1
    mask[:, int(size[1] / 2.0 + ramp_width + 1) : :] = 2
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    from stimuli.utils import plot_stim

    stim = cornsweet()
    plot_stim(stim, mask=True)
