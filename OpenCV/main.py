import cv2 as cv
import numpy as np

img = cv.imread("houses.jpg")
cv.imshow("houses", img)

key = cv.waitKey(0)
if key == ord("g"):
    img = cv.rectangle(img, (100,100), (200, 000), (0,255,0), 3)
    cv.imwrite("write.jpg", img)
elif key == ord("h"):
    
else:
    pass

cv.destroyAllWindows()


