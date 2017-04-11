


import time
import RPi.GPIO as GPIO
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,True)
while True:
    in_=input("way")

    if (in_=='1'):
        GPIO.output(11,True)
        GPIO.output(12,False)

    if (in_=='2'):
        GPIO.output(12,True)
        GPIO.output(11,False)



GPIO.cleanup()
