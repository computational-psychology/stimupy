from stimuli.transparency import TextureFactory
import matplotlib.pyplot as plt
from stimuli import contrast_measures
from stimuli import lightness

# %%
f = TextureFactory('random', 10)
i = f.get_image(0, 1)
plt.figure()
plt.imshow(i)
plt.show()

# %%
rms = contrast_measures.RMS(i)
print(rms)

# %% doesn't work yet
c = lightness.cornsweet((5, 5), 10, .5)
plt.figure()
plt.imshow(c)
plt.show()

