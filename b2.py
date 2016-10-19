#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
PIN_SW1_WHITE = 19
PIN_SW2_BLACK = 16
PIN_LED1_RED = 20
PIN_LED2_YELLOW = 21
PIN_BUZZER = 25

import os

# 1秒以上長押しでTrueを返す
def is_long_pushed(pin):
    count = 0;
    while count < 4:
        state = wp.digitalRead(pin)
        if state != 0:
            return False
        count = count + 1
        wp.delay(250)
    return True

# sw1が押されたコールバック
def sw1_callback():
    if is_long_pushed(PIN_SW1_WHITE):
        print("reboot")
        os.system("sudo reboot")
    else:
        print("reboot cancel")

# sw2が押されたコールバック
def sw2_callback():
    if is_long_pushed(PIN_SW2_BLACK):
        print("shutdown")
        os.system("sudo poweroff")
    else:
        print("shutdown cancel")

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    # 負論理なので立下りトリガ
    wp.wiringPiISR(PIN_SW1_WHITE, wp.GPIO.INT_EDGE_FALLING, sw1_callback)
    wp.wiringPiISR(PIN_SW2_BLACK, wp.GPIO.INT_EDGE_FALLING, sw2_callback)   
    while True:
        wp.delay(250)
