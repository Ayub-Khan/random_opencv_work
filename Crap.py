import cv2
x = cv2.imread('Dog6.jpg')
cv2.imwrite('new2.jpg',x,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 70])