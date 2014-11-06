# -*- coding: utf-8 -*-
"""
Generate "circles" and "voronoi" texture types, using 
point process simulation in R.
It implements same texture types used in Rosas et al. (2004). JoV

R and the CRAN package "spatstat" must be installed on the system.

See R help for more information (functions rHardcore(), rSSI() and rmh())
and references:

Baddeley and Turner. Spatstat: an R package for analyzing spatial point patterns
Journal of Statistical Software 12: 6 (2005) 1-42.


@author: G. Aguilar, Sept 2013. Update Nov 2014.
"""

import numpy as np
#import matplotlib.pyplot as plt
import os
import cairo
import math
import tessutils    # tessellation utils
import Image


def generate_hardcore(rootname, beta=3, R = 0.52, size = 42.5, factor=100, circlerad=24, algo='ssi', N=3500, tess=True ):
    """
    Generate a random spatial point process with inhibition distance (hardcore process).
    
    An instance of a random spatial point process is generated, and its 
    spatial position are used as centers for drawing circles ('polka dots')
    and simultaneously for creating a voronoi tesselation.
        
    It depends on R package 'spatstat', and on python packages cairo, PIL and rpy2.
    
    
    Parameters
    ----------
    
    rootname: string
               filename used to save output images
               
    tess: bool
            Do/don't do tesselations. Default: True
            
              
    Point process parameters
    ----------
    
    algo: 'ssi', 'rmh' or 'perfect'
            algorithm from spatstat package to be used.
            
            'perfect' calls R function rHardcore()
            'rmh' calls R function rmh()
            'ssi' calls R function rSSI()
            
            Check the documentation of those function in R for more information.
            
    beta: double
            intensity parameter for hardcore point process. Only valid for algorithms 'perfect' and 'rmh'.
    N: int
            number of dots to be generated. Only valid for algorithm 'ssi'.
    R:  double
            distance of inhibition
    size: double
            size of the (squared) surface
    factor: double
            scaling factor, it multiplies the arguments size, R and circlerad. Default: 100
            
    circlerad: double
            radius of circles in pix.
    

    Returns
    -------
    x,y : numpy arrays containing x and y coordinates of circles' centers.
    
    
    Notes
    -------
    Default values aim to replicate Rosas et al. (2004) paper, section 2.2.2.

    """
    
    #############################################################################
    ## hard-core process parameters
    # parameters from Rosas (2004), section 2.2.2, 100 times downsampled.
    
    #factor = 100
    #beta = 3        # intensity parameter of hardcore process   
    #R = 0.26*2      # * 100 = 26 pix inhibition radius , 26*2 inhibition distance
    #size = 42.5     # * 100 = 4250 pix
    #circlerad = 24  # radius of circles, [pix]
    
    totalsize = int(size * factor)
    
    #############################################################################   
    ## writing R file
    files=[]
    Rfile = rootname + ".R"         # r script
    csvfile = rootname + ".csv"     # centroids file
    tessfile = rootname + ".tess"   # tessellations file
    
    fid = open(Rfile, "w+")
    
    seq1 = ["options(width = 2000)\n",
           "library(spatstat)\n", 
           "df <- data.frame()\n"]
           
    if algo=='perfect':
        seqalgo = ['X <- rHardcore(%f, %f, square(%f))\n' % (beta, R, size)] 
    
    elif algo=='ssi':
        seqalgo = ['X <- rSSI(%f, %d, square(%f), 1e10)\n' % (R, N, size)] 
        
    else:
        seqalgo = ['mod <- list(cif="hardcore",par=list( beta = %f, hc=%f), w = square(%f) )\n' % (beta, R, size),
                   'X <- rmh(model=mod,  control=list(nrep = 1e5,nverb = 0))\n']
               
    seq2 = ["df<-coords(X)\n", 
           'write.csv(df, file="%s")\n' % csvfile]
    if tess:
        seq2.extend( ['tessetiles = tiles(dirichlet(X))\n',
           'save(tessetiles, file="%s")\n' % tessfile])
    
    seq = seq1 + seqalgo + seq2
    fid.writelines(seq)
    fid.close()
    
    ## executing R
    st = os.system("R --no-save < %s" % Rfile) 
    
    ## reading results
    if st==0:
        print "reading generated data"    
        x, y = np.loadtxt(csvfile, skiprows=1, usecols=(1,2), unpack=True, delimiter=',')    
        
    else:
        print "error in R execution"    
        
    
    ##############################################################################
    ### Step 1: creating circular texture with these centroids
    ####### working now with pix units
    circlespng = rootname + "_circles.png"
    files.append( circlespng )
    
    data = np.zeros( (totalsize, totalsize, 4), dtype=np.uint8)
    surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, totalsize, totalsize)
    cr = cairo.Context(surface)
    
    # fill with solid mid gray
    cr.set_source_rgb(0.5, 0.5, 0.5)
    cr.paint()
    
    # drawing circles
    for i in range(len(x)):
        cr.arc(x[i]*factor, y[i]*factor, circlerad, 0, 2*math.pi) # xc, yc, radius, angle1, angle2
        cr.set_line_width(0)               # width
        cr.set_source_rgb(0, 0, 0)   # r,g,b in [0,1]
        cr.fill()
        cr.stroke()
    
    # write output
    surface.write_to_png( circlespng )
    del surface
    
    
    ##############################################################################
    ### Step 2: creating tessellation texture with these centroids
    # loading tess file
    if tess:
        voronoipng = rootname + "_voronoi.png"
        files.append( voronoipng )
        
        #tess = tessutils.read_tess(tessfile)
        tess = tessutils.read_tess_Rfile(tessfile)
        
        # drawing tessels in cairo   
        data = np.zeros((totalsize, totalsize, 4), dtype=np.uint8)
        surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, totalsize, totalsize)
        cr = cairo.Context(surface)
        
        # fill with solid mid gray
        cr.set_source_rgb(0.5, 0.5, 0.5)
        cr.paint()
            
        # drawing polygons
        for i in range(len(tess)):
            
            tx = tess[i]['x']
            ty = tess[i]['y']
        
            cr.set_source_rgb(0, 0, 0)   # r,g,b in [0,1]
            
            cr.move_to(tx[0]*factor, ty[0]*factor)
            
            for p in range(len(tx)-1):
                cr.line_to(tx[p+1]*factor,ty[p+1]*factor)
            cr.close_path()
        
            cr.set_line_width(10)               # width
            #cr.fill()
            cr.stroke()
        
        # write output
        surface.write_to_png( voronoipng )
        del surface    

    return (x,y, files)



def sample(filename, n=1, size=(800, 800)):
    """
    Generates samples from a PNG image file, randomly centered.
    
    Parameters
    ----------
    
    rootname: string
               filename
    n:  int
        number of random samples
    size: tuple (width, height)
        size of sample
        
    """
    sx, sy = size[0], size[1]
    rootname = filename.split('.')[0]
    
    if sx==sy:
        prefix = rootname + "_" + str(size[0])
    else: 
        prefix = rootname + "_" + str(size[0]) + "x" + str(size[1])
    
    # reading image file
    im = np.array(Image.open(filename))
    width, height, d = im.shape
    
    assert(sx <= width)
    assert(sy <= height)
    
    #  sampling area
    x1 = int(np.ceil( sx/2.0 ))
    x2 = int(np.floor( width - sx/2.0 ))
    
    y1 = int(np.ceil( sy/2.0 ))
    y2 = int(np.floor( height - sy/2.0 ))
    
    
    # generate uniformly distributed numbers for the sample centers
    centersx = np.round(np.random.uniform(x1,x2,size= n))
    centersy = np.round(np.random.uniform(y1,y2,size= n))
    
    
    for i in range(n):
        
        cx = int(centersx[i])
        cy = int(centersy[i])
        
        sm = im[cx-sx/2:cx+sx/2][:,cy-sy/2:cy+sy/2]
        
        Image.fromarray(sm).save("%s_%d.png" % (prefix, i))

