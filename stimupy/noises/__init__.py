import numpy as np


def randomize_sign(array):
    """Randomize the sign of values in an array

    Parameters
    ----------
    array
        N-dimensional array

    Returns
    -------
    array
        Same array with randomized signs

    """
    sign = np.random.rand(*array.shape) - 0.5
    sign[sign <= 0.0] = -1.0
    sign[sign > 0.0] = 1.0
    array = array * sign
    return array


def pseudo_white_helper(
    shape,
    amplitude,
):
    """Generate pseudorandom white noise patch

    Parameters
    ----------
    shape : int or (int, int)
        Shape of noise patch in pixels (height, width)
    amplitude
        Amplitude of each (pos/neg) frequency component = A/2

    Returns
    -------
    output
        Pseudorandom white noise patch

    """
    if isinstance(shape, (float, int)):
        shape = (shape, shape)

    Re = np.random.rand(*shape) * amplitude - amplitude / 2.0
    Im = np.sqrt((amplitude / 2.0) ** 2 - Re**2)
    Im = randomize_sign(Im)
    output = Re + Im * 1j
    return output


def pseudo_white_spectrum(
    shape=(100, 100),
    amplitude=2.0,
):
    """Create pseudorandom white noise spectrum

    Code translated and adapted from Matlab scripts
    provided by T. Peromaa

    Parameters
    ----------
    shape : int or (int, int)
        Shape of noise array in pixels (height, width)
    amplitude
        Amplitude of noise power spectrum

    Returns
    -------
    spectrum
        Shifted 2d complex number spectrum. DC = 0.
        Amplitude of each (pos/neg) frequency component = A/2
        Power of each (pos/neg) frequency component = (A/2)**2

    """
    if isinstance(shape, (float, int)):
        shape = (shape, shape)

    y, x = shape
    A = amplitude

    if (y % 2 != 0) or (x % 2 != 0):
        raise ValueError("shape needs to be even-numbered")

    # We divide the noise spectrum in four quadrants with pseudorandom white noise
    quadrant1 = pseudo_white_helper((int(y / 2) - 1, int(x / 2) - 1), A)
    quadrant2 = pseudo_white_helper((int(y / 2) - 1, int(x / 2) - 1), A)
    quadrant3 = quadrant2[::-1, ::-1].conj()
    quadrant4 = quadrant1[::-1, ::-1].conj()

    # We place the quadrants in the spectrum to eventuate that each frequency component has
    # an amplitude of A/2
    spectrum = np.zeros([y, x], dtype=complex)
    spectrum[1 : int(y / 2), 1 : int(x / 2)] = quadrant1
    spectrum[1 : int(y / 2), int(x / 2) + 1 : x] = quadrant2
    spectrum[int(y / 2 + 1) : y, 1 : int(x / 2)] = quadrant3
    spectrum[int(y / 2 + 1) : y, int(x / 2 + 1) : x] = quadrant4

    # We need to fill the rows / columns that the quadrants do not cover
    # Fill first row:
    row = pseudo_white_helper((1, x), A)
    apu = np.fliplr(row)
    row[0, int(x / 2 + 1) : x] = apu[0, int(x / 2) : x - 1].conj()
    spectrum[0, :] = np.squeeze(row)

    # Fill central row:
    row = pseudo_white_helper((1, x), A)
    apu = np.fliplr(row)
    row[0, int(x / 2 + 1) : x] = apu[0, int(x / 2) : x - 1].conj()
    spectrum[int(y / 2), :] = np.squeeze(row)

    # Fill first column:
    col = pseudo_white_helper((y, 1), A)
    apu = np.flipud(col)
    col[int(y / 2 + 1) : y, 0] = apu[int(y / 2) : y - 1, 0].conj()
    spectrum[:, int(x / 2)] = np.squeeze(col)

    # Fill central column:
    col = pseudo_white_helper((y, 1), A)
    apu = np.flipud(col)
    col[int(y / 2 + 1) : y, 0] = apu[int(y / 2) : y - 1, 0].conj()
    spectrum[:, 0] = np.squeeze(col)

    # Set amplitude at filled-corners to A/2:
    spectrum[0, 0] = -A / 2 + 0j
    spectrum[0, int(x / 2)] = -A / 2 + 0j
    spectrum[int(y / 2), 0] = -A / 2 + 0j

    # Set DC = 0:
    spectrum[int(y / 2), int(x / 2)] = 0 + 0j
    return spectrum


from stimupy.noises import binaries, narrowbands, naturals, whites

__all__ = [
    "overview",
    "plot_overview",
    "pseudo_white_spectrum",
    "binaries",
    "narrowbands",
    "naturals",
    "whites",
]


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    stimuli = {}
    for stimmodule_name in __all__:
        if stimmodule_name in [
            "overview",
            "plot_overview",
            "pseudo_white_spectrum",
        ]:
            continue

        print(f"Generating stimuli from {stimmodule_name}")
        # Get a reference to the actual module
        # print(globals())
        stimmodule = globals()[stimmodule_name]

        print(stimmodule)
        try:
            stims = stimmodule.overview()

            # Accumulate
            stimuli.update(stims)
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stimuli


def plot_overview(mask=False, save=None, units="deg"):
    """Plot overview of examples in this module (and submodules)

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim

    """
    from stimupy.utils import plot_stimuli

    stims = overview(skip=True)
    plot_stimuli(stims, mask=mask, units=units, save=save)


if __name__ == "__main__":
    plot_overview()
