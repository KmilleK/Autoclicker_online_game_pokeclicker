from pynput.mouse import Button, Controller as MouseController
from threading import Thread
import time



class ClickMouse(Thread): 
    def __init__(self,delay,message_bus): 
        super().__init__()
        self.delay =delay
        self.button= Button.left
        self.mouse_c=MouseController()
        self.running=False
        self.program_running =True
        
        self.message_bus=message_bus
        self.message_bus.subscribe('autoclick_start', self.start_clicking)
        self.message_bus.subscribe('autoclick_pause', self.pause_clicking)
        self.message_bus.subscribe('autoclick_stop', self.exit)
        #print("initialise the clickMouse")

    def start_clicking(self, *args, **kwargs): 
        self.running=True
        self.message_bus.set_isRunning()
        #print("start clickMouse")
        
    def pause_clicking(self, *args, **kwargs):
        self.message_bus.unset_isRunning()
        self.running=False
        #print("pause clickMouse")
    
    def exit(self, *args, **kwargs): 
        self.pause_clicking()
        self.program_running =False 
        #print("stop listening")

    def run(self):
        while self.program_running:
            time.sleep(0.1)
            while self.running: 
                self.mouse_c.click(self.button,1)
                time.sleep(self.delay)


