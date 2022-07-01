import numpy as np
from stimuli.utils import degrees_to_pixels
from stimuli.components import square_wave_grating


def grating_illusion(
    ppd=10,
    n_bars=8,
    target_indices=(2, 4),
    bar_shape=(8, 1.),
    vbar1=0.0,
    vbar2=1.0,
    vtarget=0.5
):
    """
    Grating illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    target_indices : tuple
        tuple with bar target indices from left to right
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    vbar1 : float
        value for bar 1
    vbar2 : float
        value for bar 2
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    bar_width_px = degrees_to_pixels(bar_shape[1], ppd)
    img = square_wave_grating(ppd, n_bars, bar_shape, vbar1, vbar2)
    mask = np.zeros(img.shape)

    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    for i, idx in enumerate(target_indices):
        img[:, idx*bar_width_px:(idx+1)*bar_width_px] = vtarget
        mask[:, idx*bar_width_px:(idx+1)*bar_width_px] = i + 1
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = grating_illusion()
    plot_stim(stim, stim_name="Grating illusion")
    plt.show()
