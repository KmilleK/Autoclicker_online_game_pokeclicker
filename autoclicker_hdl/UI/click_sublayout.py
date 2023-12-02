# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QGridLayout,QLabel

from PyQt5.QtCore import Qt
 

class clickGridLayout(QWidget):
    def __init__(self):
        super().__init__()
    
        #self.squareColor=
        
        self.init_ui()
        
        
        
        
    def init_ui(self):
        grid_layout= QGridLayout(self)
        
        LabelStartSentence=QLabel("To start clicking enter:")
        grid_layout.addWidget(LabelStartSentence,0,0)
        
        LabelStartKey=QLabel("S")
        grid_layout.addWidget(LabelStartKey,0,1,alignment=Qt.AlignCenter)
        
        LabelPauseSentence=QLabel("To pause clicking enter:")
        grid_layout.addWidget(LabelPauseSentence,1,0)
        
        LabelPauseKey=QLabel("P")
        grid_layout.addWidget(LabelPauseKey,1,1,alignment=Qt.AlignCenter)
        
        LabelDisableSentence=QLabel("To disable clicking enter:")
        grid_layout.addWidget(LabelDisableSentence,2,0)
        
        LabelDisableKey=QLabel("X")
        grid_layout.addWidget(LabelDisableKey,2,1,alignment=Qt.AlignCenter)
        
        ColorIndicator=QWidget()
        ColorIndicator.setStyleSheet('background-color: black')
        
        grid_layout.addWidget(ColorIndicator,1,2,)
        
        
        self.setLayout(grid_layout)
    
        
        