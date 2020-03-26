# -*- coding: utf-8 -*-
"""
Generate stimulus resembling Todd (2010) paper, bricks on a wall.

@author: G. Aguilar, Jul 2014
"""

import numpy as np
import cairo
import Image
import random
from math import pi

def draw_rounded(cr, area, radius):
    """ draws rectangles with rounded (circular arc) corners """
    
    a,b,c,d=area
    cr.arc(a + radius, c + radius, radius, 2*(pi/2), 3*(pi/2))
    cr.arc(b - radius, c + radius, radius, 3*(pi/2), 4*(pi/2))
    cr.arc(b - radius, d - radius, radius, 0*(pi/2), 1*(pi/2))  # ;o)
    cr.arc(a + radius, d - radius, radius, 1*(pi/2), 2*(pi/2))
    cr.close_path()
    

def draw(rootname, w=500, h=2500, bh=30, bw=45, sep=7, roundrad=5, lum=(0.0, 0.65)):
    """
    Generate 'bricks' stimulus
    
    Parameters
    ----------
    
    rootname : string
            filename used as output
    w, h:  ints
        width and height of desired stimulus, in pix.
    bh, bw:  ints
        width and height of bricks, in pix.
    sep : int
        separation between bricks, in pix.
    rounrad : int  
        radius for rounded corners, in pix.
    lum : tuple (double, double)
        min and max grayvalues for bricks, in the range [0, 1]
    
    Luminance for each brick is randomly taken from uniform distribution 
    from lum min and max. Bricks separation is always maximum (white).

    """

    outputpng = "%s.png" % rootname
    lummin, lummax = lum
        
    ####### getting bricks positions
    x= np.arange(-2*bw, w+2*bw, bw+sep ) + random.random() * (bw+sep)
    y= np.arange(-2*bh, h+2*bh, bh+sep ) + random.random() * (bh+sep)

    X,Y=np.meshgrid(x,y)

    # offseting every other row
    X[0::2] = X[0::2]  + bw/2.0

    ####### drawing with cairo
    data = np.zeros( (w, h, 4), dtype=np.uint8)
    surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, w, h)
    cr = cairo.Context(surface)

    # fill with solid white
    cr.set_source_rgb(1.0, 1.0, 1.0)
    cr.paint()

    # drawing 
    for i in range( X.shape[0]):
        for j in range ( X.shape[1]):
                
            #cr.rectangle( X[i,j], Y[i,j] , bw, bh) # x, y of top left, width and height
            
            # (top, bottom, left, right) edges in absolute coordinates:
            inside_area = (X[i,j], X[i,j]+ bw, Y[i,j], Y[i,j] + bh)
            draw_rounded(cr, inside_area, roundrad)
            
            cr.set_line_width(0)               # width
            lum = random.random() * ( lummax- lummin)
            cr.set_source_rgb( lum, lum, lum)   # r,g,b in [0,1]
            cr.fill()
            cr.stroke()
            

    # write output
    surface.write_to_png( outputpng )
    del surface
        
    


