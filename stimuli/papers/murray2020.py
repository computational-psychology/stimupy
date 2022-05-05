# gitlab 

import numpy as np
import math
import matplotlib.pyplot as plt
import stimuli


def argyle_illusion():
    return stimuli.illusions.murray2020.murray.argyle_illusion() 
    
def argyle_control_illusion():
    return stimuli.illusions.murray2020.murray.argyle_control_illusion()
    
def argyle_long_illusion():
    return stimuli.illusions.murray2020.murray.argyle_long_illusion()

def snake_illusion():
    return stimuli.illusions.murray2020.murray.snake_illusion()
    
def snake_control_illusion():
    return stimuli.illusions.murray2020.murray.snake_control_illusion()
    
def koffka_adelson_illusion():
    return stimuli.illusions.murray2020.murray.koffka_adelson_illusion()
    
def koffka_broken_illusion():
    return stimuli.illusions.murray2020.murray.koffka_broken_illusion()
    
def koffka_connected_illusion():
    return stimuli.illusions.murray2020.murray.koffka_connected_illusion()

def checkassim_illusion():
    return stimuli.illusions.murray2020.murray.checkassim_illusion()
    
def simcon_illusion():
    return stimuli.illusions.murray2020.murray.simcon_illusion()
    
def simcon_articulated_illusion():
    return stimuli.illusions.murray2020.murray.simcon_articulated_illusion()
    
def white_illusion():
    return stimuli.illusions.murray2020.murray.white_illusion()

    
if __name__ == '__main__':
    
    ppd = 16
    
    plot_all = True
    if plot_all:
        stims = {"argyle_illusion": argyle_illusion(), 
                 "argyle_control_illusion": argyle_control_illusion(),
                 "argyle_long_illusion": argyle_long_illusion(),
                 "snake_illusion": snake_illusion(),
                 "snake_control_illusion": snake_control_illusion(),
                 "koffka_adelson_illusion": koffka_adelson_illusion(),
                 "koffka_broken_illusion": koffka_broken_illusion(),
                 "koffka_connected_illusion": koffka_connected_illusion(),
                 "checkassim_illusion": checkassim_illusion(),
                 "simcon_illusion": simcon_illusion(),
                 "simcon_articulated_illusion": simcon_articulated_illusion(),
                 "white_illusion": white_illusion()          
                 }
        
        a = math.ceil(math.sqrt(len(stims)))
        plt.figure(figsize=(a*3, a*3))
        for i, (stim_name, stim) in enumerate(stims.items()):
            print("Generating", stim_name+"")
            img, mask = stim["img"], stim["mask"]
            img = np.dstack([img, img, img])

            mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
            mask = np.insert(mask, 2, 0, axis=2)
            
            final = mask*100 + img
            final /= np.max(final)

            plt.subplot(a, a, i + 1)
            plt.title(stim_name + " - img")
            plt.imshow(final)

        plt.tight_layout()

    else:
        plt.imshow(img, cmap='gray')

    plt.show()
