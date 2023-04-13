import machine
import os
from machine import Pin, ADC
import utime



led_pin = machine.Pin(25, machine.Pin.OUT)


uart = machine.UART(0, baudrate=115200, bits=8, parity=None, stop=1, tx=machine.Pin(12), rx=machine.Pin(13))



POT_Value_steer = ADC(26)
POT_Value_retract = ADC(27)
POT_Value_aileron = ADC(28)
convert_factor = 2/(65536)#for voltage convertion


while True:
    led_pin.value(1)
    
    out_aileron = POT_Value_aileron.read_u16() * convert_factor
    out_round_aileron = "{:,.4f}".format(out_aileron)  
    
    out_steer = POT_Value_steer.read_u16() * convert_factor
    out_round_steer = "{:,.2f}".format(out_steer)
    
    out_retract = POT_Value_retract.read_u16() * convert_factor
    out_round_retract = "{:,.2f}".format(out_retract)

    space = " "
    out_ster_retr = str(out_round_steer) + space + str(out_round_retract) + space + str(out_round_aileron)
    uart.write(out_ster_retr)
    
        
    
    
    
    
    print("Steering:", str(out_round_steer), " ", "Retract:",  str(out_round_retract), "Aileron:", out_round_aileron)
    utime.sleep(0.1)