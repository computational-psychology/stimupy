import numpy as np


def transparency(img, mask=None, alpha=0.5, tau=0.2):
    """Applies a transparency to image at specified (mask) location if provided

    Parameters
    ----------
    img : np.array
        image to which transparancy will be applied
    mask : np.array or None (default)
        if not None, transparancy will be provided at non-zero locations
        provided in this mask
    alpha : Number
        alpha of transparency (i.e. how transparant the medium is), default 0.2
    tau : Number
        tau of transparency (i.e. value of transparent medium), default 0.5

    Returns
    -------
    img with the applied transparency
    """
    if mask is None:
        mask = np.ones(img.shape)
    img = np.where(mask, alpha * img + (1 - alpha) * tau, img)
    return img


def adapt_michelson_contrast(stim, michelson_contrast, mean_luminance=None):
    """
    Adapt Michelson contrast of image

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least keys "img" and "mask"
    michelson_contrast : float
        desired Michelson contrast
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    -------
    Updated stimulus dict with keys "img", "michelson_contrast" and "mean_luminance"

    """
    if mean_luminance is None:
        mean_luminance = stim["img"].mean()

    # Adapt Michelson contrast
    img = (stim["img"] - stim["img"].min()) / (stim["img"].max() - stim["img"].min())
    img = img * michelson_contrast * 2.0 * mean_luminance
    img += mean_luminance - michelson_contrast * mean_luminance

    stim["img"] = img
    stim["michelson_contrast"] = michelson_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_rms_contrast(stim, rms_contrast, mean_luminance=None):
    """
    Adapt rms contrast of image (std)

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least keys "img" and "mask"
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    -------
    Updated stimulus dict with keys "img", "rms_contrast" and "mean_luminance"

    """
    if mean_luminance is None:
        mean_luminance = stim["img"].mean()

    img = stim["img"] - stim["img"].mean()
    img = img / img.std() * rms_contrast + mean_luminance

    stim["img"] = img
    stim["rms_contrast"] = rms_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_normalized_rms_contrast(stim, rms_contrast, mean_luminance=None):
    """
    Adapt normalized rms contrast of image (std divided by mean)

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least keys "img"
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    -------
    Updated stimulus dict with keys "img", "rms_contrast" and "mean_luminance"

    """
    if mean_luminance is None:
        mean_luminance = stim["img"].mean()

    img = stim["img"] - stim["img"].mean()
    img = img / img.std() * rms_contrast * mean_luminance + mean_luminance

    stim["img"] = img
    stim["rms_contrast"] = rms_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_intensity_range(stim, intensity_min=0.0, intensity_max=1.0):
    """
    Adapt intensity range of image

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least keys "img"
    intensity_min : float
        new minimal intensity value
    intensity_max : float
        new maximal intensity value

    Returns
    -------
    Updated stimulus dict with keys "img", "intensity_min" and "intensity_max"

    """

    img = (stim["img"] - stim["img"].min()) / (stim["img"].max() - stim["img"].min())
    img = img * (intensity_max - intensity_min) + intensity_min

    stim["img"] = img
    stim["intensity_min"] = intensity_min
    stim["intensity_max"] = intensity_max
    return stim
