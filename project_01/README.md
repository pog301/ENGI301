# Mini Rube Goldberg with Game 

Project 1: Building a simplified system based on Rube Goldberg machines. Here is the link to the Hackster.io page for the project: .

This folder has two subfolders:

      2.1) docs
      This folder contains some documents developed for the project as part of course deliverables.  
      Note: these files were developed to help with the project and made for the class but they do not reflect the final product for the         
      project; they were not updated. For guidelines on how the end project is built and what was actually implemented, please go to my     
      Hackster.io page linked above. 
      
      2.2) project_01_python
      This itself has two subfolders:
              2.2.1) p_01_main_code
              This contains a file with the main code for the project as well as a file to configure the pins and another one to run it.
              2.2.2) p_01_other
              This contains some additional files developed for the project which are called within the main project file.        
      Any other file implemented for the project but not found within "project_01_python" can be found within the python file in the main GitHub       repository. 


Software Build and Operation Instructions:

1) Copy the project_01_python subfolder files within the project_01 folder into your repository. Also copy the button.py (button subfolder) as well as the servo.py (servo subfolder) files within the python folder.
   Note: if you decide to change any naming convention or location of any files in general, you will have to make sure that it is updated where appropriate. Also make sure that the "run_p01" is updated to show the right path. Additionally, if any other pin in the Pocketbeagle is used instead of the ones I used, make sure to update the "configure_pins_p01.sh" file as well. 
2) To run the program, use "sudo ./run_p01".
   Note that this will start a process in the background. In the case that you want to exit the game, then you will have to kill any process related to "opc".
3) In the case that you want to autoboot this project, you can use the following line within the crontab:
   @reboot sleep 30 && bash /var/lib/cloud9/ENGI301/project_01/project_01_python/p_01_main_code/run_p01 > /var/lib/cloud9/logs/cronlog 2>&1 
      
Disclaimer: This is student work developed as part of a course. As such, some components might be missing or do not work as desired, and the quality is that of someone learning this for the first time. Additionally, a lot of the code was developed as part of the course or facilitated by the work done in the course. Thus, I take no responsibility for the use of any part of the project. Also, my professor helped me throughout the whole process, from giving ideas to helping me make things work, so I might not know the answers to some of the questions.
