import numpy as np
from stimuli.utils import resize_array, write_array_to_image
import PIL as pil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# choose values by hand 
value_1 = 255
value_2 = 200
value_3 = 165
value_4 = 130

# choose ppd 
ppd = 64

def ini_matrix(ppd):
    a = []
    for i in range(ppd):
        a.append(np.zeros(ppd))
    return(a)

def get_mask(arr_list, ppd):
    mask = np.array(ini_matrix(ppd))
    target1 = arr_list[0]
    target2 = arr_list[1]
    
    
    for i in range(int(ppd/16)):
        y_diff = target1[2] - target1[0] +1
        for j in range(y_diff):
            y = target1[0]
            x = target1[1]
            mask[y+j][x+i] = 1 
    
    for i in range(int(ppd/16)):
        y_diff = target2[2] - target2[0] +1
        for j in range(y_diff):
            y = target2[0]
            x = target2[3]
            mask[y+j][x+i] = 2
        
    plt.imshow(mask)
    return(mask)


def get_array(num, row):
    arr = np.array([row])
    for i in range(num):
        arr_add = np.array([row])
        arr = (np.concatenate((arr,arr_add)))
    return arr

def koffka_mask():
    arr_1 = np.array([int(ppd/2),int(ppd *(3/4)),int(ppd *(3/4)),int(ppd *(3/4)) ])
    
    arr_2 = np.array([int(ppd *(5/16)),int(ppd *(5/16)),int(ppd *(9/16)),int(ppd *(5/16))])
    arr_list = [arr_1,arr_2]
    
    mask = get_mask(arr_list,ppd)
    
    return(mask)


def koffka_adelson_auto():
    
    a = np.ones((ppd,1), dtype = int)*value_4
    
    b = np.ones((ppd,1), dtype = int)*value_4
    x = int(ppd/8)
    y = int(ppd*(11/16))
    b[x:y] = value_2

    c = np.ones((ppd,1), dtype = int)*value_4
    x1 = int(ppd/8)
    y1 = int(ppd*(5/16))
    c[x1:y1] = value_2
    x2 = int(ppd/2)
    y2 = int(ppd*(11/16))
    c[x2:y2] = value_2

    d = np.ones((ppd,1), dtype = int)*value_1
    x1 = int(ppd*(5/16))
    y1 = int(ppd/2)
    d[x1:y1] = value_3
    x2 = int(ppd*(11/16))
    y2 = int(ppd*(7/8))
    d[x2:y2] = value_3
    
    e = np.ones((ppd,1), dtype = int)*value_1
    x1 = x1
    y1 = y2
    e[x1:y1] = value_3
    
    f = np.ones((ppd,1), dtype = int)*value_1
    
    arr = np.concatenate((get_array(int(ppd*(3/16)),a),
                         get_array(int(ppd*(3/16)),b),
                         get_array(int(ppd*(2/16)),c),
                         get_array(int(ppd*(2/16)),d),
                         get_array(int(ppd*(3/16)),e),
                         get_array(int(ppd*(3/16)),f)))

    arr = np.fliplr(np.rot90((arr),3))
    return(arr)

if __name__ == '__main__':
    #test
    #plt.imshow(koffka_adelson_auto())
    #koffka_mask()
    
      
