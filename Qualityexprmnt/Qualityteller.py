import cv2
import os

file_org = raw_input('Enter the Image URl : ')
img = cv2.imread(file_org)
siz = os.stat(file_org).st_size
file_tmp = 'Tmp' + file_org
cv2.imwrite(file_tmp,img,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , 0])
chkr = os.stat(file_tmp).st_size
dif = siz - chkr
for i in range(5,100):
    cv2.imwrite(file_tmp,img,[cv2.cv.CV_IMWRITE_JPEG_QUALITY , i])
    chkr = os.stat(file_tmp).st_size
    if abs(siz-chkr)<dif:
        dif = siz-chkr
    else:
        print i-1
        break
os.remove(file_tmp)
