import cv2
img = cv2.imread('url.jpg')
h , w , l = img.shape
for i in range(0,h/20,1):
    for j in range(0,w/20,1):
        img[i,j]=[0 , 0 , 0]
cv2.imwrite('url.jpg',img)
