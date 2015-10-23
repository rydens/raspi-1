"""My Library of Blinky Light Functions"""

import RPi.GPIO as GPIO
import time as t
import random as r

pins  = [4,17,27,22,5,6,19,26]
pins1 = [26,19,6,5,22,27,17,4] 
others = [5,6,19,26]
turtles = [22,27,17,4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(pins1,GPIO.OUT)

def on():
    GPIO.output(pins,GPIO.HIGH)

def off():
    GPIO.output(pins,GPIO.LOW)

def on1(pin):
    GPIO.output(pin,GPIO.HIGH)

def off1(pin):
    GPIO.output(pin,GPIO.LOW)

def slowoff(list=pins,delay=.1): 
    for pin in list:
        off1(pin)
        t.sleep(delay)

def slowon(list=pins,delay=.1):
    for pin in list:
        on1(pin)
        t.sleep(delay)

def chase(count=1):
    for n in range(count):
        slowon()
        slowoff()

def baf(baf=1):
    for n in range(baf):
        for pin in pins:
            on1(pin)
            t.sleep(.1)
        for pin in pins:
            off1(pin)
            t.sleep(.1)

        for pin in pins[::-1]:
            on1(pin)
            t.sleep(.1)
        for pin in pins[::-1]:
            off1(pin)
            t.sleep(.1)

def cylon(cylon=1):
    for n in range(cylon):
        for pin in pins:
            on1(pin)
            t.sleep(.07)
            off1(pin)
        for pin in pins[::-1]:
            on1(pin)
            t.sleep(.07)
            off1(pin)

def random(rand=1):
    for n in range(rand):
        q = r.choice(pins)
        GPIO.output(q, 1)
        t.sleep(.1)
        GPIO.output(q, 0)
        t.sleep(.1)

def branch(branch=1):
    for y in range(branch):
        for n in range(4):
            on1(others[n])
            on1(turtles[n])
            t.sleep(.12)
            off1(others[n])
            off1(turtles[n])
