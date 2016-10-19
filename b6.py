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

import NetworkManager
c = NetworkManager.const

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    lcd = LCD(I2C_ADDR_LCD)    
    while True:
        sw1 = wp.digitalRead(PIN_SW1_WHITE)
        sw2 = wp.digitalRead(PIN_SW2_BLACK)
        if sw1 == 0:
            lcd.clear()
            wp.delay(250)
            lcd.set_cursor(0, 0)
            lcd.print("state:")
            state = "{0}".format(c('state', NetworkManager.NetworkManager.State))
            lcd.set_cursor(0, 1)
            lcd.print(state)
        wp.delay(500)
