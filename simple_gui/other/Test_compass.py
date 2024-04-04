
import sys
from tkinter import messagebox
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import math

from PyQt5.QtWidgets import QGraphicsView ,QGraphicsScene
from numpy import rint


import qdarktheme

global calibrate_drone_direction  # north
global prev_direction

calibrate_drone_direction = 0  # north
prev_direction = calibrate_drone_direction


class MainWindow(QMainWindow):

    def __init__(self, *args, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)
         
        self.compass_app()

    def compass_app(self):
        scene_bottomLayer = QGraphicsScene()
        scene_topLayer = QGraphicsScene()
              
        arrow_pix = QPixmap("blank_compass.png")
        arrow_pix=arrow_pix.scaled(300,300)
        arrow_item = QGraphicsPixmapItem(arrow_pix)
    
        arrow_pointer_pix = QPixmap("R.png")
        arrow_pointer_pix = arrow_pointer_pix.scaled(300,300)
        arrow_pointer_item =QGraphicsPixmapItem(arrow_pointer_pix)


        scene_bottomLayer.addItem(arrow_item)
        scene_topLayer.addItem(arrow_pointer_item)

        
        self.view = QGraphicsView(scene_bottomLayer,self)
        #self.setScene(scene)
        
        self.view_top = QGraphicsView(scene_topLayer,self)
        self.view_top.setStyleSheet("background:transparent;")
        
        self.view.setGeometry(0,0, 2000,1000)
        self.view_top.setGeometry(0,0, 2000,1000)
        self.update_compass()
        
        self.temp = self.txt_box.text()
        print(self.temp)
    def update_compass(self):
        self.temp = self.txt_box.text()
        print(self.temp)
        try:
            temp_float = float(self.temp)
            temp_RotDeg = self.compassPOStoRotationalDegrees(temp_float)
            print(temp_RotDeg)
            self.view_top.rotate(temp_RotDeg)
        except:
                pass
        
    def compassPOStoRotationalDegrees(self,input_direction):
        global prev_direction
        direction = round(input_direction,1)
        angle = prev_direction - direction 
        print(angle)
        prev_direction = direction
        return angle
        
    


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()