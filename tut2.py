import cv2
import random

img = cv2.imread('assetss\\4k_Futuristic_Sports_Car_Sunset_Scenery_Digital_Art_4K_Wallpaper.jpg', 1)

img_column = range(img.shape[1])
for i in range(100):
    for j in img_column:
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

car = img[400:2000, 1000:3000]

car = cv2.resize(car, (400,400))

cv2.imshow('Image', car)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()