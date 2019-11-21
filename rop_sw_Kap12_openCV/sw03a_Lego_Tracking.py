###
# source: https://github.com/jonathanfoster/ball-tracking.git
# ROP WS2019
# 
# Erkennt gruene Rechtecke und zeichnet ein umschliessendes Rechteck und einen Ausrichtungspfeil
# Mittelpunkt und Winkel in Rad werden ausgegeben 
# Gruppe GH


from collections import deque
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

greenLower = (70, 34, 63)
greenUpper = (110, 255, 255)

if not args.get("video", False):
    camera = cv2.VideoCapture(0) #Index der Kamera 0..2 worx
else:
    camera = cv2.VideoCapture(args["video"])

ax = 0
ay = 0

while True:

    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    # Speichern des Bildes
    cv2.imwrite('bild.jpg', frame)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)

        # Erstellen umschiessendes Rechteck
        rect = cv2.minAreaRect(c)

        # Erstellen einer Punktwolke aus dem Rechteck und umwandeln der Liste in intp
        box = cv2.boxPoints(rect)   
        box = np.intp(box)          
        
        # Ermitteln des Mittelpunktes in x,y
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 10:
            ax = int(x)    
            ay = int(y)

            #Lesen des Winkels aus dem Rechteck, umwandeln in Rad
            phi = rect[2]*np.pi/180 
            
            # Erstellen der Zielpunkte des Pfeils
            x2 = int(ax + 100 * np.cos(phi))    
            y2 = int(ay + 100 * np.sin(phi))

            # Text, Rechteck und Richtungspfeil ins Bild einfuegen
            cv2.putText(frame, "Koordinate x:" + str(ax) + " y:" + str(ay) , (10,30), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
            cv2.putText(frame, "Rotation: " + str(phi) , (10,60), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))
            frame = cv2.drawContours(frame, [box], 0, (0,255,0), 2)
            frame = cv2.arrowedLine(frame, (ax,ay),(x2,y2),(255,255,255))

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(10) & 0xFF

    if key == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
