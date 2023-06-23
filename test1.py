import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pin = 21
pin2 = 12

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

while True:
    try:
        GPIO.output(pin,0)
        time.sleep(0.1)
        GPIO.output(pin,1)
        time.sleep(0.1)

        GPIO.output(pin2,0)

    except:
        print("finish!!")
        GPIO.output(pin, 0)
        GPIO.cleanup()
        
        exit(1)