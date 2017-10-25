import cv2

cv2.namedWindow('Cam')

vc = cv2.VideoCapture(0)

video = cv2.VideoWriter('video.avi',-1,25,(640,480))

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow('Cam', frame)
    rval, frame = vc.read()
    key = cv2.waitKey(10)
    video.write(frame)
    if key == 27:
        break        
cv2.destroyAllWindows()
vc.release()
video.release()
