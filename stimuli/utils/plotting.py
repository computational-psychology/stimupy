import matplotlib.pyplot as plt
import numpy as np


def compare_plots(plots):
    M = len(plots)
    for i, (plot_name, plot) in enumerate(plots.items()):
        plt.subplot(1, M, i + 1)
        plt.title(plot_name)
        plt.imshow(plot, cmap="gray")
    plt.show()


def plot_stim(stim, mask=False, stim_name="stim", ax=None):
    if ax is None:
        ax = plt.gca()

    if not mask:
        ax.imshow(stim["img"], cmap="gray", vmin=0.0, vmax=1.0)
    else:
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)
        final = mask + img
        final /= np.max(final)
        ax.imshow(final)

    ax.set_title(label=stim_name)
    return ax


def plot_stimuli(stims, mask=False):
    import math

    # Plot each stimulus+mask
    n_stim = math.ceil(math.sqrt(len(stims)))
    F = plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        ax = F.add_subplot(n_stim, n_stim, i + 1)
        plot_stim(stim, mask, stim_name=stim_name, ax=ax)

    plt.tight_layout()
    plt.show()
