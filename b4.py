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

from adt7410 import ADT7410 as THERMO
I2C_ADDR_THERMO = 0x48

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    lcd = LCD(I2C_ADDR_LCD)    
    thermo = THERMO(I2C_ADDR_THERMO)
    while True:
        sw1 = wp.digitalRead(PIN_SW1_WHITE)
        sw2 = wp.digitalRead(PIN_SW2_BLACK)
        if sw2 == 0:
            temp = thermo.read_temp() / 128.0
            lcd.clear()
            wp.delay(250)
            lcd.set_cursor(0, 0)
            lcd.print("{0:6.2f}".format(temp))
        wp.delay(250)
