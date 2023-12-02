from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Listener as MouseListener


start_key = KeyCode(char='s')
pause_key= KeyCode(char='p')
stop_key= KeyCode(char='x')

class InputListener:
    def __init__(self , message_bus):
        self.message_bus=message_bus
        self.listener_mouse= MouseListener(
            on_move=self.on_move,
            on_scroll=self.on_scroll)
        self.listener_mouse.start()
        self.listener_keyboard=Listener(on_press=self.on_press)
        self.listener_keyboard.start()
        
    def on_press(self,key):
        if  key== start_key:
            if not self.message_bus.isRunning:
                self.message_bus.publish('autoclick_start')
        elif key== pause_key:
            if self.message_bus.isRunning:
                self.message_bus.publish('autoclick_pause')
        elif key==stop_key:
            self.message_bus.publish('autoclick_stop')
            self.message_bus.set_exit_event()
              
           
    def on_move(self,x, y):
        self.message_bus.publish('autoclick_pause')
    

    def on_scroll(self,x, y, dx, dy):
        self.message_bus.publish('autoclick_pause')
   

