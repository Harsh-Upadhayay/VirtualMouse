import cv2
import numpy as np
import time
import HandTrackingModule
import pyautogui as pt


cap =  cv2.VideoCapture(0, cv2.CAP_DSHOW)
wCam = 640
hCam = 480
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = HandTrackingModule.handDetector(maxHands=1)
wScr , hScr = pt.size()


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    x1,y1,x2,y2,x3,y3 = 0,0,0,0,0,0
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    fingers = detector.fingersUp()
    print(fingers)

    # if fingers[1] and fingers[2]:
    #     x3 = np.interp(x1, (0, wCam), (0, wScr))
    #     y3 = np.interp(y1, (0, hCam), (0, hScr))
    #     pt.moveTo(x3, y3)

    #print(x1, y1, x2, y2)
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
