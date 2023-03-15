import numpy as np
from scipy.signal import fftconvolve

from stimupy.utils import resolution
from stimupy.utils.pad import add_padding, remove_padding

__all__ = [
    "convolve",
    "bandpass",
]


def convolve(
    arr1,
    arr2,
    mode="same",
    axes=None,
    padding=False,
):
    """
    Convolve two N-dimensional arrays using FFT

    Parameters
    ----------
    arr1 : numpy.ndarray
        Input array 1
    arr2 : numpy.ndarray
        Input array 2
    mode : str {"full", "valid", "same"}, optional
        String which indicates the size of the output. The default is "same".
    axes : int or None (default), optional
        Axes over which to convolve. The default is over all axes
    padding : Bool
        if True, pad array before convolving

    Returns
    -------
    out : numpy.ndarray
        Output array

    """
    c = int(arr1.shape[0] / 2)
    if padding:
        arr1 = add_padding(arr1, c, arr1.mean())
    out = fftconvolve(arr1, arr2, mode, axes)
    if padding:
        out = remove_padding(out, c)
    return out


def bandpass(
    visual_size=None,
    ppd=None,
    shape=None,
    center_frequency=None,
    bandwidth=None,
):
    """
    Function to create a 2d bandpass filter in the frequency domain

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    center_frequency : float
        center frequency of filter in cpd
    bandwidth : float
        bandwidth of filter in octaves

    Returns
    -------
    dict[str, Any]
        dict with the filter (key: "img"),
        and additional keys containing filter parameters
    """
    if center_frequency is None:
        raise ValueError("bandpass() missing argument 'center_frequency' which is not 'None'")
    if bandwidth is None:
        raise ValueError("bandpass() missing argument 'bandwidth' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if center_frequency > (min(ppd) / 2):
        raise ValueError(
            f"Center frequency ({center_frequency}) should not exceed Nyquist limit {min(ppd)/2} (ppd/2)"
        )

    # Create frequency axes
    fy = np.fft.fftshift(np.fft.fftfreq(shape[0], d=1.0 / ppd[0]))
    fx = np.fft.fftshift(np.fft.fftfreq(shape[1], d=1.0 / ppd[1]))
    Fx, Fy = np.meshgrid(fx, fy)

    # Calculate the distance of each 2d spatial frequency from requested center frequency
    distance = np.abs(center_frequency - np.sqrt(Fx**2.0 + Fy**2.0))

    # Calculate sigma to eventuate given bandwidth (in octaves)
    sigma = (
        center_frequency
        / ((2.0**bandwidth + 1) * np.sqrt(2.0 * np.log(2.0)))
        * (2.0**bandwidth - 1)
    )

    # Create bandpass filter
    fil = 1.0 / (np.sqrt(2.0 * np.pi) * sigma) * np.exp(-(distance**2.0) / (2.0 * sigma**2.0))
    fil = fil / fil.max()

    stim = {
        "img": fil,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "center_frequency": center_frequency,
        "sigma": sigma,
        "frequency_extent": [fy[0], fy[-1], fx[0], fx[-1]],
    }

    return stim
