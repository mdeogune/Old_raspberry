import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led=11
GPIO.setup(led,GPIO.OUT)
bno=int(input("how many time blink?"))
while True:
    GPIO.output(led,True)
    time.sleep(1)
    GPIO.output(led,False)
    time.sleep(1)
GPIO.cleanup()
    
