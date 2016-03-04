# My Amazing PiLights Library
# This Library was created by Ryan Densmore
# BEST IN DA WORLD, MAN

import RPi.GPIO as GPIO
import time as t
import random as r

pins  = [4,17,27,22,5,6,19,26]
pins1 = [26,19,6,5,22,27,17,4] 
brnchr = [5,6,19,26]
brnchr1 = [26,19,6,5]
brnchl = [22,27,17,4]
brnchl1 = [4,17,27,22]
red = [4,5]
yellow = [17,6]
green = [27,19]
blue = [22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(pins1,GPIO.OUT)

# Turns all lights on
def on():
    GPIO.output(pins,GPIO.HIGH)

# Turns all lights off
def off():
    GPIO.output(pins,GPIO.LOW)

# Turns on the lights, optimized for slowon/off
def on1(pin):
    GPIO.output(pin,GPIO.HIGH)

# Turns off the lights, optimized for slowon/off
def off1(pin):
    GPIO.output(pin,GPIO.LOW)

# Turns on all lights slowly, one at a time
def slowon(list=pins,delay=.1): 
    for pin in list:
        on1(pin)
        t.sleep(delay)

# Turns off all lights slowly, one at a time
def slowoff(list=pins,delay=.1):
    for pin in list:
        off1(pin)
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
            on1(brnchr[n])
            on1(brnchl[n])
            t.sleep(.1)
            off1(brnchr[n])
            off1(brnchl[n])
        for n in range(4):
            on1(brnchr1[n])
            on1(brnchl1[n])
            t.sleep(.1)
            off1(brnchr1[n])
            off1(brnchl1[n])

def all(all=1):
    on()
    t.sleep(1)
    off()
    t.sleep(1)
    slowon()
    t.sleep(1)
    slowoff()
    t.sleep(1)
    chase(2)
    t.sleep(1)
    baf(2)
    t.sleep(1)
    cylon(5)
    t.sleep(1)
    random(10)
    t.sleep(1)
    branch(2)
    off()

r1 = [4,5]
def red(red1=1):
    for w in range(red1):    
        GPIO.output(r1,1)
        GPIO.output(r1,0)

y1 = [17,6]
def yellow(yellow1=1):
    for w in range(yellow1):
        GPIO.output(y1,1)
        GPIO.output(y1,0)

g1 = [27,19]
def green(green1=1):
    for w in range(green1):
        GPIO.output(g1,1)
        GPIO.output(g1,0)

b1 = [22,26]
def blue(blue1=1):
    for b in range(blue1):
        GPIO.output(b1,1)
        GPIO.output(b1,0)

if __name__ == '__main__':
    print('Welcome to the showcase of all my PiLights functions. Please silence your cell phones now')
    print('and prepare for the show. If I had control over the lights, I would turn them off. So just')
    print('imagine this room is dark, please. :)  Now, please direct your attention to the BreadBoard')
    print('below. The show will begin shortly.')
    t.sleep(6)
    on()
    t.sleep(1)
    off()
    t.sleep(1)
    slowon()
    t.sleep(1)
    slowoff()
    t.sleep(1)
    chase(2)
    t.sleep(1)
    baf(2)
    t.sleep(1)
    cylon(5)
    t.sleep(1)
    random(10)
    t.sleep(1)
    branch(2)
    off()
