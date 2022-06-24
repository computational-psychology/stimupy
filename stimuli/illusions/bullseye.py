from stimuli.illusions.rings import ring_stimulus


def bullseye_stimulus(
    ppd=10,
    n_rings=8,
    ring_width=0.5,
    vring1=1.0,
    vring2=0.0,
    vtarget=0.5,
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
    vring1 : float
        value for even rings
    vring2 : float
        value for odd rings
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    stim = ring_stimulus(
        ppd=ppd,
        n_rings=n_rings,
        target_idx=0,
        ring_width=ring_width,
        vring1=vring1,
        vring2=vring2,
        vtarget=vtarget,
    )

    return {"img": stim["img"], "mask": stim["mask"]}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = bullseye_stimulus()
    plot_stim(stim, stim_name="Bullseye")
    plt.show()
