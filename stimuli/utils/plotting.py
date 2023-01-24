import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import warnings


def compare_plots(plots):
    M = len(plots)
    for i, (plot_name, plot) in enumerate(plots.items()):
        plt.subplot(1, M, i + 1)
        plt.title(plot_name)
        plt.imshow(plot, cmap="gray")
    plt.show()


def plot_stim(stim,
              mask=False,
              stim_name="stim",
              ax=None,
              vmin=0,
              vmax=1,
              save=None,
              ):

    single_plot = False
    if ax is None:
        ax = plt.gca()
        single_plot = True

    if not mask:
        ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax)
    else:
        img = stim["img"]
        mask_keys = [key for key in stim.keys() if key.endswith("mask")]
        
        # If target_mask exists, use it.
        if "target_mask" in mask_keys:
            mask = stim["target_mask"]
        else:
            mask = stim[mask_keys[0]]
        
        if (mask is None) or (len(np.unique(mask)) == 1):
            warnings.warn("mask is None or empty- cannot plot")
            ax.imshow(stim["img"], cmap="gray", vmin=vmin, vmax=vmax)

        else:
            img = np.dstack([img, img, img])
            mask = np.dstack([mask, mask, mask])
    
            if np.unique(mask).size > 10:
                colormap = plt.cm.tab20
            else:
                colormap = plt.cm.tab10
    
            for idx in np.unique(mask)[np.unique(mask) > 0]:
                color = colormap.colors[idx%10]
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


def plot_stimuli(stims,
                 mask=False,
                 vmin=0,
                 vmax=1,
                 save=None,
                 ):

    # Plot each stimulus+mask
    n_stim = int(np.ceil(np.sqrt(len(stims))))
    F = plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        ax = F.add_subplot(n_stim, n_stim, i + 1)
        plot_stim(stim,
                  mask,
                  stim_name=stim_name,
                  ax=ax,
                  vmin=vmin,
                  vmax=vmax,
                  save=None,
                  )

    plt.tight_layout()

    if save is None:
        plt.show()
    elif isinstance(save, str):
        plt.savefig(save)
        plt.close()
    else:
        raise ValueError("save can be None or a filepath")
