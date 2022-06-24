import numpy as np
from scipy.ndimage import gaussian_filter
from stimuli.illusions.square_wave import square_wave
from stimuli.utils import degrees_to_pixels


###################################
#        Grating induction        #
###################################
def grating_illusion(
    shape=(10, 10),
    ppd=40,
    frequency=0.5,
    target_height=0.5,
    blur=None,
    high=1.0,
    low=0.0,
    target=0.5,
    start="low",
    period="ignore",
):
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

    Returns
    -------
    A stimulus object
    """

    if blur is None:
        blur = shape[0] / 2

    height_px, width_px = degrees_to_pixels(shape, ppd)
    target_height_px = degrees_to_pixels(target_height, ppd)

    img, pixels_per_cycle = square_wave(
        shape, ppd, frequency, high, low, period, start
    )

    target_start = height_px // 2 - target_height_px // 2
    target_end = target_start + target_height_px

    mask = np.zeros((height_px, width_px))
    mask[target_start:target_end, :] = (
        img[target_start:target_end, :] - low
    ) / (high - low) + 1

    img = gaussian_filter(img, blur)
    img[target_start:target_end, :] = target

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = grating_illusion()
    plot_stim(
        stim,
        stim_name="Grating (/ counterphase lightness) induction",
    )
    plt.show()
