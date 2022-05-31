# gitlab

import math
import os.path

import matplotlib.pyplot as plt
import numpy as np
import scipy.io

data_dir = os.path.dirname(__file__)
mat_fname = os.path.join(data_dir, "murray2020.mat")
print(mat_fname)
mat_content = scipy.io.loadmat(mat_fname)


def get_mask(arr_list, ppd, mask):
    target1 = arr_list[0]
    target2 = arr_list[1]
    y = target1[0]
    x = target1[1]
    mask[y][x] = 1
    y = target1[2]
    x = target1[3]
    mask[y][x] = 1

    x_diff = target1[3] - target1[1] + 1
    for i in range(x_diff):
        y_diff = target1[2] - target1[0] + 1
        for j in range(y_diff):
            y = target1[0]
            x = target1[1]
            mask[y + j][x + i] = 1

    y = target2[0]
    x = target2[1]
    mask[y][x] = 2
    y = target2[2]
    x = target2[3]
    mask[y][x] = 2

    x_diff = target2[3] - target2[1] + 1
    for i in range(x_diff):
        y_diff = target2[2] - target2[0] + 1
        for j in range(y_diff):
            y = target2[0]
            x = target2[1]
            mask[y + j][x + i] = 2

    plt.imshow(mask)
    return mask


def argyle_illusion(ppd):
    argyle = mat_content["argyle"]
    img = np.array(((argyle[0])[0])[0])
    a = mat_content["argyle"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - int(ppd / 16), t2 - int(ppd / 16)]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def argyle_control_illusion(ppd):
    argyle_control = mat_content["argyle_control"]
    img = np.array(((argyle_control[0])[0])[0])
    a = mat_content["argyle_control"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def argyle_long_illusion(ppd):
    argyle_long = mat_content["argyle_long"]
    img = np.array(((argyle_long[0])[0])[0])
    a = mat_content["argyle_long"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def snake_illusion(ppd):
    snake = mat_content["snake"]
    img = np.array(((snake[0])[0])[0])
    a = mat_content["snake"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def snake_control_illusion(ppd):
    snake_control = mat_content["snake_control"]
    img = np.array(((snake_control[0])[0])[0])
    a = mat_content["snake_control"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def koffka_adelson_illusion(ppd):
    koffka_adelson = mat_content["koffka_adelson"]
    img = np.array(((koffka_adelson[0])[0])[0])
    a = mat_content["koffka_adelson"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def koffka_broken_illusion(ppd):
    koffka_broken = mat_content["koffka_broken"]
    img = np.array(((koffka_broken[0])[0])[0])
    a = mat_content["koffka_broken"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def koffka_connected_illusion(ppd):
    koffka_connected = mat_content["koffka_connected"]
    img = np.array(((koffka_connected[0])[0])[0])
    a = mat_content["koffka_connected"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def checkassim_illusion(ppd):
    checkassim = mat_content["checkassim"]
    img = np.array(((checkassim[0])[0])[0])
    a = mat_content["checkassim"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def simcon_illusion(ppd):
    simcon = mat_content["simcon"]
    img = np.array(((simcon[0])[0])[0])
    a = mat_content["simcon"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def simcon_articulated_illusion(ppd):
    simcon_articulated = mat_content["simcon_articulated"]
    img = np.array(((simcon_articulated[0])[0])[0])
    a = mat_content["simcon_articulated"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


def white_illusion(ppd):
    white = mat_content["white"]
    img = np.array(((white[0])[0])[0])
    a = mat_content["white"]
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t - 1, t2 - 1]
    mask = np.zeros(img.shape)
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}


if __name__ == "__main__":

    ppd = 16

    stims = {
        "argyle_illusion": argyle_illusion(ppd),
        "argyle_control_illusion": argyle_control_illusion(ppd),
        "argyle_long_illusion": argyle_long_illusion(ppd),
        "snake_illusion": snake_illusion(ppd),
        "snake_control_illusion": snake_control_illusion(ppd),
        "koffka_adelson_illusion": koffka_adelson_illusion(ppd),
        "koffka_broken_illusion": koffka_broken_illusion(ppd),
        "koffka_connected_illusion": koffka_connected_illusion(ppd),
        "checkassim_illusion": checkassim_illusion(ppd),
        "simcon_illusion": simcon_illusion(ppd),
        "simcon_articulated_illusion": simcon_articulated_illusion(ppd),
        "white_illusion": white_illusion(ppd),
    }

    a = math.ceil(math.sqrt(len(stims)))
    plt.figure(figsize=(a * 3, a * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        print("Generating", stim_name + "")
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)

        final = mask * 100 + img
        final /= np.max(final)

        plt.subplot(a, a, i + 1)
        plt.title(stim_name + " - img")
        plt.imshow(final)

    plt.tight_layout()

    plt.show()
