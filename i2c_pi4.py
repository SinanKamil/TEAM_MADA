import smbus
import struct

bus = smbus.SMBus(1)

pico_address = 0x60

value = 2.122
packed_value = struct.pack('f', value)

bus.write_i2c_block_data(pico_address, 0x00, list(packed_value))