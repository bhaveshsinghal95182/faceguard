import cv2
import numpy as np

img = cv2.resize(cv2.imread('assetss\\4k_Futuristic_Sports_Car_Sunset_Scenery_Digital_Art_4K_Wallpaper.jpg', 0), (0,0), fx=0.2, fy=0.2)
template = cv2.resize(cv2.imread('assetss\\template.jpg', 0), (0,0), fx=0.2, fy=0.2)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method=method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()