import numpy as np

def cornsweet(size, ppd, contrast, ramp_width=3, exponent=2.75,
              mean_lum=.5):
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
               the contrast at the Cornsweet edge, defined as
               (max_luminance - min_luminance) / mean_luminance
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
    stim : ndarray (2D)

    References
    ----------
    The formula and default values are taken from Boyaci, H., Fang, F., Murray,
    S.O., Kersten, D. (2007). Responses to Lightness Variations in Early Human
    Visual Cortex. Current Biology 17, 989-993.
    """
    # compute size as the closest even number of pixel corresponding to the
    # size given in degrees of visual angle.
    size = np.rint(np.tan(np.radians(np.array(size) / 2.)) /
                   np.tan(np.radians(.5)) * ppd / 2) * 2
    size = size.astype('int')
    stim = np.ones(size) * mean_lum
    dist = np.arange(size[1] / 2)
    dist = np.degrees(np.arctan(dist / 2. / ppd * 2 * np.tan(np.radians(.5)))) * 2
    dist /= ramp_width
    dist[dist > 1] = 1
    profile = (1 - dist) ** exponent * mean_lum * contrast / 2
    stim[:, :size[1] // 2] += profile[::-1]
    stim[:, size[1] // 2:] -= profile
    return stim