# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QGridLayout,
    QLabel,
    QWidget,
    QSpacerItem
)

from PyQt5.QtGui import (QPixmap)
from PyQt5.QtCore import (Qt)

from UI.animated_toggle import AnimatedToggle
from UI.click_sublayout import clickGridLayout


from clicker_action.autoclicker import ClickMouse 
from listener.input_listener import InputListener
from common.message_bus import MessageBus

import os
import sys

WINDOW_WIDTH = 500  # Set your desired window size
WINDOW_HEIGHT= 300
NEW_HEIGHT=400

class Main_Window(QMainWindow):
    def __init__(self):
        parent=None
        super().__init__(parent,Qt.WindowStaysOnTopHint)
        
        self.message_bus=MessageBus()
        self.message_bus.subscribe('autoclick_stop', self.exit)
        self.setWindowTitle("Autoclicker")
        self._createStatusBar()
        self._InitUI()
        

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Henaris Dev Labs product")
        self.setStatusBar(status)

    def _InitUI(self):
        layout = QGridLayout()

        # Title and image
        self.Title = QLabel("AUTOCLICKER")
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.Title, 0, 0)
        
        spacer_item = QSpacerItem(50,10)
        layout.addItem(spacer_item, 0,1)

        self.logo = QLabel()
        self.logo.setFixedSize(100, 100)
        self.logo.setAlignment(Qt.AlignRight)
        
        if getattr(sys,'frozen',False):
            script_path=sys._MEIPASS
            image_path = os.path.join(script_path, "data", "logo_company.jpeg")
        else: 
            script_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_path, "..", "..", "data", "logo_company.jpeg")
            
        #print(image_path)
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            print("image not load")
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        layout.addWidget(self.logo, 0, 2)
        
     
        # Spacer
        spacer_item = QSpacerItem(WINDOW_WIDTH, 50)
        layout.addItem(spacer_item, 1, 0)

        self.module1 = QLabel("Repeat click at mouse position")
        self.module1.setAlignment(Qt.AlignTop)
        self.module1.setStyleSheet("padding: 7px")
        layout.addWidget(self.module1, 2, 0,1,1)

        
        self.toggleClick = AnimatedToggle()
        self.toggleClick.setFixedSize(self.toggleClick.sizeHint())
        #self.toggleClick.setAlignment(Qt.AlignTop)
        layout.addWidget(self.toggleClick, 2, 1,1,2, alignment=Qt.AlignTop)
        
        self.toggleClick.stateChanged.connect(self.toggle_changed)
        
        self.custom_layout=clickGridLayout()
        
        layout.addWidget(self.custom_layout,3,0)
        
        window = QWidget()
        window.setLayout(layout)
        self.setCentralWidget(window)
        
        #self.toggle_changed(False)
        self.custom_layout.hide()

    
    def toggle_changed(self,state):     
        if not (state==2):
            self.click_module_disable() 
        else:
            self.click_module_enable()
            
            
    def exit(self, *args, **kwargs): 
        #print('exit toggle')
        #self.toggle_changed(False)
        self.toggleClick.setCheckState(False)
        
        
    def click_module_enable(self):
        self.custom_layout.show()
        
        self.listener_input= InputListener(self.message_bus)
        
        delay=0.05
        self.click_thread = ClickMouse(delay,self.message_bus)
        self.click_thread.start()
        #print('start the click module')
        
        
    def click_module_disable(self):
        self.custom_layout.hide()
        
        self.message_bus.set_exit_event()
        self.click_thread.exit()
        self.listener_input.listener_keyboard.stop()   # need to check if no problem with multiple run
        self.listener_input.listener_mouse.stop()
        self.click_thread.join()
        ('stop the click module')
      
        
        
            
            
            
            
       

   

