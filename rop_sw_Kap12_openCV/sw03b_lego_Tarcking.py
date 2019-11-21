#code fuer das Tracken eines gruenen Duplo-steins
# Gruppe JS
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

greenLower = (57, 93, 61)  
greenUpper = (102, 255, 255)

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        #((x, y), radius) = cv2.minEnclosingCircle(c)
        x,y,w,h = cv2.boundingRect(c)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect) # weitere Ausgaben moeglich (z.B. winkel): https://docs.opencv.org/3.4/db/dd6/classcv_1_1RotatedRect.html#a69d648b086f26dbce0029facae9bfb2d
        box = np.int0(box)
        

        if w > 10:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.drawContours(frame,[box],0,(0,0,255),2)
            cv2.circle(frame, (int(x+0.5*w), int(y+0.5*h)), int(5), (255, 0, 0), 2)
        #if radius > 10:
            #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

	print(x+0.5*w,y+0.5*h)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
