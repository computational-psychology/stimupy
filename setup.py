#!/usr/bin/env python

import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='stimuli',
        description='Library for creating different visual stimuli for psychophysic experiments',
        version='0.7',
        author='Guillermo Aguilar',
        author_email='guillermo.aguilar@mail.tu-berlin.de',
        license='GPL2',
        url='https://github.com/computational-psychology/stimuli',
        package_dir={'stimuli': 'src'},
        packages=(
            'stimuli',
            'stimuli.texture',
            'stimuli.transparency',
        ),
        package_data={'stimuli.transparency': ['checkerboard_mask.png']}
    )
