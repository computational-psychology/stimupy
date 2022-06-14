"""
Functions to create images with different noises

Created on 23.09.2021
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import randomize_sign, bandpass_filter, oriented_filter


def pseudo_white_noise_patch(shape, A):
    """Helper function used to generate pseudorandom white noise patch.

    Parameters
    ----------
    shape
        Shape of noise patch
    A
        Amplitude of each (pos/neg) frequency component = A/2

    Returns
    -------
    output
        Pseudorandom white noise patch

    """
    Re = np.random.rand(*shape) * A - A/2.
    Im = np.sqrt((A/2.)**2 - Re**2)
    Im = randomize_sign(Im)
    output = Re+Im*1j
    return output


def pseudo_white_noise(n, A=2.):
    """Function to create pseudorandom white noise. Code translated and adapted
    from Matlab scripts provided by T. Peromaa

    Parameters
    ----------
    n
        Even-numbered size of output
    A
        Amplitude of noise power spectrum

    Returns
    -------
    spectrum
        Shifted 2d complex number spectrum. DC = 0.
        Amplitude of each (pos/neg) frequency component = A/2
        Power of each (pos/neg) frequency component = (A/2)**2

    """
    # We divide the noise spectrum in four quadrants with pseudorandom white noise
    quadrant1 = pseudo_white_noise_patch((int(n/2)-1, int(n/2)-1), A)
    quadrant2 = pseudo_white_noise_patch((int(n/2)-1, int(n/2)-1), A)
    quadrant3 = quadrant2[::-1, ::-1].conj()
    quadrant4 = quadrant1[::-1, ::-1].conj()

    # We place the quadrants in the spectrum to eventuate that each frequency component has
    # an amplitude of A/2
    spectrum = np.zeros([n, n], dtype=complex)
    spectrum[1:int(n/2), 1:int(n/2)] = quadrant1
    spectrum[1:int(n/2), int(n/2)+1:n] = quadrant2
    spectrum[int(n/2+1):n, 1:int(n/2)] = quadrant3
    spectrum[int(n/2+1):n, int(n/2+1):n] = quadrant4

    # We need to fill the rows / columns that the quadrants do not cover
    # Fill first row:
    row = pseudo_white_noise_patch((1, n), A)
    apu = np.fliplr(row)
    row[0, int(n/2+1):n] = apu[0, int(n/2):n-1].conj()
    spectrum[0, :] = np.squeeze(row)

    # Fill central row:
    row = pseudo_white_noise_patch((1, n), A)
    apu = np.fliplr(row)
    row[0, int(n/2+1):n] = apu[0, int(n/2):n-1].conj()
    spectrum[int(n/2), :] = np.squeeze(row)

    # Fill first column:
    col = pseudo_white_noise_patch((n, 1), A)
    apu = np.flipud(col)
    col[int(n/2+1):n, 0] = apu[int(n/2):n-1, 0].conj()
    spectrum[:, int(n/2)] = np.squeeze(col)

    # Fill central column:
    col = pseudo_white_noise_patch((n, 1), A)
    apu = np.flipud(col)
    col[int(n/2+1):n, 0] = apu[int(n/2):n-1, 0].conj()
    spectrum[:, 0] = np.squeeze(col)

    # Set amplitude at filled-corners to A/2:
    spectrum[0, 0] = -A/2 + 0j
    spectrum[0, int(n/2)] = -A/2 + 0j
    spectrum[int(n/2), 0] = -A/2 + 0j

    # Set DC = 0:
    spectrum[int(n/2), int(n/2)] = 0 + 0j
    return spectrum


def white_noise(size: int, rms_contrast=0.2, pseudo_noise=True):
    """Function to create white noise.

    Parameters
    ----------
    size
        Size of noise image.
    rms_contrast
        rms contrast of noise.
    pseudo_noise
        Bool, if True generate pseudorandom noise with perfectly smooth
        power spectrum.

    Returns
    -------
    white_noise
        2D array with white noise.

    """

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_noise(size)

        # ifft
        white_noise = np.fft.ifft2(np.fft.ifftshift(white_noise_fft))
        white_noise = np.real(white_noise)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(size, size) * 2. - 1.

    # Adjust noise rms contrast:
    white_noise = rms_contrast * white_noise / white_noise.std()
    return white_noise


def narrowband_noise(size: int, noisefreq: float, ppd=60., rms_contrast=0.2, pseudo_noise=True):
    """Function to create narrowband noise.

    Parameters
    ----------
    size
        Size of noise image.
    noisefreq
        Noise center frequency in cpd.
    ppd
        Spatial resolution (pixels per degree).
    rms_contrast
        rms contrast of noise.
    pseudo_noise
        Bool, if True generate pseudorandom noise with perfectly smooth
        power spectrum.

    Returns
    -------
    narrow_noise
        2D array with narrowband noise.

    """

    # We calculate sigma to eventuate a ratio bandwidth of 1 octave
    sigma = noisefreq / (3.*np.sqrt(2.*np.log(2.)))

    # Prepare spatial frequency axes and create bandpass filter:
    fs = np.fft.fftshift(np.fft.fftfreq(size, d=1./ppd))
    fx, fy = np.meshgrid(fs, fs)
    bp_filter = bandpass_filter(fx, fy, noisefreq, sigma)

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_noise(size)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(size, size) * 2. - 1.
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Filter white noise with bandpass filter
    narrow_noise_fft = white_noise_fft * bp_filter

    # ifft
    narrow_noise = np.fft.ifft2(np.fft.ifftshift(narrow_noise_fft))
    narrow_noise = np.real(narrow_noise)

    # Adjust noise rms contrast:
    narrow_noise = rms_contrast * narrow_noise / narrow_noise.std()
    return narrow_noise


def pink_noise(size: int, ppd=60., rms_contrast=0.2, exponent=2., pseudo_noise=True):
    """Function to create narrowband noise.

    Parameters
    ----------
    size
        Size of noise image.
    ppd
        Spatial resolution (pixels per degree).
    rms_contrast
        rms contrast of noise.
    exponent
        Exponent used to create 1/f**exponent noise.
    pseudo_noise
        Bool, if True generate pseudorandom noise with perfectly smooth
        power spectrum.

    Returns
    -------
    pink_noise
        2D array with pink noise.

    """

    # Prepare spatial frequency axes and create bandpass filter:
    fs = np.fft.fftshift(np.fft.fftfreq(size, d=1./ppd))
    fx, fy = np.meshgrid(fs, fs)

    # Needed to create 2d 1/f**exponent noise. Prevent division by zero.
    # Note: The noise amplitude at DC is 0.
    f = np.sqrt(fx**2. + fy**2.)
    f = f**exponent
    f[f == 0.] = 1.

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_noise(size)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(size, size) * 2. - 1.
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Create 1/f noise:
    pink_noise_fft = white_noise_fft / f

    # ifft
    pink_noise = np.fft.ifft2(np.fft.ifftshift(pink_noise_fft))
    pink_noise = np.real(pink_noise)

    # Adjust noise rms contrast:
    pink_noise = rms_contrast * pink_noise / pink_noise.std()
    return pink_noise


# Create oriented noise:
def oriented_noise(noise, sigma, orientation, ppd=60., rms_contrast=0.2):
    nX = noise.shape[0]

    # Prepare spatial frequency axes and create bandpass filter:
    fs = np.fft.fftshift(np.fft.fftfreq(nX, d=1./ppd))
    fx, fy = np.meshgrid(fs, fs)
    ofilter = oriented_filter(fx, fy, sigma, orientation)

    noise_fft = np.fft.fftshift(np.fft.fft2(noise))
    ori_noise_fft = noise_fft * ofilter
    ori_noise = np.fft.ifft2(np.fft.ifftshift(ori_noise_fft))
    ori_noise = np.real(ori_noise)

    # Re-adjust noise rms contrast:
    ori_noise = rms_contrast * ori_noise / ori_noise.std()
    return ori_noise
