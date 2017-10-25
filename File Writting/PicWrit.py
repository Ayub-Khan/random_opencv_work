import cv2
img = cv2.imread('1.jpg')
fi = open('pic.nv','w')
hei , wid , lyr = img.shape
fi.write ( str(hei) + ' ' + str(wid) + ' ' + str(lyr) + '\n') 

for i in range(0,hei,1):
    for j in range(0,wid,1):
        fi.write ( str(chr(img[i,j,0])) + str(chr(img[i,j,1])) + str(chr(img[i,j,2])) + " " )

fi.close
