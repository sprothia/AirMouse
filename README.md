#                                                                                  AirMouse 

## 🔶 A computer vision project that controls your mouse using your hands. 

# Introduction
### Airmouse is an AI project built with Python and many libraries/frameworks such as Mediapipe, OpenCV, numpy, and more. Using hand recognition, you can control many actions that your computers mouse performs such as clicking and scrolling.
   * Hold up certain fingers to control things like moving your mouse or scrolling
   * Built a simple website that allows users to learn how to control their mouse with their fingers, using HTMl, CSS, Flask and Google Cloud Platform

# Requirements
 - MacOS
 - Web Cam: Attach webcam to your computer and make sure ****palm is facing towards the camera**** like in the Demo Video
 - Lighting: should have good lighting and hand should be ****clearly visible****

# Mouse Controls 
### Reminder :bell::  Palm should be facing camera like in demo video

 - ## Move Mouse ☝️  
 
    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static/mouse_away.png?raw=True" alt="Move Mouse" width="40px" height="110px"/>
    </div>
    
    ####        Keep all your fingers down except the pointer finger, which you will move inside of the purple box
 
 - ## Left Click 👆
 
    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static/mouse_click_away.png?raw=True" alt="Move Mouse" width="40px" height="110px"/>
    </div>
    
    ####       hold up the pointer finger and rapidly open and close your thumb
    
 - ## Scroll Down ✊

    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static/mouse_scroll_down_away.png?raw=True" alt="Move Mouse" width="40px" height="110px"/>
    </div>
    
    ####       hold up a fist, with every finger down
    
 - ## Scroll Up :v:
 
    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static/mouse_scroll_up_away.png?raw=True" alt="Move Mouse" width="40px" height="110px"/>
    </div>
    
    ####       hold up a 2, with only the pointer and middle finger up

# Other Controls

 - ## Volume Down :sound:
 
    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static//volume_down_Sketchpng.png?raw=True" alt="Move Mouse" width="50px" height="100px"/>
    </div>
    
    ####       lower the pointer finger slightly while holding up all other fingers.
    
 - ## Volume Up :loud_sound:

    <div style="display:flex;"> 
     <img src="https://github.com/sprothia/AirMouse/blob/main/static/volume_up_sketch.png?raw=True" alt="Move Mouse" width="50px" height="100px"/>
    </div>
    
    ####        lower the middle finger slightly while holding up all other fingers.

# Demo 
 - [![asciicast](https://github.com/sprothia/AirMouse/blob/main/static/thumbnail.png?raw=True)]([https://www.youtube.com/watch?v=06isugZY73E](https://youtu.be/Sq4yyo_Dz_Y))

# Project Website
 - https://air-mouse-389900.wm.r.appspot.com/

# Technologies
 - Python 🐍
   * OpenCV for Computer Vision
   * Mediapipe for hand detection and processing
   * Numpy
   * Pyautogui and Autopy for mouse actions
 - HTML/CSS 
   * Building the static webpage that guides users to controlling their mouse
 - Flask
   * To build the simple web app that I deployed using Google Cloud Platform web-hosting service 

# Installation :gear:
### Setup
 - Clone this repository into a new folder: 
 ``` 
 git clone https://github.com/sprothia/AirMouse.git 
 ```
 - Create a virtual environment
 - Install requirements
 ```
 pip install -r requirements.txt
 ```
 
 # License
 [MIT License](LICENSE)
