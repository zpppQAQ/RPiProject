import smbus
import time
import RPi.GPIO as GPIO
import time
import datetime
import ds as ds

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
def project_pfc():
    while True:
        bus.write_byte(address, A0)
        value = bus.read_byte(address)
        print("The voltage through the device is:")
        print((float(3.3)/float(255))*value)
        ds.ds_main2()
        
        GPIO.cleanup()
        