"""
--------------------------------------------------------------------------
LED Matrix Display
--------------------------------------------------------------------------
License:   
Copyright 2021 Erik Welsh

Based on Code from:  https://github.com/rpliu3/ENGI301/tree/master/Project_01/code
Copyright 2019 Rebecca Liu

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
Software API:

  * opc.client ensures that server is running so that LED string can be displayed
  
--------------------------------------------------------------------------
Background Information: 
 
   * Base code for LED functions came from the following repositories:
        https://markayoder.github.io/PRUCookbook/01case/case.html#_neopixels_5050_rgb_leds_with_integrated_drivers_ledscape
        https://markayoder.github.io/PRUCookbook/06io/io.html#io_uio
        https://github.com/Yona-Appletree/LEDscape.git
        https://github.com/zestyping/openpixelcontrol
        
        
        
        CODE MADE BY MODIFICATION OF LED_STRIP_TEST *** (USES OPC)
        ALSO made from understanding of Snake codes x2 ? 
        USED Combolock as reference for debugging and added a couple of comments eg (commented main code) from there too 
        (perhaps not specifically or first time it appeard)

"""

import time
import opc
#import joystick

ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)
 
 
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# Define Pixel String
STR_LEN = 10
leds    = [(255, 255, 255)] * STR_LEN

if not client.put_pixels(leds, channel=0):
    print ('not connected')

time.sleep(1)

#snake_size          = 2
#initial_pixels      = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255)]
#initial_channel_a   = 4
#initial_channel_b   = 5
#food_position       = random 
#chnl_a              = initial_channel_a
#chnl_b              = initial_channel_b 


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class LedDisplay():

   def game():
        """Runs the LED matrix ____ game."""
        
        #self.client.put_pixels(self, initial_pixels, channel=initial_channel_a)   
        #self.client.put_pixels(self, initial_pixels, channel=initial_channel_b)
        #led_path = leds(1,2,3,4,5)
        
        while True:
        #Defining path of leds
            leds[6-15] = (100, 0, 0)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
        #leds[] = (100, 100, 100)
         
        
        #while True:
            ##Uses each light's address to set display to set a color
            #def task():
            #while True:
                #print("loop")
                #for i in range (0, 255):
                #    for j in range(STR_LEN):
                #        leds[j] = (i, i, i)
            
                #    if not client.put_pixels(leds, channel=0):
                #        print ('not connected')
                    
                #    time.sleep(0.1)
                
                
                #led_path = (100, 100, 100)
                #i = 100
                #for i in range (0, 255):
                    #for j in range(STR_LEN):
                       # leds[j] = (0, i, 0)
                
                   # time.sleep(3)
                #break

                #if not client.put_pixels(leds, channel=0):
                    #print ('not connected')
                    
                #    time.sleep(0.1)
            
            #(x_dir,y_dir) = joystick.get_direction()


            #if x_dir == 2 && y_dir == 0
                #self.client.put_pixels(self, pixels, channel=chnla)   
                #self.client.put_pixels(self, pixels, channel=chnlb)
            
            #elif x_dir == 1 && y_dir == 0
            
            #elif x_dir == 0 && y_dir == 1
            
            #elif x_dir == 0 && y_dir == 2
            
            #else
            
    
    # End def      
    
    
    #def yay():
       #"""Displays yay on the LED matrix."""
       #self.client.put_pixels(self, pixels, channel=0)  
       # Display yay  
        
    # End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------
        
if __name__ == '__main__':  
    
    testled = LedDisplay()
    
    try:
        testled.game()
    
    except KeyboardInterrupt:
        print("Error")
        pass

    print("Program Complete")