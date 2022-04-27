import numpy as np
from os.path import dirname, join as pjoin
import scipy.io as sio

data_dir = pjoin(dirname(sio.__file__), 'matlab', 'ablage')  
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

# mask functions 

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
        a.append(np.zeros(25))
    return(a)


def get_mask_argyle():
   a = mat_content['argyle']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-int(ppd/16),t2-int(ppd/16)]
   #arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))   
   return (get_mask(arr_list, ppd, mask))
   
def get_mask_argyle_control():
   a = mat_content['argyle_control']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1] 
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_argyle_long():
   a = mat_content['argyle_long']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix_2(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_snake():
   a = mat_content['snake']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1] 
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_snake_control():
   a = mat_content['snake_control']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_koffka_adelson():
   a = mat_content['koffka_adelson']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1] 
   mask = np.array(ini_matrix(ppd))
   get_mask(arr_list, ppd, mask)
   
def get_mask_koffka_broken():
   a = mat_content['koffka_broken']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1] 
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_koffka_connected():
   a = mat_content['koffka_connected']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1] 
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_checkassim():
   a = mat_content['checkassim']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_simcon():
   a = mat_content['simcon']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_simcon_articulated():
   a = mat_content['simcon_articulated']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))
   
def get_mask_white():
   a = mat_content['white']
   t = np.array((((a[0])[0])[1])[0])
   t2 = np.array((((a[0])[0])[2])[0])
   arr_list = [t-1,t2-1]
   mask = np.array(ini_matrix(ppd))
   return(get_mask(arr_list, ppd, mask))

# illusion functions 

def argyle_illusion():
   img = argyle()
   mask = get_mask_argyle()
   return {"img": img, "mask": mask}

def argyle_control_illusion():
    img = argyle_control()
    mask = get_mask_argyle_control()
    return {"img": img, "mask": mask}   

def argyle_long_illusion():
    img = argyle_long()
    mask = get_mask_argyle_long()
    return {"img": img, "mask": mask}  

def snake_illusion():
    img = snake()
    mask = get_mask_snake()
    return {"img": img, "mask": mask}  

def snake_control_illusion():
    img = snake_control()
    mask = get_mask_snake_control()
    return {"img": img, "mask": mask} 

def koffka_adelson_illusion():
    img = koffka_adelson()
    mask = get_mask_koffka_adelson()
    return {"img": img, "mask": mask} 

def koffka_broken_illusion():
    img = koffka_broken()
    mask = get_mask_koffka_broken()
    return {"img": img, "mask": mask} 

def koffka_connected_illusion():
    img = koffka_connected()
    mask = get_mask_koffka_connected()
    return {"img": img, "mask": mask} 

def checkassim_illusion():
    img = checkassim()
    mask = checkassim()
    return {"img": img, "mask": mask} 

def simcon_illusion():
    img = simcon()
    mask = get_mask_simcon()
    return {"img": img, "mask": mask} 

def simcon_articulated_illusion():
    img = simcon_articulated()
    mask = get_mask_simcon_articulated()
    return {"img": img, "mask": mask} 

def white_illusion():
    img = white()
    mask = get_mask_white()
    return {"img": img, "mask": mask} 


# script 


#def argyle_illusion():
    #return stimuli.illusions.argyle_illusion()
    
#def argyle_control_illusion():
    #return stimuli.illusions.argyle_control_illusion()
    
#def argyle_long_illusion():
    #return stimuli.illusions.argyle_long_illusion()

#def snake_illusion():
    #return stimuli.illusions.snake_illusion()
    
#def snake_control_illusion():
    #return stimuli.illusions.snake_control_illusion()
    
#def koffka_adelson_illusion():
    #return stimuli.illusions.koffka_adelson_illusion()
    
#def koffka_broken_illusion():
    #return stimuli.illusions.koffka_broken_illusion()
    
#def koffka_connectedn_illusion():
    #return stimuli.illusions.koffka_connected_illusion()

#def checkassim_illusion():
    #return stimuli.illusions.checkassim_illusion()
    
#def simcon_illusion():
    #return stimuli.illusions.simcon_illusion()
    
#def simcon_articulated_illusion():
    #return stimuli.illusions.simcon_articulated_illusion()
    
#def white_illusion():
    #return stimuli.illusions.white_illusion()


if __name__ == '__main__':
    
    ppd = 16
    
    # 1
    
    # test argyle illusion
    #plt.subplot(1,2,1)
    #plt.imshow(argyle(), cmap='gray')
    #plt.subplot(1,2,2)
    #plt.imshow(get_mask_argyle(), cmap='gray')
    
    
    # 2 
    
    import matplotlib.pyplot as plt
    stim = argyle_illusion()
    #plt.imshow(stim.img, cmap='gray')
    #plt.imshow(stim['img'], cmap='gray')
    
    plt.imshow(stim['img']+stim['mask'])
    

    
    # 3
    
    #img = np.dstack([stim['img'], stim['img'], stim['img']])
    #mask = np.insert(np.expand_dims(stim['mask'], 2), 1, 0, axis=2)
    #mask = np.insert(mask, 2, 0, axis=2)
    #final = mask + img
    #final /= np.max(final)

    #import math 
    #a = math.ceil(math.sqrt(len(stim)))
    #plt.figure(figsize=(a*3, a*3))

    #plt.subplot(a, a, 0 + 1)
    #plt.title("argyle" + " - img")
    
    #plt.imshow(stim['img'])
    mask = stim['mask']*100
    plt.imshow((stim['img']+mask)/np.max(stim['img']+stim['mask']))
    #plt.imshow(mask)
    #plt.imshow(final)
    #plt.show()
    
    
