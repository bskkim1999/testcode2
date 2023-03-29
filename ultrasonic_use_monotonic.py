import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 15
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, 1)
    
    start_time = time.monotonic()  #시작시간측정
    # set Trigger after 0.01ms to LOW
    
    while True:
        current_time = time.monotonic()
        if current_time - start_time >= 0.00001:
            start_time=current_time
            break
    

    GPIO.output(GPIO_TRIGGER, 0)
 
    StartTime = time.monotonic()
    StopTime = time.monotonic()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.monotonic()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.monotonic()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            
            while True:
                current_time = time.monotonic()
                if current_time - start_time >= 0.1:
                    start_time=current_time
                    break
 
    
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()