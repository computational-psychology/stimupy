import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

__all__ = [
    "compare_plots",
    "plot_stim",
    "plot_stimuli",
]

def compare_plots(plots):
    """
    Plot multiple plots in one plot for comparing.

    Parameters
    ----------
    plots : list of plots
        List containing plots which should be plotted

    """
    M = len(plots)
    for i, (plot_name, plot) in enumerate(plots.items()):
        plt.subplot(1, M, i + 1)
        plt.title(plot_name)
        plt.imshow(plot, cmap="gray")
    plt.show()


def plot_stim(
    stim,
    mask=False,
    stim_name="stim",
    ax=None,
    vmin=0,
    vmax=1,
    save=None,
    extent_key="shape",
):
    """
    Utility function to plot stimulus array (key: "img") from stim dict and mask (optional)

    Parameters
    ----------
    stim : dict
        stimulus dict containing stimulus-array (key: "img")
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    stim_name : str, optional
        Stimulus name used for plotting (default: "stim")
    ax : Axis object, optional
        If not None (default), plot in the specified Axis object
    vmin : float, optional
        Minimal intensity value for plotting. The default is 0.
    vmax : float, optional
        Minimal intensity value for plotting. The default is 1.
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    extent_key : str, optional
        Key to extent which will be used for plotting.
        Default is "shape", using the image size in pixels as extent.

    Returns
    -------
    ax : Axis object
        If ax was passed and plotting is None, returns updated Axis object.

    """
    print("Plotting:", stim_name)

    single_plot = False
    if ax is None:
        ax = plt.gca()
        single_plot = True

    if extent_key in stim.keys():
        if len(stim[extent_key]) == 2:
            extent = [0, stim[extent_key][1], 0, stim[extent_key][0]]
        elif len(stim[extent_key]) == 4:
            extent = stim[extent_key]
        else:
            raise ValueError("extent should either contain 2 or 4 values")
    else:
        warnings.warn("extent_key does not exist in dict, using pixel-extent")
        extent = [0, stim["img"].shape[0], 0, stim["img"].shape[1]]

    if not mask:
        ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax, extent=extent)
    else:
        img = stim["img"]
        if isinstance(mask, str):
            mask_keys = [mask]
        else:
            mask_keys = [key for key in stim.keys() if key.endswith("mask")]

        # If target_mask exists, use it.
        if "target_mask" in mask_keys:
            mask = stim["target_mask"]
        else:
            mask = stim[mask_keys[0]]

        if (mask is None) or (len(np.unique(mask)) == 1):
            warnings.warn("mask is None or empty- cannot plot")
            ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax, extent=extent)

        else:
            img = np.dstack([img, img, img])
            mask = np.dstack([mask, mask, mask])

            if np.unique(mask).size >= 20:
                colormap = plt.cm.colors.ListedColormap(np.random.rand(mask.max() + 1, 3))
            elif np.unique(mask).size > 10 and np.unique(mask).size < 20:
                colormap = plt.cm.tab20
            else:
                colormap = plt.cm.tab10

            for idx in np.unique(mask)[np.unique(mask) > 0]:
                color = colormap.colors[idx]
                color = np.reshape(color, (1, 1, 3))
                img = np.where(mask == idx, color, img)
            ax.imshow(img, extent=extent)

            # Colorbar for mask indices
            bounds = list(np.unique(mask))
            norm = mpl.colors.BoundaryNorm(bounds, len(bounds) + 1, extend="both")
            plt.colorbar(
                mpl.cm.ScalarMappable(norm=norm, cmap=colormap),
                ax=ax,
            )

    ax.set_title(label=stim_name)

    if save is None and single_plot:
        plt.show()
        return ax
    elif save is None and not single_plot:
        return ax
    elif isinstance(save, str):
        plt.savefig(save)
        plt.close()
    else:
        raise ValueError("save can be None or a filepath")


def plot_stimuli(
    stims,
    mask=False,
    vmin=0,
    vmax=1,
    save=None,
    extent_key="shape",
):
    """
    Utility function to plot multuple stimuli (key: "img") from stim dicts and mask (optional)

    Parameters
    ----------
    stims : dict of dicts
        dictionary composed of stimulus dicts containing stimulus-array (key: "img")
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    vmin : float, optional
        Minimal intensity value for plotting. The default is 0.
    vmax : float, optional
        Minimal intensity value for plotting. The default is 1.
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    extent_key : str, optional
        Key to extent which will be used for plotting.
        Default is "shape", using the image size in pixels as extent.

    """

    # Plot each stimulus+mask
    n_stim = int(np.ceil(np.sqrt(len(stims))))
    F = plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        ax = F.add_subplot(n_stim, n_stim, i + 1)
        plot_stim(
            stim,
            mask,
            stim_name=stim_name,
            ax=ax,
            vmin=vmin,
            vmax=vmax,
            save=None,
            extent_key=extent_key,
        )

    plt.tight_layout()

    if save is None:
        plt.show()
    elif isinstance(save, str):
        plt.savefig(save)
        plt.close()
    else:
        raise ValueError("save can be None or a filepath")