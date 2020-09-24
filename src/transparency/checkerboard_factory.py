# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:08:01 2020

@author: max
"""

from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import string
import warnings


class CheckerboardFactory:
    """
    Creates 3D checkerboard images with transparent partial overlay as in [1].

    Example usage:
    >>> f = CheckerboardFactory()
    >>> f.find_checkerboard(n_checks=8)
    >>> f.build_image(tau=2, alpha=.5)
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
        self.camera_offsets_specified = False

        base_path = path.dirname(__file__)
        p = path.join(base_path, 'checkerboard_mask.png')
        mask = Image.open(p).convert('L')
        self.mask = np.array(mask) / 255.0
        self.cropped_mask = self.mask[289:377, 139:341]

    def find_checkerboard(self, n_checks, reflectances=None, sample_repeat=9,
                          strict_sampling=True, controlled_sampling=False):
        """
        Find a checkerboard pattern where no two adjacent checks have the same value, and save internally.

        Parameters
        ----------
        n_checks : int
            Number of checks in each direction.
        reflectances : list[float] or None, optional
            Reflectance values [in povray a.u.] for the checks to draw from randomly.
            When None, default values as in Wiebel, Aguilar and Maertens 2017 are used.
        sample_repeat : int, optional
            Repeating >reflectances< this many times, to sample the board from (without replacing).
        strict_sampling : bool, optional
            If True, the entire board is (re-)sampled until no two adjacent checks have the same value.
            If False, problematic checks will be corrected one by one, which is faster, but might lead to
            - some reflectances occurring more often than >sample_repeat<, and
            - slight inconsistencies in overall distribution / deviations.
        controlled_sampling : bool, optional
            If True and n_checks!=8, the lower quadrant of the board (which will be mostly covered by the transparent
            rectangle) will be sampled independently in order to control the distribution of reflectances there.
            If True and n_checks=8, 26 checks known to be fully or partially covered by the transparency will be used.
            If False, the entire board will be sampled equally.
        """
        self.n_checks = n_checks
        total_checks = n_checks*n_checks

        if reflectances is None:
            reflectances = [0.06, 0.11, 0.19, 0.31, 0.46, 0.63, 0.82, 1.05, 1.29, 1.50, 1.67, 1.95, 2.22]

        if len(reflectances) * sample_repeat < total_checks:
            sample_repeat = int(np.ceil(total_checks / len(reflectances)))
            warnings.warn('Given value for sample_repeat was too small and has been changed to %d.' % sample_repeat)

        # repeated concatenation of reflectances / multiset of values the cells will be sampled from without replacing
        np.random.shuffle(reflectances)
        sample_set = np.tile(reflectances, sample_repeat)

        # mask for the part of the board to be sampled first (see docstring)
        if controlled_sampling:
            mask = np.full((n_checks, n_checks), False)
            if n_checks == 8:
                x = [3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 2, 2, 3, 4, 5, 6, 7, 7]
                y = [0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 4, 5]
                mask[(x, y)] = True
            else:
                t = int(np.ceil(n_checks/2))
                mask[t:, :t] = True
            mask_size = np.count_nonzero(mask)
        else:
            mask = mask_size = None

        # board sampling loop
        iterations = 0
        max_iterations = 100000
        while True:
            if iterations >= max_iterations:
                raise RuntimeWarning('No board found after %d attempts. Consider setting strict_sampling to False.'
                                     % max_iterations)
            iterations += 1

            if controlled_sampling:
                # split sample_set into two buckets to sample controlled and uncontrolled checks from,
                # to guarantee occurrence of all reflectances amongst the controlled checks
                # (this is because draw_set is the repeated concatenation of the ordered reflectances)
                board = np.zeros((n_checks, n_checks))
                board[mask] = np.random.choice(sample_set[:mask_size], mask_size, replace=False)
                board[~mask] = np.random.choice(sample_set[mask_size:], total_checks - mask_size, replace=False)
            else:
                board = np.random.choice(sample_set, (n_checks, n_checks), replace=False)

            # check that no two adjacent cells have the same value (by checking top and left neighbour of each cell)
            for (i, j), val in np.ndenumerate(board):
                top_neighbour = board[i-1, j] if i > 0 else None
                left_neighbour = board[i, j-1] if j > 0 else None

                if val == top_neighbour or val == left_neighbour:
                    if not strict_sampling:
                        # redraw the value from all non-adjacent reflectances (see strict_sampling description)
                        restricted_draw_set = [r for r in reflectances if r != top_neighbour and r != left_neighbour]
                        board[i, j] = np.random.choice(restricted_draw_set)
                    else:
                        break  # break the for-loop in order to *not* enter the else-block and continue in while-loop
            else:
                break  # else-block wasn't entered => no adjacent duplicates => break the while-loop

        # fill r_checks with values from the board
        for i in range(n_checks):
            for j in range(n_checks):
                key = '%s%.2d' % (string.ascii_lowercase[i], j + 1)
                self.r_checks[key] = board[i, j]

    def build_image(self, tau, alpha, background=.27, camera_offset=None, look_at_offset=None,
                    transparency_coords=None, filename='checkerboard', resolution=(480, 480)):
        """
        Add the transparency layer to the checkerboard and generate the image.
        
        Parameters
        ----------
        tau : float
            Reflectance [in povray a.u.] of the transparent partial overlay. [0.0, 10.0]
        alpha : float
            Alpha value of the transparent partial overlay. [0.0, 1.0]
        background : float
            Background luminance. [0.0, 1.0]
        camera_offset, look_at_offset : tuple[int], None
            xyz coordinate offset from default camera position / look_at focus position
            !!! Attention: If offsets are specified, no functionality associated with masks or cutouts will work!
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
        if camera_offset is None:
            camera_offset = (0, 0, 0)
        else:
            self.camera_offsets_specified = True
        if look_at_offset is None:
            look_at_offset = (0, 0, 0)
        else:
            self.camera_offsets_specified = True

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

    def get_checkerboard(self, cropped=False, return_mask=False):
        """
        Get the entire image of the checkerboard and the transparent rectangle.

        Parameters
        ----------
        cropped : bool
            If True, there will be no rows/cols with containing only the background.
        return_mask : bool
            see below

        Returns
        -------
        checkerboard : np.ndarray
            The image as 2D array.
        mask : np.ndarray, optional
            A mask for the intersection of checkerboard and transparent rectangle.
        """
        checkerboard = self.image.copy()

        if cropped:
            if self.camera_offsets_specified:
                warnings.warn('Camera offsets have been specified. All cutouts and masks are incorrect!')
            if return_mask:
                return checkerboard[209:425, 63:417], self.mask[209:425, 63:417]
            else:
                return checkerboard[209:425, 63:417]
        else:
            if return_mask:
                return checkerboard, self.mask
            else:
                return checkerboard

    def get_cutout(self, cropped=False, return_mask=False):
        """
        Get the cutout of the intersection of the transparent rectangle and the checkerboard.

        Parameters
        ----------
        cropped : bool
            If True, there will be no rows/cols with containing only the background.
        return_mask : bool
            see below

        Returns
        -------
        cutout : np.ndarray
            The image as 2D array.
        mask : np.ndarray, optional
            A mask for the cutout.
        """
        if self.camera_offsets_specified:
            warnings.warn('Camera offsets have been specified. All cutouts and masks are incorrect!')

        cutout = self.image.copy()
        bg = cutout[0, 0]
        cutout[self.mask == 0] = bg

        if cropped:
            if return_mask:
                return cutout[289:377, 139:341], self.mask[289:377, 139:341]
            else:
                return cutout[289:377, 139:341]
        else:
            if return_mask:
                return cutout, self.mask
            else:
                return cutout

    def get_stacked(self, distance=100, return_masks=False):
        """
        Combine cutout and non-cutout-checkerboard in one image, stacked atop each other.

        Parameters
        ----------
        distance : int, optional
            space in between object
        return_masks : bool, optional
            see below

        Returns
        -------
        stacked : np.ndarray
            the image with values between 0.0 and 1.0
        mask_checkerboard : np.ndarray, optional
            mask for the intersection of checkerboard and transparent rectangle in the upper part
        mask_cutout : np.ndarray, optional
            mask for the cutout in the lower part
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

        if return_masks:
            return stacked, mask_checkerboard, mask_cutout
        else:
            return stacked


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
        background luminance
    light : float
        light source intensity
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
    # calculate a n-dimensional pattern
    n = 8
    f.find_checkerboard(n)

    # render an image, including transparent rectangle
    tau = 2
    alpha = .5
    f.build_image(tau, alpha, background=.5)
    # get a comparable stacked version of the original image and a cutout of the board-transparency intersection
    img1 = f.get_stacked()

    plt.figure()
    plt.imshow(img1, cmap='gray', vmin=0, vmax=1)
    plt.show()

    # move the camera to the right (but keep look_at point constant) before rendering
    f.build_image(0, 1, camera_offset=(5, 0, 0), look_at_offset=(0, 0, 0))
    # when offsets are specified, only get_checkerboard may be used
    img1 = f.get_checkerboard()

    plt.figure()
    plt.imshow(img1, cmap='gray', vmin=0, vmax=1)
    plt.show()


if __name__ == "__main__":
    main()
