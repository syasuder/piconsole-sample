#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
PIN_SW1_WHITE = 19
PIN_SW2_BLACK = 16
PIN_LED1_RED = 20
PIN_LED2_YELLOW = 21
PIN_BUZZER = 25

from st7032i import St7032iLCD as LCD
I2C_ADDR_LCD = 0x3e

import os
from datetime import timedelta, datetime

class DamnCamera:
    """
    damn camera class
    """
    def __init__(self):
        self.lcd = LCD(I2C_ADDR_LCD)
        self.lcd.clear()
        self.sw1_old = 1
        self.sw2_old = 1

    def beep(self, duration = 100):
        wp.digitalWrite(PIN_BUZZER, 1)
        wp.delay(duration)
        wp.digitalWrite(PIN_BUZZER, 0)        

    def proc_inputs(self):
        sw1 =  wp.digitalRead(PIN_SW1_WHITE)
        if sw1 == 0 and self.sw1_old == 1:
            sw1_pushed = True
        else:
            sw1_pushed = False
        self.sw1_old = sw1
        sw2 =  wp.digitalRead(PIN_SW2_BLACK)
        if sw2 == 0 and self.sw2_old == 1:
            sw2_pushed = True
        else:
            sw2_pushed = False
        self.sw2_old = sw2
        return (sw1_pushed, sw2_pushed)
    
    def run(self):
        while True:
            (sw1, sw2) = self.proc_inputs()
            if sw1:
                return False
            if sw2:
                self.lcd.clear()
                self.lcd.set_cursor(0, 0)
                self.lcd.print("<capturing...>")
                self.beep()
                fn = datetime.now().strftime('%m%d_%H%M%S.jpg')
                os.system("raspistill -o {0}".format(fn))
                self.lcd.clear()
                self.lcd.set_cursor(0, 0)
                self.lcd.print("{0}".format(fn))
                self.beep(200)
            wp.delay(250)            

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    wp.digitalWrite(PIN_BUZZER, 0)

    cam = DamnCamera()
    cam.run()
    
