import RPi.GPIO as GPIO
import servo_sensor as servo_sensor
import led as led
import ds as ds
import pcf as pcf
import i_project as i_project
GPIO.setmode(GPIO.BCM)
num = "0"

try:
    while True:
        print("1.distance sensor")
        print("2.servo sensor")
        print("3.led")
        print("4.PCF8591 AD/DA module")
        print("5.Social Distance Check(total))")
        num = raw_input("ENTER A NUMBER according to the list above(or quit): ")
        if num == "quit":
            num = "0"
            GPIO.setmode(GPIO.BCM)
            GPIO.cleanup()
            break
        if int(num) == 1:
            ds.ds_main()
        elif int(num) == 2:
            servo_sensor.servo_main() 
        elif int(num) == 3:
            led.led_main()
        elif int(num) == 4:
            pcf.pcf_main
        elif int(num) == 5:
            i_project.project_pfc()
        else:
            num = "0"
            GPIO.setmode(GPIO.BCM)
            GPIO.cleanup()
            break

finally:
    GPIO.cleanup()
    