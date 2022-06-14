import numpy as np
from stimuli.Stimulus import Stimulus


def cornsweet(
    size=(10, 10),
    ppd=10,
    contrast=0.5,
    ramp_width=2,
    exponent=2.75,
    mean_lum=0.5,
):
    # TODO: the parameters aren't analogous to the other stimuli
    """
    Create a matrix containing a rectangular Cornsweet edge stimulus.
    The 2D luminance profile of the stimulus is defined as
    L = L_mean +/- (1 - X / w) ** a * L_mean * C/2 for the ramp and
    L = L_mean for the area beyond the ramp.
    X is the distance to the edge, w is the width of the ramp, a is a variable
    determining the steepness of the ramp, and C is the contrast at the edge,
    defined as C = (L_max-L_min) / L_mean.

    Parameters
    ----------
    size : tuple of 2 numbers
           the size of the matrix in degrees of visual angle
    ppd : number
          the number of pixels in one degree of visual angle
    contrast : float, in [0,1]
               the contrast at the Cornsweet edge, defined as Michelson contrast
               (max_luminance - min_luminance) / (max_luminance + min_luminance)
    ramp_width : number (optional)
                 the width of the luminance ramp in degrees of visual angle.
                 Default is 3.
    exponent : number (optional)
               Determines the steepness of the ramp. Default is 2.75. An
               exponent value of 0 leads to a stimulus with uniform flanks.
    mean_lum : number
               The mean luminance of the stimulus, i.e. the value outside of
               the ramp area.

    Returns
    -------
    Dictionary with img: ndarray (2D) and empty mask

    References
    ----------
    The formula and default values are taken from Boyaci, H., Fang, F., Murray,
    S.O., Kersten, D. (2007). Responses to Lightness Variations in Early Human
    Visual Cortex. Current Biology 17, 989-993.
    """
    size = [int(size[0] * ppd), int(size[1] * ppd)]
    img = np.ones(size) * mean_lum
    dist = np.arange(size[1] / 2.0)
    dist = dist / (ramp_width * ppd)
    dist[dist > 1.0] = 1.0
    profile = (1.0 - dist) ** exponent * mean_lum * contrast
    img[:, : int(np.ceil(size[1] / 2.0))] += profile[::-1]
    img[:, size[1] // 2 :] -= profile
    mask = None
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = cornsweet()
    plt.imshow(stim, cmap="gray")
    plt.show()
