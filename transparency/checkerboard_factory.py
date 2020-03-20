# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:08:01 2020

@author: max
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import subprocess
import string


class CheckerboardFactory:
    """
    Creates 3D checkerboard images with transparent partial overlay as in [1].

    Example usage:
    >>> f = CheckerboardFactory()
    >>> f.find_checkerboard(n_checks=8)
    >>> f.build_image(tau=2, alpha=.5, camera_offset=(1, 0, 0))
    >>> checkerboard = f.get_checkerboard()
    >>> cutout = f.get_cutout()
    >>> stacked = f.get_stacked()

    References
    ----------
    [1] Wiebel, Aguilar and Maertens (2017).
    """

    def __init__(self):
        self.n_checks = 0
        self.r_checks = {}
        self.image = None

        mask = Image.open("checkerboard_mask.png").convert('L')
        self.mask = np.array(mask) / 255.0
        self.cropped_mask = self.mask[289:377, 139:341]

    def find_checkerboard(self, n_checks, reflectances=None, sample_repeat=9):
        """
        Find a checkerboard pattern where no two adjacent checks have the same value, and save internally.

        n_checks : int
            Number of checks in each direction.
        reflectances : list[float] or None
            Reflectance values for the checks to draw from randomly.
            When None, default values as in Wiebel, Aguilar and Maertens 2017 are used.
        sample_repeat : int
            Repeating >reflectances< this many times, then drawing without replacing.
        """
        if reflectances is None:
            reflectances = [0.06, 0.11, 0.19, 0.31, 0.46, 0.63, 0.82, 1.05, 1.29, 1.50, 1.67, 1.95, 2.22]

        self.n_checks = n_checks

        # build n x n matrix with values drawn from reflectances with at most >sample_repeat< repeats of each value
        draw_set = np.repeat(reflectances, sample_repeat)
        board = np.random.choice(draw_set, (n_checks, n_checks), replace=False)

        for i, j in np.ndindex((n_checks, n_checks)):
            # if check value is identical to top or left adjacent cell, draw a different sample
            if (i > 0 and board[i, j] == board[i - 1, j]) or (j > 0 and board[i, j] == board[i, j - 1]):
                board[i, j] = np.random.choice([a for a in reflectances if a != board[i, j]])
                # TODO is it important that a value doesn't occur more than >sample_repeat< times?

            key = '%s%.2d' % (string.ascii_lowercase[i], j + 1)
            self.r_checks[key] = board[i, j]

    def build_image(self, tau, alpha, background=.27, camera_offset=(0, 0, 0), look_at_offset=(0, 0, 0),
                    transparency_coords=None, filename="checkerboard", resolution=(480, 480)):
        """
        Add the transparency layer to the checkerboard and generate the image.
        
        Parameters
        ----------
        tau : float
            Luminosity of the transparent partial overlay. [0.0, 10.0]
        alpha : float
            Alpha value of the transparent partial overlay. [0.0, 1.0]
        background : float
            Background luminosity. [0.0, 1.0]
        camera_offset, look_at_offset : tuple[int]
            xyz coordinate offset from default camera position / look_at focus position
        transparency_coords : list or None, optional
            The coordinates of the transparent partial overlay.
            Default (when None given) is horizontal.
            Vertical: [[-1.4, 2.85, -8.0], [-1.4, 0.4, -8.0], [1.4, 0.4, -8.0], [1.4, 2.85, -8.0]]
        filename : string, optional
            Filename of .pov and .png files to be created.
        resolution : tuple[int]
            image dimensions
        """
        if transparency_coords is None:
            transparency_coords = [[-2.0, 1.85, -8.0], [-2.0, -0.2, -8.0], [2.0, -0.2, -8.0], [2.0, 1.85, -8.0]]

        positions = get_positions(n_checks=self.n_checks, y1=-1.00, y2=-0.71)
        cb_transf = 'rotate y * 45'
        transparency = get_transparency(tau, alpha, transparency_coords)

        # write and run pov file
        write_pov(filename, r_checks=self.r_checks, positions=positions, cb_transf=cb_transf, transparency=transparency,
                  background=background, camera_offset=camera_offset, look_at_offset=look_at_offset)
        run_povray('%s.pov' % filename, res=resolution)

        # get the image to work on
        image = Image.open('%s.png' % filename).convert('L')
        self.image = np.array(image) / 255.0

    def get_checkerboard(self, cropped=False):
        """
        Get the entire image of the checkerboard and the transparent rectangle.

        Parameters
        ----------
        cropped : bool

        Returns
        -------
        np.ndarray
            numpy array with values between 0.0 and 1.0
        """
        checkerboard = self.image.copy()
        if cropped:
            return checkerboard[209:425, 63:417]
        else:
            return checkerboard

    def get_cutout(self, cropped=False):
        """
        Get the cutout of the intersection of the transparent rectangle and the checkerboard.

        Parameters
        ----------
        cropped : bool

        Returns
        -------
        np.ndarray
            numpy array with values between 0.0 and 1.0
        """
        cutout = self.image.copy()
        bg = cutout[0, 0]
        cutout[self.mask == 0] = bg

        if cropped:
            return cutout[289:377, 139:341]
        else:
            return cutout

    def get_stacked(self, distance=100):
        """
        Combine cutout and non-cutout-checkerboard in one image, stacked atop each other.

        Parameters
        ----------
        distance : int
            space in between object
        Returns
        -------
        np.ndarray
            numpy array with values between 0.0 and 1.0
        """
        checkerboard = self.get_checkerboard(cropped=True)
        cutout = self.get_cutout(cropped=True)
        bg = checkerboard[0, 0]

        # calculate margin from top and bottom based on distance in between objects
        margin = (480 - (checkerboard.shape[0] + cutout.shape[0] + distance)) // 2
        if margin < 0:
            raise ValueError("Distance too big.")

        stacked = np.full((480, 480), bg)
        mask_checkerboard = np.zeros((480, 480))
        mask_cutout = np.zeros((480, 480))

        # coordinates of cutout within the stacked image
        y2 = 480 - margin
        y1 = y2 - cutout.shape[0]
        x1 = 240 - (cutout.shape[1] // 2)
        x2 = x1 + cutout.shape[1]
        stacked[y1:y2, x1:x2] = cutout

        # coordinates of the mask-shape within the respective masks
        mask_cutout[y1:y2, x1:x2] = self.cropped_mask
        y1 = margin + 80
        y2 = y1 + self.cropped_mask.shape[0]
        mask_checkerboard[y1:y2, x1:x2] = self.cropped_mask

        # coordinates of checkerboard within the stacked image
        y1 = margin
        y2 = y1 + checkerboard.shape[0]
        x1 = 240 - (checkerboard.shape[1] // 2)
        x2 = x1 + checkerboard.shape[1]
        stacked[y1:y2, x1:x2] = checkerboard

        return stacked, mask_checkerboard, mask_cutout


def get_positions(n_checks=10, xz1=-2.9, xz2=2.9, y1=-0.75, y2=-0.71):
    """
    Build dict with xyz positions of a n_checks x n_checks checkerboard.

    Parameters
    ----------
    n_checks : int, optional
        number of checks per side
    xz1, xz2 : float, optional
        range in x and z coordinates of the checkerboard
    y1, y2: float, optional
        coordinates in the y dimension, i.e. the checkerboard height is y2-y1

    Returns
    -------
    dict
    """

    coords = np.linspace(xz1, xz2, n_checks + 1).round(2)

    positions = {}
    for i in range(n_checks):
        for j in range(n_checks):
            key = '%s%.2d' % (string.ascii_lowercase[i], j + 1)
            positions[key] = [[coords[i], y1, coords[j]], [coords[i + 1], y2, coords[j + 1]]]

    return positions


def get_transparency(tau, alpha, coords):
    """
    Build dict with transparency.

    Parameters
    ----------
    tau, alpha : float
    coords : list

    Returns
    -------
    dict
    """
    transparency = {'xyz': coords,
                    'color': [tau, tau, tau],
                    'transmit': alpha,
                    'transformations': 'rotate x *15\ntranslate<0, -2.3, 0>\n'}

    return transparency


def write_pov(filename, r_checks, positions, transparency=None, cb_transf=None, light_pos='right', planes=None,
              pointers=None, background=0.27, light=1.0, camera_offset=(0, 0, 0), look_at_offset=(0, 0, 0)):
    """
    Writes a Povray file .pov containing the specifications for rendering a variegated checkerboard
    with or without transparency.

    Parameters
    ----------
    filename : string
        for .pov and .png files
    r_checks : dict
        See Also CheckerboardFactory.find_checkerboard
    positions : dict
        See Also get_positions
    transparency : dict or tuple or None
        See Also get_transparency
    cb_transf : str or None
        spatial transformation povray instruction
    light_pos : {'left', 'right'}
    planes, pointers : list[str]
        list of povray instructions
    background : float
        background luminosity
    light : float
        light source luminosity
    camera_offset, look_at_offset : tuple[float]
        xyz coordinate offset from default camera position / look_at focus position
    """
    # write povray description file
    out_name = '%s.pov' % filename
    out_file = open(out_name, 'w')

    # povray version 3.7 needs specification of gamma. As it assumes 2.2, we need to give the same number
    # so that the final gamma will be 1.0 (no gamma correction)

    out_file.write('#version 3.7;\n\n')
    # out_file.write('global_settings {assumed_gamma 2.2}\n\n')

    out_file.write('background { color rgb <%2.2f, %2.2f,%2.2f>}\n\n' % tuple(np.repeat(background, 3)))
    # out_file.write('#declare lens=camera{perspective location <0, 16,-50>  look_at <0,0,0>  angle 9.2};\n')
    cx, cy, cz = camera_offset
    lx, ly, lz = look_at_offset
    out_file.write('#declare lens=camera{perspective location <%.2d,%.2d,%.2d>  look_at <%.2d,%.2d,%.2d>  angle 12};\n'
                   % (cx, cy+16, cz-50, lx, ly, lz))

    out_file.write('camera{lens}\n\n')

    if light_pos == 'right':
        out_file.write(
            'light_source{<20, 10, 7>  color rgb <%2.2f, %2.2f, %2.2f> area_light 6*x, 6*y, 12, 12}\n\n'
            % tuple(np.repeat(light, 3)))
    elif light_pos == 'left':
        out_file.write(
            'light_source{<-20, 10, 7>  color rgb <%2.2f, %2.2f, %2.2f> area_light 6*x, 6*y, 12, 12}\n\n'
            % tuple(np.repeat(light, 3)))

    # checkerboard
    out_file.write('union{\n')
    for label, pos in positions.items():
        x1, y1, z1 = pos[0]
        x2, y2, z2 = pos[1]

        c1 = r_checks[label]
        c2 = c1
        c3 = c1

        out_file.write(
            'box{<%f, %f, %f>, <%f, %f, %f> pigment{ color rgb <%f, %f, %f> }}// %s \n'
            % (x1, y1, z1, x2, y2, z2, c1, c2, c3, label))

    # spatial transformations for the checkerboard
    if cb_transf is not None:
        out_file.write(cb_transf)

    out_file.write('}\n\n')

    # planes
    if planes is not None:
        for plane in planes:
            out_file.write(plane)

    # writing transparencies
    if isinstance(transparency, dict):
        write_transparency(transparency, out_file)

    elif isinstance(transparency, tuple):
        for t in transparency:
            if t is not None:
                write_transparency(t, out_file)

    # pointers indicating which checks to compare
    if pointers is not None:
        for line in pointers:
            out_file.write(line)

    # closes file
    out_file.close()


def write_transparency(transparency, out_file):
    """
    Writes transparency specification into pov-ray file

    Parameters
    ----------
    transparency : dict
        'xyz': list of 4 containing the xyz coordinates of the transparency
        'transformation': string containing spatial transformation that can be applied to the transparency
        'color' and 'transmittance': transparency's reflectance  and transmittance
    out_file : IO
    """
    x1, y1, z1 = transparency['xyz'][0]
    x2, y2, z2 = transparency['xyz'][1]
    x3, y3, z3 = transparency['xyz'][2]
    x4, y4, z4 = transparency['xyz'][3]

    out_file.write('polygon{4, <%f, %f, %f> <%f, %f, %f> <%f, %f, %f> <%f, %f, %f>\n'
                   % (x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4))

    if 'transformations' in transparency:
        out_file.write(transparency['transformations'])

    c1, c2, c3 = transparency['color']
    tr = transparency['transmit']

    out_file.write('texture{pigment {color rgb <%f, %f, %f> transmit %f}}}\n\n' % (c1, c2, c3, tr))


def run_povray(filename, res=(1024, 768)):
    """
    Calls povray for rendering file given as argument

    Parameters
    ----------
    filename : str
    res : tuple
    """
    return subprocess.call(["povray", "-W%d" % res[0], "-H%d" % res[1], "+A0.1", "Display=false", filename])


def main():
    f = CheckerboardFactory()
    f.find_checkerboard(10)
    tau = 2
    alpha = .5

    f.build_image(tau, alpha, background=.5)
    img1 = f.get_checkerboard()
    f.build_image(tau, alpha, background=.5, camera_offset=(1, 0, 0))
    img2 = f.get_checkerboard()

    plt.imshow(img1, cmap='gray', vmin=0, vmax=1)
    plt.show()
    plt.imshow(img2, cmap='gray', vmin=0, vmax=1)
    plt.show()


if __name__ == "__main__":
    main()
