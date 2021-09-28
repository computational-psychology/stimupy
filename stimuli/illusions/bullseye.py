import numpy as np
from stimuli.illusions.rings import ring_pattern
from stimuli.utils import degrees_to_pixels, pad_img
from stimuli.Stimulus import Stimulus

def bullseye_illusion(ppd=10, n_rings=8, ring_width=.5, target_pos_l=0, target_pos_r=0, padding=(1.0,1.0,1.0,1.0), back=0., rings=1., target=.5):
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
    stim1 = ring_pattern(n_rings=n_rings, target_pos_l=target_pos_l, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=False, double=False)
    stim2 = ring_pattern(n_rings=n_rings, target_pos_l=target_pos_r, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=True, double=False)

    img = np.hstack((stim1.img, stim2.img))
    mask = np.hstack((stim1.target_mask, stim2.target_mask))

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    """
    Generates Bullseye illusion as used in the Domijan 2015 paper.
    """

    img = bullseye_illusion(
        n_rings=8,
        ring_width=0.5,
        target_pos_l=0,
        target_pos_r=0,
        padding=(0.9, 1.0, 0.9, 1.0),
        back=1.0,
        rings=9.0,
        target=5.0,
    )
    return img


def RHS2007_bullseye_thin():
    """
    Generates Bullseye thin illusion as used in the Robinson, Hammon and de Sa 2007 paper.
    """
    return bullseye_illusion(
        n_rings=8,
        ring_width=1,
        padding=(100, 100, 100, 100),
        back=1.0,
        rings=9.0,
        target=5.0,
    )


def RHS2007_bullseye_thick():
    """
    Generates Bullseye thick illusion as used in the Robinson, Hammon and de Sa 2007 paper.
    """

    return bullseye_illusion(
        n_rings=8,
        ring_width=1,
        padding=(50, 50, 50, 50),
        back=1.0,
        rings=9.0,
        target=5.0,
    )


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = bullseye_illusion()
    plt.imshow(stim.img, cmap='gray')
    plt.show()
