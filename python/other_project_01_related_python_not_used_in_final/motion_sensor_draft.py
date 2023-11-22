"""
--------------------------------------------------------------------------
Button Driver
--------------------------------------------------------------------------
License:   
Copyright 2021-2023 - Paula Ortega Gimenez

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

Motion Sensor

*** This file was made by modifying the Button file. (Before I found the motion sensor code.) 
  
"""
import time

import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class MotionSensor():
    """ Button Class """
    pin             = None
    no_motion_value = None
    motion_value    = None
    sleep_time      = None
    
    def __init__(self, pin=None):
        """ Initialize variables and set up the motion sensor """
        if (pin == None):
            raise ValueError("Pin not provided for Motion Sensor()")
        else:
            self.pin = pin

        self.no_motion_value = 1
        self.motion_value   = 0
    
        self.sleep_time      = 1

        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        GPIO.setup(self.pin, GPIO.IN)

    # End def


    def motion(self):
        """ Is there motion?
           Returns:  True  - Motion detected ____ 
                     False - Motion not detected
        """
        return GPIO.input(self.pin) == self.motion_value

    # End def


    def wait_for_motion(self, function=None):
        """ Wait for the the motion to detect a motion.  This function will 
           wait for a motion to be detected 
        
           Arguments:
               function - Optional argument that is the functon to 
                          executed while waiting for the button to 
                          be pressed
        
           Returns:
               tuple - [0] Time otion was detected
                     - [1] Data returned by the "function" argument
        """
        function_return_value = None
        motion_time     = None
        
        # Execute function if it is not None
        #   - This covers the case that the button is pressed prior 
        #     to entering this function
        if function is not None:
            function_return_value = function()
        
        # Wait for motion
        #   If the function is not None, execute the function
        #   Sleep for a short amount of time to reduce the CPU load
        while(GPIO.input(self.pin) == self.no_motion_value):
        
            if function is not None:
                function_return_value = function()
                
            time.sleep(self.sleep_time)
        
        # Record time
        motion_time = time.time()
        

        while(GPIO.input(self.pin) == self.motion_value):
            time.sleep(self.sleep_time)
        
        # Compute the motion_time
        motion_time = time.time() - motion_time

        # Return a tuple:  (button press time, function return value)        
        return (motion_time, function_return_value)
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Button Test")

    # Create instantiation of the button
    button = Button("P2_2")
    
    # Create an function to test the wait_for_press function
    def print_time():
        ret_val = time.time()
        print("    Print Time = {0}".format(ret_val))
        return ret_val
    # End def

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        # Check if the button is pressed
        print("Is the button pressed?")
        print("    {0}".format(button.is_pressed()))

        print("Press and hold the button.")
        time.sleep(4)
        
        # Check if the button is pressed
        print("Is the button pressed?")
        print("    {0}".format(button.is_pressed()))
        
        print("Release the button.")
        time.sleep(4)
        
        print("Waiting for button press ...")
        value = button.wait_for_press()
        print("    Button pressed for {0} seconds. ".format(value[0]))
        print("    Function return value = {0}".format(value[1]))
        
        print("Waiting for button press with optional argument ...")
        value = button.wait_for_press(print_time)
        print("    Button pressed for {0} seconds. ".format(value[0]))
        print("    Function return value = {0}".format(value[1]))
        
    except KeyboardInterrupt:
        pass

    print("Test Complete")

