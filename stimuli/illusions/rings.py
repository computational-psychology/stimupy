import numpy as np
from stimuli.utils import degrees_to_pixels, plot_stim


def ring_stimulus(
    ppd=10,
    n_rings=8,
    target_idx=4,
    ring_width=0.5,
    vring1=1.0,
    vring2=0.0,
    vtarget=0.5
):
    """
    Ring Pattern stimulus

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_rings : int
        the number of rings
    target_idx : int or tuple or list
        indices of target ring(s)
    ring_width : float
        width per ring in degrees visual angle
    vring1 : float
        value for even rings
    vring2 : float
        value for odd rings
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    ring_width_px = degrees_to_pixels(ring_width, ppd)

    # calculate Minkowski-p=inf distances from centre
    x = np.arange(0, n_rings)
    x = np.hstack([np.flip(x), x])
    radii = np.maximum(np.abs(x[np.newaxis]), np.abs(x[:, np.newaxis]))

    # build array representing rings
    arr = np.ones((n_rings * 2, n_rings * 2)) * vring1
    mask_arr = np.zeros((n_rings * 2, n_rings * 2))
    arr[radii % 2 == 1] = vring2
    if isinstance(target_idx, int):
        target_idx = [target_idx]
    elif isinstance(target_idx, tuple):
        target_idx = list(target_idx)
    target_idx = list(np.array(target_idx))
    for idx in target_idx:
        arr[radii == idx] = vtarget
        mask_arr[radii == idx] = 1

    # build image from array
    img = np.repeat(
        np.repeat(arr, ring_width_px, axis=0), ring_width_px, axis=1
    )
    mask = np.repeat(
        np.repeat(mask_arr, ring_width_px, axis=0), ring_width_px, axis=1
    )

    y_c, x_c = img.shape
    y_c //= 2
    x_c //= 2

    row_c = img[y_c, :]
    row_c_mask = mask[y_c, :]
    img = np.insert(img, y_c, row_c, axis=0)
    mask = np.insert(mask, y_c, row_c_mask, axis=0)

    col_c = img[:, x_c]
    col_c_mask = mask[:, x_c]
    img = np.insert(img, x_c, col_c, axis=1)
    mask = np.insert(mask, x_c, col_c_mask, axis=1)
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = ring_stimulus()
    plot_stim(stim, mask=True)
