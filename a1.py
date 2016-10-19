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

from datetime import timedelta, datetime

class RamenTimer:
    """
    ramen-timer class
    """
    def __init__(self):
        self.lcd = LCD(I2C_ADDR_LCD)
        self.lcd.clear()
        self.timer = 3
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
    
    def timer_select(self):
        while True:
            (sw1, sw2) = self.proc_inputs()
            if sw1:
                return            
            if sw2:
                self.beep()
                self.timer = self.timer + 1
            if self.timer > 5:
                self.timer = 3
            self.lcd.clear()
            self.lcd.set_cursor(0, 0)
            self.lcd.print("{0}:00".format(self.timer))        
            wp.delay(100)

    def timer_run(self):
        start = datetime.now()
        while True:
            (sw1, sw2) = self.proc_inputs()
            if sw1:
                return False
            delta = datetime.now() - start
            elapse = delta.seconds
            self.lcd.clear()
            self.lcd.set_cursor(0, 0)
            self.lcd.print("{0}:{1:02d}".format(int(elapse/60), elapse % 60))
            if elapse >= self.timer*60:
                return True
            wp.delay(250)
            
    def timer_buzz(self):
        count = 0
        while True:
            (sw1, sw2) = self.proc_inputs()
            if sw1 or sw2:
                wp.digitalWrite(PIN_BUZZER, 0)
                return
            if count in [0, 2, 4]:
                wp.digitalWrite(PIN_BUZZER, 1)
            else:
                wp.digitalWrite(PIN_BUZZER, 0)
            if count in [0, 2, 4, 6, 8]:
                wp.digitalWrite(PIN_LED1_RED, 1)
            else:
                wp.digitalWrite(PIN_LED1_RED, 0)
            count = (count + 1) % 10
            wp.delay(100)

if __name__ == '__main__':
    wp.wiringPiSetupGpio()
    wp.pinMode(20,1)
    wp.pinMode(21,1)
    wp.pinMode(25,1)
    wp.digitalWrite(PIN_BUZZER, 0)

    rt = RamenTimer()
    rt.timer_select()
    ret = rt.timer_run()
    if ret:
        rt.timer_buzz()
    
