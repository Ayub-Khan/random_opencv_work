import cv2
x = cv2.imread('1.jpg')
cv2.imwrite('new1.jpg',x,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 100])
x = cv2.imread('3.jpg')
cv2.imwrite('new3.jpg',x,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 100])
x = cv2.imread('4.jpg')
cv2.imwrite('new4.jpg',x,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 100])
##for i in range(50,100,1):
##    y = str(i) + 'new2.jpg'
##    cv2.imwrite(y,x,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , i])
