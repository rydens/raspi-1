"""My Library of Blinky Light Functions"""

import RPi.GPIO as GPIO
import time as t

pins  = [4,27,5,26]
pins1 = [26,5,27,4] 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)
GPIO.setup(pins1,GPIO.OUT)

def on(pin):
    GPIO.output(pin,GPIO.HIGH)

def off(pin):
    GPIO.output(pin,GPIO.LOW)

def slowoff(list=pins,delay=.1): 
    for pin in list:
        off(pin)
        t.sleep(delay)

def chase(count=1):
    for n in range(count):
        slowon()
        slowoff()

def baf(baf=1):
    for n in range(baf):
        for pin in pins:
	    bky.on(pin)
    	    t.sleep(.1)
        for pin in pins:
    	    bky.off(pin)
            t.sleep(.1)

        for pin in bky.pins[::-1]:
            bky.on(pin)
            t.sleep(.1)
        for pin in bky.pins[::-1]:
            bky.off(pin)
            t.sleep(.1)

