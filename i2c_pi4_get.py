import smbus
import time

# Setup I2C bus
bus = smbus.SMBus(1)

# I2C address of the Pico

while True:
    bus.write_byte(0x41, 3)