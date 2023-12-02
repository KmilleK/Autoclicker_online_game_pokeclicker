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

import os

WINDOW_WIDTH = 500  # Set your desired window size
WINDOW_HEIGHT= 300
NEW_HEIGHT=400

class Main_Window(QMainWindow):
    def __init__(self,message_bus):
        super().__init__(parent=None)
        self.setWindowTitle("Autoclicker")

        self.message_bus=message_bus
        self.message_bus.subscribe('autoclick_stop', self.exit)
        
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

        script_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_path, "..", "..", "data", "logo_company.jpeg")
        print(image_path)
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
        
        self.toggle_changed(False)

    
    def toggle_changed(self,state):
        
        if not (state==2):
            self.custom_layout.hide()
        else:
            self.custom_layout.show()
            
    def exit(self, *args, **kwargs): 
        print('exit toggle')
        #self.toggle_changed(False)
        self.toggleClick.setCheckState(False)
            
            
            
            
       

   

