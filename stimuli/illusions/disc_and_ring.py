import numpy as np
from stimuli.utils.utils import degrees_to_pixels, resize_array
from stimuli.Stimulus import Stimulus


def disc_and_ring(
    shape=(10, 10), radii=(4, 2), values=(0.5, 1), bg=0, ppd=30, ssf=5
):
    # TODO: the parameters aren't analogous to the other stimuli
    """
    Create a disc and ring stimulus with an arbitrary number of rings.

    Parameters
    ----------
    shape : tuple of 2 numbers
            The shape of the stimulus in degrees of visual angle. (y,x)
    radii : tuple of numbers
            the radii of the circles in degrees of visual angle, starting from
            the largest.
    values : tuple of numbers
             the gray values to assign to the circles, starting at the
             outermost. Must be the same length as radii.
    bg : number (optional)
         the  background value of the stimulus. Default is 0.
    ppd : number (optional)
          the number of pixels in one degree of visual angle. Default is 30.
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    stim : ndarray (2D)
           the stimulus
    """
    assert len(radii) == len(values)

    # create stimulus at 5 times size to allow for supersampling antialiasing
    img = (
        np.ones(degrees_to_pixels(np.array(shape), ppd).astype(int) * ssf) * bg
    )
    # compute distance from center of array for every point, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    radii = degrees_to_pixels(np.array(radii), ppd) * ssf
    for radius, value in zip(radii, values):
        img[dist < radius] = value

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))

    mask = None  # TODO add this
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    img, mask = disc_and_ring()
    plt.imshow(img, cmap="gray")
    plt.show()
