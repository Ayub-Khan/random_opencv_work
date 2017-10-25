import cv2

image = cv2.imread('k.jpg',cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.namedWindow('Pic',cv2.cv.CV_WINDOW_NORMAL)
cv2.imshow('Pic', image)
cv2.waitKey()
