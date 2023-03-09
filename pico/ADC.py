from machine import Pin, ADC
import utime

POT_Value = ADC(26)
convert_factor = 12/ (65536)#for voltage convertion
while True:
    print(POT_Value.read_u16() * convert_factor,"volts")
    utime.sleep(0.1)