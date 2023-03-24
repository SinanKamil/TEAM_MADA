import serial
import RPi.GPIO as GPIO
import smbus
bus = smbus.SMBus(1)

def validate_data(serial_obj):
    while True:
        try:
            data = serial_obj.readline(4)
            data_float = float(data)
            if 0.00 <= data_float <= 2.00:
                data_float = "{:.2f}".format(data_float)
                return data_float
        except ValueError:
            pass

def i2c_validate_data():
    try:
        aileron_num = bus.read_byte(0x41)
        aileron_num_int = int(aileron_num)
        if 0 <= aileron_num_int <= 200:
            return aileron_num_int
    except ValueError:
        pass
    except OSError:
        pass

ser = serial.Serial("/dev/ttyS0", 115200)

while True:
    steering = validate_data(ser)
    aileron = i2c_validate_data()
    if aileron is not None:
        print("Steering: ", steering, "Aileron: ", aileron)

ser.close()