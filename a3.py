#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
import time

PIN_SW1_WHITE = 19
PIN_SW2_BLACK = 16
PIN_LED1_RED = 20
PIN_LED2_YELLOW = 21
PIN_BUZZER = 25

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    while True:
        sw1 = wp.digitalRead(PIN_SW1_WHITE)
        wp.digitalWrite(PIN_LED1_RED, ~sw1 & 1)
        print(sw1, end='')
