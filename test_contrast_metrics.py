from src import contrast_metrics as cm
import numpy as np

# %%
arr = np.random.randint(1, 10, (10, 10))

x = cm.SAM(arr, mode="chunk", chunk_size=2)
y = cm.SAM(arr, mode="complete")
z = cm.SAM(arr, mode="unique")
print(x, y, z)

# %%
arr = np.random.randint(1, 10, (4, 4))
mask = np.array([
    [False, False, False, False],
    [False, True, True, False],
    [False, True, True, False],
    [False, False, False, False]
])

x = cm.SAM(arr, mask=mask, mode="chunk", chunk_size=2)
print(x)

# %%
arr = np.random.randint(2, 10, (10, 10))
print(cm.SAM(arr))
print(cm.SAMLG(arr))
print(cm.SDMC(arr))
print(cm.SAW(arr))
print(cm.SAWLG(arr))
print(cm.RMS(arr))
print(cm.SD(arr))
print(cm.SDLG(arr))

