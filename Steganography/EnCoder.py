import cv2
import numpy
import sys

mat = cv2.imread('1.jpg')
h, w, l = mat.shape
closer = False 
    

if mat[7,7,1] == 7 and mat[8,8,2] == 8 and mat[6,6,3] == 6:
    print 'Already have some Encoded Message. . . !'
    print 'Want to Overwrite or not'
    x = bool(raw_input())
    if(x==False):
        closer = True

if closer == False :
    x = raw_input('Enter the Message : ')
    Ary = list(x)
    a , b , c = 8 , 9 , 7
    
    
    
