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


def chunk_means(arr, chunk_size):
    """
    Slice a 2D array into square chunks and compute the mean of each chunk.
    If width or height of arr aren't divisible by chunk size, the righter- and lower-most chunks
    are accordingly smaller.

    Parameters
    ----------
    arr : ndarray (2D)
    chunk_size : int

    Returns
    -------
    ndarray (1D)
    """
    assert np.ndim(arr) == 2, "Chunk mode only works on 2D arrays."
    h, w = arr.shape
    chunk_size = min(chunk_size, h, w)
    chunk_rows = int(np.ceil(h/chunk_size))
    chunk_cols = int(np.ceil(w/chunk_size))

    # pad the array with NaN values for partial blocks (to be ignored in mean calculation)
    h_pad = chunk_size * chunk_rows - h
    w_pad = chunk_size * chunk_cols - w
    arr = np.pad(arr, ((0, h_pad), (0, w_pad)), constant_values=np.nan)

    # the actual chunking; https://stackoverflow.com/a/16858283
    chunks = arr.reshape((chunk_rows, chunk_size, -1, chunk_size))\
        .swapaxes(1, 2).reshape(-1, chunk_size, chunk_size)
    # print(chunks)

    # compute the mean value of every chunk, ignoring padding and masked values
    chunks = chunks[~np.all(np.isnan(chunks), axis=(1, 2))]
    means = np.nanmean(chunks, axis=(1, 2))
    return means


def preprocess_arr(arr, mask, mode, chunk_size):
    """Apply the mask and the mode rules to the array."""
    arr = arr.astype('float')
    if mask is None:
        mask = np.True_
    if mode == "chunk":
        arr[~mask] = np.nan
        arr = chunk_means(arr, chunk_size)
    elif mode == "complete":
        arr = arr[mask].flatten()
    elif mode == "unique":
        arr = np.unique(arr[mask])
    else:
        raise ValueError("Unknown mode.")
    return arr


def _SAM_or_SAW(func, arr, mask, mode, chunk_size, return_pair_contrasts=False):
    """
    For reduced redundancy, this method implements the logic for SAM and SAW. See those methods for documentation.
    """
    if np.any(arr == 0):
        raise ValueError('Space-average contrast is not defined for luminance values of 0.')

    arr = preprocess_arr(arr, mask, mode, chunk_size)

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


def SAM(arr, mask=None, mode="unique", chunk_size=10, return_pair_contrasts=False):
    """
    Space-Average Michelson contrast of all pairs of values in arr:
    mean{ |(lum_i-lum_j)/(lum_i+lum_j)| } for i, j in [0, arr_size].

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region. Compatible with chunk mode.
    mode : {"complete", "chunk", "unique"}, optional
        unique (default): only unique values in arr are compared
        chunk: arr is sliced into chunks and chunk means are compared
        complete: every value of arr is compared with every other value (resource-intensive)
    chunk_size : int, optional
        Height and width of the chunks in chunk mode.
    return_pair_contrasts : bool, optional

    Returns
    -------
    contrast : float
    contrast_terms : list, optional
        List of individual contrast terms between the pairs of values.
        Includes each unordered pair of values once, i.e. (i,j), but not (j,i).
        Doesn't include self-contrasts (i,i).
    """
    return _SAM_or_SAW('SAM', arr, mask, mode, chunk_size, return_pair_contrasts)


def SAMLG(arr, mask=None, mode="unique", chunk_size=10):
    """
    Space-Average Michelson contrast of all pairs of the logarithm of values in arr.
    See SAM for details.
    SAMLG(arr) = SAM(log(arr))
    """
    return SAM(np.log(arr), mask, mode, chunk_size)


def SDMC(arr, mask=None, mode="unique", chunk_size=10):
    """
    Standard deviation of Michelson contrasts between the values in arr.
    Amount of contrast modulation.
    See SAM for details.
    """
    _, contrasts = SAM(arr, mask, mode, chunk_size, return_pair_contrasts=True)
    return np.std(contrasts)


def SAW(arr, mask=None, mode="unique", chunk_size=10, return_pair_contrasts=False):
    """
    Space-Average Whittle contrast of all pairs of values in arr:
    mean{ |(lum_i-lum_j)/min(lum_i, lum_j)| } for i, j in [0, arr_size].

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region. Compatible with chunk mode.
    mode : {"complete", "chunk", "unique"}, optional
        unique (unique): only unique values in arr are compared
        chunk: arr is sliced into chunks and chunk means are compared
        complete: every value of arr is compared with every other value (resource-intensive)
    chunk_size : int, optional
        Height and width of the chunks in chunk mode.
    return_pair_contrasts : bool, optional

    Returns
    -------
    contrast : float
    contrast_terms : list, optional
        List of individual contrast terms between the pairs of values.
        Includes each unordered pair of values once, i.e. (i,j), but not (j,i).
        Doesn't include self-contrasts (i,i).
    """
    return _SAM_or_SAW('SAW', arr, mask, mode, chunk_size, return_pair_contrasts)


def SAWLG(arr, mask=None, mode="unique", chunk_size=10):
    """
    Space-Average Whittle contrast of all pairs of the logarithm of values in arr.
    See SAW for details.
    SAWLG(arr) = SAW(log(arr))
    """
    return SAW(np.log(arr), mask, mode, chunk_size)


def RMS(arr, mask=None, mode="complete", chunk_size=10):
    """
    Root mean square of values in arr.

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region. Compatible with chunk mode.
    mode : {"complete", "chunk", "unique"}, optional
        complete (default): RMS of entire arr
        chunk: arr is sliced into chunks and RMS of chunk means is computed
        unique: RMS of unique values in arr
    chunk_size : int, optional
        Height and width of the chunks in chunk mode.

    Returns
    -------
    contrast : float
    """
    arr = preprocess_arr(arr, mask, mode, chunk_size)
    return np.sqrt(np.mean(arr**2))


def SD(arr, mask=None, mode="complete", chunk_size=10):
    """
    Standard deviation of values in arr.

    Parameters
    ----------
    arr : ndarray
        2D image or a 1D array of luminance values.
    mask : ndarray or None, optional
        Boolean mask for 2D arr. Limits contrast computation to this region. Compatible with chunk mode.
    mode : {"complete", "chunk", "unique"}, optional
        complete (default): SD of entire arr
        chunk: arr is sliced into chunks and SD of chunk means is computed
        unique: SD of unique values in arr
    chunk_size : int, optional
        Height and width of the chunks in chunk mode.

    Returns
    -------
    contrast : float
    """
    arr = preprocess_arr(arr, mask, mode, chunk_size)
    return np.std(arr)


def SDLG(arr, mask=None, mode="complete", chunk_size=10):
    """
    Standard deviation of logarithms of values in arr.
    SDLG(arr) != SD(log(arr)), because the log of the mean of arr is used, not the mean of logs of arr.
    """
    arr = preprocess_arr(arr, mask, mode, chunk_size)
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


def alpha_metelli(plain, medium):
    """
    ratio of luminance ranges
    """
    a = plain.max()
    b = plain.min()
    p = medium.max()
    q = medium.min()
    return np.around((p - q) / (a - b), decimals=2)


def alpha_c_minmax(plain, medium):
    """
    ratio of luminance ranges adjusted by additional offset term
    """
    a_l = alpha_metelli(plain, medium)

    plain_mean = (plain.min() + plain.max()) / 2
    med_mean = (medium.min() + medium.max()) / 2
    return a_l / (1 + (med_mean - plain_mean) / plain_mean)
