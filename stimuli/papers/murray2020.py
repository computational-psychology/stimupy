import os.path

import matplotlib.pyplot as plt
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


def argyle():
    a = mat_content["argyle"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0]) - [1, 0, 1, 0]
    target2 = np.array((((a[0])[0])[2])[0]) - [1, 0, 1, 0]
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def argyle_control():
    a = mat_content["argyle_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0]) - [1, 0, 1, 0]
    target2 = np.array((((a[0])[0])[2])[0]) - [1, 0, 1, 0]
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def argyle_long():
    a = mat_content["argyle_long"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0]) - [1, 0, 1, 0]
    target2 = np.array((((a[0])[0])[2])[0]) - [1, 0, 1, 0]
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def snake():
    a = mat_content["snake"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def snake_control():
    a = mat_content["snake_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def koffka_adelson():
    a = mat_content["koffka_adelson"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def koffka_broken():
    a = mat_content["koffka_broken"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def koffka_connected():
    a = mat_content["koffka_connected"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def checkassim():
    a = mat_content["checkassim"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def simcon():
    a = mat_content["simcon"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def simcon_articulated():
    a = mat_content["simcon_articulated"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


def white():
    a = mat_content["white"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)
    return {"img": img, "mask": mask}


if __name__ == "__main__":

    stims = {
        "argyle": argyle(),
        "argyle_control": argyle_control(),
        "argyle_long": argyle_long(),
        "snake": snake(),
        "snake_control": snake_control(),
        "koffka_adelson": koffka_adelson(),
        "koffka_broken": koffka_broken(),
        "koffka_connected": koffka_connected(),
        "checkassim": checkassim(),
        "simcon": simcon(),
        "simcon_articulated": simcon_articulated(),
        "white": white(),
    }

    n_stim = math.ceil(math.sqrt(len(stims)))
    plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        print("Generating", stim_name + "")
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)

        final = mask * 100 + img
        final /= np.max(final)

        plt.subplot(n_stim, n_stim, i + 1)
        plt.title(stim_name)
        plt.imshow(final)

    plt.tight_layout()

    plt.show()
