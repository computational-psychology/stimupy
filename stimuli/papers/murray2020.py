"""Stimuli from Murray (2020) https://doi.org/10/gh57gf

This module reproduces most of the stimuli used by Murray (2020)
exactly as they were provided to the model described in that paper.
The stimuli are show in Fig 1 of the paper.
NOTE that the Haze illusion (Fig 1m) is not provided.

Each stimulus is provided by a separate function,
a full list can be found as stimuli.papers.murray2020.__all__

The output of each of these functions is a dict
with at least the keys:
    - "img", containing a 2D numpy array providing the stimulus image
      in cd/m2
    - "mask", containing a 2D numpy array providing a mask for the
      target regions in the stimulus, each indicated by an integer index.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/murray2020.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimuli.papers.murray2020 import *

References
-----------
Murray, R. F. (2020). A model of lightness perception guided by
probabilistic assumptions about lighting and reflectance.
Journal of Vision, 20(7), 28. https://doi.org/10/gh57gf
"""

import os.path

import numpy as np
import scipy.io

__all__ = [
    "argyle",
    "argyle_control",
    "argyle_long",
    "snake",
    "snake_control",
    "koffka_adelson",
    "koffka_broken",
    "koffka_connected",
    "checkassim",
    "simcon",
    "simcon_articulated",
    "white",
]

data_dir = os.path.dirname(__file__)
mat_fname = os.path.join(data_dir, "murray2020.mat")
mat_content = scipy.io.loadmat(mat_fname)

PPD = 16 / 8.0


def gen_all(skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating murray2020.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func()

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def get_mask(target1, target2, shape):
    mask = np.zeros(shape)

    # Convert MATLAB 1-based index to numpy 0-based index
    target1 = target1 - 1
    target2 = target2 - 1

    # Fill target1 mask
    for x in range(target1[1], target1[3] + 1):
        for y in range(target1[0], target1[2] + 1):
            mask[y][x] = 1

    # Fill target2 mask
    for x in range(target2[1], target2[3] + 1):
        for y in range(target2[0], target2[2] + 1):
            mask[y, x] = 2

    return mask


def argyle(ppd=PPD):
    """Argyle illusion, Murray (2020) Fig 1a

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["argyle"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def argyle_control(ppd=PPD):
    """Argyle control figure, Murray (2020) Fig 1c

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["argyle_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def argyle_long(ppd=PPD):
    """Long-range Argyle illusion, Murray (2020) Fig 1b

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["argyle_long"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def snake(ppd=PPD):
    """Snake illusion, Murray (2020) Fig 1i

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["snake"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def snake_control(ppd=PPD):
    """Snake control figure, Murray (2020) Fig 1j

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["snake_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def koffka_adelson(ppd=PPD):
    """Koffka-Adelson figure, Murray (2020) Fig 1e

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["koffka_adelson"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def koffka_broken(ppd=PPD):
    """Koffka ring, broken, Murray (2020) Fig 1d

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["koffka_broken"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def koffka_connected(ppd=PPD):
    """Koffka ring, connected, Murray (2020) Fig 1f

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["koffka_connected"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def checkassim(ppd=PPD):
    """Checkerboard assimilation, Murray (2020) Fig 1h

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["checkassim"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def simcon(ppd=PPD):
    """Classic simultaneous contrast figure, Murray (2020) Fig 1k

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["simcon"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def simcon_articulated(ppd=PPD):
    """Articulated simultaneous contrast figure, Murray (2020) Fig 1l

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["simcon_articulated"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


def white(ppd=PPD):
    """White's illusion, Murray (2020) Fig 1A

    Returns
    -------
    dict of str
        dict with the stimulus, with at least the keys:
        - "img" containing a 2D numpy array providing the stimulus image
          [in cd/m2]
        - "mask", containing a 2D numpy array providing a mask for the
          target regions in the stimulus, each indicated by an integer index.
    """
    a = mat_content["white"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(
        repeats=int(ppd / PPD), axis=1
    )

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    # Generate all stimuli exported in __all__
    stims = gen_all(skip=True)

    plot_stimuli(stims, mask=False)
