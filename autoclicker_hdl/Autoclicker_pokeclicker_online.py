# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:33:27 2022

@author: camille 

Updated on Mon October 30 2023:
    Update dungeoning part as the color change in the game to detect the type of case
    autoclicker stop when the mouse is moved by user (not by the autoclicker)
    

To do: 
    - Change dungeon to use html balise and the type of case: not possible as the content of the page is generate dynamicaly
    - Info print to user when autoclicker is on or off (visual)
"""

from pynput.mouse import Button, Controller as MouseController
from pynput import mouse
from pynput.keyboard import KeyCode, Controller as KeyboardController, Listener

from PIL import ImageGrab
from threading import Thread
from threading import Event
import time

################### Initialisation for mouse and keyboard control 

mouse_c = MouseController()

start_key = KeyCode(char='s')
pause_key= KeyCode(char='p')
stop_key= KeyCode(char='x')
delay =0.05
button =Button.left

################## class for repetability 

class ClickMouse(Thread): 
    def __init__(self,delay,button): 
        super().__init__()
        self.delay =delay
        self.button =button
        self.running=False
        self.program_running =True
        print("initialise the clickMouse")

    def start_clicking(self): 
        self.running=True
        print("start clickMouse")

    def stop_clicking(self):
        if (self.running==True):
            print("stop clickMouse")
        self.running=False
        

    def exit(self): 
        self.stop_clicking()
        self.program_running =False 

    def run(self):
        while self.program_running:
            time.sleep(0.1)
            while self.running: 
                mouse_c.click(self.button,1)
                time.sleep(self.delay)
                
 
################### Thread starting for autoclick

event =Event()    # Shared event to stop our thread when exit button is clicked

click_thread= ClickMouse(delay,button)
click_thread.start()

################### Listener definition and start 

def on_press(key):
    if  key== start_key: 
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
            
    elif key==stop_key:
        event.set()
        event_move_from_code.clear()
        #dungeon_thread.exit()
        click_thread.exit()
        listener_mouse.stop()
        listener_keyboard.stop()
        print("Autoclicker Disable")
        
        """
       if  key== start_dungeon_key: 
           if dungeon_thread.running: 
               dungeon_thread.stop_dungeoning()
           else: 
               dungeon_thread.start_dungeoning()  
        """ 
        
def on_move(x, y):
    if not (event_move_from_code.is_set()):
      #  dungeon_thread.stop_dungeoning()
        click_thread.stop_clicking()
        #print("Mouse moved to position: ({}, {})".format(x, y))
    else:
        print("mouse move by python code")
    

def on_scroll(x, y, dx, dy):
    if not (event_move_from_code.is_set()):
        #dungeon_thread.stop_dungeoning()
        click_thread.stop_clicking()
        #print("Mouse scrolled at position: ({}, {})".format(x, y))
        #print("Scroll distance: ({}, {})".format(dx, dy))
    else: 
        print("mouse scroll by python code")

event_move_from_code= Event()    # Shared event to not do anything when the movement is from the python controller

listener_mouse = mouse.Listener(
    on_move=on_move,
    on_scroll=on_scroll)
listener_mouse.start()

listener_keyboard=Listener(on_press=on_press) 
listener_keyboard.start()



"""
class ClickDungeon(Thread): 
    def __init__(self, event): 
        super().__init__()
        self.running=False
        self.program_running =True
        self.event=event
        print("initialise the Clickdungeon")

    def start_dungeoning(self): 
        self.running=True
        print("start clickdungeon")

    def stop_dungeoning(self):
        if (self.running==True):
            print("stop clickdungeon")
        self.running=False
        

    def exit(self): 
        self.program_running =False 

    def run(self):
        while self.program_running:
            time.sleep(0.1)
            while self.running: 
                clear_dungeon(self.event)
                time.sleep(0.1)
                
                
            
def clear_dungeon(event):
    
    ###################  INITIALISATION & ENTER DUNGEON ###########################
    
    #Constants to change in function of youtee
    
    entrance_button_position=(428,320)
    screenshot_box=(500,300,1320,700) 
    position_boss_pixel=(400,315)
    rgb_boss_pixel=(240, 65, 36)
    
    
    #Small dungeon: 5x5
    dungeon_height=5
    dungeon_width=5
    
    max_battle_time=1.5
    
    boss_beaten= False
    movement_direction=1
    # Positioning and Click for entrance 
    
    event_move_from_code.set()
    
    mouse_c.scroll(0, 10)         
    time.sleep(0.1)
    mouse_c.position = entrance_button_position
    time.sleep(0.1)
    mouse_c.click(Button.left,1)
    time.sleep(0.1)
    
    event_move_from_code.clear()
    # Launch autoclicker 
    
    if event.is_set():
        return
        
    
    
    
        
    ###################  LABYRINTH DUNGEON ###########################
    
           
    
    #Process for each case of the labyrinthe: Move, detect boss, stop if needed, click to finish case
    def Case_move(keyboard_key_direction):
        boss_beaten_local=False
        keyboard_c.type(keyboard_key_direction)
        time.sleep(0.5)
        
        #get image from the screen
        screenshot_image =ImageGrab.grab(screenshot_box)
        #screenshot_image.show()
        screenshot_image=screenshot_image.convert("RGB")
        
        #print(screenshot_image.getpixel((400,250)))
        if screenshot_image.getpixel(position_boss_pixel)== rgb_boss_pixel:      # Final boss 
            print('detectBoss')
            boss_beaten_local=True
        
        click_thread.start_clicking()
        time.sleep(max_battle_time)
        click_thread.stop_clicking()
        
        return boss_beaten_local

    #Step 1: all the case on the left down + one up for consistency of grid latter
    
    for i in range(int((dungeon_width-1)/2)):
        if event.is_set():
            return
        if not boss_beaten:
            print("first movement")
            boss_beaten=Case_move('a')
            
    if event.is_set():
        return
    
    if not boss_beaten:        
        print("inbetween movement")
        boss_beaten=Case_move('w')
        
    #Step 2: all the left upper part
    
    for i in range(int((dungeon_width-1)/2)+1):
        for j in range(dungeon_height-2):
            if event.is_set():
                return
            if not boss_beaten:
                print("second movement section")
                if movement_direction==1:
                    boss_beaten=Case_move('w')
                elif movement_direction==-1:
                    boss_beaten=Case_move('s')
               
        movement_direction=-1*movement_direction
        if event.is_set():
            return
        if not boss_beaten:   
            boss_beaten=Case_move('d')    
        
    
    #Step 3: all the case on the right

    for i in range(int((dungeon_width-1)/2)):
        for j in range(dungeon_height):
            if event.is_set():
                return   
            if not boss_beaten:
                print("third movement section")
                if movement_direction==1:
                    boss_beaten=Case_move('w')
                elif movement_direction==-1:
                    boss_beaten=Case_move('s')
                
        movement_direction=-1*movement_direction
        if event.is_set():
            return   
        if not boss_beaten:        
            boss_beaten=Case_move('d')    
    
dungeon_thread= ClickDungeon(event)
dungeon_thread.start()                
                
                
"""



    


