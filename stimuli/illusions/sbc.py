import numpy as np
from stimuli.utils import pixels_to_degrees, degrees_to_pixels, pad_img, pad_img_to_shape
from stimuli.components import rectangle, disc, square_wave_grating


def simultaneous_contrast(
    ppd=10,
    im_size=(4.0, 4.0),
    target_size=(2.0, 2.0),
    target_pos=(1.0, 1.0),
    vback=0.0,
    vtarget=0.5,
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


def sbc_with_dots(
        ppd=10,
        n_dots=(8, 9),
        dot_radius=3.,
        distance=1.,
        target_shape=(4, 3),
        vback=0.,
        vdots=1.,
        vtarget=0.5,
        ):
    """
    Simultaneous contrast stimulus with dots

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_dots : (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : (int, int)
        target shape defined as the number of dots that fit into the target
    vback : float
        value for background
    vdots : float
        value for dots
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    padding = (distance/2., distance/2., distance/2., distance/2.)
    patch = disc(ppd, dot_radius, vback=0., vdisc=vdots)
    patch = pad_img(patch, padding, ppd, 0.)

    img_height = pixels_to_degrees(n_dots[0] * patch.shape[0], ppd)
    img_width = pixels_to_degrees(n_dots[1] * patch.shape[1], ppd)
    rec_height = pixels_to_degrees(target_shape[0] * patch.shape[0], ppd)
    rec_width = pixels_to_degrees(target_shape[1] * patch.shape[1], ppd)

    # Create the sbc in the background:
    tposy = (img_height-rec_height) / 2.
    tposx = (img_width-rec_width) / 2.
    img = rectangle(ppd, im_size=(img_height, img_width), rect_size=(rec_height, rec_width),
                    rect_pos=(tposy, tposx), vback=vback, vrect=vtarget)
    mask = np.zeros(img.shape)
    mask[img == vtarget] = 1

    patch = np.tile(patch, (n_dots[0], n_dots[1]))
    indices_dots = np.where((patch != 0))
    img[indices_dots] = vdots
    mask[indices_dots] = 0
    return {"img": img, "mask": mask}


def dotted_sbc(
        ppd=10,
        n_dots=(8, 9),
        dot_radius=3.,
        distance=1.,
        target_shape=(4, 3),
        vback=0.,
        vdots=1.,
        vtarget=0.5,
        ):
    """
    Simultaneous contrast stimulus with dots

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_dots : (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : (int, int)
        target shape defined as the number of dots that fit into the target
    vback : float
        value for background
    vdots : float
        value for dots
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    padding = (distance/2., distance/2., distance/2., distance/2.)
    patch = disc(ppd, dot_radius, vback=0., vdisc=vdots)
    patch = pad_img(patch, padding, ppd, 0.)

    img_height = pixels_to_degrees(n_dots[0] * patch.shape[0], ppd)
    img_width = pixels_to_degrees(n_dots[1] * patch.shape[1], ppd)
    rec_height = pixels_to_degrees(target_shape[0] * patch.shape[0], ppd)
    rec_width = pixels_to_degrees(target_shape[1] * patch.shape[1], ppd)

    # Create the sbc and img:
    tposy = (img_height-rec_height) / 2.
    tposx = (img_width-rec_width) / 2.
    sbc = rectangle(ppd, im_size=(img_height, img_width), rect_size=(rec_height, rec_width),
                    rect_pos=(tposy, tposx), vback=vback, vrect=vtarget)
    img = np.ones(sbc.shape) * vback

    patch = np.tile(patch, (n_dots[0], n_dots[1]))
    indices_dots_back = np.where((patch != 0) & (sbc == vback))
    indices_dots_target = np.where((patch != 0) & (sbc == vtarget))
    img[indices_dots_back] = vdots
    img[indices_dots_target] = vtarget
    mask = np.zeros(img.shape)
    mask[indices_dots_target] = 1
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "SBC": simultaneous_contrast(),
        "SBC with dots": sbc_with_dots(),
        "Dotted SBC": dotted_sbc(),
    }

    plot_stimuli(stims, mask=True)
    plt.show()
