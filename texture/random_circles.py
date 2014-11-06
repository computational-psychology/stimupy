#!/usr/bin/python
# -*- coding: latin-1 -*-

from __future__ import division

import numpy as np

def intersect(circle, circles, distance=0):
    x, y, r = circle
    for x2, y2, r2 in circles:
        if (x - x2) ** 2 + (y - y2) ** 2 <= (r + r2 + distance) ** 2:
            return True
    return False

def place_circles(shape, radii, weights=1, density=.5, distance=0):
    circles = []
    if not np.iterable(radii):
        radii = (radii,)
    if not np.iterable(weights):
        weights = (weights,) * len(radii)
    # compute number of circles for each radius in accordance with area weights
    n_circles = np.round(shape[0] * shape[0] * density * np.asarray(weights) /
                            (np.pi * np.asarray(radii) ** 2))
    for radius, n in zip(radii, n_circles):
        placed = 0
        while placed < n:
            x = np.random.randint(radius, shape[1] - radius)
            y = np.random.randint(radius, shape[0] - radius)
            if not intersect((x, y, radius), circles, distance):
                circles.append((x, y, radius))
                placed += 1
    return circles

def draw_circles(shape, circles, circle_val, bg_val):
    canvas = np.ones(shape) * bg_val
    for x, y, radius in circles:
        x = np.arange(-x, shape[1] - x)
        y = np.arange(-y, shape[0] - y)
        Dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)
        Dist = np.fmin(np.ones(shape), np.fmax(np.zeros(shape), Dist - radius))
        canvas = Dist * canvas + (1 - Dist) * circle_val
    return canvas
