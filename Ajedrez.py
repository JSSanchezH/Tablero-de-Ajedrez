import cv2
import numpy as np
import matplotlib.pyplot as plt

dimX = 8
dimY = 8

img = np.zeros((dimY, dimX, 3), np.uint8)

for x in range(0, dimX):
    for y in range(0, dimY):
        if (x+y) % 2 == 0:
            img[y, x] = (255, 255, 255)
        else:
            img[y, x] = (0, 0, 0)


plt.imshow(img)  # mostramos nuestra imagen
plt.show()
