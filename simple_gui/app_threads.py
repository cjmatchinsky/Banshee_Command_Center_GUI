from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import json
import matplotlib.pyplot as plt
import cv2
import numpy as np
import folium
import io


# Video stream thread
class VideoThread(QThread):
    frame_signal = pyqtSignal(np.ndarray)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                self.frame_signal.emit(frame)
            self.msleep(25)  # Adjust the sleep duration as needed

# Map and marker thread
class MapThread(QThread):
    update_map_signal = pyqtSignal()

    def run(self):
        while True:
            # Your map handling logic here
            
            self.update_map_signal.emit()
            self.msleep(30000)  # Adjust the sleep duration as needed

# Drone data thread
class Battery_Level_Gauge_Thread(QThread):
    update_BatteryLevelGauge_signal = pyqtSignal(int)
    def run(self):
        counter =100
        while True:
            # Your drone data handling logic here
            self.update_BatteryLevelGauge_signal.emit(counter)
            self.msleep(750)  # Adjust the sleep duration as needed
            counter-=5
            if(counter<2):
                counter=100

class Compass_Gauge_Thread(QThread):
    update_compass_signal = pyqtSignal(int)
    def run(self):
        counter =360
        while True:
            # Your drone data handling logic here
            self.update_compass_signal.emit(counter)
            self.msleep(720)  # Adjust the sleep duration as needed
            counter-=1
            if(counter<1):
                counter=360

class Roll_Gauge_Thread(QThread):
    update_Roll_signal = pyqtSignal(int)
    def run(self):
        counter =360
        while True:
            # Your drone data handling logic here
            self.update_Roll_signal.emit(counter)
            self.msleep(720)  # Adjust the sleep duration as needed
            counter-=1
            if(counter<1):
                counter=360

class Pitch_Gauge_Thread(QThread):
    update_Pitch_signal = pyqtSignal(int)
    def run(self):
        counter =360
        while True:
            # Your drone data handling logic here
            self.update_Pitch_signal.emit(counter)
            self.msleep(720)  # Adjust the sleep duration as needed
            counter-=1
            if(counter<1):
                counter=360


class Radar_Thread(QThread):

    update_Radar_signal = pyqtSignal(QPixmap,int)

    def run(self):
        counter=360
        while True:
             
            self.msleep(50)  # Adjust the sleep duration as needed
            counter-=5
            if(counter<1):
                counter=360


                        # Configure plot
            plt.close()
            fig, ax = plt.subplots(figsize=(10.7, 10.7),subplot_kw={'projection': 'polar'})

            # Define data
            theta = 70  # Compass bearing in degrees
            distance = 10
            theta = theta *-1
            theta = 360 - theta - 180 - 90 -90

            # Add data point
            ax.plot(np.radians(theta), distance, marker='s', markersize=15, markerfacecolor='red', zorder=2)

            # Set axis limits and ticks
            ax.set_rmax(12)  # Adjusted the maximum radial limit
            ax.set_rticks([1, 3, 6, 9, 12])
            ax.set_rlabel_position(-22.5)
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)

            # Enable grid and adjust appearance
            ax.grid(True, linestyle='--', alpha=0.7, zorder=0)

            # Set title and labels
            #ax.set_title("Compass Plot with Distance Ticks", va='bottom')
            #ax.set_xlabel('Compass Bearing')
            #ax.set_ylabel('Distance (m)')

            # Set background color to dark green
          
            ax.set_facecolor('darkgreen')
            fig.set_facecolor('#15152e')
            #fig.patch.set_alpha()
            # Initialize FigureCanvas with fig
            canvas = FigureCanvas(fig)
            canvas.draw()
            pixmap = canvas.grab()
            # Your drone data handling logic here
            self.update_Radar_signal.emit(pixmap,counter)
            self.msleep(30)  # Adjust the sleep duration as needed
            
def update_video_frame(self, frame):
    # Update the video frame on the GUI

    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgbFrame = cv2.resize(rgbFrame,(540,540))
    h, w, ch = rgbFrame.shape
    bytesPerLine = ch * w
    convertToQtFormat = QtGui.QImage(rgbFrame.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap(convertToQtFormat)
    self.video_feed_label.setPixmap(pixmap)

def update_radar(self,pixmap,value):
    scene = QGraphicsScene(self)
    pixmap_item = QGraphicsPixmapItem(pixmap)
    scene.addItem(pixmap_item)
    self.Radar_widget.setScene(scene)
    # Optional: Resize the radar_widget to fit the pixmap

        # PROGRESSBAR STYLESHEET BASE
    ###     
        ####   background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:360, stop:0.81 rgba(255, 11, 133, 0), stop:0.83 rgba(255, 0, 0, 255), stop:0.85 rgba(255, 11, 133, 0))
    # End color (position 1)
    styleSheet = """
    border-radius: 412px; 
    background: qconicalgradient(cx:0.5, cy:0.5, angle:0, 
        stop:0.0 rgba(255, 255, 255, 0), 
        stop:0.5 rgba(0, 202, 150, 1), 
        stop:1.0 rgba(0, 200, 57, 0.07));
    """




    # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
    # stop works of 1.000 to 0.000
    #value = 360
    barring = value
    barring = (360 - barring) / 360.0
    barring = barring

    if (value == 360 or value == 0):
        stop_1 = str(.007)
        stop_2 = str(.005)
        stop_3 = str(.001)
    else:
        # GET NEW VALUES
        stop_1 = str(barring-.03)
        stop_2 = str(barring)
        stop_3 = str(barring+.03)
    # SET VALUES TO NEW STYLESHEET
    newStylesheet = styleSheet.replace("{stop1}", stop_1).replace("{stop2}", stop_2).replace("{stop3}", stop_3)
    #print("New Stylesheet:", newStylesheet)
    # APPLY STYLESHEET WITH NEW VALUES
    self.frame_2.setStyleSheet(newStylesheet)

def find_childs(self):
    self.video_feed_label = self.findChild(QLabel, 'RGB_video_feed')
    self.map_viewer = self.findChild(QWebEngineView, 'map')
    self.name_remove_maker = self.findChild(QLineEdit, 'name_remove_maker')
    self.btn_add_marker = self.findChild(QPushButton, 'add_marker_btn')
    self.btn_remove_maker = self.findChild(QPushButton, 'remove_marker_btn')
    self.txt_latitude_input = self.findChild(QLineEdit, 'latitude_input_TextBox')
    self.txt_longitude_input = self.findChild(QLineEdit, 'longitude_input_TextBox')
    self.txt_name_add_marker = self.findChild(QLineEdit, 'name_add_maker')
    self.txt_description_add_marker = self.findChild(QLineEdit, 'description_input_text_box')
    self.Battery_Gauge_widget = self.findChild(QWidget, 'Battery_Gauge_widget')
    self.Compass_Gauge_widget = self.findChild(QWidget, 'Compass_Gauge_widget')
    self.ROLL_Gauge_widget = self.findChild(QWidget, 'Roll_Gauge_widget')
    self.Pitch_Gauge_widget = self.findChild(QWidget, 'PITCH_Gauge_widget')
    self.WeatherAPP_location_widget = self.findChild(QWidget, 'widget_weather')
    self.WeatherAPp_4_location_widget = self.findChild(QWidget, 'widget_weather_4')
    self.Radar_widget = self.findChild(QGraphicsView, 'radar_widget')
 