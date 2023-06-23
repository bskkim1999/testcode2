import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pin = 21

GPIO.setup(pin, GPIO.OUT)


while True:
    GPIO.output(pin,0)
    time.sleep(0.1)
    GPIO.output(pin,1)
    time.sleep(0.1)