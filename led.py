import RPi.GPIO as GPIO
import time


def led_main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.OUT)
    led = GPIO.PWM(12,60)
    led.start(50)
    time.sleep(2) 
    try:
        while True:
            led.ChangeDutyCycle(20)
            time.sleep(2)
            led.ChangeDutyCycle(80)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    led.stop()
    led.ChangeDutyCycle(0)
    GPIO.cleanup()
    print("LED done")
def led_flash():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.OUT)
    led = GPIO.PWM(12,60)
    j = 0
    try:
        while j < 5:
            led.ChangeDutyCycle(90)
            time.sleep(0.5)
            led.ChangeDutyCycle(20)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

        
        
