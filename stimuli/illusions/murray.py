import numpy as np
import matplotlib.pyplot as plt  
import math 
from os.path import dirname, join as pjoin
import scipy.io as sio
  
data_dir = pjoin(dirname(sio.__file__), 'matlab', 'ablage')   
mat_fname = pjoin(data_dir, 'grid_stimuli.mat')
mat_content = sio.loadmat(mat_fname)

# mask function

def get_mask(arr_list, ppd, mask):
    target1 = arr_list[0]
    target2 = arr_list[1]
    y = target1[0]
    x = target1[1]
    mask[y][x] = 1
    y = target1[2]
    x = target1[3]
    mask[y][x] = 1
    
    x_diff = target1[3] - target1[1] +1
    for i in range(x_diff):
        y_diff = target1[2] - target1[0] +1
        for j in range(y_diff):
            y = target1[0]
            x = target1[1]
            mask[y+j][x+i] = 1  
      
    y = target2[0]
    x = target2[1]
    mask[y][x] = 2
    y = target2[2]
    x = target2[3]
    mask[y][x] = 2
    
    x_diff = target2[3] - target2[1] +1
    for i in range(x_diff):
        y_diff = target2[2] - target2[0] +1
        for j in range(y_diff):
            y = target2[0]
            x = target2[1]
            mask[y+j][x+i] = 2

    plt.imshow(mask)
    return(mask)

    
def ini_matrix(ppd):
    a = []
    for i in range(ppd):
        a.append(np.zeros(ppd))
    return(a)

def ini_matrix_2(ppd):
    a = []
    for i in range(ppd):
        a.append(np.zeros(24))
    return(a)

  
# illusion functions

def argyle_illusion(ppd):
   argyle = mat_content['argyle']
   img = np.array(((argyle[0])[0])[0])
   a = mat_content['argyle']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-int(ppd/16),t2-int(ppd/16)]
   mask = np.array(ini_matrix(ppd)) 
   mask = get_mask(arr_list, ppd, mask)
   return {"img": img, "mask": mask}


def argyle_control_illusion(ppd):
    argyle_control = mat_content['argyle_control']
    img = np.array(((argyle_control[0])[0])[0])
    a = mat_content['argyle_control']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1] 
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def argyle_long_illusion(ppd):
    argyle_long = mat_content['argyle_long']
    img = np.array(((argyle_long[0])[0])[0])
    a = mat_content['argyle_long']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix_2(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}  


def snake_illusion(ppd):
    snake = mat_content['snake']
    img = np.array(((snake[0])[0])[0])
    a = mat_content['snake']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1] 
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask}  


def snake_control_illusion(ppd):
    snake_control = mat_content['snake_control']
    img = np.array(((snake_control[0])[0])[0])
    a = mat_content['snake_control']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def koffka_adelson_illusion(ppd):
    koffka_adelson = mat_content['koffka_adelson']
    img = np.array(((koffka_adelson[0])[0])[0])
    a = mat_content['koffka_adelson']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1] 
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def koffka_broken_illusion(ppd):
    koffka_broken = mat_content['koffka_broken']
    img = np.array(((koffka_broken[0])[0])[0])
    a = mat_content['koffka_broken']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1] 
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def koffka_connected_illusion(ppd):
    koffka_connected = mat_content['koffka_connected']
    img = np.array(((koffka_connected[0])[0])[0])
    a = mat_content['koffka_connected']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1] 
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 



def checkassim_illusion(ppd):
    checkassim = mat_content['checkassim']
    img = np.array(((checkassim[0])[0])[0])
    a = mat_content['checkassim']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def simcon_illusion(ppd):
    simcon = mat_content['simcon']
    img = np.array(((simcon[0])[0])[0])
    a = mat_content['simcon']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def simcon_articulated_illusion(ppd):
    simcon_articulated = mat_content['simcon_articulated']
    img = np.array(((simcon_articulated[0])[0])[0])
    a = mat_content['simcon_articulated']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 


def white_illusion(ppd):
    white = mat_content['white']
    img = np.array(((white[0])[0])[0])
    a = mat_content['white']
    t = np.array((((a[0])[0])[1])[0])
    t2 = np.array((((a[0])[0])[2])[0])
    arr_list = [t-1,t2-1]
    mask = np.array(ini_matrix(ppd))
    mask = get_mask(arr_list, ppd, mask)
    return {"img": img, "mask": mask} 

