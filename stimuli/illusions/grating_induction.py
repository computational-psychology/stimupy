import numpy as np
from scipy.ndimage.filters import gaussian_filter
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus
from stimuli import illusions

###################################
#        Grating induction        #
###################################
def grating_illusion(shape=(10,10), ppd=40, frequency=0.5, target_height=0.5, blur=None, high=1., low=0., target=.5, start='low', period='ignore', padding=(2,2,2,2)):
    """
    Grating induction illusions

    Parameters
    ----------
    shape : (float, float)
        Shape of the illusion in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    target_height : float
        height of the target in degrees visual angle
    blur : float
        amount of blur to apply
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    start : string in ['low','high']
        whether to start with a bright or a low stripes
    period : string in ['ignore', 'full', 'half'] 
        see square_wave.py for details about this
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle

    Returns
    -------
    A stimulus object
    """

    if blur == None:
        blur = shape[0]/2

    height_px, width_px = degrees_to_pixels(shape, ppd)
    target_height_px = degrees_to_pixels(target_height, ppd)

    img, pixels_per_cycle = illusions.square_wave(shape, ppd, frequency, high, low, period, start)
    img = gaussian_filter(img, blur)
    mask = np.zeros((height_px, width_px))

    target_start = height_px//2 - target_height_px//2
    target_end = target_start + target_height_px
    img[target_start:target_end, :] = target
    mask[target_start:target_end, :] = 1

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim

def RHS2007_grating_induction():
    total_height, total_width, ppd = (32,)*3
    n_cycles = 4
    height, width = 12, 16
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    img = illusions.grating_induction.grating_illusion(shape=(height, width), ppd=ppd, frequency=frequency, target_height=1, blur=10, start='high', padding=padding)
    return img


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = grating_illusion()
    plot_stim(stim, mask=True)
