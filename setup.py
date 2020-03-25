#!/usr/bin/env python

import distutils.core

if __name__ == '__main__':
    distutils.core.setup(
        name='stimuli',
        description='Library for creating different visual stimuli for psychophysic experiments',
        version='0.1',
        author='Guillermo Aguilar',
        author_email='guillermo.aguilar@mail.tu-berlin.de',
        license='GPL2',
        url='https://github.com/computational-psychology/stimuli',
        package_dir={
            'stimuli.lightness': 'lightness',
            'stimuli.texture': 'texture',
            'stimuli.transparency': 'transparency',
            'stimuli.contrast_measures': 'contrast_measures',
            'stimuli.utils': 'utils',
        },
        packages=[
            'stimuli.lightness',
            'stimuli.texture',
            'stimuli.transparency',
            'stimuli.contrast_measures',
            'stimuli.utils'
        ],
        python_requires='>=3.6'
    )
