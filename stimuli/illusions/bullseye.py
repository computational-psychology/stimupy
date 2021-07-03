import numpy as np
from stimuli.illusions.rings import ring_pattern
from stimuli.utils import degrees_to_pixels, pad_img

def bullseye_illusion(ppd=10, n_rings=8, ring_width=.5, target_pos_l=0, target_pos_r=0, padding=(1.0,1.0,1.0,1.0), back=0., rings=1., target=.5):
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
    img1, mask1 = ring_pattern(n_rings=n_rings, target_pos_l=target_pos_l, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=False, double=False)
    img2, mask2 = ring_pattern(n_rings=n_rings, target_pos_l=target_pos_r, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=True, double=False)

    return (np.hstack((img1, img2)), np.hstack((mask1, mask2)))

def domijan2015():
    img =  bullseye_illusion(n_rings=8, ring_width=.5, target_pos_l=0, target_pos_r=0, padding=(.9,1.0,.9,1.0), back=1., rings=9., target=5.)
    return img

def RHS2007_bullseye_thin():
    return bullseye_illusion(n_rings=8, ring_width=1, padding=(100,100,100,100), back=1., rings=9., target=5.)

def RHS2007_bullseye_thick():
    return bullseye_illusion(n_rings=8, ring_width=1, padding=(50,50,50,50), back=1., rings=9., target=5.)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img, mask = bullseye_illusion()
    plt.imshow(img, cmap='gray')
    plt.show()