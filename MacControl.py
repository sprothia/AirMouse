import cv2
import numpy as np
import autopy
import mediapipe as mp
import HandTracking as htm
import macCommands as macCom
import time
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = htm.handDetector(True, maxHands=1, detectionCon=int(0.25))
wScr, hScr = autopy.screen.size()
frameReduction = 100
smooth = 7
pLocX,pLocY = 0,0
cLocX,cLocY = 0,0

joint_list_pointer = [8,7,4]
joint_list_middle = [12,11,15]
joint_list_thumb = [4,3,2]

def draw_finger_angle_pointer(results, joint_list_pointer):
    for hand in results.multi_hand_landmarks:

        a = np.array([hand.landmark[joint_list_pointer[0]].x, hand.landmark[joint_list_pointer[0]].y])
        b = np.array([hand.landmark[joint_list_pointer[1]].x, hand.landmark[joint_list_pointer[1]].y])
        c = np.array([hand.landmark[joint_list_pointer[2]].x, hand.landmark[joint_list_pointer[2]].y])
        
        radians = np.arctan2(c[1]-b[1], c[0] - b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle > 180.0:
            angle = 360-angle 
            
        if angle < 116.0:
            print("volume up")
            macCom.increment_volume()
            time.sleep(0.5)
                

def draw_finger_angle_middle(results, joint_list_middle):

    for hand in results.multi_hand_landmarks:  
             
        a = np.array([hand.landmark[joint_list_middle[0]].x, hand.landmark[joint_list_middle[0]].y])
        b = np.array([hand.landmark[joint_list_middle[1]].x, hand.landmark[joint_list_middle[1]].y])
        c = np.array([hand.landmark[joint_list_middle[2]].x, hand.landmark[joint_list_middle[2]].y])

        radians = np.arctan2(c[1]-b[1], c[0] - b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle > 180.0:
            angle = 360-angle 
            
        if angle > 130.0:
            print("Volume Down")
            macCom.decrement_volume()
            time.sleep(0.5)

while True:

    success, image = cap.read()
    image = detector.findHands(image)
    lmList, bbox = detector.findPosition(image)
    
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]

        fingers = detector.fingersUp()
        
        #Volume
        if detector.results.multi_hand_landmarks:
            if fingers[0] == 1 and fingers[3] == 1 and fingers[4] == 1:                             
                draw_finger_angle_pointer(detector.results, joint_list_pointer)
                draw_finger_angle_middle(detector.results, joint_list_middle)
                 
        cv2.rectangle(image, (frameReduction, frameReduction), (wCam-frameReduction, hCam-frameReduction), (255,0,255), 2)

        #Mouse
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            x3 = np.interp(x1, (frameReduction,wCam-frameReduction), (0,wScr)) 
            y3 = np.interp(y1, (frameReduction,hCam-frameReduction), (0,hScr)) 
            
            cLocX = pLocX + (x3-pLocX) / smooth
            cLocY = pLocY + (y3-pLocY) / smooth

            autopy.mouse.move(wScr - cLocX, cLocY)
            cv2.circle(image, (x1,y1), 3, (255,0,255), cv2.FILLED)
            pLocX, pLocY = cLocX, cLocY
            
            
    
        #Click
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(4,12,image)
            autopy.mouse.click()
            time.sleep(0.2)
            
        #Scroll
        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            pyautogui.scroll(-1)
        elif fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            pyautogui.scroll(1)
        
        #Custom Command #2
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            print("Choose command")

    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
    
