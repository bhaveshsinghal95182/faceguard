import cv2

img = cv2.imread('assetss\\4k_Futuristic_Sports_Car_Sunset_Scenery_Digital_Art_4K_Wallpaper.jpg', 1)
img = cv2.resize(img, (0,0), fy=0.5, fx=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()