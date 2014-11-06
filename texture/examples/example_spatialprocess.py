# -*- coding: utf-8 -*-
"""
Example script that generate a texture of random dots using 
stochastic geometry. It creates the 'polka dots' texture, that consist of 
randomly placed circles with an inhibition distance, and a voronoi 
tesselation. Both are computed using a 'hardcore' point process in R.

These functions generate the centers and draws them immediately to a png file.

Dependencies: R with the 'spatstat' package.
              in python: PIL, cairo and rpy2.
              
@author: G. Aguilar, 2013-14
"""
import sys
sys.path.append('..')

from spatialprocess import hardcore

# Generates one instance of 3500 number of circles / centroids, using
# default parameters of size and inhibition distance. It also creates a 
# tesselation using those points as centroids.

rootname = "test"
x,y, files = hardcore.generate_hardcore(rootname, N=3500, tess=True)


# from the image files, it creates 5 different samples at random locations. 
hardcore.sample(files[0], n=5)
hardcore.sample(files[1], n=5)

    

