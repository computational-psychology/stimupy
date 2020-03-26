#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:53:53 2018

@author: guille
"""

import numpy as np


def mc(t, s):
    """
    compute michelson contrast from target and surround luminances
    """
    s_m = np.mean(s)
    return (t - s_m) / (t + s_m)


def SD(luminance):
    """
    standard deviation of luminances
    """
    sq_diff = (luminance - luminance.mean()) ** 2
    return np.sqrt(np.sum(sq_diff) / luminance.size)


def SDLG(luminance):
    """
    standard deviation of LOG luminances
    """
    sq_diff = (np.log(luminance) - np.log(luminance.mean())) ** 2
    return np.sqrt(np.sum(sq_diff) / luminance.size)


def SAM(luminance):
    """
    space-average michelson contrast of all possible pairs of luminances
    """
    contrast = []
    n = luminance.size
    for t in np.nditer(luminance):
        for s in np.nditer(luminance):
            contrast.append(mc(t, s))
    m_contrast = np.reshape(contrast, (n, n))
    idx = np.tril_indices(n, -1)
    return np.mean(m_contrast[idx])


def SAMLG(luminance):
    """
    space-average michelson contrast of all possible pairs of luminances
    """
    return SAM(np.log(luminance))


def SDMC(luminance):
    """
    standard deviation of michelson contrast of all possible pairs of luminances
    amount of contrast modulation
    """
    contrast = []
    n = luminance.size
    for t in np.nditer(luminance):
        for s in np.nditer(luminance):
            contrast.append(mc(t, s))
    m_contrast = np.reshape(contrast, (n, n))
    idx = np.tril_indices(n, -1)
    return np.std(m_contrast[idx])


def SAW(luminance):
    contrast = []
    for t in np.nditer(luminance):
        for s in np.nditer(luminance):
            a = (t - s)
            mm = np.min((t, s))
            x = np.abs(a / mm)
            contrast.append(x)
    n = luminance.size
    m_contrast = np.reshape(contrast, (n, n))
    return np.mean(m_contrast)


def SAWLG(luminance):
    return SAW(np.log(luminance))


def RMS(luminance):
    return np.sqrt(np.mean(luminance**2))


def mc_single(t, s):
    """
    compute mean michelson contrast between target and each of the surround luminances
    """
    return np.mean([mc(t, k) for k in s])


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


def mcontrast_loglum(medium):
    """
    Michelson contrast of log luminances
    """
    return (np.log(medium.max()) - np.log(medium.min())) / (np.log(medium.max()) + np.log(medium.min()))
