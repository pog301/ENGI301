"""
--------------------------------------------------------------------------
Button Driver
--------------------------------------------------------------------------
License:   
Copyright 2021-2023 - Paula Ortega Gimenez

Based on Code from: https://www.hackster.io/babs-ogunbanwo/pocketbeagle-automatic-light-switch-f0588f *** 

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
"""

# Import Libraries
#import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

# Initial Variables

PIR_PIN="P2_4"

# Get PIR Output
# Setup digital input for PIR sensor:
direction = GPIO.setup(PIR_PIN, GPIO.IN)
# Get PIR output from GPIO port
pir = GPIO.input(PIR_PIN)

class Motion():

    #def __init__(self, PIR_PIN="P2_4"):
        #""" Initialize variables and set up display """

        #self.pir_pin    = PIR_PIN
    
    # End def
    
    
    def run():
        
        pir_value = 0
        motion = 0
        # Main loop that will run forever:
        #old_value = pir_value
        
        while pir_value == 0:
            pir_value = GPIO.input(PIR_PIN)
            print("pir_value = {0}".format(pir_value))
            
            if pir_value == 1:
                # PIR is detecting movement!
                # Check if this is the first time movement was
                # detected and print a message
                #if not old_value:
                # Rotate the servo CCW 180 degrees
                print('Motion detected!')
                motion = 1
                break 
                    
            #else:
                # PIR is not detecting movement. 
                # Again check if this is the first time movement
                # stopped and print a message.
                #if old_value:
                # Rotate the servo CW 180 degrees
                #print('No motion detected')
                #motion = 0
            
            return(motion)
            
            #old_value = pir_value
            
            time.sleep(2.0)
        
        #End def
        

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    motionsensor = Motion()

    try:
        # Run the program
        Motion.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        print("Error")

    print("Program Complete")

