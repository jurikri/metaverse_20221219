# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:49:02 2022

@author: PC
"""

import pyautogui

myScreenshot = pyautogui.screenshot()
savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_RGB_presentUI\\'
myScreenshot.save(savepath + 'test.jpg')

#%%

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QCoreApplication

from time import sleep


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.filepath = []
        self.filepath.append(savepath + 'blue.png')
        self.filepath.append(savepath + 'red.png')
        self.cnt = 0
        
        self.lbl_img = QLabel()

        self.timer = QTimer(self)
        self.timer.start(2000)
        self.timer.timeout.connect(self.initUI)

    def initUI(self):
        
        # def show_img(filepath):
        if self.cnt == 0:
            pixmap = QPixmap(self.filepath[0])
            
            
            self.lbl_img.setPixmap(pixmap)
            vbox = QVBoxLayout()
            vbox.addWidget(self.lbl_img)
            
            self.setLayout(vbox)
            self.setWindowTitle('QPixmap')
            self.move(300, 300)
            self.show() 
        # self.repaint()
            
        # show_img(self.filepath[0])
            
        # show_img(savepath + 'red.png')
        # if self.cnt % 2 == 0:
        #     show_img(self.filepath[0])
        # elif self.cnt % 2 == 1:
        #     show_img(self.filepath[1])
        
        if self.cnt > 0:
            ix = int(self.cnt % 2)
            pixmap = QPixmap(self.filepath[ix])
            self.lbl_img.setPixmap(pixmap)
            
        print(self.cnt)
        self.cnt += 1
        
        # print(self.filepath[0], self.filepath[1])
        # timerVar = QTimer()
        # timerVar.setInterval(2000)
        # timerVar.timeout.connect(show_img(savepath + 'blue.png'))
        # timerVar.start()
        
        
        # # QCoreApplication.instance().quit
        
        # sleep(2)
        
        
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())

#%%



































