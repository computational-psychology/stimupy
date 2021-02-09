import numpy as np
from stimuli import contrast_metrics as cm

# %% testing gaussian-distribution
# size of image
s = (30, 30)

# creating a matrix with random values, Gausian-distributed with s.d. = sigma 
# the 'true' SD contrast is thus 0.1
arr = np.ones(s) + np.random.normal(loc=0, scale=0.1, size=s)

y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")

# the methods of computing the metric should give results close to the true
# value, and similar among each other
print(y.round(3), z.round(3))
assert(y==z)

# %% testing with known ground truths
arr = np.ones(s)
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
assert(y==0.0)
assert(z==0.0)


arr = np.vstack((np.ones(s), np.zeros(s)))
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
assert(y==0.5)
assert(z==0.5)

arr = np.vstack((np.ones(s), np.zeros(s)))
y = cm.RMS(arr, mode="complete")
z = cm.RMS(arr, mode="unique")
assert(y==1.0)
assert(z==1.0)

# %%
arr = np.random.randint(1, 10, (10, 10))

y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
print(y, z)

# %%
arr = np.random.randint(1, 10, (4, 4))
mask = np.array([
    [False, False, False, False],
    [False, True, True, False],
    [False, True, True, False],
    [False, False, False, False]
])

y = cm.SAM(arr, mask=mask, mode="complete")
z = cm.SAM(arr, mask=mask, mode="unique")
print(y, z)

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

