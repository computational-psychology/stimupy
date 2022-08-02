import numpy as np
from stimuli.components import square_wave
from stimuli.utils import degrees_to_pixels


def white_generalized(
    shape=(10, 10),
    ppd=10,
    grating_frequency=0.8,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices=(2, 5, 8, 11, 14),
    target_center_offsets=(3, 1.5, 0, -1.5, -3),
    target_sizes=(0.1, 0.2, 0.4, 0.8, 1),
    period="full",
):
    """
    White's stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices : int or tuple of ints
        bar indices where target(s) will be placed. As many targets as ints.
    target_center_offsets : float or tuple of floats
        offset from target center to image center in degree visual angle.
        If only one float is passed, the same offset is used for all targets.
        If a tuple of floats is passed, pass as many floats as there are targets.
    target_sizes : float or tuple of floats
        target sizes (i.e. height / length) in degrees visual angle
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    height_px, width_px = degrees_to_pixels(shape, ppd)
    target_offsets_px = degrees_to_pixels(target_center_offsets, ppd)
    target_sizes_px = degrees_to_pixels(target_sizes, ppd)
    cycle_width_px = degrees_to_pixels(1. / (grating_frequency*2), ppd) * 2
    phase_width_px = cycle_width_px // 2

    if isinstance(shape, (float, int)):
        shape = (shape, shape)
    if len(shape) != 2:
        raise ValueError("shape needs to be a single float or a tuple of two floats")

    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)
    if isinstance(target_center_offsets, (float, int)):
        target_center_offsets = (target_center_offsets,) * len(target_indices)
        target_offsets_px = (target_offsets_px,) * len(target_indices)

    if len(vbars) != 2:
        raise ValueError("vbars needs to be a tuple of two floats")
    if len(target_indices) != len(target_offsets_px):
        raise ValueError("# of target indices != # of target offsets")
    if not isinstance(vtarget, (float, int)):
        raise ValueError("vtarget should be a single float / int")
    if isinstance(target_sizes, (float, int)):
        target_sizes = (target_sizes,)*len(target_indices)
        target_sizes_px = (target_sizes_px,)*len(target_indices)
    if any(np.array(target_center_offsets)*ppd % 1 != 0):
        offsets_new = target_offsets_px / ppd
        print("Warning: White target offsets rounded to %s because of ppd" % offsets_new)
    if len(target_sizes) != len(target_indices):
        raise ValueError("# of target indices != # of target sizes")

    img = square_wave(shape, ppd, grating_frequency, vbars, period=period)
    mask = np.zeros((height_px, width_px))
    height, width = img.shape

    for i, index in enumerate(target_indices):
        # Calculate vertical placement of targets
        if target_offsets_px[i] < 0:
            offset = target_offsets_px[i] - target_sizes_px[i] // 2
        else:
            offset = target_offsets_px[i] - target_sizes_px[i] // 2
        y_start = height // 2 + offset
        y_end = y_start + target_sizes_px[i]
        if (y_start < 0) or (y_end > height):
            raise ValueError("White targets do not fully fit into stimulus")

        # Calculate horizontal placement of targets
        if index >= 0:
            x_start = index * phase_width_px
        else:
            # Calculate the number of phases based on resolution of grating:
            phases = int(2 * (int(shape[1] * ppd / phase_width_px) // 2))
            x_start = int((phases + index) * phase_width_px)
        x_end = x_start + phase_width_px

        img[y_start:y_end, x_start:x_end] = vtarget
        mask[y_start:y_end, x_start:x_end] = i + 1

    if period != "ignore":
        new_shape = (img.shape[0]/ppd, img.shape[1]/ppd)
        print("Warning: White shape changed from %s to %s" % (shape, new_shape))

    return {"img": img, "mask": mask}


def white(
    shape=(4.2, 4.2),
    ppd=20,
    grating_frequency=1.2,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices=(1, 3, -2, -4),
    target_size=1.,
    period="ignore",
):
    """
    White's stimulus where all targets are vertically aligned at half the stimulus height

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices : int or tuple of ints
        bar indices where target(s) will be placed. As many targets as ints.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = white_generalized(
        shape=shape,
        ppd=ppd,
        grating_frequency=grating_frequency,
        vbars=vbars,
        vtarget=vtarget,
        target_indices=target_indices,
        target_center_offsets=0,
        target_sizes=target_size,
        period=period,
        )
    return stim


# TODO: Add another function in which you specify n_targets instead of target_indices
def white_two_rows(
    shape=(4, 4),
    ppd=20,
    grating_frequency=2,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices_top=(1, 3, 5, 7, 9, 11),
    target_indices_bottom=(-2, -4, -6),
    target_center_offset=0.8,
    target_size=0.8,
    period="ignore",
):
    """
    White's stimulus where targets are placed in two rows (top, bottom) that have the same
    distance from the center.

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if not isinstance(target_center_offset, (float, int)):
        raise ValueError("target_center_offset should be a single float / int")
    if isinstance(target_indices_top, (float, int)):
        target_indices_top = (target_indices_top,)
    if isinstance(target_indices_bottom, (float, int)):
        target_indices_bottom = (target_indices_bottom,)

    target_indices = target_indices_top + target_indices_bottom
    offsets_top = (-target_center_offset,)*len(target_indices_top)
    offsets_bottom = (target_center_offset,)*len(target_indices_bottom)
    target_center_offsets = offsets_top + offsets_bottom

    stim = white_generalized(
        shape=shape,
        ppd=ppd,
        grating_frequency=grating_frequency,
        vbars=vbars,
        vtarget=vtarget,
        target_indices=target_indices,
        target_center_offsets=target_center_offsets,
        target_sizes=target_size,
        period=period,
        )
    return stim


def white_anderson(
    shape=(4, 4),
    ppd=20,
    grating_frequency=2,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices_top=5,
    target_indices_bottom=-6,
    target_center_offset=0.6,
    target_size=0.8,
    vstripes=(1., 0.),
    stripe_center_offset=0.8,
    stripe_size=0.8,
    period="ignore",
):
    """
    Anderson variation of White's stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    vstripes : (float, float)
        intensity values of horizontal stripes
    stripe_center_offset : float
        offset from stripe centers to image center in degree visual angle.
    stripe_size = float
        stripe size (i.e. height / length) in degrees visual angle
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = white_two_rows(
        shape=shape,
        ppd=ppd,
        grating_frequency=grating_frequency,
        vbars=vbars,
        vtarget=vtarget,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        period=period,
        )

    img = stim['img']
    mask = stim['mask']
    stripe_center_offset_px = degrees_to_pixels(stripe_center_offset, ppd)
    stripe_size_px = degrees_to_pixels(stripe_size, ppd)
    cycle_width_px = degrees_to_pixels(1. / (grating_frequency*2), ppd) * 2
    phase_width_px = cycle_width_px // 2
    height, width = img.shape
    nbars = width // phase_width_px
    ttop, tbot = np.array(target_indices_top), np.array(target_indices_bottom)
    ttop[ttop < 0] = nbars + ttop[ttop < 0]
    tbot[tbot < 0] = nbars + tbot[tbot < 0]

    if stripe_size_px/2. > stripe_center_offset_px:
        raise ValueError("Stripes overlap! Increase stripe offset or decrease stripe size.")
    if (target_size/2 - target_center_offset + stripe_size/2 - stripe_center_offset) > 0:
        raise ValueError("Stripes overlap with targets! Increase stripe or target offsets or decrease stripe or target size")
    if stripe_center_offset*ppd % 1 != 0:
        offsets_new = stripe_center_offset_px / ppd
        print("Warning: Anderson stripe offsets rounded to %s because of ppd" % offsets_new)

    # Add stripe at top
    ystart = height // 2 - stripe_center_offset_px - stripe_size_px // 2
    img[ystart:ystart+stripe_size_px, 0:phase_width_px*np.min(ttop)] = vstripes[0]
    img[ystart:ystart+stripe_size_px, phase_width_px*(np.max(ttop)+1)::] = vstripes[0]
    if (ystart < 0) or (ystart+stripe_size_px > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    # Add stripe at bottom
    ystart = height // 2 + stripe_center_offset_px - stripe_size_px // 2
    img[ystart:ystart+stripe_size_px, 0:phase_width_px*np.min(tbot)] = vstripes[1]
    img[ystart:ystart+stripe_size_px, phase_width_px*(np.max(tbot)+1)::] = vstripes[1]
    if (ystart < 0) or (ystart+stripe_size_px > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    return {"img": img, "mask": mask}


def white_howe(
    shape=(4, 4),
    ppd=20,
    grating_frequency=2,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices_top=5,
    target_indices_bottom=-6,
    target_center_offset=0.3,
    target_size=0.5,
    vstripes=(1., 0.),
    period="ignore",
):
    """
    Howe variation of White's stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    vstripes : (float, float)
        intensity values of horizontal stripes
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    return white_anderson(
        shape=shape,
        ppd=ppd,
        grating_frequency=grating_frequency,
        vbars=vbars,
        vtarget=vtarget,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        vstripes=vstripes,
        stripe_center_offset=target_center_offset,
        stripe_size=target_size,
        period=period,
        )


def white_yazdanbakhsh(
    shape=(4, 4),
    ppd=20,
    grating_frequency=2,
    vbars=(1., 0.),
    vtarget=0.5,
    target_indices_top=5,
    target_indices_bottom=-6,
    target_center_offset=0.6,
    target_size=1.,
    vstripes=(1., 0.),
    gap_size=0.2,
    period="ignore",
):
    """
    Yazsdanbakhsh variation of White's stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    vbars : (float, float)
        intensity values of bars
    vtarget : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    vstripes : (float, float)
        intensity values of horizontal stripes
    stripe_size = float
        stripe size (i.e. height / length) in degrees visual angle
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = white_two_rows(
        shape=shape,
        ppd=ppd,
        grating_frequency=grating_frequency,
        vbars=vbars,
        vtarget=vtarget,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        period=period,
        )

    img = stim['img']
    mask = stim['mask']
    gap_size_px = degrees_to_pixels(gap_size, ppd)
    target_offset_px = degrees_to_pixels(target_center_offset, ppd)
    tsize_px = degrees_to_pixels(target_size, ppd)
    cycle_width_px = degrees_to_pixels(1. / (grating_frequency*2), ppd) * 2
    phase_width_px = cycle_width_px // 2
    height, width = img.shape
    nbars = width // phase_width_px
    ttop, tbot = np.array(target_indices_top), np.array(target_indices_bottom)
    ttop[ttop < 0] = nbars + ttop[ttop < 0]
    tbot[tbot < 0] = nbars + tbot[tbot < 0]

    if isinstance(target_indices_top, (float, int)):
        ttop = (ttop,)
    if isinstance(target_indices_bottom, (float, int)):
        tbot = (tbot,)

    if any(t in ttop for t in tbot) and (target_offset_px - tsize_px//2 - gap_size_px) < 0:
        raise ValueError("Stripes overlap! Replace or decrease targets or decrease stripe size.")

    # Add stripes at top
    ystart = height // 2 - target_offset_px - gap_size_px - tsize_px // 2
    ystart2 = height // 2 - target_offset_px + tsize_px // 2
    for t in ttop:
        img[ystart:ystart+gap_size_px, t*phase_width_px:(t+1)*phase_width_px] = vstripes[0]
        img[ystart2:ystart2+gap_size_px, t*phase_width_px:(t+1)*phase_width_px] = vstripes[0]

    # Add stripes at bottom
    ystart = height // 2 + target_offset_px - tsize_px // 2 - gap_size_px
    ystart2 = height // 2 + target_offset_px + tsize_px // 2
    for t in tbot:
        img[ystart:ystart+gap_size_px, t*phase_width_px:(t+1)*phase_width_px] = vstripes[1]
        img[ystart2:ystart2+gap_size_px, t*phase_width_px:(t+1)*phase_width_px] = vstripes[1]

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "White flexible": white_generalized(),
        "White single row": white(),
        "White two rows": white_two_rows(),
        "Anderson's variation": white_anderson(),
        "Yazdanbakhsh variation": white_yazdanbakhsh(),
        "Howe's variation": white_howe(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
