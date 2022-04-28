import numpy as np
import math
import matplotlib.pyplot as plt
import stimuli


def argyle_illusion():
    return stimuli.illusions.argyle_illusion()
    
def argyle_control_illusion():
    return stimuli.illusions.argyle_control_illusion()
    
def argyle_long_illusion():
    return stimuli.illusions.argyle_long_illusion()

def snake_illusion():
    return stimuli.illusions.snake_illusion()
    
def snake_control_illusion():
    return stimuli.illusions.snake_control_illusion()
    
def koffka_adelson_illusion():
    return stimuli.illusions.koffka_adelson_illusion()
    
def koffka_broken_illusion():
    return stimuli.illusions.koffka_broken_illusion()
    
def koffka_connected_illusion():
    return stimuli.illusions.koffka_connected_illusion()

def checkassim_illusion():
    return stimuli.illusions.checkassim_illusion()
    
def simcon_illusion():
    return stimuli.illusions.simcon_illusion()
    
def simcon_articulated_illusion():
    return stimuli.illusions.simcon_articulated_illusion()
    
def white_illusion():
    return stimuli.illusions.white_illusion()

    
if __name__ == '__main__':
    
    ppd = 16
    
    plot_all = True
    if plot_all:
        stims = {"argyle_illusion": argyle_illusion(), 
                 "argyle_control_illusion": argyle_control_illusion(),
                 #"argyle_long_illusion": argyle_long_illusion(),
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
            
            mask = stim['mask']*100
            final = (stim['img']+mask)/np.max(stim['img']+stim['mask'])
            
            plt.subplot(a, a, i + 1)
            plt.title(stim_name + " - img")
            plt.imshow(final)

        plt.tight_layout()

    else:
        plt.imshow(stim['img'], cmap='gray')

    plt.savefig("overview_murray2020.png")
    plt.show()
    
