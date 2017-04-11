import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
ONE=11
TWO=13
PWM=12
GPIO.setup(ONE,GPIO.OUT)
GPIO.setup(TWO,GPIO.OUT)
GPIO.setup(PWM,GPIO.OUT)
print "Motor A Direction one"
GPIO.output(ONE, GPIO.HIGH)

time.sleep(2)

GPIO.output(TWO, GPIO.LOW)

print "Motor A Direction two"
GPIO.output(TWO, GPIO.HIGH)

time.sleep(2)

GPIO.output(ONE, GPIO.LOW)

# This command clears the configuration from the GPIO interface
GPIO.cleanup()
