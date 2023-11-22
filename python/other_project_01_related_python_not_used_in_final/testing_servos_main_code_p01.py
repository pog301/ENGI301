""" """

import servo                as SERVO
import time


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

SERVO_OFF         = 100     # Fully anti-clockwise
SERVO_ON          = 0       # Fully clockwise
#CON_SERVO_OFF     = 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Rube():
    """ Rube: name for Project_01's main class """
    
    def __init__(self, servo_1="P1_33", servo_2="P1_36"):
        """ Initialize variables """

        self.servo_1                 = SERVO.Servo(servo_1, default_position=SERVO_OFF)
        self.servo_2                 = SERVO.Servo(servo_2, default_position=SERVO_OFF)
        self.debug                   = False
    
    # End def
      
    
    def run(self):
        """Execute the main program."""
        
        
        while(1):
        # wait for motion --> motion sensor
        
            #if(motion==1):
            self.servo_1.turn(0)
            time.sleep(3)
            self.servo_1.turn(100)
            self.servo_2.turn(0)
            time.sleep(1)
            #continuous_servo.
            time.sleep(2)
            self.servo_2.turn(100)
        
            
            self.servo_continuous_on()
            
        
    # End def


# End class


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Let's start the game! Move your hand in front of the motion sensor when ready to start.")

    # Create instantiation of project_01
    project_01 = Rube()

    try:
        # Run the lock
        project_01.run()

    except KeyboardInterrupt:
        pass

    print("The game is done. I hope you enjoyed!")

