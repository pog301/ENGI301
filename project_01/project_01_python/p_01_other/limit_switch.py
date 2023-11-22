"""
--------------------------------------------------------------------------
Limit Switch Driver
--------------------------------------------------------------------------
License:   
Copyright 2023 - Paula Ortega

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

Limit Switch Driver

  This driver is built for limit switches connected such that the pin to the left 
  (with the pressing flat pointing to that side) is connected to ground, the pin 
  in the middle is connected to to a pull up resistor going to 3.3V, and the pin 
  to teh right is connected to the PocketBeagle (output pin)

Software API:

  LimitSwitch(pin)
    - Provide pin that the limit switch monitors
    
    is_pressed()
      - Return a boolean value (i.e. True/False) on if limit switch is pressed
      - Function consumes no time
    
    wait_for_press(function=None)
      - Wait for the limit switch to be pressed 
      - Optionally takes in an argument "function" which is the function 
        to be executed when waiting for the limit switch to be pressed
      - Function consumes time
      - Returns a tuple:  
        (<time limit switch was pressed>, <data returned by the "function" argument>)
        
        
- This file was made using the button.py file code from class (python folder in 
GitHub repository).        

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

class LimitSwitch():
    """ Limit Switch Class """
    pin             = None
    unpressed_value = None
    pressed_value   = None
    sleep_time      = None
    
    def __init__(self, pin=None):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for LimitSwitch()")
        else:
            self.pin = pin
        
        # By default the unpressed_value is "1" and the pressed
        # value is "0".  This is done to make it easier to change
        # in the future
        self.unpressed_value = 0
        self.pressed_value   = 1
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = 0.1

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        GPIO.setup(self.pin, GPIO.IN)

    # End def


    def is_pressed(self):
        """ Is the LimitSwitch pressed?
        
           Returns:  True  - Limit switch is pressed
                     False - Limit switch is not pressed
        """
        return GPIO.input(self.pin) == self.pressed_value

    # End def


    def wait_for_press(self, function=None):
        """ Wait for the button to be pressed.  This function will 
           wait for the button to be pressed and released so there
           are no race conditions.
        
           Arguments:
               function - Optional argument that is the functon to 
                          executed while waiting for the button to 
                          be pressed
        
           Returns:
               tuple - [0] Time button was pressed
                     - [1] Data returned by the "function" argument
        """
        function_return_value       = None
        limit_switch_press_time     = None
        
        # Execute function if it is not None
        #   - This covers the case that the limit switch is pressed prior 
        #     to entering this function
        if function is not None:
            function_return_value = function()
        
        # Wait for limit switch press
        #   If the function is not None, execute the function
        #   Sleep for a short amount of time to reduce the CPU load

        while(GPIO.input(self.pin) == self.unpressed_value):
        
            if function is not None:
                function_return_value = function()
                
            time.sleep(self.sleep_time)
        
        # Record time
        limit_switch_press_time = time.time()
        
        # Wait for limit switch release
        #   Sleep for a short amount of time to reduce the CPU load
        #

        while(GPIO.input(self.pin) == self.pressed_value):
            time.sleep(self.sleep_time)
        
        # Compute the limit_switch_press_time
        limit_switch_press_time = time.time() - limit_switch_press_time

        # Return a tuple:  (limit switch press time, function return value)        
        return (limit_switch_press_time, function_return_value)
        
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Limit Switch Test")

    # Create instantiation of the limit switch
    limit_switch = LimitSwitch("P2_6")
    
    # Create an function to test the wait_for_press function
    def print_time():
        ret_val = time.time()
        print("    Print Time = {0}".format(ret_val))
        return ret_val
    # End def

    # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
    try:
        # Check if the limit switch is pressed
        print("Is the limit_switch pressed?")
        print("    {0}".format(limit_switch.is_pressed()))

        print("Press and hold the limit_switch.")
        time.sleep(4)
        
        # Check if the limit switch is pressed
        print("Is the limit switch pressed?")
        print("    {0}".format(limit_switch.is_pressed()))
        
        print("Release the limit switch.")
        time.sleep(4)
        
        print("Waiting for limit switch press ...")
        value = limit_switch.wait_for_press()
        print("    Limit switch pressed for {0} seconds. ".format(value[0]))
        print("    Function return value = {0}".format(value[1]))
        
        print("Waiting for limit switch press with optional argument ...")
        value = limit_switch.wait_for_press(print_time)
        print("    Limit switch pressed for {0} seconds. ".format(value[0]))
        print("    Function return value = {0}".format(value[1]))
        
    except KeyboardInterrupt:
        pass

    print("Test Complete")


