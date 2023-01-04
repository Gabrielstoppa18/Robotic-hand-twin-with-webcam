from pyfirmata import Arduino, SERVO, util
from time import sleep
from cvzone.HandTrackingModule import HandDetector
import cv2

################################
######Controle Mão Arduino######
################################
port= 'COM4'
pin1 = 2
pin2 = 3
pin3 = 4
pin4 = 5
pin5 = 6

board= Arduino(port)

dedo1=board.digital[pin1]
dedo2=board.digital[pin2]
dedo3=board.digital[pin3]
dedo4=board.digital[pin4]
dedo5=board.digital[pin5]

dedo1.mode=SERVO
dedo2.mode=SERVO
dedo3.mode=SERVO
dedo4.mode=SERVO
dedo5.mode=SERVO
#################################
######## Controle video #########

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)
state=[1,1,1,1,1]

def open_hand():
    dedo1.write(0)
    dedo2.write(0)
    dedo3.write(0)
    dedo4.write(0)
    dedo5.write(0)

def close_hand():
    dedo1.write(110)
    dedo2.write(110)
    dedo3.write(110)
    dedo4.write(110)
    dedo5.write(110)

################################


while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw

    if hands:
        # Hand 1
        hand = hands[0]
        #lmList = hand["lmList"]  # List of 21 Landmark points
        state=detector.fingersUp(hand)
        if state[0]==1:
            dedo4.write(0)
        else:
            dedo4.write(110)

        if state[1]==1:
            dedo5.write(0)
        else:
            dedo5.write(110)

        if state[2]==1:
            dedo3.write(0)
        else:
            dedo3.write(110)

        if state[3]==1:
            dedo2.write(0)
        else:
            dedo2.write(110)

        if state[4]==1:
            dedo1.write(0)
        else:
            dedo1.write(110)
        '''if state == [1,1,1,1,1]:
            open_hand()
        
        elif state == [0,0,0,0,0]:
            close_hand()'''
            
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(5) & 0xFF == 27:
        break