import RPi.GPIO as GPIO
import time
import datetime
import led as led
import servo_sensor as servo_sensor
SPEED_OF_SOUND=330/float(1000000)

def getDistance(td):
    global SPEED_OF_SOUND
    distance=SPEED_OF_SOUND*td/float(2)
    return distance
def ds_main():
    try:
        while True:
            TRIGGER_PIN = 23
            ECHO_PIN = 22
            HIGH_TIME=0.1
            LOW_TIME=1-HIGH_TIME
        
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            while True:
                GPIO.output(TRIGGER_PIN,GPIO.HIGH)
            #    print 'Trigger HIGH'
                time.sleep(HIGH_TIME)
                GPIO.output(TRIGGER_PIN,GPIO.LOW)
            #    print 'Trigger LOW'
            
            
            
                while GPIO.input(ECHO_PIN)==False:
            # pulse is LOW
                    pass
            
            
                starttime = datetime.datetime.now().microsecond
                while GPIO.input(ECHO_PIN)==True:
            # pulse is HIGH
                    pass
            
            # pulse is LOW
                endtime = datetime.datetime.now().microsecond
                travel_time=endtime - starttime
                print getDistance(travel_time)
                time.sleep(LOW_TIME)
    except KeyboardInterrupt:
        pass
def ds_main2():
    try:
        while True:
            TRIGGER_PIN = 23
            ECHO_PIN = 22
            HIGH_TIME=0.1
            LOW_TIME=1-HIGH_TIME
        
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            GPIO.setup(TRIGGER_PIN,GPIO.OUT)
            GPIO.setup(ECHO_PIN,GPIO.IN)
            while True:
                GPIO.output(TRIGGER_PIN,GPIO.HIGH)
            #    print 'Trigger HIGH'
                time.sleep(HIGH_TIME)
                GPIO.output(TRIGGER_PIN,GPIO.LOW)
            #    print 'Trigger LOW'
  
                while GPIO.input(ECHO_PIN)==False:
            # pulse is LOW
                    pass
            
            
                starttime = datetime.datetime.now().microsecond
                while GPIO.input(ECHO_PIN)==True:
            # pulse is HIGH
                    pass
            
            # pulse is LOW
                endtime = datetime.datetime.now().microsecond
                travel_time=endtime - starttime
                mperd = 4 / float(180)
                print("The distance between these two people is: ")
                d = getDistance(travel_time)
                print(d)
                deg = d * mperd
                if(d > 2):
                    servo_sensor.rotate(deg)
                    print("safety distance")
                else:
                    servo_sensor.rotate(deg)
                    print("SOCIAL DISTANCE!!")
                    led.led_flash()
                break

    except KeyboardInterrupt:
        pass
