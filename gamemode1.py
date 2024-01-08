import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import random

pic = []
noise = PerlinNoise(octaves=2, seed=1)
offsetX = random.randint(0, 1000)
offsetY = random.randint(0, 1000)
xpix, ypix = 500, 500
for i in range(offsetY, ypix + offsetY):
    pic.append([])
    for j in range(offsetX, xpix + offsetX):
        initNoise = noise([i/xpix, j/ypix])
        if (initNoise <= -0.07):
            pic[-1].append(-1)
        else:
            pic[-1].append(1)

plt.imshow(pic, cmap='gray')
plt.show()
