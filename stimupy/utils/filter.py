import numpy as np


def bandpass_filter(fx, fy, fcenter, sigma):
    """Function to create a bandpass filter

    Parameters
    ----------
    fx
        Array with frequencies in x-direction.
    fy
        Array with frequencies in y-direction.
    fcenter
        Center frequency of the bandpass filter
    sigma
        Sigma that defines the spread of the Gaussian in deg.

    Returns
    -------
    dog
        2D Difference-of-Gaussian filter in frequency domain.

    """
    # Calculate the distance of each 2d spatial frequency from requested center frequency
    distance = np.abs(fcenter - np.sqrt(fx**2.0 + fy**2.0))

    # Create bandpass filter:
    gauss = (
        1.0 / (np.sqrt(2.0 * np.pi) * sigma) * np.exp(-(distance**2.0) / (2.0 * sigma**2.0))
    )
    gauss = gauss / gauss.max()
    return gauss


# Create oriented Gaussian filter:
def oriented_filter(fx, fy, sigma, orientation):
    # convert orientation parameter to radians
    theta = np.deg2rad(orientation)

    # determine a, b, c coefficients
    a = np.cos(theta) ** 2 / (2 * sigma**2)
    b = -(np.sin(2 * theta) / (4 * sigma**2))
    c = np.sin(theta) ** 2 / (2 * sigma**2)

    # create Gaussian
    ofilter = np.exp(-(a * fx**2 + 2 * b * fx * fy + c * fy**2))
    return ofilter


# Apply Gaussian envelope to a stimulus
def apply_gaussian_env(stimulus, sigma):
    # Inputs:
    #    stimulus: Input stimulus, numpy array
    #    sigma: Sigma of Gaussian in px
    #    norm: Bool, if True normalize output array between 0 and 1
    # Output:
    # 2d numpy array with stimulus multiplied with Gaussian envelope

    # Create a meshgrid:
    size = stimulus.shape[0]
    xx, yy = np.mgrid[:size, :size] - size / 2.0

    # Create a Gaussian envelope:
    gauss = (
        1.0
        / (np.sqrt(2.0 * np.pi) * sigma)
        * np.exp(-(xx**2.0 + yy**2.0) / (2.0 * sigma**2.0))
    )
    gauss = gauss / gauss.max()
    stimulus = stimulus * gauss
    return stimulus
