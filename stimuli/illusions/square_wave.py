import numpy as np
from stimuli.utils.utils import degrees_to_pixels


def square_wave(shape, ppd, contrast, frequency, mean_lum=.5, period='ignore',
                start='high'):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    shape : tuple of 2 numbers
            The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : number
          the number of pixels in one degree of visual angle
    contrast : float, in [0,1]
               the contrast of the grating, defined as
               (max_luminance - min_luminance) / mean_luminance
    frequency : number
                the spatial frequency of the wave in cycles per degree
    mean_lum : number
               the mean luminance of the grating, i.e. (max_lum + min_lum) / 2.
               The average luminance of the actual stimulus can differ slightly
               from this value if the stimulus is not an integer of cycles big.
    period : string in ['ignore', 'full', 'half'] (optional)
             specifies if the period of the wave is taken into account when
             determining exact stimulus dimensions.
             'ignore' simply converts degrees to pixels
             'full' rounds down to guarantee a full period
             'half' adds a half period to the size 'full' would yield.
             Default is 'ignore'.
    start : string in ['high', 'low'] (optional)
            specifies if the wave starts with a high or low value. Default is
            'high'.

    Returns
    -------
    stim : ndarray (2D)
           the square wave stimulus
    """
    if period not in ['ignore', 'full', 'half']:
        raise TypeError('size not understood: %s' % period)
    if start not in ['high', 'low']:
        raise TypeError('start value not understood: %s' % start)
    if frequency > ppd / 2:
        raise ValueError('The frequency is limited to 1/2 cycle per pixel.')

    shape = degrees_to_pixels(np.array(shape), ppd).astype(int)
    pixels_per_cycle = int(degrees_to_pixels(1. / frequency / 2, ppd) + .5) * 2

    if period is 'full':
        shape[1] = (shape[1] // pixels_per_cycle) * pixels_per_cycle
    elif period is 'half':
        shape[1] = (shape[1] // pixels_per_cycle) * pixels_per_cycle + \
                   pixels_per_cycle / 2
    diff = type(mean_lum)(contrast * mean_lum)
    high = mean_lum + diff
    low = mean_lum - diff
    stim = np.ones(shape) * (low if start is 'high' else high)
    index = [i + j for i in range(pixels_per_cycle // 2)
             for j in range(0, shape[1], pixels_per_cycle)
             if i + j < shape[1]]
    stim[:, index] = low if start is 'low' else high
    return stim
