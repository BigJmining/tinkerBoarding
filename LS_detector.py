#!/usr/bin/env python

import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(26, gpio.IN)

gpio.setup([16,21], gpio.OUT)

gpio.PWM(23, 50)
gpio.PWM(24, 50)
gpio.PWM(25, 50)


# gpio.setup(8,  gpio.OUT)
# gpio.setup(12, gpio.OUT)
# gpio.setup(16, gpio.OUT)

laser = 21
switch = 16

light_g = 24
light_b = 23
light_r = 25

sensor = 26

statusBank = []

all_lights = [23,24,25]

#pwm = gpio.PWM(lite_pin, 50)
#pwm.start(0)


try:
    while 1:
        # for i in range(10):
        # gpio.output(all_lights, 0)
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

            #gpio.output(light_g,1)
            #gpio.output(laser, 0)
            statusBank.append('on\n')

        if scan == 1:
            print('The light is off')

            # gpio.output(all_lights,0)

            pwm = gpio.PWM(light_r ,50)
            pwm.start(0)

            for x in range(0,101,.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)

            for x in range(100,0,-.25):
                pwm.ChangeDutyCycle(x)
                sleep(.2)

            #gpio.output(light_r,1)
            #gpio.output(laser, 1)
            statusBank.append('off\n')

        sleep(.2)

except KeyboardInterrupt:
    gpio.output(all_lights,0)
    gpio.output(laser,0)
    pwm.stop()

    print(statusBank)
    
gpio.cleanup()


