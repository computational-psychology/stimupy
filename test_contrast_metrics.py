from src import contrast_metrics as cm
import numpy as np

# %% testing chunking
# size of image
s = (30, 30)

# creating a matrix with random values, Gausian-distributed with s.d. = sigma 
# the 'true' SD contrast is thus 0.1
arr = np.ones(s) + np.random.normal(loc=0, scale=0.1, size=s)

x = cm.SD(arr, mode="chunk", chunk_size=2)
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")

# the three methods of computing the metric should give results close to the true
# value, and similar among each other
print(x.round(3), y.round(3), z.round(3))
assert(x==y)
assert(y==z)
# TODO: not the case for when chunk_size > 1

# %% testing with known ground truths
# TODO: maybe it would be a good idea to do some unittesting here with known ground truths
arr = np.ones(s)
x = cm.SD(arr, mode="chunk", chunk_size=5)
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
assert(x==0.0)
assert(y==0.0)
assert(z==0.0)


arr = np.vstack((np.ones(s), np.zeros(s)))
x = cm.SD(arr, mode="chunk", chunk_size=5)
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
assert(x==0.5)
assert(y==0.5)
assert(z==0.5)

# TODO: RMS is not returning correct value
arr = np.vstack((np.ones(s), np.zeros(s)))
x = cm.RMS(arr, mode="chunk", chunk_size=1)
y = cm.RMS(arr, mode="complete")
z = cm.RMS(arr, mode="unique")
assert(x==1.0)
assert(y==1.0)
assert(z==1.0)

print(cm.SD(arr)/arr.mean())


# %%
arr = np.random.randint(1, 10, (10, 10))

x = cm.SD(arr, mode="chunk", chunk_size=2)
y = cm.SD(arr, mode="complete")
z = cm.SD(arr, mode="unique")
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

