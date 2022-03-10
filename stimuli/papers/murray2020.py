import numpy as np
from os.path import dirname, join as pjoin
import scipy.io as sio
import matplotlib.pyplot as plt
   
data_dir = pjoin(dirname(sio.__file__), 'your_directory_1', 'your_directory_2')   
mat_fname = pjoin(data_dir, 'grid_stimuli.mat')
mat_content = sio.loadmat(mat_fname)
    
def argyle():
    argyle = mat_content['argyle']
    argyle = np.array(((argyle[0])[0])[0])
    #print(argyle)
    return argyle 

def argyle_control():
    argyle_control = mat_content['argyle_control']
    argyle_control = np.array(((argyle_control[0])[0])[0])
    #print(argyle_control)
    return argyle_control 

def argyle_long():
    argyle_long = mat_content['argyle_long']
    argyle_long = np.array(((argyle_long[0])[0])[0])
    #print(argyle_long)
    return argyle_long 

def snake():
    snake = mat_content['snake']
    snake = np.array(((snake[0])[0])[0])
    #print(snake)
    return snake 

def snake_control():
    snake_control = mat_content['snake_control']
    snake_control = np.array(((snake_control[0])[0])[0])
    #print(snake_control)
    return snake_control 

def koffka_adelson():
    koffka_adelson = mat_content['koffka_adelson']
    koffka_adelson = np.array(((koffka_adelson[0])[0])[0])
    #print(koffka_adelson)
    return koffka_adelson 

def koffka_broken():
    koffka_broken = mat_content['koffka_broken']
    koffka_broken = np.array(((koffka_adelson[0])[0])[0])
    #print(koffka_broken)
    return koffka_broken 

def koffka_connected():
    koffka_connected = mat_content['koffka_connected']
    koffka_connected = np.array(((koffka_connected[0])[0])[0])
    #print(koffka_connected)
    return koffka_connected

def checkassim():
    checkassim = mat_content['checkassim']
    checkassim = np.array(((checkassim[0])[0])[0])
    #print(checkassim)
    return checkassim

def simcon():
    simcon = mat_content['simcon']
    simcon = np.array(((simcon[0])[0])[0])
    #print(simcon)
    return simcon

def simcon_articulated():
    simcon_articulated = mat_content['simcon_articulated']
    simcon_articulated = np.array(((simcon_articulated[0])[0])[0])
    #print(simcon_articulated)
    return simcon_articulated

def white():
    white = mat_content['white']
    white = np.array(((white[0])[0])[0])
    #print(white)
    return white


#if __name__ == '__main__':
    #plt.imshow(argyle())
