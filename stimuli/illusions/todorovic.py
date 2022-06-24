import numpy as np
from stimuli.components import cross, rectangle
from stimuli.utils import degrees_to_pixels, pad_img_to_shape


def todorovic_in(
    im_size=(10.0, 10.0),
    ppd=10,
    target_size=(4.0, 4.0),
    target_pos=(3.0, 3.0),
    covers_height=2.0,
    covers_width=2.0,
    covers_posx=(2.0, 6.0, 2.0, 6.0),
    covers_posy=(2.0, 6.0, 6.0, 2.0),
    vback=0.0,
    vtarget=0.5,
    vcovers=1.0,
):
    """
    Todorovic's illusion with rectangular target and rectangles added

    Parameters
    ----------
    im_size : (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_size : (float, float)
        size of the target in degrees of visual angle (height, width)
    target_pos : (float, float)
        coordinates where to place the target
    covers_height : float or tuple of floats
        height of covers; if single float, all covers have the same height
    covers_width : float or tuple of floats
        width of covers; if single float, all covers have the same width
    covers_posx : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_posy : tuple of floats
        y coordinates of covers; as many covers as there are coordinates
    vback : float
        value for background
    vtarget : float
        value for target
    vcovers : float
        value for covers

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(covers_height, (float, int)):
        covers_height = [covers_height] * len(covers_posx)
    if isinstance(covers_width, (float, int)):
        covers_width = [covers_width] * len(covers_posy)

    if any(
        len(lst) != len(covers_height)
        for lst in [covers_width, covers_posx, covers_posy]
    ):
        raise Exception(
            "covers_height, covers_width, covers_posx and covers_posy need the"
            " same length."
        )

    # Create image with square
    img = rectangle(ppd, im_size, target_size, target_pos, vback, vtarget)

    # Add covers
    covers_height = degrees_to_pixels(covers_height, ppd)
    covers_width = degrees_to_pixels(covers_width, ppd)
    covers_posx = degrees_to_pixels(covers_posx, ppd)
    covers_posy = degrees_to_pixels(covers_posy, ppd)

    for i in range(len(covers_height)):
        img[
            covers_posy[i] : covers_posy[i] + covers_height[i],
            covers_posx[i] : covers_posx[i] + covers_width[i],
        ] = vcovers

    mask = np.copy(img)
    mask[mask == vback] = 0
    mask[mask == vcovers] = 0
    mask[mask == vtarget] = 1
    return {"img": img, "mask": mask}


def todorovic_out(
    im_size=(12.0, 12.0),
    ppd=10,
    target_size=(4.0, 4.0, 4.0, 4.0),
    target_thickness=2.0,
    covers_height=2.0,
    covers_width=2.0,
    covers_posx=(3.0, 7.0, 3.0, 7.0),
    covers_posy=(3.0, 7.0, 7.0, 3.0),
    vback=0.0,
    vtarget=0.5,
    vcovers=1.0,
):
    """
    Todorovic's illusion with cross target and rectangles added

    Parameters
    ----------
    im_size : (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_size : (float, float, float, float)
        size of the target's arms in degrees visual angle in form (top, bottom, left, right)
    target_thickness : float
        thickness of target cross
    covers_height : float or tuple of floats
        height of covers; if single float, all covers have the same height
    covers_width : float or tuple of floats
        width of covers; if single float, all covers have the same width
    covers_posx : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_posy : tuple of floats
        y coordinates of covers; as many covers as there are coordinates
    vback : float
        value for background
    vtarget : float
        value for target
    vcovers : float
        value for covers

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(covers_height, (float, int)):
        covers_height = [covers_height] * len(covers_posx)
    if isinstance(covers_width, (float, int)):
        covers_width = [covers_width] * len(covers_posy)

    if any(
        len(lst) != len(covers_height)
        for lst in [covers_width, covers_posx, covers_posy]
    ):
        raise Exception(
            "covers_height, covers_width, covers_posx and covers_posy need the"
            " same length."
        )

    img = cross(ppd, target_size, target_thickness, vback, vtarget)
    img = pad_img_to_shape(img, np.array(im_size) * ppd, val=vback)

    covers_height = degrees_to_pixels(covers_height, ppd)
    covers_width = degrees_to_pixels(covers_width, ppd)
    covers_posx = degrees_to_pixels(covers_posx, ppd)
    covers_posy = degrees_to_pixels(covers_posy, ppd)

    # Add covers
    for i in range(len(covers_height)):
        img[
            covers_posy[i] : covers_posy[i] + covers_height[i],
            covers_posx[i] : covers_posx[i] + covers_width[i],
        ] = vcovers

    mask = np.copy(img)
    mask[mask == vback] = 0
    mask[mask == vcovers] = 0
    mask[mask == vtarget] = 1
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Todorovic (in)": todorovic_in(),
        "Todorovic (out)": todorovic_out(),
    }
    plot_stimuli(stims)
    plt.show()
