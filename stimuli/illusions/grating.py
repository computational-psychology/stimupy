import numpy as np
from stimuli.utils import degrees_to_pixels


def grating_illusion(
    ppd=10,
    n_bars=8,
    target_indices=(2, 4),
    bar_width=1.0,
    bar_height=8.0,
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
    bar_width : float
        width of bar in degrees visual angle
    bar_height : float
        height of bar in degrees visual angle
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

    bar_height_px, bar_width_px = degrees_to_pixels(
        bar_height, ppd
    ), degrees_to_pixels(bar_width, ppd)

    # create array of grating
    img = np.ones([1, n_bars]) * vbar2
    img[:, ::2] = vbar1
    mask = np.zeros([1, n_bars])

    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    for i, idx in enumerate(target_indices):
        img[:, idx] = vtarget
        mask[:, idx] = i + 1

    img = img.repeat(bar_width_px, axis=1).repeat(bar_height_px, axis=0)
    mask = mask.repeat(bar_width_px, axis=1).repeat(bar_height_px, axis=0)

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = grating_illusion()
    plot_stim(stim, stim_name="Grating illusion")
    plt.show()
