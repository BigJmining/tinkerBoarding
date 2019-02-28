#!/usr/bin/env python

import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

## photo sensor
gpio.setup(26, gpio.IN)

## switch and laser
gpio.setup([16,21], gpio.OUT)

## set LED pins to pwm
gpio.PWM(23, 50)
gpio.PWM(24, 50)
gpio.PWM(25, 50)

## optional items added to GPOIO pins
laser = 21
switch = 16

## LED lights
light_g = 24
light_b = 23
light_r = 25

## photo sensor
sensor = 26

statusBank = []

all_lights = [23,24,25]

try:
    while 1:
        pwm.start(0)
        scan = gpio.input(sensor)
        print(scan)

        if scan == 0:
            print('A Light is on')

            pwm = gpio.PWM(light_g,50)
            pwm.start(0)

            for x in range(0,101,.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)

            for x in range(100,0,-.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)
                
            statusBank.append('on\n')

        if scan == 1:
            print('The light is off')

            pwm = gpio.PWM(light_r ,50)
            pwm.start(0)

            for x in range(0,101,.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)

            for x in range(100,0,-.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)

            statusBank.append('off\n')

        sleep(.2)

except KeyboardInterrupt:
    gpio.output(all_lights,0)
    gpio.output(laser,0)
    pwm.stop()
    ## printout a history of light sensor status
    print(statusBank)
    
gpio.cleanup()


