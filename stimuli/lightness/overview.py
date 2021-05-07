import matplotlib.pyplot as plt
import math

import lightness

shape=(15, 15)
ppd=5
contrast=0.5
frequency = 0.4

illusions = {
    "cornsweet": lightness.cornsweet(size=shape, ppd=ppd, contrast=contrast),
    #"todorovic": lightness.todorovic() -> TODO: parameters need to be added here
    "square_wave": lightness.square_wave(shape=shape, ppd=ppd, contrast=contrast, frequency=frequency),
    "whites_illusion_bmcc": lightness.whites_illusion_bmcc(shape=shape, ppd=ppd, contrast=contrast, frequency=frequency),
    #"contours_white_bmmc": lightness.contours_white_bmmc(shape=shape, ppd=ppd, contrast=contrast, frequency=frequency),
    "whites illusion gil": lightness.whites_illusion_gil(shape=shape, ppd=ppd, contrast=contrast, frequency=frequency),
    "disc and ring": lightness.disc_and_ring(shape=shape, radii=(2,3,4), values=(6,9,3))
}



M = len(illusions)
a = int(math.ceil(math.sqrt(M)))

plt.figure(figsize=(20, 20))


for i, (name, img) in enumerate(illusions.items()):
    plt.subplot(a, a, i+1)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.xticks([])
    plt.yticks([])
    plt.title(name, fontsize=25)
    plt.imshow(img)


plt.savefig("illusions_overview.png")
plt.show()