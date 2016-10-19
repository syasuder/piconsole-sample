#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
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
        sw2 = wp.digitalRead(PIN_SW2_BLACK)
        
        # swが負論理なので反転してLED出力に設定
        wp.digitalWrite(PIN_LED1_RED, ~sw1 & 1)
        wp.digitalWrite(PIN_LED2_YELLOW, ~sw2 & 1)
        wp.delay(250)
