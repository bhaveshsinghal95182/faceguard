import numpy as np
import cv2
import random

img = cv2.imread('assetss\\4k_Futuristic_Sports_Car_Sunset_Scenery_Digital_Art_4K_Wallpaper.jpg')
img = cv2.resize(img, (400,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
corners = np.intp(corners)

for corner in corners:
    x, y = np.ravel(corner)
    cv2.circle(img, (x,y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, 3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('picture', img)
cv2.waitKey(0)
cv2.destroyAllWindows()