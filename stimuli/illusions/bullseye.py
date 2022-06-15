import numpy as np
from stimuli.illusions.rings import ring_pattern, ring_single
from stimuli.utils import plot_stim


def bullseye_illusion(
    ppd=10,
    n_rings=8,
    ring_width=0.5,
    target_pos_l=0,
    target_pos_r=0,
    padding=(1.0, 1.0, 1.0, 1.0),
    back=0.0,
    rings=1.0,
    target=0.5,
):
    """
    Bullseye Illusion.
    Two ring patterns (see ring_pattern func), with target in centre and one ring pattern inverted.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_rings : int
        the number of rings
    ring_width : float
        width per ring in degrees visual angle
    target_pos_l : int
        specify the target index in the left ring
    target_pos_r : int
        specify the target index in the right ring
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    back : float
        background value
    rings : float
        value for grid cells
    target : float
        value for target

    Returns
    -------
    A stimulus object
    """
    stim1 = ring_pattern(
        ppd=ppd,
        n_rings=n_rings,
        target_pos_l=target_pos_l,
        ring_width=ring_width,
        padding=padding,
        back=back,
        rings=rings,
        target=target,
        invert_rings=False,
        double=False,
    )
    stim2 = ring_pattern(
        ppd=ppd,
        n_rings=n_rings,
        target_pos_l=target_pos_r,
        ring_width=ring_width,
        padding=padding,
        back=back,
        rings=rings,
        target=target,
        invert_rings=True,
        double=False,
    )

    img = np.hstack((stim1["img"], stim2["img"]))
    # Increase target mask values to differentiate from single-stimulus targets:
    stim2["mask"][stim2["mask"] != 0] += 1
    mask = np.hstack((stim1["mask"], stim2["mask"]))

    return {"img": img, "mask": mask}


def bullseye_single(
    ppd=10,
    n_rings=8,
    target_idx=0,
    ring_width=0.5,
    vring1=1.0,
    vring2=0.0,
    vtarget=0.5
):
    """
    Bullseye Illusion.

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
    A stimulus object
    """
    stim = ring_single(
        ppd=ppd,
        n_rings=n_rings,
        target_idx=target_idx,
        ring_width=ring_width,
        vring1=vring1,
        vring2=vring2,
        vtarget=vtarget
    )

    return {"img": stim['img'], "mask": stim['mask']}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = bullseye_single()
    plot_stim(stim, mask=True)
