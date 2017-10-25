import cv2
import time

vc = cv2.VideoCapture('OP.mp4')
c=1

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    cv2.imwrite(str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
