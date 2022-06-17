from stimuli.utils import plot_stim
from stimuli.components import rectangle


def simultaneous_contrast(
        ppd=10,
        im_size=(4., 4.),
        target_size=(2., 2.),
        target_pos=(1., 1.),
        vback=0.,
        vtarget=0.5
        ):
    """
    Simultaneous contrast stimulus

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    im_size : (float, float)
        size of the image in degree visual angle
    target_size : (float, float)
        size of the target in degree visual angle
    target_pos : (float, float)
        coordinates of the target in degree visual angle
    vback : float
        value for background
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    img = rectangle(ppd, im_size, target_size, target_pos, vback, vtarget)
    mask = rectangle(ppd, im_size, target_size, target_pos, 0, 1)
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = simultaneous_contrast()
    plot_stim(stim, mask=True)
