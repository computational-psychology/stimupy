import numpy as np
from stimuli.utils.utils import degrees_to_pixels


def square_wave(shape=(10,10), ppd=10, frequency=1, high=1.0, low=0.0, period='ignore',
                start='high'):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int 
        pixels per degree (visual angle)
    high : float
        value of the bright pixels
    low : float
        value of the dark pixels
    frequency : float
        the spatial frequency of the wave in cycles per degree
    period : string in ['ignore', 'full', 'half'] 
        specifies if the period of the wave is taken into account when determining exact stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.
    start : string in ['high', 'low'] 
        specifies if the wave starts with a high or low value. Default is 'high'.

    Returns
    -------
    (2D ndarray, pixels_per_cycle)
    """


    if period not in ['ignore', 'full', 'half']:
        raise TypeError('size not understood: %s' % period)
    if start not in ['high', 'low']:
        raise TypeError('start value not understood: %s' % start)
    if frequency > ppd / 2:
        raise ValueError('The frequency is limited to 1/2 cycle per pixel.')

    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1. / (frequency*2) , ppd) * 2

    if period is 'full':
        width = (width // pixels_per_cycle) * pixels_per_cycle
    elif period is 'half':
        width = (height // pixels_per_cycle) * pixels_per_cycle + pixels_per_cycle / 2

    stim = np.ones((height, width)) * (low if start is 'high' else high)

    index = [i + j for i in range(pixels_per_cycle // 2)
             for j in range(0, width, pixels_per_cycle)
             if i + j < width]
    stim[:, index] = low if start is 'low' else high
    return (stim, pixels_per_cycle)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.imshow(square_wave()[0], cmap='gray')
    plt.show()
