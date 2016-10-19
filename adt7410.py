#!/usr/bin/python
# -*- coding: utf-8 -*-

import wiringpi as wp
import time

I2C_ADDR_THERMO = 0x48

# 2の補数表現変換
# http://stackoverflow.com/questions/1604464/twos-complement-in-python
def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

class ADT7410:
    """
    ADT7410 thermometer control class
    """
    def __init__(self, i2c_addr = I2C_ADDR_THERMO):
        self.i2c = wp.I2C()
        self.fd = self.i2c.setup(i2c_addr)
        # 分解能を16ビットに設定
        self._write(0x003, 0x80)

    def _write(self, offset, data):
        self.i2c.writeReg8(self.fd, offset, data)

    def _read(self, offset):
        datum = self.i2c.readReg8(self.fd, offset)
        return datum

    def read_temp(self):
        msb = self._read(0x00)
        lsb = self._read(0x01)
        temp = (msb << 8 | lsb)  # MSB, LSB
        temp = twos_comp(temp, 16)
        return temp    

if __name__ == '__main__':
    thermo = ADT7410(I2C_ADDR_THERMO)
    while True:
        temp = thermo.read_temp()
        print("Temperature:%6.2f" % (temp / 128.0))
        time.sleep(1)
