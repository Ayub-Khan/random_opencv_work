import cv2
import time

cv2.namedWindow('Vid')

vc = cv2.VideoCapture('32.3gp')
o=0
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while rval:
    time.sleep(0.04)
    cv2.imshow('Vid', frame)
    rval, frame = vc.read()
    if(o<5):
        cv2.imwrite(str(o) + '25.jpg',frame)
        o= o+1
    key = cv2.waitKey(1)
    if key == 27:
        break        
cv2.destroyAllWindows()
vc.release()
