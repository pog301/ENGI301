"""
--------------------------------------------------------------------------
Project 01 
--------------------------------------------------------------------------
License:   
Copyright 2023 - Paula Ortega Gimenez

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

Use the following hardware components to make this project:  
  - Button x1
  - Servo motor (normal) x2
  - Continuous rotation servo x1
  - LED 16x16 matrix x1
    - Level Shifter x1 
  - Joystick x1
  - Motion sensor x1 
Use the following other physical components to make this project:
  - Marble
  - Marble path
  - Base/breadboards to arrange the project and hold the componentx in place 

Requirements:
  - Hardware:
    - Summary: 
        - When off (no initial motion detected in motion sensor): normal servos 
        are closed; continous servo is still; LED screen is off. 
        - When on (initial motion detected in motion sensor): program runs 
    - Button:
    - Servo 1:
    - Servo 2: 
    - Continuous Servo: 
    - LED matrix:
    - Joystick:
    - Motion Sensor: 
    - User interaction:
      - Needs to be able to start the project by an initial motion in front of
      the motion sensor
      - Needs to be able to play the game in the LED matrix after the screen is
      turned on

Uses:
  - Libraries developed in class (button, servo, ) and was developed using
  a project developed in class as guidance. ***COMBO_LOCK 
  - Libraries developed for this project (led_matrix_display, )
  
  USED SERVO CLASS CODE TO WRITE THE SERVO RELATED CODE 

"""

import time

import button               as BUTTON
import servo                as SERVO
import led_matrix_display   as MATRIX
import limit_switch         as SWITCH


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

SERVO_OFF         = 100     # Fully anti-clockwise
SERVO_ON          = 0       # Fully clockwise

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Rube():
    """ Rube: name for Project_01's main class """
    button            = None
    servo_1           = None
    led_matrix        = None 
    limit_switch      = None
    
    def __init__(self, button="P2_2", servo_1="P1_33", led_matrix="P1_08", limit_switch="P2_6"):
        """ Initialize variables """

        self.button                  = BUTTON.Button(button)
        self.servo_1                 = SERVO.Servo(servo_1, default_position=SERVO_OFF)
        self.led_matrix              = MATRIX.LedDisplay("P1_21", "P1_23", "P1_20", led_matrix)
        self.limit_switch            = SWITCH.LimitSwitch(limit_switch)
        self.debug                   = False

        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        self.led_matrix.clear()

    # End def
    
    #def servo_1_on(self)
        #"""Get Servo 1 to work."""
        
        # call servo code
        # servo 1 turns, wait X seconds, turns back 
    
    # End def
    
    def run(self):
        """Execute the main program."""
        
        while(1):
            
            self.button.wait_for_press()[0]
            self.servo_1.turn(0)
            self.limit_switch.wait_for_press()[0]
            time.sleep(2)
            self.servo_1.turn(100)
            self.led_matrix.game()
            
            break
    # End def
    
    
    #def cleanup(self):
        #"""Cleanup the hardware components."""

        # Set Display to something fun to show program is complete

        # Clean up hardware
        
    # End def

# End class


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Let's start the game! Press the button when ready to start.")

    # Create instantiation of project_01
    project_01 = Rube()

    try:
        # Run the lock
        project_01.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        #project_01.cleanup()
        print("The game is done. I hope you enjoyed!")



