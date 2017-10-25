import numpy
import cv2
import cv2.cv as cv

for n in range(2,25):
    tmp = cv2.imread(str(n)+'.jpg')
    img = cv2.imread(str(n-1)+'.jpg')
    h , w , l = img.shape    
    co = 0
    tmp2 = cv2.imread(str(n)+'.jpg')
    for i in range(h):
        for j in range(w):
            if(tmp[i,j,0]==img[i,j,0] and tmp[i,j,1]==img[i,j,1] and tmp[i,j,2]==img[i,j,2]):
               co = co +1
               tmp2[i,j,0]=255
               tmp2[i,j,1]=255
               tmp2[i,j,2]=255
    print co
    cv2.imwrite('new' + str(n)+'.jpg',tmp2)
    
print 'Total : ' + str(h*w)

