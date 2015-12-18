"""My Library of Blinky Light Functions"""
#This Library was created by Ryan Densmore.
import RPi.GPIO as GPIO
import time as t
import random as r

pins  = [4,17,27,22,5,6,19,26]
pins1 = [26,19,6,5,22,27,17,4] 
brnchr = [5,6,19,26]
brnchr1 = [26,19,6,5]
brnchl = [22,27,17,4]
brnchl1 = [4,17,27,22]

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
