import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img


def checkerboard_contrast_contrast_effect(
    ppd=10,
    n_checks=8,
    check_size=1.0,
    target_length=4,
    padding=(1.0, 1.0, 1.0, 1.0),
    check1=0.0,
    check2=2.0,
    tau=0.5,
    alpha=0.5,
    limit_mask_vals=True,
):
    """
    Contrast-contrast effect on checkerboard with square transparency layer.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_checks : int
        number of checks per board in each direction
    check_size : float
        size of a check in degrees visual angle
    target_length : int
        size of the target in # checks
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    check1 : float
        first check value
    check2 : float
        other check value
    tau : float
        tau of transparency
    alpha : float
        alpha of transparency

    Returns
    -------
    A stimulus object
    """

    check_size_px = degrees_to_pixels(check_size, ppd)

    arr1 = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr1[i, j] = check1 if i % 2 == j % 2 else check2

    mask_arr1 = np.zeros((n_checks, n_checks))

    idx = np.zeros((n_checks, n_checks), dtype=bool)
    tpos = (n_checks - target_length) // 2
    idx[tpos : tpos + target_length, tpos : tpos + target_length] = True
    arr1[idx] = alpha * arr1[idx] + (1 - alpha) * tau
    mask_id = 0
    for i, _ in enumerate(idx):
        for j, el in enumerate(_):
            if el:
                if limit_mask_vals:
                    mask_id = 1
                else:
                    mask_id += 1
                mask_arr1[i, j] = mask_id

    arr2 = arr1.copy()
    arr2[~idx] = tau
    mask_arr2 = mask_arr1.copy()
    mask_arr2[mask_arr2 != 0] += mask_id

    img1 = np.repeat(
        np.repeat(arr1, check_size_px, axis=0), check_size_px, axis=1
    )
    img1 = pad_img(img1, padding, ppd, tau)
    img2 = np.repeat(
        np.repeat(arr2, check_size_px, axis=0), check_size_px, axis=1
    )
    img2 = pad_img(img2, padding, ppd, tau)

    mask1 = np.repeat(
        np.repeat(mask_arr1, check_size_px, axis=0), check_size_px, axis=1
    )
    mask1 = pad_img(mask1, padding, ppd, 0)
    mask2 = np.repeat(
        np.repeat(mask_arr2, check_size_px, axis=0), check_size_px, axis=1
    )
    mask2 = pad_img(mask2, padding, ppd, 0)

    img = np.hstack([img1, img2])
    # Increase target mask values to differentiate from single-stimulus targets:
    mask = np.hstack([mask1, mask2])

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = checkerboard_contrast_contrast_effect()

    plot_stim(stim, stim_name="Checkerboard Contrast-Contrast")
    plt.show()
