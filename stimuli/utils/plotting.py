import matplotlib as mpl
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
        img, mask = stim["img"], np.ndarray.astype(stim["mask"], int)
        img = np.dstack([img, img, img])
        mask = np.dstack([mask, mask, mask])

        if np.unique(mask).size > 10:
            colormap = plt.cm.tab20
        else:
            colormap = plt.cm.tab10

        for idx in np.unique(mask)[np.unique(mask) > 0]:
            color = colormap.colors[idx]
            color = np.reshape(color, (1, 1, 3))
            img = np.where(mask == idx, color, img)
        ax.imshow(img)

        # Colorbar for mask indices
        bounds = list(np.unique(mask))
        norm = mpl.colors.BoundaryNorm(bounds, len(bounds) + 1, extend="both")
        plt.colorbar(
            mpl.cm.ScalarMappable(norm=norm, cmap=colormap),
            ax=ax,
        )

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
