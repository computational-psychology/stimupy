import numpy as np
from stimuli.illusions.rings import ring_pattern
from stimuli import utils

def bullseye_illusion(n_rings=8, ring_width=5, padding=(10,10,10,10), back=0., rings=1., target=.5):
    """
    Bullseye Illusion.
    Two ring patterns (see ring_pattern func), with target in centre and one ring pattern inverted.

    Parameters
    ----------
    n_rings: the number of rings
    ring_width: width per ring in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    back: value for background
    rings: value for grid cells
    target: value for target

    Returns
    -------
    2D numpy array
    """
    img1 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=False, double=False)
    img2 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=True, double=False)

    return np.hstack([img1, img2])

def domijan2015():
    img =  bullseye_illusion(n_rings=8, ring_width=5, padding=(9,10,9,10), back=1., rings=9., target=5.)
    return img

def RHS2007_bullseye_thin():
    return bullseye_illusion(n_rings=8, ring_width=5, padding=(600,600,600,600), back=1., rings=9., target=5.)

def RHS2007_bullseye_thick():
    return bullseye_illusion(n_rings=8, ring_width=5, padding=(500,500,500,500), back=1., rings=9., target=5.)


