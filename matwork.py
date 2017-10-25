import cv2

image = cv2.imread('k.jpg')
h , w, l= image.shape

if image[0,0,1] == image[0,0,1] :
    print image[0,0,1]
    print image[0,0]
