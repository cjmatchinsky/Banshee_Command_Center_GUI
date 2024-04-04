

from sre_constants import SRE_FLAG_MULTILINE
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


import folium
import streamlit as st

from streamlit_folium import st_folium

from PyQt5 import QtCore, QtGui ,QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QGridLayout , QLineEdit, QLabel ,QPushButton 
from PyQt5.QtWebEngineWidgets import QWebEngineView 
import io, folium
from numpy import double

import qdarktheme
import cv2

from PyQt5.QtWidgets import QWidget



global calibrate_drone_direction  # north
global prev_direction

calibrate_drone_direction = 0  # north
prev_direction = calibrate_drone_direction

class MainWindow(QMainWindow):

    def __init__(self, *args, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)
        loadUi('GUI_Banshee_Command_Center.ui',self)
        self.setWindowIcon(QIcon('Banshee_logo.png'))
        self.setWindowTitle('Banshee Command Center')
        self.setWindowOpacity(0.95)
        # define and find child name in ui file
        self.video_feed_label = self.findChild(QLabel,'RGB_video_feed')
        self.map_viewer = self.findChild(QWebEngineView,'map')
        self.btn_add_marker = self.findChild(QPushButton, "add_marker_btn")
        self.txt_latitude_input = self.findChild(QLineEdit,'latitude_input_TextBox')
        self.txt_longitude_input = self.findChild(QLineEdit,'longitude_input_TextBox')
        self.txt_name_add_marker = self.findChild(QLineEdit, 'name_add_maker')
        self.txt_description_add_marker = self.findChild(QLineEdit, 'description_input_text_box')
        self.compass_graphicsView = self.findChild(QGraphicsView, 'compass_graphicsView')
        

        # QpushButton Controls
        self.btn_add_marker.clicked.connect(self.add_maker)

        # Set the map data to the webview
        coordinate = (34.0555, -117.8088)
        marker_coordinate = (33.0555, -119.8088)
        self.bcc_map = folium.Map(location=coordinate, zoom_start=4  )
        folium.Marker(location=marker_coordinate).add_to(self.bcc_map)
        self.update_map()

        # compass 
        self.compass_app()

        #print('testsetsets')

        # Set up a timer to update the video frame periodically
        self.cap = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)  # Update frame every 20 milliseconds
        self.timer.timeout.connect(self.update)
        self.timer.start()


    def update(self):
        ret, frame = self.cap.read()
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgbFrame = cv2.resize(rgbFrame,(1080,1080))
        h, w, ch = rgbFrame.shape
        bytesPerLine = ch * w
        convertToQtFormat = QtGui.QImage(rgbFrame.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(convertToQtFormat)
        self.video_feed_label.setPixmap(pixmap)

        #update compass
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

        
        self.view_bottomLayer = QGraphicsView(scene_bottomLayer,self)
        self.view_bottomLayer.setStyleSheet("background:transparent;")
        self.view_top = QGraphicsView(scene_topLayer,self)
        self.view_top.setStyleSheet("background:transparent;")
        
        self.view_bottomLayer.setGeometry(3220,1120, 511,431)
        self.view_top.setGeometry(3220,1120, 511,431)
        self.update_compass(62)
        

    def update_compass(self, input):
        temp = input
        #print(temp)
        try:
            temp_float = float(temp)
            temp_RotDeg = self.compassPOStoRotationalDegrees(temp_float)
            #print(temp_RotDeg)
            self.view_top.rotate(temp_RotDeg)
        except:
                pass
        
    def compassPOStoRotationalDegrees(self,input_direction):
        global prev_direction
        direction = round(input_direction,1)
        angle = prev_direction - direction 
        #print(angle)
        prev_direction = direction
        return angle



    def add_maker(self):
        #self.txt_latitude_input = self.findChild(QLineEdit,'latitude_input_TextBox')
        #self.txt_longitude_input = self.findChild(QLineEdit,'longitude_input_TextBox')
        #self.txt_name_add_marker = self.findChild(QLineEdit, 'name_add_maker')
        #self.txt_description_add_marker = self.findChild(QTextEdit, 'description_add_marker')
        temp_name = self.txt_name_add_marker.text()
        temp_description = self.txt_description_add_marker.text()
        temp_latitude = self.txt_latitude_input.text()
        temp_longitude = self.txt_longitude_input.text()
        try:
            temp_marker_coordinate = (float(temp_latitude),float(temp_longitude))
            temp_description= str(str(temp_marker_coordinate) +" - " +temp_description)

            folium.Marker(location=temp_marker_coordinate, popup=temp_description, tooltip=temp_name).add_to(self.bcc_map)
            self.update_map()
       
            self.txt_latitude_input.clear()
            self.txt_longitude_input.clear() 
            self.txt_name_add_marker.clear()
            self.txt_description_add_marker.clear()
        except:
            print('Error - Clearing Text Input Dialog... ')
            self.txt_latitude_input.clear()
            self.txt_longitude_input.clear() 
            self.txt_name_add_marker.clear()
            self.txt_description_add_marker.clear()
            

    def update_map(self):
        data = io.BytesIO()
        self.bcc_map.save(data, close_file=False)
        self.map_viewer.setHtml(data.getvalue().decode())

 



def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()