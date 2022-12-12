import numpy as np

from stimuli.components import square_wave
from stimuli.utils import degrees_to_pixels


__all__ = [
    "white_generalized",
    "white",
    "white_two_rows",
    "white_anderson",
    "white_howe",
    "white_yazdanbakhsh",
]

def white_generalized(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices=None,
    target_center_offsets=None,
    target_sizes=None,
    period="ignore",
):
    """
    White's stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of targets
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

    References
    ----------
    White, M. (1979). A new effect of pattern on perceived lightness. Perception,
        8(4), 413–416. https://doi.org/10.1068/p080413
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    height_px, width_px = degrees_to_pixels(visual_size, ppd)
    target_offsets_px = degrees_to_pixels(target_center_offsets, ppd)
    target_sizes_px = degrees_to_pixels(target_sizes, ppd)
    cycle_width_px = degrees_to_pixels(1.0 / (grating_frequency * 2), ppd) * 2
    phase_width_px = cycle_width_px // 2

    if isinstance(target_center_offsets, (float, int)):
        target_center_offsets = (target_center_offsets,) * len(target_indices)
        target_offsets_px = (target_offsets_px,) * len(target_indices)
    if len(intensity_bars) != 2:
        raise ValueError("intensity_bars needs to be a tuple of two floats")
    if len(target_indices) != len(target_offsets_px):
        raise ValueError("# of target indices != # of target offsets")
    if not isinstance(intensity_target, (float, int)):
        raise ValueError("intensity_target should be a single float / int")
    if isinstance(target_sizes, (float, int)):
        target_sizes = (target_sizes,) * len(target_indices)
        target_sizes_px = (target_sizes_px,) * len(target_indices)
    if any(np.array(target_center_offsets) * ppd % 1 != 0):
        offsets_new = target_offsets_px / ppd
        print(
            "Warning: White target offsets rounded from %s to %s because of ppd"
            % (target_center_offsets, offsets_new)
        )
    if len(target_sizes) != len(target_indices):
        raise ValueError("# of target indices != # of target sizes")

    stim = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=grating_frequency,
        intensity_bars=intensity_bars,
        period=period,
    )
    img = stim["img"]
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
            phases = int(2 * (int(visual_size[1] * ppd / phase_width_px) // 2))
            x_start = int((phases + index) * phase_width_px)
        x_end = x_start + phase_width_px

        img[y_start:y_end, x_start:x_end] = intensity_target
        mask[y_start:y_end, x_start:x_end] = i + 1

    new_size = (img.shape[0] / ppd, img.shape[1] / ppd)
    if period != "ignore" and visual_size != new_size:
        print("Warning: White shape changed from %s to %s" % (visual_size, new_size))

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "grating_frequency": grating_frequency,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_indices": target_indices,
        "target_center_offsets": target_center_offsets,
        "target_sizes": target_sizes,
        "period": period,
    }

    return stim


def white(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices=(1, 3, -2, -4),
    target_size=None,
    period="ignore",
):
    """
    White's stimulus where all targets are vertically aligned at half the stimulus height

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
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

    References
    ----------
    White, M. (1979). A new effect of pattern on perceived lightness. Perception,
        8(4), 413–416. https://doi.org/10.1068/p080413
    """

    stim = white_generalized(
        visual_size=visual_size,
        ppd=ppd,
        grating_frequency=grating_frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices=target_indices,
        target_center_offsets=0,
        target_sizes=target_size,
        period=period,
    )
    return stim


# TODO: Add another function in which you specify n_targets instead of target_indices
def white_two_rows(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=None,
    target_size=None,
    period="ignore",
):
    """
    White's stimulus where targets are placed in two rows (top, bottom) that have the same
    distance from the center.

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
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

    References
    ----------
    White, M. (1979). A new effect of pattern on perceived lightness. Perception,
        8(4), 413–416. https://doi.org/10.1068/p080413
    """
    if not isinstance(target_center_offset, (float, int)):
        raise ValueError("target_center_offset should be a single float / int")
    if isinstance(target_indices_top, (float, int)):
        target_indices_top = (target_indices_top,)
    if isinstance(target_indices_bottom, (float, int)):
        target_indices_bottom = (target_indices_bottom,)

    target_indices = target_indices_top + target_indices_bottom
    offsets_top = (-target_center_offset,) * len(target_indices_top)
    offsets_bottom = (target_center_offset,) * len(target_indices_bottom)
    target_center_offsets = offsets_top + offsets_bottom

    stim = white_generalized(
        visual_size=visual_size,
        ppd=ppd,
        grating_frequency=grating_frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices=target_indices,
        target_center_offsets=target_center_offsets,
        target_sizes=target_size,
        period=period,
    )
    return stim


def white_anderson(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=None,
    target_size=None,
    intensity_stripes=(1.0, 0.0),
    stripe_center_offset=None,
    stripe_size=None,
    period="ignore",
):
    """
    Anderson variation of White's stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    intensity_stripes : (float, float)
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

    References
    -----------
    Anderson, B. L. (2001). Contrasting theories of White’s illusion. Perception, 30, 1499–1501
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005). Oriented multiscale spatial ﬁltering
        and contrast normalization: a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast. Vision Research,
        45, 607–615.
    """

    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        grating_frequency=grating_frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        period=period,
    )

    img = stim["img"]
    mask = stim["mask"]
    stripe_center_offset_px = degrees_to_pixels(stripe_center_offset, ppd)
    stripe_size_px = degrees_to_pixels(stripe_size, ppd)
    cycle_width_px = degrees_to_pixels(1.0 / (grating_frequency * 2), ppd) * 2
    phase_width_px = cycle_width_px // 2
    height, width = img.shape
    nbars = width // phase_width_px
    ttop, tbot = np.array(target_indices_top), np.array(target_indices_bottom)
    ttop[ttop < 0] = nbars + ttop[ttop < 0]
    tbot[tbot < 0] = nbars + tbot[tbot < 0]

    if stripe_size_px / 2.0 > stripe_center_offset_px:
        raise ValueError("Stripes overlap! Increase stripe offset or decrease stripe size.")
    if (target_size / 2 - target_center_offset + stripe_size / 2 - stripe_center_offset) > 0:
        raise ValueError(
            "Stripes overlap with targets! Increase stripe or target offsets or"
            "decrease stripe or target size"
        )
    if stripe_center_offset * ppd % 1 != 0:
        offsets_new = stripe_center_offset_px / ppd
        print(
            "Warning: Anderson stripe offsets rounded from %s to %s because of ppd"
            % (stripe_center_offset, offsets_new)
        )

    # Add stripe at top
    ystart = height // 2 - stripe_center_offset_px - stripe_size_px // 2
    img[ystart : ystart + stripe_size_px, 0 : phase_width_px * np.min(ttop)] = intensity_stripes[0]
    img[
        ystart : ystart + stripe_size_px, phase_width_px * (np.max(ttop) + 1) : :
    ] = intensity_stripes[0]
    if (ystart < 0) or (ystart + stripe_size_px > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    # Add stripe at bottom
    ystart = height // 2 + stripe_center_offset_px - stripe_size_px // 2
    img[ystart : ystart + stripe_size_px, 0 : phase_width_px * np.min(tbot)] = intensity_stripes[1]
    img[
        ystart : ystart + stripe_size_px, phase_width_px * (np.max(tbot) + 1) : :
    ] = intensity_stripes[1]
    if (ystart < 0) or (ystart + stripe_size_px > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "grating_frequency": grating_frequency,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_indices_top": target_indices_top,
        "target_indices_bottom": target_indices_bottom,
        "target_center_offset": target_center_offset,
        "target_size": target_size,
        "period": period,
    }

    return {"img": img, "mask": mask, **params}


def white_howe(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=None,
    target_size=None,
    intensity_stripes=(1.0, 0.0),
    period="ignore",
):
    """
    Howe variation of White's stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    intensity_stripes : (float, float)
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

    References
    -----------
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005). Oriented multiscale spatial ﬁltering
        and contrast normalization: a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast. Vision Research,
        45, 607–615.
    Howe, P. D. L. (2001). A comment on the Anderson (1997), the Todorovic (1997), and the Ross
        and Pessoa (2000) explanations of White’s eﬀect. Perception, 30, 1023–1026
    """
    return white_anderson(
        visual_size=visual_size,
        ppd=ppd,
        grating_frequency=grating_frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        intensity_stripes=intensity_stripes,
        stripe_center_offset=target_center_offset,
        stripe_size=target_size,
        period=period,
    )


def white_yazdanbakhsh(
    visual_size=None,
    ppd=None,
    grating_frequency=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=None,
    target_size=None,
    intensity_stripes=(1.0, 0.0),
    gap_size=None,
    period="ignore",
):
    """
    Yazsdanbakhsh variation of White's stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        the spatial frequency of the grating in cycles per degree
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_size : float
        target size (i.e. height / length) in degrees visual angle
    intensity_stripes : (float, float)
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

    References
    ----------
    Yazdanbakhsh, A., Arabzadeh, E., Babadi, B., and Fazl, A. (2002). Munker-White-
        like illusions without T-junctions. Perception 31, 711–715.
        https://doi.org/10.1068/p3348
    """

    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        grating_frequency=grating_frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_size=target_size,
        period=period,
    )

    img = stim["img"]
    mask = stim["mask"]
    gap_size_px = degrees_to_pixels(gap_size, ppd)
    target_offset_px = degrees_to_pixels(target_center_offset, ppd)
    tsize_px = degrees_to_pixels(target_size, ppd)
    cycle_width_px = degrees_to_pixels(1.0 / (grating_frequency * 2), ppd) * 2
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

    if any(t in ttop for t in tbot) and (target_offset_px - tsize_px // 2 - gap_size_px) < 0:
        raise ValueError("Stripes overlap! Replace or decrease targets or decrease stripe size.")

    # Add stripes at top
    ystart = height // 2 - target_offset_px - gap_size_px - tsize_px // 2
    ystart2 = height // 2 - target_offset_px + tsize_px // 2
    for t in ttop:
        img[
            ystart : ystart + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[0]
        img[
            ystart2 : ystart2 + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[0]

    # Add stripes at bottom
    ystart = height // 2 + target_offset_px - tsize_px // 2 - gap_size_px
    ystart2 = height // 2 + target_offset_px + tsize_px // 2
    for t in tbot:
        img[
            ystart : ystart + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[1]
        img[
            ystart2 : ystart2 + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[1]

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "grating_frequency": grating_frequency,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_indices_top": target_indices_top,
        "target_indices_bottom": target_indices_bottom,
        "target_center_offset": target_center_offset,
        "target_size": target_size,
        "period": period,
    }

    return {"img": img, "mask": mask, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "visual_size": 10,
        "ppd": 10,
        "grating_frequency": 0.5,
        }

    stims = {
        "White flexible": white_generalized(**params, target_indices=(1, 3), target_center_offsets=(-1, -3), target_sizes=(2, 3)),
        "White single row": white(**params, target_indices=(2, -3), target_size=2),
        "White two rows": white_two_rows(**params, target_indices_top=(2,4), target_indices_bottom=(-2, -4), target_size=1, target_center_offset=2),
        "Anderson's variation": white_anderson(**params, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2, stripe_center_offset=1.5, stripe_size=2),
        "Yazdanbakhsh variation": white_yazdanbakhsh(**params, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2, gap_size=0.5),
        "Howe's variation": white_howe(**params, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2),
    }

    plot_stimuli(stims, mask=False, save=None)
