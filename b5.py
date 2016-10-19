#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
PIN_SW1_WHITE = 19
PIN_SW2_BLACK = 16
PIN_LED1_RED = 20
PIN_LED2_YELLOW = 21
PIN_BUZZER = 25

from adt7410 import ADT7410 as THERMO
I2C_ADDR_THERMO = 0x48

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    thermo = THERMO(I2C_ADDR_THERMO)
    t1 = 32.0   # 閾値1
    print("threshold t1:{0:6.2f}".format(t1))
    while True:
        sw1 = wp.digitalRead(PIN_SW1_WHITE)
        sw2 = wp.digitalRead(PIN_SW2_BLACK)
        temp = thermo.read_temp() / 128.0
        print("{0:6.2f}".format(temp))
        if temp > t1:
            print("over t1")
            wp.digitalWrite(PIN_BUZZER, 1)
        else:
            wp.digitalWrite(PIN_BUZZER, 0)
        wp.delay(500)
