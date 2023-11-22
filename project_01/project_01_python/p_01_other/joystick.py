"""
--------------------------------------------------------------------------
Project 01 
--------------------------------------------------------------------------
License:   
Copyright 2023 - Paula Ortega Gimenez

Based on Code from: https://github.com/lucasesnaola/ENGI301/blob/main/python/RCboat/remote/joystick/joystick.py 
Copyright 2020 Lucas Esnaola

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

- 

This program reads the raw analog voltage value of the joysticks Vrx and Vry
and then determines the state of .

Analog Voltage Information
-Vrx range(AIN1): 0 to 3550, centerpoint around 1000
-Vry range(AIN2): 0 to 3550, centerpoint around 1000

ALOS USED SOME HELP FROM COMBOLOCK 

"""


import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Joystick():
    """Joystick components"""
    vertical   = None
    horizontal = None
    switch     = None
    
    
    def __init__(self, horizontal="AIN1", vertical="AIN2", switch="P1_20"):
        "Initialize variables"
        self.vertical   = vertical
        self.horizontal = horizontal
        self.switch     = switch
        
        self._setup()
        
    #End def
       
        
    def _setup(self):
       "Setup hardware components" 
       
       #Initialize switch
       GPIO.setup(self.switch, GPIO.IN)
       
       #Initialize Analog Input
       ADC.setup()
    
    #End def
    
    
    def read_analog_value(self):
        """"Reads raw analog voltage values for Vrx and Vry"""
        print(self.horizontal)
        xvalue = ADC.read_raw(self.horizontal) 
        yvalue = ADC.read_raw(self.vertical)
        
        return (xvalue,yvalue)
       
    #End def
    
    
    def get_direction(self):
        """Determines state of the DC motor and servo based on analog values"""
        
    #while(1):
        #Import raw analog values
        (xvalue,yvalue) = self.read_analog_value()
        
        # y directions 
        if yvalue <= 750:
            # Go Up
            ydirection = 1
        elif yvalue >= 1500:
            # Go Down 
            ydirection = 2
        else:
            # Do not move
            ydirection = 0

        #Directions for the servo
        if xvalue <= 750:
            # Go Right
            xdirection = 2
        elif xvalue >= 1500:
            # Go Left
            xdirection = 1
        else: 
            # Do not move
            xdirection = 0
            
        print(xdirection)
        print(ydirection)
        return (xdirection,ydirection)

    
    #End def
    
       
    def cleanup(self):
        
        """Clean up the hardware components"""
        
        GPIO.cleanup()
        
    #End def
    
    
# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    try:
        #Create instantiation of the joystick program
        joystick=Joystick()
 
        joystick.get_direction()
  
    except KeyboardInterrupt:
    # Clean up hardware when exiting
        pass
    
    
    
    
    