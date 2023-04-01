import serial
import RPi.GPIO as GPIO
import smbus
bus = smbus.SMBus(1)

def retract_validate_data(serial_obj):
        try:
            data = serial_obj.readline(9).decode('utf-8')
            data_str = str(data)
            split_float = data_str.split(" ")
            data_float_retract = float(split_float[1])
            if 0 <= data_float_retract <= 2.00:
                data_float_retract = "{:.2f}".format(data_float_retract)
            return float(data_float_retract)
        except ValueError:
            pass
def steering_validate_data(serial_obj):
        try:
            data = serial_obj.readline(9).decode('utf-8')
            data_str = str(data)
            split_float = data_str.split(" ")
            data_float_steering = float(split_float[0])
            if 0 <= data_float_steering <= 2.00:
                data_float_steering = "{:.2f}".format(data_float_steering)
            return float(data_float_steering)
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
    steering = steering_validate_data(ser)
    retract = retract_validate_data(ser)
    aileron = i2c_validate_data()
    #if aileron is not None:
    print("Steering: ", steering, "Retract: ", retract ,"Aileron: ", aileron)

ser.close()