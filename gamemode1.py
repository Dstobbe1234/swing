import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import random
import math

pic = []
noise = PerlinNoise(octaves=2, seed=1)
# offsetX = random.randint(0, 1000)
# offsetY = random.randint(0, 1000)
xpix, ypix = 500, 500
# - max((abs(i * 2 - xpix)/xpix), (abs(i * 2 - ypix)/ypix))
pic = [[noise([i/xpix, j/ypix]) - max((abs(j * 2 - xpix)/xpix), (abs(i * 2 - ypix)/ypix)) for j in range(xpix)] for i in range(ypix)] 

plt.imshow(pic, cmap='gray')
plt.show()

