import smbus
import time
import struct
# Setup I2C bus
bus = smbus.SMBus(1)

# I2C address of the Pico

while True:
    value1 = bus.read_byte(0x41)
    #value = struct.unpack('>H', bytes(value1))[0]
    print(value1)