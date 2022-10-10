from stimuli.illusions.rings import ring_stimulus


def bullseye_stimulus(
    ppd=10,
    n_rings=8,
    ring_width=0.5,
    intensity_rings=(1., 0.),
    intensity_target=0.5,
):
    """
    Bullseye Illusion.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_rings : int
        the number of rings
    ring_width : float
        width per ring in degrees visual angle
    intensity_rings : (float, float)
        intensity values for even rings
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    stim = ring_stimulus(
        ppd=ppd,
        n_rings=n_rings,
        target_idx=0,
        ring_width=ring_width,
        intensity_rings=intensity_rings,
        intensity_target=intensity_target,
    )

    return stim


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = bullseye_stimulus()
    plot_stim(stim, stim_name="Bullseye")
    plt.show()
