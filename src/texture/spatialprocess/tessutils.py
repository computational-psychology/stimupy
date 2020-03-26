# -*- coding: utf-8 -*-
"""
Utility functions to read and write .tess files

@author: G. Aguilar, Sept 2013
"""


 
 
def read_tess_Rfile(filename):
    """ 
    Internal function of hardcore module
    """

    from rpy2 import robjects
    
    robjects.r['load'](filename)
    tessetiles = robjects.r['tessetiles']
    
    nt = len(tessetiles)
    tessels = list()
    
    for i in range(nt):
        
        j = list(tessetiles[i].names).index('bdry')
        
        x = list(tessetiles[i][j][0][0])
        y = list(tessetiles[i][j][0][1])
        
        tessels.append(dict())
        tessels[i]['x'] = x
        tessels[i]['y'] = y
    
    return tessels
    
    
    
def read_tess(filename):
    #### deprecated and buggy function ####

    f = open(filename)
    lines = f.readlines()
    f.close()
    
    tessels = list()
    flag = 0
    i=0
    
    for l in lines:
        
        assert(l.split()[0]=='[1]')
        
        n = len(l.split())
        
        if flag==0 and n==2:  # we are at the beginng of a new tessel
            
            tessels.append(dict()) # initialize dictionary 
            tessels[i]['area'] = float(l.split()[1]) # we save the area
            flag=1
            
        elif flag==1 and n>2: # we save x values
            tessels[i]['x'] = [float(el) for el in l.split()[1:]]
            flag=2
            
        elif flag==2 and n>2: # we save y values
            tessels[i]['y'] = [float(el) for el in l.split()[1:]]
            
            assert(len(tessels[i]['x'])==len(tessels[i]['y']))
            
            flag=0
            i=i+1
            
            
        else:
            print("error in parsing the .tess file !!")
    
    # checks that all values have been read
    assert(len(tessels)==len(lines)/3.0)
    
    return tessels
    
   
