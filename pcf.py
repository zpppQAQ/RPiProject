import smbus
import time

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
def pcf_main():
    try:
        while True:
            bus.write_byte(address, A0)
            value = bus.read_byte(address)
            print(value)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    