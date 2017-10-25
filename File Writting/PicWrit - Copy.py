import cv2
img = cv2.imread('1.jpg')
hei , wid , lyr = img.shape
for i in range(0,hei,2):
    for j in range(0,wid,2):
        img[i,j] = [0,0,0]
cv2.imwrite('2.jpg',img)
