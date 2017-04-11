import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
##GPIO.setup(12,GPIO.OUT)
####GPIO.setup(13,GPIO.OUT)
##GPIO.output(12, True)
p=GPIO.PWM(11,200)
p.start(2)
try:
##    while True:
    GPIO.output(11,True)
##        time.sleep(1)
##        GPIO.cleanup()
##    GPIO.output(11, False)

except KeyboardInterrupt:
    pass

time.sleep(5)
p.stop()
GPIO.cleanup() 
          
