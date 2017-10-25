import cv2

val1 = 50
val2 = 0
cv2.namedWindow("main1",cv2.cv.CV_WINDOW_NORMAL)
cv2.createTrackbar("Track:1","main1",val1,255,None)
nb1 = "Button 1"
nb2 = "Button 2"
cv2.createButton(nb1,callbackButton,nb1,cv2.cv.CV_CHECKBOX,1)
