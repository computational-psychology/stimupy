import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from stimupy.utils import resolution

__all__ = [
    "plot_stim",
    "plot_stimuli",
    "plot_comparison",
]


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
    ncols=None,
    nrows=None,
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
    ncols : int or None, optional
        number of columns in gridspec, or figure it out (default)
    nrows : int or None, optional
        number of rows in gridspec, or figure it out (default)
    """

    # Setup facets
    if ncols and nrows:
        if ncols * nrows < len(stims):
            raise Exception(
                f"Invalid ncols/nrows: more stimuli {len(stims)} than facets {ncols * nrows}"
            )
    elif ncols:
        nrows = np.ceil(len(stims) / ncols)
    elif nrows:
        ncols = np.ceil(len(stims) / nrows)
    else:
        ncols = np.ceil(np.sqrt(len(stims)))
        nrows = np.ceil(len(stims) / ncols)
    ncols = int(ncols)
    nrows = int(nrows)

    # Plot each stimulus (& mask)
    F = plt.figure(figsize=(nrows * 2, ncols * 2))
    for idx, (stim_name, stim) in enumerate(stims.items()):
        ax = F.add_subplot(nrows, ncols, idx + 1)
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


def plot_comparison(original_img, new_img):
    """Plots visual comparison of two image-arrays

    Parameters
    ----------
    original_img : numpy.ndarray
        original image-array
    new_img : numpy.ndarray
        new image-array

    Returns
    -------
    matplotlib.Figure
        Figure containing plots of images, and their comparison(s)
    """
    vmin, vmax = 0, 1

    fig = plt.figure(figsize=(20, 6))
    plt.subplot(1, 4, 1)
    plt.imshow(original_img, cmap="gray", vmin=vmin, vmax=vmax)
    plt.title("Original")

    plt.subplot(1, 4, 2)
    plt.imshow(new_img, cmap="gray", vmin=vmin, vmax=vmax)
    plt.title("New")

    plt.subplot(1, 4, 3)
    plt.imshow(original_img - new_img, cmap="coolwarm", vmin=-vmax, vmax=vmax)
    plt.colorbar()
    num_pix_off = np.prod(original_img.shape) - np.sum(np.isclose(original_img, new_img))
    plt.title(f"Difference: {num_pix_off} pix")

    plt.subplot(1, 4, 4)
    plt.plot(original_img[:, 128], label="Original")
    plt.plot(new_img[:, 128], label="New")
    plt.legend()

    return fig
