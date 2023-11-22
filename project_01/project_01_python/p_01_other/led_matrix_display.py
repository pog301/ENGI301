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

Went over Connect 4 code and it helped me understand; applied the old and new positions and reinforced idea of diving by
sections (if <x etc.) https://github.com/craannj/ECE434-connect4/blob/master/connect4final.py
Used combolock code for making 

"""

import time
import opc
import joystick as JOYSTICK

ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)
 
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# Define Pixel String
STR_LEN = 256
leds    = [(255, 255, 255)] * STR_LEN

#if not client.put_pixels(leds, channel=0):
    #print ('not connected')

time.sleep(1)

#initial_channel_a   = 4
#initial_channel_b   = 5
#chnl_a              = initial_channel_a
#chnl_b              = initial_channel_b 


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class LedDisplay():
    """Class for the LED Display"""
    joystick         = None
    
    def __init__(self, j_horizontal="P1_21", j_vertical="P1_23", j_switch="P1_20", matrix_pin="P1_08"):
        """ Initialize variables"""

        self.joystick     = JOYSTICK.Joystick(j_horizontal, j_vertical, j_switch)
    
    # End def
    
    #xpos = 0  
    #ypos = 0    
    #xpos_old = 0
    #ypos_old = 0
    
    
    #def movePiece(leds, xpos, xpos_old, ypos, ypos_old):
    
    #def moveDot():
        
    #End def
    
    
    def game(self):
        """Runs the LED matrix ____ game."""
        
        #self.client.put_pixels(self, initial_pixels, channel=initial_channel_a)   
        #self.client.put_pixels(self, initial_pixels, channel=initial_channel_b)
        #led_path = leds(1,2,3,4,5)
        
        for j in range(STR_LEN):
            leds[j] = (0, 0, 0)
                
        initial_position = 28
        end_game = 0
        final_led = 223
        location = initial_position
        old_location = initial_position
        
        leds[0] = (0, 30, 0)
        leds[1] = (0, 30, 0)
        leds[2] = (0, 30, 0)
        leds[3] = (0, 30, 0)
        leds[4] = (0, 30, 0)
        leds[5] = (0, 30, 0)
        leds[6] = (0, 30, 0)
        leds[7] = (0, 30, 0)
        leds[8] = (0, 30, 0)
        leds[9] = (0, 30, 0)
        leds[10] = (0, 30, 0)
        leds[11] = (0, 30, 0)
        leds[12] = (0, 30, 0)
        leds[13] = (0, 30, 0)
        leds[14] = (0, 30, 0)
        leds[15] = (0, 30, 0)
        leds[32] = (0, 30, 0)
        leds[33] = (0, 30, 0)
        leds[34] = (0, 30, 0)
        leds[35] = (0, 30, 0)
        leds[36] = (0, 30, 0)
        leds[37] = (0, 30, 0)
        leds[38] = (0, 30, 0)
        leds[39] = (0, 30, 0)
        leds[40] = (0, 30, 0)
        leds[41] = (0, 30, 0)
        leds[42] = (0, 30, 0)
        leds[43] = (0, 30, 0)
        leds[44] = (0, 30, 0)
        leds[46] = (0, 30, 0)
        leds[47] = (0, 30, 0)
        leds[64] = (0, 30, 0)
        leds[65] = (0, 30, 0)
        leds[66] = (0, 30, 0)
        leds[68] = (0, 30, 0)
        leds[69] = (0, 30, 0)
        leds[70] = (0, 30, 0)
        leds[71] = (0, 30, 0)
        leds[72] = (0, 30, 0)
        leds[73] = (0, 30, 0)
        leds[74] = (0, 30, 0)
        leds[75] = (0, 30, 0)
        leds[76] = (0, 30, 0)
        leds[77] = (0, 30, 0)
        leds[78] = (0, 30, 0)
        leds[79] = (0, 30, 0)
        leds[80] = (0, 30, 0)
        leds[96] = (0, 30, 0)
        leds[97] = (0, 30, 0)
        leds[98] = (0, 30, 0)
        leds[99] = (0, 30, 0)
        leds[100] = (0, 30, 0)
        leds[101] = (0, 30, 0)
        leds[102] = (0, 30, 0)
        leds[103] = (0, 30, 0)
        leds[104] = (0, 30, 0)
        leds[105] = (0, 30, 0)
        leds[106] = (0, 30, 0)
        leds[107] = (0, 30, 0)
        leds[108] = (0, 30, 0)
        leds[109] = (0, 30, 0)
        leds[111] = (0, 30, 0)
        leds[112] = (0, 30, 0)
        leds[114] = (0, 30, 0)
        leds[115] = (0, 30, 0)
        leds[126] = (0, 30, 0)
        leds[127] = (0, 30, 0)
        leds[128] = (0, 30, 0)
        leds[129] = (0, 30, 0)
        leds[131] = (0, 30, 0)
        leds[132] = (0, 30, 0)
        leds[133] = (0, 30, 0)
        leds[134] = (0, 30, 0)
        leds[135] = (0, 30, 0)
        leds[136] = (0, 30, 0)
        leds[137] = (0, 30, 0)
        leds[138] = (0, 30, 0)
        leds[140] = (0, 30, 0)
        leds[141] = (0, 30, 0)
        leds[143] = (0, 30, 0)
        leds[144] = (0, 30, 0)
        leds[149] = (0, 30, 0)
        leds[158] = (0, 30, 0)
        leds[159] = (0, 30, 0)
        leds[160] = (0, 30, 0)
        leds[161] = (0, 30, 0)
        leds[162] = (0, 30, 0)
        leds[163] = (0, 30, 0)
        leds[164] = (0, 30, 0)
        leds[165] = (0, 30, 0)
        leds[166] = (0, 30, 0)
        leds[167] = (0, 30, 0)
        leds[168] = (0, 30, 0)
        leds[170] = (0, 30, 0)
        leds[171] = (0, 30, 0)
        leds[172] = (0, 30, 0)
        leds[173] = (0, 30, 0)
        leds[174] = (0, 30, 0)
        leds[175] = (0, 30, 0)
        leds[176] = (0, 30, 0)
        leds[183] = (0, 30, 0)
        leds[188] = (0, 30, 0)
        leds[189] = (0, 30, 0)
        leds[190] = (0, 30, 0)
        leds[191] = (0, 30, 0)
        leds[192] = (0, 30, 0)
        leds[193] = (0, 30, 0)
        leds[194] = (0, 30, 0)
        leds[195] = (0, 30, 0)
        leds[197] = (0, 30, 0)
        leds[198] = (0, 30, 0)
        leds[200] = (0, 30, 0)
        leds[201] = (0, 30, 0)
        leds[202] = (0, 30, 0)
        leds[203] = (0, 30, 0)
        leds[204] = (0, 30, 0)
        leds[205] = (0, 30, 0)
        leds[207] = (0, 30, 0)
        leds[208] = (0, 30, 0)
        leds[217] = (0, 30, 0)
        leds[218] = (0, 30, 0)
        leds[224] = (0, 30, 0)
        leds[225] = (0, 30, 0)
        leds[226] = (0, 30, 0)
        leds[227] = (0, 30, 0)
        leds[228] = (0, 30, 0)
        leds[229] = (0, 30, 0)
        leds[230] = (0, 30, 0)
        leds[231] = (0, 30, 0)
        leds[232] = (0, 30, 0)
        leds[233] = (0, 30, 0)
        leds[234] = (0, 30, 0)
        leds[235] = (0, 30, 0)
        leds[236] = (0, 30, 0)
        leds[237] = (0, 30, 0)
        leds[238] = (0, 30, 0)
        leds[239] = (0, 30, 0)
        leds[initial_position] = (0, 0, 100)
        
        if not client.put_pixels(leds, channel=0):
            print ('not connected')
    
        #Moving led 
        while end_game == 0:
            (xdirection, ydirection) = self.joystick.get_direction()
            
            if xdirection == 1 & ydirection == 0: 
                # go left
                location = old_location + 1

                if leds[location] == (0, 0, 0):
                    leds[old_location] = (0, 0, 0)
                    leds[location] = (0, 0, 100)
                    if not client.put_pixels(leds, channel=0):
                        print ('not connected')
                    old_location = location
                    time.sleep(1)
                else: 
                    location = old_location
            
            elif xdirection == 2 & ydirection == 0:
                # go right
                location = old_location - 1
                
                if leds[location] == (0, 0, 0):
                    leds[old_location] = (0, 0, 0)
                    leds[location] = (0, 0, 100)
                    if not client.put_pixels(leds, channel=0):
                        print ('not connected')
                    old_location = location
                    time.sleep(1)
                else: 
                    location = old_location
                 
            elif xdirection == 0 & ydirection == 1:
                # go up
                location = old_location - 16
                 
                if leds[location] == (0, 0, 0):
                    leds[old_location] = (0, 0, 0)
                    leds[location] = (0, 0, 100)
                    if not client.put_pixels(leds, channel=0):
                        print ('not connected')
                    old_location = location
                    time.sleep(1)
                else: 
                    location = old_location
                    
            elif xdirection == 0 & ydirection == 2:
                # go down
                location = old_location + 16
                 
                if leds[location] == (0, 0, 0):
                    leds[old_location] = (0, 0, 0)
                    leds[location] = (0, 0, 100)
                    if not client.put_pixels(leds, channel=0):
                        print ('not connected')
                    old_location = location 
                    time.sleep(1)
                else: 
                    location = old_location
           
            elif xdirection == 0 & ydirection == 0:
                location = location
                leds[location] = (0, 0, 100)
                if not client.put_pixels(leds, channel=0):
                        print ('not connected')
                        
            #else:
                #location = old_location
               #leds[location] = (0, 0, 100)
               # if not client.put_pixels(leds, channel=0):
               #     print ('not connected')
                    
            if location == final_led:
                end_game = 1
            
        for j in range(STR_LEN):
            leds[j] = (50, 50, 50)
            
               # elif y == 2:
                # go down
               # if location == 18:
                #    location = 45
               # elif location == 60:
               #     location = 67
               # elif location == 67:
                 #   location = 91
               # elif location == 80:
                #    location = 
                #else:
                #    location = location
                
                #if leds[location] == (0, 0, 0):
                #   led[old_location] = (0, 0, 0)
                #   leds[location] = (0, 0, 100)
                #   old_location = location
 
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
    
    
    def clear(self):
        "Clearing the LED matrix."
        for j in range(STR_LEN):
            leds[j] = (0, 0, 0)
    
    #End def
    

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------
        
if __name__ == '__main__':  
    
    test = LedDisplay()
    
    try:
        test.game()
        
    except KeyboardInterrupt:
        test.clear()

    print("Program Complete")