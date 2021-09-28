import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus


def ring_pattern(
    ppd=10,
    n_rings=8,
    target_pos_l=4,
    target_pos_r=3,
    ring_width=0.5,
    padding=(
        1.0,
        1.0,
        1.0,
        1.0,
    ),
    back=0.0,
    rings=1.0,
    target=0.5,
    invert_rings=False,
    double=True,
):
    """
    Ring Pattern White's-like illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_rings : int   
        the number of rings
    target_pos_l : int
        the "index" of the target ring on the left half
    target_pos_r : int
        the "index" of the target ring on the right half
    ring_width : float
        width per ring in degrees visual angle 
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    back : float
        value for background
    rings : float
        value for grid cells
    target : float
        value for target
    invert_rings : bool 
        inverts ordering of rings and background
    double : bool
        whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    A stimulus object
    """

    ring_width_px = degrees_to_pixels(ring_width, ppd)

    # calculate Minkowski-p=inf distances from centre
    x = np.arange(0, n_rings)
    x = np.hstack([np.flip(x), x])
    radii = np.maximum(np.abs(x[np.newaxis]), np.abs(x[:, np.newaxis]))

    # build array representing rings
    arr = np.ones((n_rings*2, n_rings*2)) * back
    arr[radii % 2 == (0 if invert_rings else 1)] = rings
    arr[radii == target_pos_l] = target

    mask_arr = np.zeros((n_rings*2, n_rings*2))
    mask_arr[radii == target_pos_l] = 1


    # build image from array
    img = np.repeat(np.repeat(arr, ring_width_px, axis=0), ring_width_px, axis=1)
    mask = np.repeat(np.repeat(mask_arr, ring_width_px, axis=0), ring_width_px, axis=1)

    y_c, x_c = img.shape
    y_c //=2
    x_c //=2

    row_c = img[y_c, :]
    row_c_mask = mask[y_c, :]
    img = np.insert(img, y_c, row_c, axis=0)
    mask = np.insert(mask, y_c, row_c_mask, axis=0)

    col_c = img[:, x_c]
    col_c_mask = mask[:, x_c]
    img = np.insert(img, x_c, col_c, axis=1)
    mask = np.insert(mask, x_c, col_c_mask, axis=1)

    img = pad_img(img, padding, ppd, back)
    mask = pad_img(mask, padding, ppd, 0)

    # create right half of stimulus
    if double:
        stim2 = ring_pattern(
            ppd=ppd,
            n_rings=n_rings,
            target_pos_l=target_pos_r,
            target_pos_r=0,
            ring_width=ring_width,
            padding=padding,
            back=back,
            rings=rings,
            target=target,
            invert_rings=invert_rings,
            double=False,
        )
        img = np.hstack([img, stim2.img])
        mask = np.hstack([mask, stim2.target_mask])

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    img = ring_pattern(
        ppd=10,
        n_rings=8,
        target_pos_l=4,
        target_pos_r=3,
        ring_width=0.5,
        padding=(0.9, 1.0, 0.9, 1.0),
        back=1.0,
        rings=9.0,
        target=5.0,
        invert_rings=False,
        double=True,
    )
    return img


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = ring_pattern()
    plot_stim(stim, mask=True)
