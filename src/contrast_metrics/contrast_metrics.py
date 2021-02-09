#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:53:53 2018

@author: guille
"""

import numpy as np


def mc(t, s):
    """
    Compute either the Michelson contrast between two scalar values: (t-s)/(t+s),
    or the Michelson contrast of target t within a certain surround region s: (t-mean(s))/(t+mean(s)).

    Parameters
    ----------
    t : float
    s : float or array_like

    Returns
    -------
    float
    """
    s_m = np.mean(s)
    return (t - s_m) / (t + s_m)


def mc_single(t, s):
    """
    Compute mean Michelson contrast between target and each of the luminances in the surround region:
    mean_i{ (t-s_i)/(t+s_i) }.

    Parameters
    ----------
    t : float
    s : array_like

    Returns
    -------
    float
    """
    return np.mean([mc(t, k) for k in s])


def preprocess_arr(arr, mask, mode):
    """Apply the mask and the mode rules to the array."""
    arr = arr.astype('float')
    if mask is None:
        arr = arr.flatten()
    elif mode == "complete":
        arr = arr[mask].flatten()
    elif mode == "unique":
        arr = np.unique(arr[mask])
    else:
        raise ValueError("Unknown mode.")
    return arr


def _SAM_or_SAW(func, arr, mask, mode, return_pair_contrasts=False):
    """
    For reduced redundancy, this method implements the logic for SAM and SAW. See those methods for documentation.
    """
    if np.any(arr == 0):
        raise ValueError('Space-average contrast is not defined for luminance values of 0.')

    arr = preprocess_arr(arr, mask, mode)

    n = len(arr)
    pair_contrasts = []
    # contrast between all possible pairs; contr(i,j)=contr(j,i)
    for i in range(n):
        for j in range(i+1, n):
            diff = arr[i] - arr[j]
            divisor = arr[i] + arr[j] if func == "SAM" else min(arr[i], arr[j])
            x = abs(diff/divisor)
            pair_contrasts.append(x)

    # every pair was compared once, but the SAM/SAW formulas is defined on ordered pairs
    contrast = 2 * np.sum(pair_contrasts) / (n * n)

    if return_pair_contrasts:
        return contrast, pair_contrasts
    else:
        return contrast


def SAM(arr, mask=None, mode="unique", return_pair_contrasts=False):
    """
    Space-Average Michelson contrast of all pairs of values in arr:
    mean{ |(lum_i-lum_j)/(lum_i+lum_j)| } for i, j in [0, arr_size].

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region.
    mode : {"complete", "unique"}, optional
        unique (default): only unique values in arr are compared
        complete: every value of arr is compared with every other value (resource-intensive)
    return_pair_contrasts : bool, optional

    Returns
    -------
    contrast : float
    contrast_terms : list, optional
        List of individual contrast terms between the pairs of values.
        Includes each unordered pair of values once, i.e. (i,j), but not (j,i).
        Doesn't include self-contrasts (i,i).
    """
    return _SAM_or_SAW('SAM', arr, mask, mode, return_pair_contrasts)


def SAMLG(arr, mask=None, mode="unique"):
    """
    Space-Average Michelson contrast of all pairs of the logarithm of values in arr.
    See SAM for details.
    SAMLG(arr) = SAM(log(arr))
    """
    return SAM(np.log(arr), mask, mode)


def SAMLG_Moulden(arr, mask=None, mode="complete", return_pair_contrasts=False):
    """
    Space-Average Log Michelson contrast of all pairs of values in arr.
    This formula comes from Moulden, Kingdom, Gatley 1990.
    
    Different than SAMLG, which uses formula in Robilotto 2002
    """
    
    n = len(arr)
    
    c, pair_contrasts = _SAM_or_SAW('SAM', arr, mask, mode, return_pair_contrasts=True)
    
    # current ATF has identical values, resolution problem! I had to remove
    # equal values manually
    #pair_contrasts = np.array(pair_contrasts)
    #pair_contrasts = pair_contrasts[pair_contrasts!=0]
    # not needed anymore as I'm taking analytical ATFs
    
    pair_contrasts = np.log(pair_contrasts)
    contrast = 2 * np.sum(pair_contrasts) / (n * n)
    
    return contrast


def SAWLG_Moulden(arr, mask=None, mode="complete", return_pair_contrasts=False):
    """
    Space-Average Log Whittle contrast of all pairs of values in arr.
    This formula comes from Moulden, Kingdom, Gatley 1990.
    
    Different than SAWLG, which uses formula in Robilotto 2002
    """
    
    n = len(arr)
    
    c, pair_contrasts = _SAM_or_SAW('SAW', arr, mask, mode, return_pair_contrasts=True)
    
    # current ATF has identical values, resolution problem! I had to remove
    # equal values manually
    #pair_contrasts = np.array(pair_contrasts)
    #pair_contrasts = pair_contrasts[pair_contrasts!=0]
    # not needed anymore as I'm taking analytical ATFs
    
    pair_contrasts = np.log(pair_contrasts)
    contrast = 2 * np.sum(pair_contrasts) / (n * n)
    
    return contrast


def SDMC(arr, mask=None, mode="unique"):
    """
    Standard deviation of Michelson contrasts between the values in arr.
    Amount of contrast modulation.
    See SAM for details.
    """
    _, contrasts = SAM(arr, mask, mode, return_pair_contrasts=True)
    return np.std(contrasts)


def SAW(arr, mask=None, mode="unique", return_pair_contrasts=False):
    """
    Space-Average Whittle contrast of all pairs of values in arr:
    mean{ |(lum_i-lum_j)/min(lum_i, lum_j)| } for i, j in [0, arr_size].

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region.
    mode : {"complete", "unique"}, optional
        unique (unique): only unique values in arr are compared
        complete: every value of arr is compared with every other value (resource-intensive)
    return_pair_contrasts : bool, optional

    Returns
    -------
    contrast : float
    contrast_terms : list, optional
        List of individual contrast terms between the pairs of values.
        Includes each unordered pair of values once, i.e. (i,j), but not (j,i).
        Doesn't include self-contrasts (i,i).
    """
    return _SAM_or_SAW('SAW', arr, mask, mode, return_pair_contrasts)


def SAWLG(arr, mask=None, mode="unique"):
    """
    Space-Average Whittle contrast of all pairs of the logarithm of values in arr.
    See SAW for details.
    SAWLG(arr) = SAW(log(arr))
    """
    return SAW(np.log(arr), mask, mode)


def RMS(arr, mask=None, mode="complete"):
    """
    RMS contrast, defined as standard_deviation(arr) / mean(arr.)

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region
    mode : {"complete", "unique"}, optional
        complete (default): RMS of entire arr
        unique: RMS of unique values in arr

    Returns
    -------
    contrast : float
    """
    arr = preprocess_arr(arr, mask, mode)
    return np.std(arr) / np.mean(arr)


def SD(arr, mask=None, mode="complete"):
    """
    Standard deviation of values in arr.

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region.
    mode : {"complete", "unique"}, optional
        complete (default): SD of entire arr
        unique: SD of unique values in arr

    Returns
    -------
    contrast : float
    """
    arr = preprocess_arr(arr, mask, mode)
    return np.std(arr)


def SDLG(arr, mask=None, mode="complete"):
    """
    Standard deviation of logarithms of values in arr.
    SDLG(arr) != SD(log(arr)), because the log of the mean of arr is used, not the mean of logs of arr.
    """
    arr = preprocess_arr(arr, mask, mode)
    x = (np.log(arr) - np.log(np.mean(arr)))**2
    return np.sqrt(np.mean(x))


def alpha_c(plain, medium):
    """
    after Singh and Anderson, 2002
    ratio of contrasts, contrast based on min and max luminance in range
    """
    a = plain.max()
    b = plain.min()
    p = medium.max()
    q = medium.min()
    c_medium = (p - q) / (p + q)
    c_plain = (a - b) / (a + b)
    return c_medium / c_plain


##### TODO complete docstrings
def alpha_metelli(plain, medium):
    """
    ratio of luminance ranges
    """
    a = plain.max()
    b = plain.min()
    p = medium.max()
    q = medium.min()
    return np.around((p - q) / (a - b), decimals=2)

##### TODO complete docstrings
def alpha_c_minmax(plain, medium):
    """
    ratio of luminance ranges adjusted by additional offset term
    """
    a_l = alpha_metelli(plain, medium)

    plain_mean = (plain.min() + plain.max()) / 2
    med_mean = (medium.min() + medium.max()) / 2
    return a_l / (1 + (med_mean - plain_mean) / plain_mean)
