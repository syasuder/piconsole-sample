#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wiringpi as wp
PIN_SW1_WHITE = 19
PIN_SW2_BLACK = 16
PIN_LED1_RED = 20
PIN_LED2_YELLOW = 21
PIN_BUZZER = 25

import sys, socket, struct
from fcntl import ioctl
SIOCGIFADDR = 0x8915

from st7032i import St7032iLCD as LCD
I2C_ADDR_LCD = 0x3e

def get_ip(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ifreq  = struct.pack(b'16s16x', interface)
        ifaddr = ioctl(s.fileno(), SIOCGIFADDR, ifreq)
    finally:
        s.close()
    _, sa_family, port, in_addr = struct.unpack(b'16sHH4s8x', ifaddr)
    return (socket.inet_ntoa(in_addr))

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    while True:
        sw1 = wp.digitalRead(PIN_SW1_WHITE)
        sw2 = wp.digitalRead(PIN_SW2_BLACK)
        if sw1 == 0:
            ip_addr_eth0 = get_ip(b'eth0')
            lcd = LCD(I2C_ADDR_LCD)    
            lcd.clear()
            wp.delay(500)
            lcd.set_cursor(0, 0)
            lcd.print(ip_addr_eth0)
        wp.delay(250)
