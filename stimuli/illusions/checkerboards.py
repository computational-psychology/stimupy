import numpy as np
from stimuli.utils import degrees_to_pixels
from stimuli.components import checkerboard


def contrast(
    ppd=30,
    board_shape=(8, 8),
    check_size=1.0,
    target_indices=((3, 2), (5, 5)),
    extend_targets=False,
    vcheck1=0.0,
    vcheck2=1.0,
    vtarget=0.5,
):
    """
    Checkerboard Contrast

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    board shape : (int, int)
        number of checks per board in y, x direction
    check_size : float
        size of a check in degrees visual angle
    targets_indices : tuple of (int, int)
        tuple with check-indices (row, col)
    extend_targets : bool
        cross targets instead of single-check targets
    vcheck1 : float
        first check value
    vcheck2 : float
        other check value
    vtarget: float
        target value

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    check_size_px = degrees_to_pixels(check_size, ppd)
    nchecks_height, nchecks_width = board_shape

    img = checkerboard(ppd, board_shape, check_size, vcheck1, vcheck2)
    mask = np.zeros(img.shape)

    for i, coords in enumerate(target_indices):
        ypos = int(coords[0]*check_size_px)
        xpos = int(coords[1]*check_size_px)
        img[ypos:ypos+check_size_px, xpos:xpos+check_size_px] = vtarget
        mask[ypos:ypos+check_size_px, xpos:xpos+check_size_px] = i + 1

    if extend_targets:
        for i, coords in enumerate(target_indices):
            for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ypos = int(coords[0]*check_size_px + idx[0]*check_size_px)
                xpos = int(coords[1]*check_size_px + idx[1]*check_size_px)
                img[ypos:ypos+check_size_px, xpos:xpos+check_size_px] = vtarget
                mask[ypos:ypos+check_size_px, xpos:xpos+check_size_px] = i + 1
    return {"img": img, "mask": mask}


def contrast_contrast(
    ppd=10,
    board_shape=(4, 6),
    check_size=1.0,
    target_shape=(2, 3),
    vcheck1=0.0,
    vcheck2=1.0,
    tau=0.5,
    alpha=0.2,
):
    """
    Contrast-contrast effect on checkerboard with square transparency layer.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    board shape : (int, int)
        number of checks in y, x direction
    check_size : float
        size of a check in degrees visual angle
    targets_shape : (int, int)
        number of checks with transparecny in y, x direction
    vcheck1 : float
        first check value
    vcheck2 : float
        other check value
    tau : float
        tau of transparency (i.e. value of transparent medium)
    alpha : float
        alpha of transparency (i.e. how transparant the medium is)

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    check_size_px = degrees_to_pixels(check_size, ppd)
    nchecks_height, nchecks_width = board_shape

    img = checkerboard(ppd, board_shape, check_size, vcheck1, vcheck2)
    mask = np.zeros(img.shape)

    idx = np.zeros(img.shape, dtype=bool)
    tposy = (img.shape[0] - target_shape[0]*check_size_px) // 2
    tposx = (img.shape[1] - target_shape[1]*check_size_px) // 2
    idx[tposy:tposy+target_shape[0]*check_size_px, tposx:tposx+target_shape[1]*check_size_px] = True
    img[idx] = alpha * img[idx] + (1 - alpha) * tau
    mask[idx] = 1
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Checkerboard contrast": contrast(),
        "Checkerboard contrast contrast": contrast_contrast(),
    }
    ax = plot_stimuli(stims, mask=False)
    plt.show()
