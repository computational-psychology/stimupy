#!/usr/bin/env python

import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='stimuli',
        description='Library for creating different visual stimuli for psychophysic experiments',
        version='0.8',
        author='Guillermo Aguilar',
        author_email='guillermo.aguilar@mail.tu-berlin.de',
        license='GPL2',
        url='https://github.com/computational-psychology/stimuli',
        package_dir={'stimuli': 'src'},
        packages=(
            'stimuli',
            'stimuli.lightness',
            'stimuli.contrast_metrics',
            'stimuli.utils',
            'stimuli.texture',
            'stimuli.transparency',
            'stimuli.illusions'
        ),
        package_data={'stimuli.transparency': ['checkerboard_mask.png']},
        install_requires=[
            'numpy',
            'scipy',
            'matplotlib',
            'pillow'
        ]
    )
