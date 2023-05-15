import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from stimupy.utils import resolution

__all__ = [
    "plot_stim",
    "plot_stimuli",
    "compare_plots",
]


def compare_plots(plots):
    """Plot multiple plots in one plot for comparing.

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
    units="deg",
    origin="mean",
):
    """Plot a stimulus

    Plots the stimulus-array (key: "img") directly from stim dict.
    Optionally also plots mask.

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
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim

    Returns
    -------
    ax : Axis object
        If ax was passed and plotting is None, returns updated Axis object.

    """
    single_plot = False
    if ax is None:
        ax = plt.gca()
        single_plot = True

    # Figure out what units need to go on axes
    if units in ["px", "pix", "pixels"]:
        extent = [0, stim["img"].shape[1], stim["img"].shape[0], 0]
    elif units in ["deg", "degrees"]:
        if "visual_size" in stim:
            x, y = resolution.visual_size_to_axes(
                stim["visual_size"], shape=stim["img"].shape, origin=origin
            )
            extent = [x.min(), x.max(), y.max(), y.min()]
        else:
            warnings.warn("no visual_size provided")
            extent = [0, stim["img"].shape[1], stim["img"].shape[0], 0]
    elif units in stim.keys():
        if len(stim[units]) == 2:
            # provided 2 values for units, so assume formatted like visual_size
            x, y = resolution.visual_size_to_axes(
                stim[units], shape=stim["img"].shape, origin=origin
            )
            extent = [x.min(), x.max(), y.min(), y.max()]
        elif len(stim[units]) == 4:
            # provided 4 values for units, so assume proper formatting
            extent = stim[units]
        else:
            raise ValueError("extent should either contain 2 or 4 values")
    else:
        warnings.warn("units does not exist in dict, using pixel-extent")
        extent = [0, stim["img"].shape[1], 0, stim["img"].shape[0]]

    if not mask:
        ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax, extent=extent)
    else:
        img = stim["img"]
        if isinstance(mask, str):
            mask_keys = [mask]
        else:
            mask_keys = [key for key in stim.keys() if key.endswith("mask")]

        if len(mask_keys) == 0:
            ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax, extent=extent)
        else:
            # If target_mask exists, use it.
            if "target_mask" in mask_keys:
                mask = stim["target_mask"]
            else:
                mask = stim[mask_keys[0]]

            if (mask is None) or (len(np.unique(mask)) == 1):
                warnings.warn("mask is None or empty- cannot plot mask")
                ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax, extent=extent)

            else:
                img = np.dstack([img, img, img])
                mask = np.dstack([mask, mask, mask])

                if np.unique(mask).size >= 20:
                    colormap = plt.cm.colors.ListedColormap(np.random.rand(mask.max() + 1, 3))
                elif np.unique(mask).size >= 10 and np.unique(mask).size < 20:
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
    units="deg",
):
    """Plot multiple stimuli

    Plots the stimulus-arrays (keys: "img") directly from stim dicts.
    Arranges stimuli in a grid.
    Optionally also plots masks.

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
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim
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
            units=units,
        )

    plt.tight_layout()

    if save is None:
        plt.show()
    elif isinstance(save, str):
        plt.savefig(save)
        plt.close()
    else:
        raise ValueError("save can be None or a filepath")
