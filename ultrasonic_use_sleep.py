import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO Pins
GPIO_TRIGGER = 21
GPIO_ECHO = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    
    GPIO.output(GPIO_TRIGGER, 0)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, 1)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, 0)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def gpio_clean():

    GPIO.output(GPIO_TRIGGER, 0)
    

    return None



if __name__ == '__main__':
    try:
        while True:
            distance()
            #print ("Measured Distance = %.1f cm" % dist)
            #time.sleep(0.1)
            
 
    
    # Reset by pressing CTRL + C
    except:
        print("Measurement stopped by User")
        gpio_clean()
        GPIO.cleanup()