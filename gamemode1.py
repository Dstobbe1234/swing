import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import random

pic = []
noise = PerlinNoise(octaves=2, seed=1)
xpix, ypix = 500, 500
for i in range(ypix):
    pic.append([])
    for j in range(xpix):
        initNoise = noise([i/xpix, j/ypix])
        if (initNoise <= -0.1):
            pic[-1].append(-1)
        else:
            pic[-1].append(1)

plt.imshow(pic, cmap='gray')
plt.show()
