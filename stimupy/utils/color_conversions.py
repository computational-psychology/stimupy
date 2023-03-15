import numpy as np

__all__ = [
    "luminance2munsell",
    "munsell2luminance",
]


def luminance2munsell(lum_values, reference_white):
    """
    Transform luminance values into Munsell values.
    The luminance values do not have to correspond to specific units, as long
    as they are in the same unit as the reference white, because Munsell values
    are a perceptually uniform scale of relative luminances.

    Parameters
    ----------
    lum_values : numpy-array
    reference_white : number

    Returns
    -------
    munsell_values : numpy-array

    Reference: H. Pauli, "Proposed extension of the CIE recommendation
    on 'Uniform color spaces, color difference equations, and metric color
    terms'," J. Opt. Soc. Am. 66, 866-867 (1976)
    """

    x = lum_values / float(reference_white)
    idx = x <= (6.0 / 29) ** 3
    y1 = 841.0 / 108 * x[idx] + 4.0 / 29
    y2 = x[~idx] ** (1.0 / 3)
    y = np.empty(x.shape)
    y[idx] = y1
    y[~idx] = y2
    return 11.6 * y - 1.6


def munsell2luminance(munsell_values, reference_white):
    """
    Transform Munsell values to luminance values.
    The luminance values will be in the same unit as the reference white, which
    can be arbitrary as long as the scale is linear.

    Parameters
    ----------
    munsell_values : numpy-array
    reference_white : number

    Returns
    -------
    lum_values : numpy-array

    Reference: H. Pauli, "Proposed extension of the CIE recommendation
    on 'Uniform color spaces, color difference equations, and metric color
    terms'," J. Opt. Soc. Am. 66, 866-867 (1976)
    """
    lum_values = (munsell_values + 1.6) / 11.6
    idx = lum_values <= 6.0 / 29
    lum_values[idx] = (lum_values[idx] - 4.0 / 29) / 841 * 108
    lum_values[~idx] **= 3
    return lum_values * reference_white
