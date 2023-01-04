from pyfirmata import Arduino, SERVO, util
import speech_recognition as sr
from time import sleep

###########################
##### Controle da mão #####
###########################

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

###########################
###########################

###################################
##### Reconhecimento de Audio #####
###################################

rec=sr.Recognizer()
while True:
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Start")
        audio=rec.listen(mic)

        sound=rec.recognize_google(audio, language="pt-br")
        try:
            if sound== 'abre':
                print('Abre')
                open_hand()
            elif sound== 'fecha':
                print('Fecha')
                close_hand()
            else :
                print('...')
        except:
            print('..bug..')



