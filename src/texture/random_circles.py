#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Provides functionality to draw textures made up of randomly placed circles
of different sizes. Basic usage is to first create a list of circle coordinates
using place_circles, and then drawing these into a numpy array using
draw_circles.
"""

from __future__ import division

import numpy as np

def intersect(circle, circles, distance=0):
    """Test if a circle intersects, within a given margin, with any of the
    cirles in a list.
    """
    x, y, r = circle
    for x2, y2, r2 in circles:
        if (x - x2) ** 2 + (y - y2) ** 2 <= (r + r2 + distance) ** 2:
            return True
    return False

def place_circles(shape, radii, weights=1, density=.4, distance=0):
    """Randomly determine locations for non-intersecting circles on a canvas.

    Parameters
    ----------
    shape : tuple of two elements
            the shape of the canvas (y,x)
    radii : int or tuple of ints
            the radii of the circles, in pixels. Ordering them from highest to
            lowest makes higher densities possible.
    weights : scalar or tuple of scalars.
              The relative proportion of surface area covered by circles of
              different radii. weights[0] is the proportion assigned to circles
              of radius radii[0].
    density : scalar from [0,1]
              the ratio of surface area that should be covered by circles. Too
              high values will lead to infinite loops, because the function
              will keep sampling random locations, but not find any that do not
              have an intercept with an already placed circle. This should be
              fixed sometime. Default is .4
    distance : int
               the minimum distance between neighboring cirles, in pixels.
               Default is 0.

    Returns
    -------
    circles : list
              a list of circles, represented as three element tuples (x, y, r)
    """
    circles = []
    if not np.iterable(radii):
        radii = (radii,)
    if not np.iterable(weights):
        weights = (weights,) * len(radii)
    weights = np.asarray(weights, dtype=float)
    weights /= sum(weights)
    # compute number of circles for each radius in accordance with area weights
    n_circles = np.round(shape[0] * shape[1] * density * np.asarray(weights) /
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
    """Draw a list of circles in a numpy array.

    Parameters
    ----------
    shape : tuple of two elements
            the shape of the canvas (y,x)
    circles : list of circles
              this is the output of place_circles.
    circle_val : number
                 the value to be used for the area of the circles.
    bg_val : number
            the background value of the canvas.

    Returns
    -------
    arr : 2D numpy array
          an array with the circles drawn onto it.
    """
    canvas = np.ones(shape) * bg_val
    for x, y, radius in circles:
        x = np.arange(-x, shape[1] - x)
        y = np.arange(-y, shape[0] - y)
        Dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)
        Dist = np.fmin(np.ones(shape), np.fmax(np.zeros(shape), Dist - radius))
        canvas = Dist * canvas + (1 - Dist) * circle_val
    return canvas
