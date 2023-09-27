# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Code to Blink the USR3 LED at 5 Hz
--------------------------------------------------------------------------
License:   
Copyright 2023 - Paula Ortega Gimenez

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Code for the USR3 LED that will 
  - 



--------------------------------------------------------------------------
"""

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# Frequency of 5 Hz
rate = 5

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

self.pin = pin

# Set up pins as inputs or outputs
GPIO.setup(pin, GPIO.IN)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin, GPIO.OUT)  

# used the Adafruit code but now sure about everything (eg. don't know what range is)
for i in range(4):
    GPIO.setup("USR3" % i, GPIO.OUT)

while True:
    for i in range(4):
        GPIO.output("USR3" % i, 1)
        time.sleep(0.2)
    for i in range(4):
        GPIO.output("USR3" % i, 0)
        time.sleep(0.2)




# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

import sysfs

import time

import Adafruit_BBIO.GPIO as GPIO


if __name__ == '__main__':
  
  
  # make it go to cd   /sys/class/leds/beaglebone:green:usr3
  # some way to blink back and forth 
    # echo "1" > brightness
    # wait 0.2 s (1/frequency = 1/5Hz = 0.2s)
    # echo "0" > brightness
    # repeat"










