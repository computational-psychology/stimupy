#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
This module provides functions for creating mondrian style stimuli, and for
rotating them in 3D. Use create_mondrian() to create a Mondrian texture with
given parameters.

"""
import random
import bisect
import numpy as np

from .. import utils

def distribute_patches(size, mean_edge_len, colors, weights=None, write=False):
    """
    Create a mondrian display of given size, mean edge length and colors.
    Optionanlly, weights for the colors, i.e. the probability that a patch will
    receive a certain color, can be specified.

    Parameters
    ----------
    size : tuple of two ints
    mean_edge_len : int
                   the mean length of edges of new patches. Actual edge length
                   will randomly vary between 2/3 and 4/3 times this value, to
                   allow for aspect ratios up to 2:1.
    colors : list of ints
            a list of possible gray values for the patches
    weights : list of floats (optional)
              a list of probabilities for the different colors. If not
              specified, all colors get equal probability.
    write : boolean (optional)
            if True, specification of how the Mondrian was constructed will be
            written to /tmp/mondrian_out. Default is False.

    Returns
    -------
    M : numpy.ndarray
       the mondrian as a numpy array
    """
    if weights is None:
        weights = [1. / len(colors) for _ in colors]
    elif len(weights) != len(colors):
        raise ValueError(
                "number of weights must be equal to number of colors, but " +
                "is %d weights for %d colors" %(len(weights), len(colors)))
    rng = WeightedRandomGenerator(weights)
    M = -np.ones(size)
    x = 0
    if write:
        out_file = open('/tmp/mondrian_out', 'w')

    while True:
        try:
            y = (M[:,x] == -1).nonzero()[0][0]
        except IndexError:
            to_fill = (M == -1).nonzero()
            if to_fill[0].size:
                y = to_fill[0][0]
                x = to_fill[1][0]
            else:
                break
        width = int((random.random() * 2. / 3 + 2. / 3) * mean_edge_len)
        height = int((random.random() * 2. / 3 + 2. / 3) * mean_edge_len)
        # create some overlap, maximally 10% of the mean edge length
        x = max(0, x - random.randint(0, int(mean_edge_len / 10)))
        y = max(0, y - random.randint(0, int(mean_edge_len / 10)))
        M[y : y + height, x : x + width] = colors[rng()]
        if write:
            out_file.write(('y: %3d, x: %3d, height: %3d, width: %3d,' +
                ' value: %3d\n') % (y, x, height, width, M[y,x]))
        x += width
        if x >= size[1]:
            x = 0
    if write:
        out_file.close()
    return M

def create_mondrian(size, mean_edge_len, colors, weights=None,
                    accuracy=.05, max_cycles=1000, write=False):
    """
    Create a mondrian on which the difference between desired color
    distribution and actual color distribution is smaller than some accuracy
    value. If no randomly created mondrian fulfills this criterion before some
    cycle count is reached, the best mondrian generated so far is returned.

    Parameters
    ----------
    size : tuple of two ints
    mean_edge_len : int
                   the mean length of edges of new patches. Actual edge length
                   will randomly vary between 2/3 and 4/3 times this value, to
                   allow for aspect ratios up to 2:1.
    colors : list of ints
            a list of possible gray values for the patches
    weights : list of floats (optional)
              a list of probabilities for the different colors. If not
              specified, all colors get equal probability.
    accuracy : float (optional)
               the maximally allowed deviation between the relative frequency
               of a color and its specified weight. Default is 0.05.
    max_cycles : int (optional)
                 the maximal number of mondrians created before the function
                 aborts and returns the best mondrian so far. Default is 1000.
    write : boolean (optional)
            if True, specification of how the Mondrian was constructed will be
            written to /tmp/mondrian_out. If the script terminates because
            max_cycles is reached, the file need not correspond to the best
            mondrian, so be careful. Default is False.

    Returns
    -------
    M : numpy.ndarray
       the mondrian as a 2D numpy array

    """

    if weights is None:
        weights = [1. / len(colors) for _ in colors]
    elif len(weights) != len(colors):
        raise ValueError(
                "number of weights must be equal to number of colors, but " +
                "is %d weights for %d colors" %(len(weights), len(colors)))
    bins = list(colors)
    bins.append(bins[-1] + 1)
    min_diff = 1
    counter = 0
    while True:
        counter += 1
        m = distribute_patches(size, mean_edge_len, colors, weights, write)
        counts = (np.histogram(m, bins)[0].astype(float) / m.size)
        if all(np.abs(counts - weights) < min_diff):
            best = m
            min_diff = np.abs(counts - weights).max()
            if min_diff < accuracy:
                return best
        if counter > max_cycles:
            return best

def rotate_3d(m, rot_angle, ppd, constant_side='l', background=0, factor=1):
    """
    Compute the 2D projection of a rotation of m around one of its sides.

    Parameters
    ----------
    m : 2D numpy array
        the matrix to be rotated
    rot_angle : number in ]90, 180[
                the angle between the resulting matrix and the viewing axis.
                90 leaves the matrix unchanged, smaller values rotate it
                towards the observer, larger values away from the observer.
    ppd : number
          pixels per degree of visual angle of the target display.
    constant_side : ['l', 'r'], optional
                    the side of the array used as the rotation axis. Default is
                    'l'.
    background : number, optional
                 the value used to fill in the returned image in the locations
                 not covered by the rotated surface. Default is 0.
    factor : number, optional
             if the function is called with a resized array, the resize factor
             can be passed to ensure that the output size is a multiple of the
             resize factor. Default is 1.

    Returns
    -------
    rotated : 2D numpy array
    """
    #check input
    if not 0 < rot_angle < 180:
        raise ValueError("Rotation angle must be in ]0, 180[, is %d." %
                         rot_angle)
    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        raise ValueError("Input must be 2D numpy array")
    if not constant_side in ['l', 'r']:
        raise ValueError("Constant side must be 'l' or 'r', is '%s'." %
                          constant_side)

    # determine screen distance and width of rotated image
    distance = ppd / 2. / np.tan(np.radians(.5))
    theta = np.radians(rot_angle)
    alpha = np.arcsin(m.shape[1] * np.sin(theta) / np.sqrt(distance ** 2 +
        m.shape[1] ** 2 - 2 * distance * m.shape[1] * np.cos(theta)))
    width = np.floor(distance * np.tan(alpha) / factor) * factor
    rotated = background * np.ones((m.shape[0], width))

    if constant_side == 'r':
        m = m[:, ::-1]

    for x in np.arange(width):
        alpha = np.arctan(x / distance)
        x_coord = np.round(distance * np.sin(alpha) /
                                            np.sin(np.pi - alpha - theta))
        obj_dist = np.sqrt(distance ** 2 + x_coord ** 2 -
                                2 * distance * x_coord * np.cos(theta))
        screen_dist = x / np.sin(alpha) if x > 0 else distance
        height = m.shape[0] * screen_dist / obj_dist
        height = np.floor(height) + (m.shape[0] - np.floor(height)) % 2
        h_diff = (m.shape[0] - int(height)) / 2
        if h_diff == 0:
            rotated[:, x] = m[:, x_coord]
        else:
            rotated[h_diff:-h_diff, x] = m[:,x_coord][
                np.linspace(0, m.shape[0], height, endpoint=False).astype(int)]
    return rotated if constant_side == 'l' else rotated[:, ::-1]

def rotate_3d_smooth(m, rot_angle, ppd, constant_side='l', background=0,
                        factor=10):
    """
    Produce an antialiased version of the 3D rotated Mondrian (or any other
    surface).
    Uses super-sampling and averaging. Relatively slow, but artifactfree.

    Parameters
    ----------
    m : 2D numpy array
        the matrix to be rotated
    rot_angle : number in ]0, 180[
                the angle between the resulting matrix and the viewing axis.
                90 leaves the matrix unchanged, smaller values rotate it
                towards the observer, larger values away from the observer.
    ppd : number
          pixels per degree of visual angle of the target display.
    constant_side : ['l', 'r'], optional
                    the side of the array used as the rotation axis. Default is
                    'l'.
    background : number, optional
                 the value used to fill in the returned image in the locations
                 not covered by the rotated surface. Default is 0.
    factor : odd number, optional
             the super-sampling factor. Default is 5.

    Returns
    -------
    rotated : 2D numpy array

    """
    m = utils.resize_array(m, (factor, factor))
    rotated = rotate_3d(m, rot_angle, ppd * factor, constant_side, background,
                            factor)
    averager1 = utils.resize_array(
                    np.eye(rotated.shape[0] / factor), (1, factor))
    averager2 = utils.resize_array(
                    np.eye(rotated.shape[1] / factor), (factor, 1))
    return np.dot(averager1, np.dot(rotated, averager2)) / factor ** 2

def angled_mondrians(left, right, angle, ppd, background=0):
    """
    Arrange two arrays (ususally Mondrians), side by side, rotated such that
    the corner forms a given angle.

    Parameters
    ----------
    left : 2D array
           the array that will be placed on the left
    right : 2D array
            the array that will be placed on the right
    angle : number in ]0, 180[
            the inner angle between the two arrays forming a roof
    ppd : number
          pixels per degree of visual angle of the target display.
    background : number, optional
                 the value used to fill in the returned image in the locations
                 not covered by the rotated surface. Default is 0.

    Returns
    -------
    2D array
    """

    left = rotate_3d_smooth(left, 180 - angle / 2., ppd, 'r', background)
    right = rotate_3d_smooth(right, 180 - angle / 2., ppd, 'l', background)
    return np.hstack((left, right))

def overlapping_patch(left, right, size, value, y_offset=None, x_offset=None):
    """
    Change values in the two arrays such that when they are placed side by
    side, there is an overlapping patch of the specified value.

    Parameters
    ----------
    left : 2D array
           the array that will be placed on the left
    right : 2D array
            the array that will be placed on the right
    size : 2-element tuple
           the size of the patch (y,x)
    value : number
            the value set for the patch
    y_offset : number, optional
               the vertical offset of the patch from the top of the image. By
               default, the patch will be placed in the center.
    x_offset : number, optional
               the horizontal offset of the patch from the midline. Should be
               a negative value such that the patch starts in the left half.
               Default is half of the horizontal patch size.

    Returns
    -------
    None
    """

    if y_offset is None:
        y_offset = left.shape[0] / 2 - size[0] / 2

    if x_offset is None:
        x_offset = -size[1] / 2

    left[y_offset:y_offset + size[0], x_offset:] = value
    right[y_offset:y_offset + size[0], 0:size[1] + x_offset] = value
    return


class WeightedRandomGenerator(object):
    """
    A random number generator that returns indices into a list weighted by
    the values of the list items.
    Usage: initialize an rng-object by passing a list. Calling the object
    returns a random int that is an index into the list.

    >>> rng = WeightedRandomGenerator([.2, .5, .3])
    >>> rng. next()
    1   #random

    Implementation copied from
    http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python
    """

    def __init__(self, weights):
        self.totals = []
        running_total = 0

        for w in weights:
            running_total += w
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        return bisect.bisect_right(self.totals, rnd)

    def __call__(self):
        return self.next()

