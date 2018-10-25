import cv2
import time
import numpy as np
from gpiozero import LED

rightSignal = LED(2)
leftSignal = LED(3)

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    width = frame.shape[1]

    img = cv2.medianBlur(frame,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(cimg,cv2.cv.CV_HOUGH_GRADIENT,2,50,param1=70,param2=50,minRadius=0,maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
	x = 0
	maxSize = 0
        for i in circles[0,:]:
		if x < 2:
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
                x += 1
                if i[2] > maxSize:
                    maxSize = i[2]
                    largestPosX = i[0]
                else:
	            x = 0
		    break
				
        middleLine = width/2

        if largestPosX < middleLine:
            #Largest Circle at Left side
            leftSignal.on()
        else:
            leftSignal.off()

        if largestPosX > middleLine:
            #Largest Circle at Right side
            rightSignal.on()
        else:
            rightSignal.off()
    else:
        rightSignal.off()
	leftSignal.off()
		
    cv2.imshow('detected circles',cimg)
    time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()