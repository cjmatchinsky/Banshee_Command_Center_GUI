from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QGraphicsView, QVBoxLayout, QGraphicsScene, QGraphicsPixmapItem, QHBoxLayout, QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import os
import sys
import json
import cv2
import io
import folium
from PyQt5.QtCore import QThread, pyqtSignal
from app_threads import VideoThread, MapThread, Radar_Thread, Compass_Gauge_Thread, Battery_Level_Gauge_Thread, Pitch_Gauge_Thread, Roll_Gauge_Thread, find_childs
from weatherApp import WeatherAPP
from gauges import Pitch_gauge, Roll_gauge, compass_gauge, color_gauge

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        loadUi('ui/GUI_Banshee_Command_Center.ui', self)

        self.setWindowIcon(QIcon('images/Banshee_logo.png'))
        self.setWindowTitle('Banshee Command Center')
        self.setWindowOpacity(0.98)

        find_childs(self)

        self.Radar_widget = self.findChild(QGraphicsView,'radar_widget')
        
        #Initialize widgets
        # Weather app
        self.weather_widget = WeatherAPP()
        # layout_weather_widget = QVBoxLayout(self.WeatherAPP_location_widget)
        # layout_weather_widget.addWidget(self.weather_widget)

        # Weather app 2
        self.weather_widget2 = WeatherAPP()
        # layout_weather_widget2= QVBoxLayout(self.WeatherAPp_4_location_widget)
        # layout_weather_widget2.addWidget(self.weather_widget2)


        # # Set up video thread
        # self.video_thread = VideoThread()
        # self.video_thread.frame_signal.connect(self.update_video_frame)
        # self.video_thread.start()
        self.video_label = QLabel(self) 
        #Open video source
        self.capture = cv2.VideoCapture(0)
        #Start video playback
        self.play()

        # Set up map thread
        # self.map_thread = MapThread()
        # self.map_thread.update_map_signal.connect(self.update_map)
        # self.map_thread.start()
 

        # Set up Battery data thread
        self.BatteryLevelGaugeThread = Battery_Level_Gauge_Thread()
        self.BatteryLevelGaugeThread.update_BatteryLevelGauge_signal.connect(self.update_BatteryLevelGauge)
        self.BatteryLevelGaugeThread.start()

        # Set up Compass data thread
        self.CompassLevelGaugeThread = Compass_Gauge_Thread()
        self.CompassLevelGaugeThread.update_compass_signal.connect(self.update_compassGauge)
        self.CompassLevelGaugeThread.start()
   
        # Set up ROLL thread
        self.RollLevelGaugeThread = Roll_Gauge_Thread()
        self.RollLevelGaugeThread.update_Roll_signal.connect(self.update_rollGauge)
        self.RollLevelGaugeThread.start()

        # Set up Pitch  thread
        self.PitchLevelGaugeThread = Pitch_Gauge_Thread()
        self.PitchLevelGaugeThread.update_Pitch_signal.connect(self.update_PitchGauge)
        self.PitchLevelGaugeThread.start()

        # Set up Radar data thread
        # self.RadarGaugeThread = Radar_Thread()
        # self.RadarGaugeThread.update_Radar_signal.connect(self.update_radar)
        # self.RadarGaugeThread.start()
   

        ## btn setup 
        self.btn_add_marker.pressed.connect(self.add_maker_btn_function)
        self.btn_remove_maker.pressed.connect(self.remove_marker)

        # Create an instance of your Battery progress bar
        self.Battery_color_gauge_w = color_gauge(QMainWindow)
        # Set up the layout and add the Battery progress bar to the widget

        # Create an instance of your compass progress bar
        self.Compass_color_gauge_w = compass_gauge(QMainWindow)
        # Set up the layout and add the compass progress bar to the widget

        # Create an instance of your ROLL progress bar
        self.ROLL_color_gauge_w = Roll_gauge(QMainWindow)
        # Set up the layout and add the ROLL progress bar to the widget

        
        # Create an instance of your Pitch progress bar
        self.Pitch_color_gauge_w = Pitch_gauge(QMainWindow)
        
        # Create the layout
        layout = QGridLayout()

        # Add the video_label to the top-left corner
        layout.addWidget(self.video_label, 0, 0)

        # Add the weather widgets to the top-right corner
        layout.addWidget(self.weather_widget, 0, 2)
        layout.addWidget(self.weather_widget2, 0, 3)

        # Create a layout for the gauges
        gauge_layout = QHBoxLayout()
        gauge_layout.addWidget(self.ROLL_color_gauge_w)
        gauge_layout.addWidget(self.Pitch_color_gauge_w)
        gauge_layout.addWidget(self.Compass_color_gauge_w)
        gauge_layout.addWidget(self.Battery_color_gauge_w)

        # Add the gauge layout to the bottom row
        layout.addLayout(gauge_layout, 2, 0, 1, 4)

        # Set the layout on the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)


        
    # def update_video_frame(self, frame):
    #     # Update the video frame on the GUI
 
    #     rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     rgbFrame = cv2.resize(rgbFrame,(1080,1080))
    #     h, w, ch = rgbFrame.shape
    #     bytesPerLine = ch * w
    #     convertToQtFormat = QtGui.QImage(rgbFrame.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
    #     pixmap = QtGui.QPixmap(convertToQtFormat)
    #     self.video_feed_label.setPixmap(pixmap)
    def play(self):
            # Read the next video frame
            ret, frame = self.capture.read()

            if ret:
                # Convert the frame to RGB format
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Create a QImage from the resized frame
                image = QImage(
                    frame_rgb.data, #RGB image values
                    frame_rgb.shape[1], #Width
                    frame_rgb.shape[0], #Height
                    QImage.Format_RGB888
                )
                        # Create a QPixmap from the QImage
            pixmap = QPixmap.fromImage(image)

            # Set the QPixmap as the image in the QLabel
            self.video_label.setPixmap(pixmap)
            self.video_label.setScaledContents(True)

            # Call the play method again after 15 milliseconds (change the delay as needed)
            QTimer.singleShot(15, self.play)
    def update_radar(self,pixmap,value):
        try:
            scene = QGraphicsScene()
            pixmap_item = QGraphicsPixmapItem(pixmap)
            scene.addItem(pixmap_item)
            self.Radar_widget.setScene(scene)
        except Exception as e:
            print(f"Error updating radar: {e}")
        # Optional: Resize the radar_widget to fit the pixmap

            # PROGRESSBAR STYLESHEET BASE
        ###     
            ####   background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:360, stop:0.81 rgba(255, 11, 133, 0), stop:0.83 rgba(255, 0, 0, 255), stop:0.85 rgba(255, 11, 133, 0))
        styleSheet = """
        QFrame{
            border-radius: 412px; 
            background-color:
            qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:{stop1} rgba(255, 255, 255, 0), stop:{stop2} rgba(0, 202, 150, 255), stop:{stop3} rgba(0, 200,57, 7));
        }
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

    def update_map(self):
        # Update the map on the GUI
        # Your map update logic here
        # Load data from the JSON file into a dictionary
        self.bcc_map = folium.Map(location=(34,-117), zoom_start=8 )
        json_file_path = 'coordinate_markers.json'
        with open(json_file_path, 'r') as json_file:
            coordinate_markers = json.load(json_file)
        for key, value in coordinate_markers.items():
            name = key
            temp_latitude,temp_longitude = coordinate_markers[key]['location']
            temp_description = coordinate_markers[key]['description']
            temp_marker_coordinate = (float(temp_latitude), float(temp_longitude))
            temp_description =  temp_description
            temp_name = name
            # Adding a marker with a popup (description) and a tooltip (name)
            folium.Marker(location=temp_marker_coordinate, popup=temp_description, tooltip=temp_name).add_to(self.bcc_map)

        data = io.BytesIO()
        self.bcc_map.save(data, close_file=False)
        self.map_viewer.setHtml(data.getvalue().decode())
        

    def update_BatteryLevelGauge(self,data):
        self.Battery_color_gauge_w.progressBarValue(data)
            

    def update_compassGauge(self,data):
        self.Compass_color_gauge_w.progressBarValue(data)
            
    def update_rollGauge(self,data):
        self.Compass_color_gauge_w.progressBarValue(data)

 
    def update_PitchGauge(self,data):
        #self.Pitch_color_gauge_w.progressBarValue(data)
        pass


    def add_maker_btn_function(self):
        json_file_path = 'coordinate_markers.json'

        if not os.path.isfile(json_file_path):
            # File doesn't exist, create it with an empty dictionary
            with open(json_file_path, 'w') as json_file:
                json.dump({}, json_file)

        # The rest of your code can proceed with reading and updating the JSON file
        
        #self.txt_latitude_input = self.findChild(QLineEdit,'latitude_input_TextBox')
        #self.txt_longitude_input = self.findChild(QLineEdit,'longitude_input_TextBox')
        #self.txt_name_add_marker = self.findChild(QLineEdit, 'name_add_maker_btn_fuction')
        #self.txt_description_add_marker = self.findChild(QTextEdit, 'description_add_marker')
        temp_name = self.txt_name_add_marker.text()
        temp_description = self.txt_description_add_marker.text()
        temp_latitude = self.txt_latitude_input.text()
        temp_longitude = self.txt_longitude_input.text()
        try:
            temp_marker_coordinate = (float(temp_latitude),float(temp_longitude))
            temp_description= str(temp_marker_coordinate) +" - " +temp_description
            print('IN TRY')
                        
            # Open the JSON file in read mode
            with open(json_file_path, 'r') as json_file:
                # Load the JSON data into a dictionary
                coordinate_markers = json.load(json_file)

            # Add new markers to the dictionary
            coordinate_markers[temp_name] = {'location': (temp_latitude, temp_longitude), 'description': temp_description}
            #coordinate_markers['Name4'] = {'location': (10, 40), 'description': 'This is marker 4'}

            # Open the JSON file in write mode
            with open(json_file_path, 'w') as json_file:
                # Dump the updated dictionary to the JSON file
                json.dump(coordinate_markers, json_file, indent=2)

            #folium.Marker(location=temp_marker_coordinate, popup=temp_description, tooltip=temp_name).add_to(self.bcc_map)
            #self.update_map()
            #data = io.BytesIO()
            #self.bcc_map.save(data, close_file=False)
            #self.map_viewer.setHtml(data.getvalue().decode())

            self.txt_latitude_input.clear()
            self.txt_longitude_input.clear() 
            self.txt_name_add_marker.clear()
            self.txt_description_add_marker.clear()
        except Exception as e:
            print(f'Error: {e}')
            print('Error - Clearing Text Input Dialog... ')
            self.txt_latitude_input.clear()
            self.txt_longitude_input.clear()
            self.txt_name_add_marker.clear()
            self.txt_description_add_marker.clear()

    def remove_marker(self):
        json_file_path = 'coordinate_markers.json'

        with open(json_file_path, 'r') as json_file:
            coordinate_markers = json.load(json_file)

        temp_removal_name = self.name_remove_maker.text()
        if temp_removal_name in coordinate_markers:
            del coordinate_markers[str(temp_removal_name)]
        else:
            print(f'ERROR - No waypoint named: {temp_removal_name}')
            # Open the JSON file in write mode
        with open(json_file_path, 'w') as json_file:
            # Dump the updated dictionary to the JSON file
            json.dump(coordinate_markers, json_file, indent=2)

        self.name_remove_maker.clear()

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
