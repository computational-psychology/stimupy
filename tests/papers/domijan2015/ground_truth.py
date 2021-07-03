import numpy as np

lum_white = 9.0
lum_black = 1.0
lum_gray = 5.0

def get_dungeon():
    # Dungeon illusion (Bressan, 2001)
    img = lum_black * np.ones([110, 220])
    img[:, 110:220] = lum_white

    for i in range(9, 90, 20):
        for j in range(9, 90, 20):
            img[i : i + 10, j : j + 10] = lum_white
        for j in range(119, 210, 20):
            img[i : i + 10, j : j + 10] = lum_black

    img[49:59, 29:39] = lum_gray
    img[49:59, 49:59] = lum_gray
    img[49:59, 69:79] = lum_gray
    img[49:59, 139:149] = lum_gray
    img[49:59, 159:169] = lum_gray
    img[49:59, 179:189] = lum_gray

    img[29:39, 49:59] = lum_gray
    img[69:79, 49:59] = lum_gray
    img[29:39, 159:169] = lum_gray
    img[69:79, 159:169] = lum_gray
    
    return img

def get_cube():
    # Cube illusion (Agostini & Galmonte, 2002)
    img = lum_black * np.ones([100, 200])

    img[:, 100:200] = lum_white
    img[9:20, 9:90] = lum_white
    img[9:90, 9:20] = lum_white
    img[79:90, 9:90] = lum_white
    img[9:90, 79:90] = lum_white

    img[9:20, 109:190] = lum_black
    img[9:90, 109:120] = lum_black
    img[79:90, 109:190] = lum_black
    img[9:90, 179:190] = lum_black

    img[27:32, 9:90] = lum_black
    img[47:52, 9:90] = lum_black
    img[67:72, 9:90] = lum_black

    img[9:90, 27:32] = lum_black
    img[9:90, 47:52] = lum_black
    img[9:90, 67:72] = lum_black

    img[32:47, 9:20] = lum_gray
    img[52:67, 79:90] = lum_gray
    img[79:90, 32:47] = lum_gray
    img[9:20, 52:67] = lum_gray

    img[27:32, 109:190] = lum_white
    img[47:52, 109:190] = lum_white
    img[67:72, 109:190] = lum_white

    img[9:90, 127:132] = lum_white
    img[9:90, 147:152] = lum_white
    img[9:90, 167:172] = lum_white

    img[32:47, 109:120] = lum_gray
    img[52:67, 179:190] = lum_gray
    img[79:90, 132:147] = lum_gray
    img[9:20, 152:167] = lum_gray
    
    return img

def get_grating():
    # Grating illusion
    img = lum_black * np.ones([100, 220])
    img[:, 110:220] = lum_white

    for j in range(9, 100, 20):
        img[9:90, j : j + 10] = lum_white

    for j in range(119, 210, 20):
        img[9:90, j : j + 10] = lum_black

    img[9:90, 49:59] = lum_gray
    img[9:90, 159:169] = lum_gray
    
    return img

def get_ring():
    # Ring pattern
    img = lum_black * np.ones([100, 200])
    img[9:90, 9:90] = lum_white
    img[14:85, 14:85] = lum_black
    img[19:80, 19:80] = lum_white
    img[24:75, 24:75] = lum_gray
    img[29:70, 29:70] = lum_white
    img[34:65, 34:65] = lum_black
    img[39:60, 39:60] = lum_white
    img[44:55, 44:55] = lum_black

    img[9:90, 109:190] = lum_white
    img[14:85, 114:185] = lum_black
    img[19:80, 119:180] = lum_white
    img[24:75, 124:175] = lum_black
    img[29:70, 129:170] = lum_gray
    img[34:65, 134:165] = lum_black
    img[39:60, 139:160] = lum_white
    img[44:55, 144:155] = lum_black
    
    return img

def get_bullseye():
    # Bullseye illusion
    img = lum_black * np.ones([100, 200])
    img[9:90, 9:90] = lum_white
    img[14:85, 14:85] = lum_black
    img[19:80, 19:80] = lum_white
    img[24:75, 24:75] = lum_black
    img[29:70, 29:70] = lum_white
    img[34:65, 34:65] = lum_black
    img[39:60, 39:60] = lum_white
    img[44:55, 44:55] = lum_gray

    img[14:85, 114:185] = lum_white
    img[19:80, 119:180] = lum_black
    img[24:75, 124:175] = lum_white
    img[29:70, 129:170] = lum_black
    img[34:65, 134:165] = lum_white
    img[39:60, 139:160] = lum_black
    img[44:55, 144:155] = lum_gray
    
    return img

def get_sbc():
    # Simultaneous brightness contrast
    img = lum_black * np.ones([100, 200])
    img[:, 0:100] = lum_white
    img[39:60, 39:60] = lum_gray
    img[39:60, 139:160] = lum_gray
    
    return img

def get_white():
    # White illusion
    img = lum_gray * np.ones([100, 100])
    img[9:90, 9:19] = lum_black
    img[9:90, 19:29] = lum_white
    img[9:90, 29:39] = lum_black
    img[9:90, 39:49] = lum_white
    img[9:90, 49:59] = lum_black
    img[9:90, 59:69] = lum_white
    img[9:90, 69:79] = lum_black
    img[9:90, 79:89] = lum_white
    img[39:60, 29:39] = lum_gray
    img[39:60, 59:69] = lum_gray
    
    return img

def get_benary():
    # Benary's cross
    img = lum_white * np.ones([100, 100])
    img[39:60, 9:90] = lum_black
    img[9:90, 39:60] = lum_black
    img[39:50, 79:90] = lum_gray
    img[28:39, 28:39] = lum_gray
    
    return img

def get_todorovic():
    # Todorovic's illusion
    img = lum_white * np.ones([100, 200])
    img[:, 0:100] = lum_black
    img[29:70, 29:70] = lum_gray
    img[29:70, 129:170] = lum_gray

    img[14:45, 14:45] = lum_white
    img[14:45, 54:85] = lum_white
    img[54:85, 14:45] = lum_white
    img[54:85, 54:85] = lum_white

    img[14:45, 114:145] = lum_black
    img[14:45, 154:185] = lum_black
    img[54:85, 114:145] = lum_black
    img[54:85, 154:185] = lum_black
    
    return img

def get_contrast_contrast():
    # Contrast-contrast effect
    img = lum_gray * np.ones([100, 200])
    img[9:89, 9:89] = lum_black

    for i in range(9, 80, 20):
        for j in range(19, 80, 20):
            img[i : i + 10, j : j + 10] = lum_white
            img[j : j + 10, i : i + 10] = lum_white

    img[29:69, 29:69] = (lum_white + lum_gray) / 2.0
    for i in range(29, 60, 20):
        for j in range(29, 60, 20):
            img[i : i + 10, j : j + 10] = (lum_black + lum_gray) / 2.0
            k, l = i + 10, j + 10
            img[k : k + 10, l : l + 10] = (lum_black + lum_gray) / 2.0

    img[29:69, 129:169] = img[29:69, 29:69]
    
    return img

def get_checkerboard():
    # Checkerboard contrast
    img = lum_gray * np.ones([100, 100])
    img[9:89, 9:89] = lum_white

    for i in range(9, 80, 20):
        for j in range(9, 80, 20):
            img[i : i + 10, j : j + 10] = lum_black
            k, l = i + 10, j + 10
            img[k : k + 10, l : l + 10] = lum_black

    img[39:49, 29:39] = lum_gray
    img[59:69, 59:69] = lum_gray
    
    return img

def get_checkerboard_extended():
    # Extended version of checkerboard contrast
    img = lum_gray * np.ones([100, 100])
    img[9:89, 9:89] = lum_white

    for i in range(9, 80, 20):
        for j in range(9, 80, 20):
            img[i : i + 10, j : j + 10] = lum_black
            k, l = i + 10, j + 10
            img[k : k + 10, l : l + 10] = lum_black

    img[39:49, 19:49] = lum_gray
    img[59:69, 49:79] = lum_gray
    img[29:59, 29:39] = lum_gray
    img[49:79, 59:69] = lum_gray

    return img
