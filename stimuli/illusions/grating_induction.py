import numpy as np
from scipy.ndimage import gaussian_filter

from stimuli.components import square_wave
from stimuli.utils import degrees_to_pixels


###################################
#        Grating induction        #
###################################
def grating_illusion(
    visual_size=(10, 10),
    ppd=40,
    grating_frequency=0.5,
    target_height=0.5,
    blur=5,
    intensity_bars=(0., 1.),
    intensity_target=0.5,
    period="ignore",
):
    """
    Grating induction illusions

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        frequency of the grid in cycles per degree visual angle
    target_height : float
        height of the target in degrees visual angle
    blur : float
        amount of blur to apply
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of targets
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    height, width = degrees_to_pixels(visual_size, ppd)
    theight = degrees_to_pixels(target_height, ppd)

    img = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=grating_frequency,
        intensity_bars=intensity_bars,
        period=period)["img"]

    tstart = height // 2 - theight // 2
    tend = tstart + theight

    low = np.minimum(intensity_bars[0], intensity_bars[1])
    high = np.maximum(intensity_bars[0], intensity_bars[1])
    mask = np.zeros((height, width))
    mask[tstart:tend, :] = (img[tstart:tend, :] - low) / (high - low) + 1

    img = gaussian_filter(img, blur)
    img[tstart:tend, :] = intensity_target
    
    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "grating_frequency": grating_frequency,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_height": target_height,
        "blur": blur,
        "period": period,
    }

    return {"img": img, "mask": mask.astype(int), **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stim

    stim = grating_illusion()
    plot_stim(
        stim,
        stim_name="Grating (/ counterphase lightness) induction",
    )
    plt.show()
