import numpy as np

__all__ = [
    "transparency",
    "adapt_michelson_contrast",
    "adapt_rms_contrast",
    "adapt_normalized_rms_contrast",
    "adapt_intensity_range",
    "adapt_michelson_contrast_dict",
    "adapt_rms_contrast_dict",
    "adapt_normalized_rms_contrast_dict",
    "adapt_intensity_range_dict",
]


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


def adapt_michelson_contrast(img, michelson_contrast, mean_luminance=None):
    """
    Adapt Michelson contrast of image

    Parameters
    ----------
    img : np.ndarray
        stimulus array
    michelson_contrast : float
        desired Michelson contrast
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    img : np.ndarray
        image with adapted michelson contrast and mean luminance if passed
    """
    if mean_luminance is None:
        mean_luminance = img.mean()

    # Adapt Michelson contrast
    img = (img - img.min()) / (img.max() - img.min())
    img = img * michelson_contrast * 2.0 * mean_luminance
    img += mean_luminance - michelson_contrast * mean_luminance
    return img


def adapt_rms_contrast(img, rms_contrast, mean_luminance=None):
    """
    Adapt rms contrast of image (std)

    Parameters
    ----------
    img : np.ndarray
        stimulus array
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    img : np.ndarray
        image with adapted rms contrast and mean luminance if passed
    """
    if mean_luminance is None:
        mean_luminance = img.mean()

    # Adapt rms contrast
    img = img - img.mean()
    img = img / img.std() * rms_contrast + mean_luminance
    return img


def adapt_normalized_rms_contrast(img, rms_contrast, mean_luminance=None):
    """
    Adapt normalized rms contrast of image (std divided by mean)

    Parameters
    ----------
    img : np.ndarray
        stimulus array
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    img : np.ndarray
        image with adapted rms contrast and mean luminance if passed
    """
    if mean_luminance is None:
        mean_luminance = img.mean()

    img = img - img.mean()
    img = img / img.std() * rms_contrast * mean_luminance + mean_luminance
    return img


def adapt_intensity_range(img, intensity_min=0.0, intensity_max=1.0):
    """
    Adapt intensity range of image

    Parameters
    ----------
    img : np.ndarray
        stimulus array
    intensity_min : float
        new minimal intensity value
    intensity_max : float
        new maximal intensity value

    Returns
    ----------
    img : np.ndarray
        image with adapted intensity range
    """

    img = (img - img.min()) / (img.max() - img.min())
    img = img * (intensity_max - intensity_min) + intensity_min
    return img


def adapt_michelson_contrast_dict(stim, michelson_contrast, mean_luminance=None):
    """
    Adapt Michelson contrast of image in dict

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least key "img"
    michelson_contrast : float
        desired Michelson contrast
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        Michelson contrast (key: "michelson_contrast"),
        mean luminance ("mean_luminance")
        and additional keys containing stimulus parameters
    """

    # Adapt Michelson contrast of image
    img = adapt_michelson_contrast(stim["img"], michelson_contrast, mean_luminance)

    stim["img"] = img
    stim["michelson_contrast"] = michelson_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_rms_contrast_dict(stim, rms_contrast, mean_luminance=None):
    """
    Adapt rms contrast of image (std)

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least key "img"
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        RMS contrast (key: "rms_contrast"),
        mean luminance ("mean_luminance")
        and additional keys containing stimulus parameters
    """
    # Adapt rms_contrast of image
    img = adapt_rms_contrast(stim["img"], rms_contrast, mean_luminance)

    stim["img"] = img
    stim["rms_contrast"] = rms_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_normalized_rms_contrast_dict(stim, rms_contrast, mean_luminance=None):
    """
    Adapt normalized rms contrast of image (std divided by mean)

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least key "img"
    rms_contrast : float
        desired rms contrast (std divided by mean intensity)
    mean_luminance : float
        desired mean luminance; if None (default), dont change mean luminance

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        RMS contrast (key: "rms_contrast"),
        mean luminance ("mean_luminance")
        and additional keys containing stimulus parameters
    """

    # Adapt normalized rms contrast
    img = adapt_normalized_rms_contrast(stim["img"], rms_contrast, mean_luminance)

    stim["img"] = img
    stim["rms_contrast"] = rms_contrast
    stim["mean_luminance"] = mean_luminance
    return stim


def adapt_intensity_range_dict(stim, intensity_min=0.0, intensity_max=1.0):
    """
    Adapt intensity range of image

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing at least key "img"
    intensity_min : float
        new minimal intensity value
    intensity_max : float
        new maximal intensity value

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        intensity range (key: "intensity_range"),
        and additional keys containing stimulus parameters
    """

    img = adapt_intensity_range(stim["img"], intensity_min, intensity_max)

    stim["img"] = img
    stim["intensity_range"] = (intensity_min, intensity_max)
    return stim
