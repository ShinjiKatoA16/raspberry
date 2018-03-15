#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import RPi.GPIO as gpio

gpio_min = 2
gpio_max = 27

if len(sys.argv) < 2:
    print('pin number need to be spedified')
    print('python3', sys.argv[0], 'pin_number')
    raise

pin = int(sys.argv[1])
if pin < gpio_min or pin > gpio_max:
    print('pin number shall be between', gpio_min, 'and', gpio_max)
    raise

gpio.setmode(gpio.BCM)  # Use GPIO Pin number
gpio.setup(pin, gpio.IN) # set to input mode

print ('Pin', pin, 'Value:', gpio.input(pin))

