import numpy as np
from stimuli.utils import degrees_to_pixels, plot_stim


def checkerboard_contrast(
    ppd=10,
    board_shape=(8, 8),
    check_size=1.0,
    targets_coords=((3, 2), (5, 5)),
    extend_targets=False,
    check1=0.0,
    check2=1.0,
    target=0.5,
):
    # TODO: targets_coords used to be coord1 and coords2, now multiple targets are allowed. This should be changed in all places calling this function
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
    target1_coords : (int, int)
        check-coordinates of target check 1 (row, col)
    target2_coords : (int, int)
        check-coordinates of target check 2 (row, col)
    extend_targets : bool
        cross targets instead of single-check targets
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    check1 : float
        first check value
    check2 : float
        other check value
    target: float
        target value

    Returns
    -------
    A stimulus object
    """

    check_size_px = degrees_to_pixels(check_size, ppd)
    height_checks, width_checks = board_shape

    arr = np.ndarray((height_checks, width_checks))
    mask = np.zeros((height_checks, width_checks))

    for i, j in np.ndindex((height_checks, width_checks)):
        arr[i, j] = check1 if i % 2 == j % 2 else check2

    for i, coords in enumerate(targets_coords):
        arr[coords] = target
        mask[coords] = i + 1

    if extend_targets:
        for i, coords in enumerate(targets_coords):
            for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                arr[coords[0] + idx[0], coords[1] + idx[1]] = target
                mask[coords[0] + idx[0], coords[1] + idx[1]] = i + 1

    img = np.repeat(
        np.repeat(arr, check_size_px, axis=0), check_size_px, axis=1
    )
    mask = np.repeat(
        np.repeat(mask, check_size_px, axis=0), check_size_px, axis=1
    )

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    stim = checkerboard_contrast()

    plot_stim(stim, mask=True)
