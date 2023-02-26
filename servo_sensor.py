import RPi.GPIO as GPIO
import time




def servo_main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    p = GPIO.PWM(27,50)
    p.start(0)
    try:
        while True:
            angle = float(input("Enter angle between 0 to 180: "))
            p.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            p.ChangeDutyCycle(0)
    except KeyboardInterrupt:
        pass
def rotate(deg):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    p = GPIO.PWM(27,50)
    p.start(0)
    p.ChangeDutyCycle(2+(deg/18))
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    pass