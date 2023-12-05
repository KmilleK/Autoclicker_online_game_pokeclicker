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


from UI.main_page import Main_Window

from PyQt5.QtWidgets import QApplication
import sys

def main():
    
    
    app=QApplication([])
    main_window = Main_Window()
    main_window.show()
    
    
    try:
        sys.exit(app.exec_())
           
    except KeyboardInterrupt:
        pass

        
    

if __name__=="__main__":
    main()



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



    


