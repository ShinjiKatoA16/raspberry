#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

pin18 = 18  # GPIO Pin18 = Pysical Pin12

gpio.setmode(gpio.BCM)  # Use GPIO Pin number
gpio.setup(pin18, gpio.OUT)  # Pin18: output mode

for i in range(10):
    gpio.output(pin18, gpio.HIGH)
    time.sleep(1.0) # Wait 1sec
    gpio.output(pin18, gpio.LOW)
    time.sleep(1.0) # Wait 1sec

