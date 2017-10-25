import cv2
img = cv2.imread('1.jpg')
cv2.imwrite('2.jpg',img,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 100])

