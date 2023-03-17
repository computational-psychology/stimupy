import numpy as np

__all__ = [
    "avg_target_values",
    "avg_img_values",
    "all_img_values",
    "img_values",
]


def avg_target_values(stim, mask_key="target_mask", f_average=np.median):
    """Average pixel value in each target region of stimulus

    Parameters
    ----------
    stim : dict[str: Any]
        stimulus-dict with at least "img" and "mask"
        containing the stimulus image and integer-mask, respectively.
    mask_key : str
        string with mask-key name
    f_average: function, default=numpy.median
        How to average/summarise the pixels in each target region

    Returns
    -------
    list[float]
        each entry in the list is the average value of pixels in target region,
        index in the list is the integer index in the mask

    See Also
    --------
    avg_img_values
    """
    return avg_img_values(image=stim["img"], mask=stim[mask_key], f_average=f_average)


def avg_img_values(image, mask, f_average=np.median):
    """Average values of pixels in image, per target region in integer mask

    Values are calculated as means or medians, depending on the mode.

    Parameters
    ----------
    image : 2D numpy array
        2D numpy array containing pixel values of the image
    mask : 2D numpy array
        2D numpy array of same size as image. Each target patch has an integer value.
        Each pixel inside this patch has this integer value.
        Patches do not need to be continuous.
    f_average: function, default=numpy.median
        How to average/summarise the pixels in each target region

    Returns
    -------
    list[float]
        each entry in the list is the average value of pixels in target region,
        index in the list is the integer index in the mask

    See Also
    --------
    all_img_values
    """
    masked_outputs = all_img_values(image, mask)
    values = [f_average(o[np.isfinite(o)]) for o in masked_outputs]

    return values


def all_img_values(img, mask):
    """Isolate all image values/pixels, per target region specified in integer mask

    Parameters
    ----------
    img : numpy.ndarray
        Image-array of pixel values to be masked
    mask : numpy.ndarray
        Array of same size as img.
        Each region-of-interest in mask is represented by an integer index.
        Each pixel inside this patch has this integer value.
        Patches do not need to be contiguous.

    Returns
    -------
    list[numpy.arrays]
        Each image/element of the list is a numpy.ndarray representing an image.
        There is one image for each target patch in the integer mask.
        In each image all values are set to NaN
        except the ones corresponding to the target values of the respective target patch.

    See Also
    --------
    img_values

    """
    idc = np.unique(mask.astype(int))
    imgs = [img_values(img, mask == idx) for idx in idc]
    return imgs


def img_values(img, mask):
    """Isolate only image pixels specified by a binary mask

    Parameters
    ----------
    img : numpy.ndarray
        Image-array of pixel values to be masked
    mask : numpy.ndarray
        Array of same size as img.
        All non-zero pixels/values are treated as ones in a binary bit mask.

    Returns
    -------
    numpy.ndarray
        numpy.ndarray of same size as img.
        All bits corresponding to zero bits in the mask are set to NaN.
    """

    return np.where(mask, img, np.nan)
