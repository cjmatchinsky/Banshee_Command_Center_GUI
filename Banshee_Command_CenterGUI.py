
from PyQt5.QtCore import Qt , QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import PIL.Image as Image
import re
import os
import sys
import json
import requests  
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import folium
import streamlit 
import os
from streamlit_folium import st_folium
import math
import io, folium
import cv2
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np





#### start up weather APP

def get_forecast_weather(api_key, lat, lon,weather_data):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": "{},{}".format(lat, lon),
        "days": 4,  # You can adjust the number of forecast days as needed
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_data['maxtemp_f'] = data["forecast"]["forecastday"][0]['day']['maxtemp_f']
            weather_data['mintemp_f'] = data["forecast"]["forecastday"][0]['day']['mintemp_f']
            weather_data['chance_of_rain'] = data["forecast"]["forecastday"][0]['day']['daily_chance_of_rain']
            weather_data['chance_of_snow'] = data["forecast"]["forecastday"][0]['day']['daily_chance_of_snow']
            weather_data['sunrise_time'] = data["forecast"]["forecastday"][0]['astro']['sunrise']
            weather_data['sunset_time'] = data["forecast"]["forecastday"][0]['astro']['sunset']


            weather_data['OneDayOUT']['date'] = data["forecast"]["forecastday"][1]['date']
            weather_data['OneDayOUT']['maxtemp_f'] = data["forecast"]["forecastday"][1]['day']['maxtemp_f']
            weather_data['OneDayOUT']['mintemp_f'] = data["forecast"]["forecastday"][1]['day']['mintemp_f']
            weather_data['OneDayOUT']['chance_of_rain'] = data["forecast"]["forecastday"][1]['day']['daily_chance_of_rain']
            weather_data['OneDayOUT']['chance_of_snow'] = data["forecast"]["forecastday"][1]['day']['daily_chance_of_snow']
            weather_data['OneDayOUT']['maxwind_mph'] = data["forecast"]["forecastday"][1]['day']['maxwind_mph']
            weather_data['OneDayOUT']['avgvis_miles'] = data["forecast"]["forecastday"][1]['day']['avgvis_miles']
            weather_data['OneDayOUT']['condition_msg'] = data["forecast"]["forecastday"][1]['day']['condition']['text']
            icon = data["forecast"]["forecastday"][1]['day']['condition']['icon']
            weather_data['OneDayOUT']['icon_URL'] = 'http:'+icon

            #print(self.weather_data['OneDayOUT']['date'])

            weather_data['TwoDayOUT']['date'] = data["forecast"]["forecastday"][2]['date']
            weather_data['TwoDayOUT']['maxtemp_f'] = data["forecast"]["forecastday"][2]['day']['maxtemp_f']
            weather_data['TwoDayOUT']['mintemp_f'] = data["forecast"]["forecastday"][2]['day']['mintemp_f']
            weather_data['TwoDayOUT']['chance_of_rain'] = data["forecast"]["forecastday"][2]['day']['daily_chance_of_rain']
            weather_data['TwoDayOUT']['chance_of_snow'] = data["forecast"]["forecastday"][2]['day']['daily_chance_of_snow']
            weather_data['TwoDayOUT']['maxwind_mph'] = data["forecast"]["forecastday"][2]['day']['maxwind_mph']
            weather_data['TwoDayOUT']['avgvis_miles'] = data["forecast"]["forecastday"][2]['day']['avgvis_miles']
            weather_data['TwoDayOUT']['condition_msg'] = data["forecast"]["forecastday"][2]['day']['condition']['text']
            icon = data["forecast"]["forecastday"][2]['day']['condition']['icon']
            weather_data['TwoDayOUT']['icon_URL'] = 'http:'+icon

            #print(self.weather_data['TwoDayOUT']['date'])

            weather_data['ThreeDayOUT']['date'] = data["forecast"]["forecastday"][3]['date']
            weather_data['ThreeDayOUT']['maxtemp_f'] = data["forecast"]["forecastday"][3]['day']['maxtemp_f']
            weather_data['ThreeDayOUT']['mintemp_f'] = data["forecast"]["forecastday"][3]['day']['mintemp_f']
            weather_data['ThreeDayOUT']['chance_of_rain'] = data["forecast"]["forecastday"][3]['day']['daily_chance_of_rain']
            weather_data['ThreeDayOUT']['chance_of_snow'] = data["forecast"]["forecastday"][3]['day']['daily_chance_of_snow']
            weather_data['ThreeDayOUT']['maxwind_mph'] = data["forecast"]["forecastday"][3]['day']['maxwind_mph']
            weather_data['ThreeDayOUT']['avgvis_miles'] = data["forecast"]["forecastday"][3]['day']['avgvis_miles']
            weather_data['ThreeDayOUT']['condition_msg'] = data["forecast"]["forecastday"][3]['day']['condition']['text']
            icon = data["forecast"]["forecastday"][3]['day']['condition']['icon']
            weather_data['ThreeDayOUT']['icon_URL'] = 'http:'+icon

            #print(self.weather_data['ThreeDayOUT']['date'])
 
        else:
            print("Failed to get current weather data. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)



def get_current_weather(api_key, lat, lon, weather_data):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "{},{}".format(lat, lon),
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:

            weather_data['city'] = data["location"]["name"]
            weather_data['state'] = data["location"]["region"]
            weather_data['latitude'] = data["location"]["lat"]
            weather_data['longitude'] = data["location"]["lon"]

            weather_data['updated_time'] = data["current"]["last_updated"]
            weather_data['temp_f']  = data["current"]["temp_f"]
            weather_data['night_or_day']  = data["current"]["is_day"]

            weather_data['condition_msg']  = data["current"]["condition"]["text"]
            icon = data["current"]["condition"]["icon"]
            weather_data['icon_URL'] = 'http:'+icon

            weather_data['wind_mph'] = data["current"]["wind_mph"]
            weather_data['wind_dir'] = data["current"]["wind_dir"]
            weather_data['pressure_mb'] = data["current"]["pressure_mb"]
            weather_data['precip_mm'] = data["current"]["precip_mm"]
            weather_data['humidity'] = data["current"]["humidity"]
            weather_data['cloud_cover'] = data["current"]["cloud"]
            weather_data['feelslikeTEMp_f'] = data["current"]["feelslike_f"]
            weather_data['visibilty_miles'] = data["current"]["vis_miles"]
            weather_data['uv_index'] = data["current"]["uv"]
            weather_data['gust_mph'] = data["current"]["gust_mph"]



        else:
            print("Failed to get current weather data. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", e)


def get_weather_info(latitude, longitude ,weather_data):
    api_key = " "
    get_current_weather(api_key, latitude, longitude ,weather_data)
    get_forecast_weather(api_key, latitude, longitude ,weather_data)
 
    print(weather_data)
 
class WeatherAPP(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        uic.loadUi('weatherAPP_ui.ui', self)
        
        self.setWindowIcon(QIcon('Banshee_logo.png'))
        self.setWindowTitle('Banshee Command Center')
        self.setWindowOpacity(0.98)
    
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

             # Initialize variables for handling window dragging
        self.draggable = False
        self.offset = QPoint()

        self.application()

    def mousePressEvent(self, event):
        # Capture the initial position when the mouse is pressed
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        # Move the window if draggable
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        # Reset draggable state when the mouse is released
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def application(self):
 
        self.location_data = ["45.09, -92.59", "34.05, -117.82"]
        self.weather_data = {
            'city': None,
            'state'  : None,
            'latitude' : None,
            'longitude' : None,
            'updated_time': None,
            'temp_f'  : None,
            'night_or_day' : None,
            'condition_msg' : None,
            'icon_URL' : None,
            'wind_mph' : None,
            'wind_dir': None,
            'pressure_mb' : None,
            'precip_mm': None,
            'humidity' : None,
            'cloud_cover' : None,
            'feelslikeTEMp_f' : None,
            'visibilty_miles' : None,
            'uv_index' : None,
            'gust_mph' : None,
            'maxtemp_f' : None,
            'mintemp_f' : None,
            'chance_of_rain' : None,
            'chance_of_snow': None,
            'sunrise_time': None,
            'sunset_time' : None,
            'current_snow_or_rain_chance_value': None,
            'current_snow_or_rain_chance_text' : None,
            'OneDayOUT': {},
            'TwoDayOUT': {},
            'ThreeDayOUT': {}
        }
        
 

        self.exit_btn = self.findChild(QPushButton,'exit_btn')
        self.clear_btn = self.findChild(QPushButton,'clear_btn')
        self.clear_btn.pressed.connect(self.clear_text_function)
        self.exit_btn.pressed.connect(self.exit_function)
        
        self.combo_box = self.findChild(QComboBox, "comboBox")  # Find the combo box
        self.combo_box.addItems(self.location_data)
        self.combo_box.currentIndexChanged.connect(self.current_selection_function)


        self.current_snow_or_rain_chance_value_txt = self.findChild(QLabel,'current_snow_or_rain_chance_value_txt')
        self.current_temp_value_txt = self.findChild(QLabel,'current_temp_value_txt')
        self.current_image_png = self.findChild(QLabel,'current_image_png')
        self.current_change_of_rainORsnow_txt = self.findChild(QLabel,'current_change_of_rainORsnow_txt')
        self.current_wind_speed_value_txt = self.findChild(QLabel,'current_wind_speed_value_txt')
        self.current_max_temp_value_txt = self.findChild(QLabel,'current_max_temp_value_txt')
        self.current_min_temp_value_txt = self.findChild(QLabel,'current_min_temp_value_txt')
        self.current_pressure_value_txt = self.findChild(QLabel,'current_pressure_value_txt')
        self.Current_Amount_rainORsnow_txt = self.findChild(QLabel,'Current_Amount_rainORsnow_txt')
        self.current_snow_or_rain_amount_value_txt = self.findChild(QLabel,'current_snow_or_rain_amount_value_txt')
        self.current_condition_alert_value_txt = self.findChild(QLabel,'current_condition_alert_value_txt')
        self.current_humidity_percentage_value_txt = self.findChild(QLabel,'current_humidity_percentage_value_txt')
        self.current_cloud_cover_percentage_value_txt = self.findChild(QLabel,'current_cloud_cover_percentage_value_txt')
        self.current_feels_like_value_txt = self.findChild(QLabel,'current_feels_like_value_txt')
        self.current_vis_value_txt = self.findChild(QLabel,'current_vis_value_txt')
        self.current_uv_value_txt = self.findChild(QLabel,'current_uv_value_txt')
        self.current_gusts_speed_value_txt = self.findChild(QLabel,'current_gusts_speed_value_txt')
        self.city_value_txt = self.findChild(QLabel,'city_value_txt')
        self.state_value_txt = self.findChild(QLabel,'state_value_txt')
        self.lat_and_lon_value_txt = self.findChild(QLabel,'lat_and_lon_value_txt')
        self.OneDayOut_image_png = self.findChild(QLabel,'OneDayOut_image_png')
        self.ThreeDayOut_image_png = self.findChild(QLabel,'ThreeDayOut_image_png')
        self.TwoDayOut_image_png = self.findChild(QLabel,'TwoDayOut_image_png')
        self.Current_Date_value_txt = self.findChild(QLabel,'Current_Date_value_txt')
        self.OneDayOut_Date_value_txt = self.findChild(QLabel,'OneDayOut_Date_value_txt')
        self.TwoDayOut_Date_value_txt = self.findChild(QLabel,'TwoDayOut_Date_value_txt')
        self.ThreeDayOut_Date_value_txt = self.findChild(QLabel,'ThreeDayOut_Date_value_txt')
        self.current_sunrise_value_txt = self.findChild(QLabel,'current_sunrise_value_txt')
        self.current_sunset_value_txt = self.findChild(QLabel,'current_sunset_value_txt')
        self.OneDayOut_minTEMP_value_txt = self.findChild(QLabel,'OneDayOut_minTEMP_value_txt')
        self.OneDayOut_maxTEMP_value_txt = self.findChild(QLabel,'OneDayOut_maxTEMP_value_txt')
        self.TwoDayOut_maxTEMP_value_txt = self.findChild(QLabel,'TwoDayOut_maxTEMP_value_txt')
        self.TwoDayOut_minTEMP_value_txt = self.findChild(QLabel,'TwoDayOut_minTEMP_value_txt')
        self.ThreeDayOut_maxTEMP_value_txt = self.findChild(QLabel,'ThreeDayOut_maxTEMP_value_txt')
        self.ThreeDayOut_minTEMP_value_txt = self.findChild(QLabel,'ThreeDayOut_minTEMP_value_txt')
        self.OneDayOut_wind_speed_value_txt = self.findChild(QLabel,'OneDayOut_wind_speed_value_txt')
        self.OneDayOut_change_of_rainORsnow_txt = self.findChild(QLabel,'OneDayOut_change_of_rainORsnow_txt')
        self.OneDayOut_snow_or_rain_chance_value_txt = self.findChild(QLabel,'OneDayOut_snow_or_rain_chance_value_txt')
        self.OneDayOut_vis_value_txt = self.findChild(QLabel,'OneDayOut_vis_value_txt')
        self.OneDayOut_condition_alert_value_txt = self.findChild(QLabel,'OneDayOut_condition_alert_value_txt')
        self.TwoDayOut_vis_value_txt = self.findChild(QLabel,'TwoDayOut_vis_value_txt')
        self.TwoDayOut_condition_alert_value_txt = self.findChild(QLabel,'TwoDayOut_condition_alert_value_txt')
        self.TwoDayOut_wind_speed_value_txt = self.findChild(QLabel,'TwoDayOut_wind_speed_value_txt')
        self.TwoDayOut_snow_or_rain_chance_value_txt = self.findChild(QLabel,'TwoDayOut_snow_or_rain_chance_value_txt')
        self.TwoDayOut_change_of_rainORsnow_txt = self.findChild(QLabel,'TwoDayOut_change_of_rainORsnow_txt')
        self.ThreeDayOut_wind_speed_value_txt = self.findChild(QLabel,'ThreeDayOut_wind_speed_value_txt')
        self.ThreeDayOut_condition_alert_value_txt = self.findChild(QLabel,'ThreeDayOut_condition_alert_value_txt')
        self.ThreeDayOut_snow_or_rain_chance_value_txt = self.findChild(QLabel,'ThreeDayOut_snow_or_rain_chance_value_txt')
        self.ThreeDayOut_vis_value_txt = self.findChild(QLabel,'ThreeDayOut_vis_value_txt')
        self.ThreeDayOut_change_of_rainORsnow_txt = self.findChild(QLabel,'ThreeDayOut_change_of_rainORsnow_txt')
        self.updated_time_txt = self.findChild(QLabel,'updated_time')
        
    def update_weather_data(self):
        
        image_download(self.weather_data['icon_URL'],0)
        image_download(self.weather_data['OneDayOUT']['icon_URL'],1)
        image_download(self.weather_data['TwoDayOUT']['icon_URL'],2)
        image_download(self.weather_data['ThreeDayOUT']['icon_URL'],3)

        

        weather_icon_pixmap0 = QPixmap('weather_icon_images/temp_weatherICON0.png')
        self.weather_data['icon_URL'] = weather_icon_pixmap0

        weather_icon_pixmap1 = QPixmap('weather_icon_images/temp_weatherICON1.png')
        self.weather_data['OneDayOUT']['icon_URL'] = weather_icon_pixmap1
        
        weather_icon_pixmap2 = QPixmap('weather_icon_images/temp_weatherICON2.png')
        self.weather_data['TwoDayOUT']['icon_URL'] = weather_icon_pixmap2

        weather_icon_pixmap3 = QPixmap('weather_icon_images/temp_weatherICON3.png')
        self.weather_data['ThreeDayOUT']['icon_URL'] = weather_icon_pixmap3

        todays_date_temp  = subtract_one_day(format_date(str(self.weather_data['OneDayOUT']['date'])))
        todays_date  = get_day_of_week(str(todays_date_temp)) +' - '+ str(todays_date_temp)

        self.weather_data['OneDayOUT']['date'] = get_day_of_week(format_date(str(self.weather_data['OneDayOUT']['date'])))
        self.weather_data['TwoDayOUT']['date'] = get_day_of_week(format_date(str(self.weather_data['TwoDayOUT']['date'])))
        self.weather_data['ThreeDayOUT']['date'] = get_day_of_week(format_date(str(self.weather_data['ThreeDayOUT']['date'])))

        #self.weather_data['current_snow_or_rain_chance_value'], self.weather_data['current_snow_or_rain_chance_text'] =  self.snowORrain_function(20,65, 'Rain', 'Snow')

        self.weather_data['current_snow_or_rain_chance_value'], self.weather_data['current_snow_or_rain_chance_text'] =  self.snowORrain_function(self.weather_data['chance_of_rain'], self.weather_data['chance_of_snow'], 'Rain', 'Snow')
        self.weather_data['OneDayOUT']['current_snow_or_rain_chance_value'], self.weather_data['OneDayOUT']['current_snow_or_rain_chance_text'] =  self.snowORrain_function(self.weather_data['OneDayOUT']['chance_of_rain'], self.weather_data['OneDayOUT']['chance_of_snow'], 'Rain', 'Snow')
        self.weather_data['TwoDayOUT']['current_snow_or_rain_chance_value'], self.weather_data['TwoDayOUT']['current_snow_or_rain_chance_text'] =  self.snowORrain_function(self.weather_data['TwoDayOUT']['chance_of_rain'], self.weather_data['TwoDayOUT']['chance_of_snow'], 'Rain', 'Snow')
        self.weather_data['ThreeDayOUT']['current_snow_or_rain_chance_value'], self.weather_data['ThreeDayOUT']['current_snow_or_rain_chance_text'] =  self.snowORrain_function(self.weather_data['ThreeDayOUT']['chance_of_rain'], self.weather_data['ThreeDayOUT']['chance_of_snow'], 'Rain', 'Snow')



        self.city_value_txt.setText(str(self.weather_data['city'])) 
        self.state_value_txt.setText(str(self.weather_data['state'])) 
        self.lat_and_lon_value_txt.setText(str(self.weather_data['latitude']) +',  '+ str(self.weather_data['longitude']))


        self.updated_time_txt.setText(str(self.weather_data['updated_time'])) 
        self.current_snow_or_rain_chance_value_txt.setText(str(self.weather_data['current_snow_or_rain_chance_value']))
        self.current_temp_value_txt.setText(str(self.weather_data['temp_f'])) 
        self.current_image_png.setPixmap((self.weather_data['icon_URL'])) 
        self.current_change_of_rainORsnow_txt.setText(str(self.weather_data['current_snow_or_rain_chance_text'] + ':')) 
        self.current_wind_speed_value_txt.setText(str(self.weather_data['wind_mph'])+' '+ (self.weather_data['wind_dir']))  
        self.current_max_temp_value_txt.setText(str(self.weather_data['maxtemp_f']))  
        self.current_min_temp_value_txt.setText(str(self.weather_data['mintemp_f'])) 
        self.current_pressure_value_txt.setText(str(self.weather_data['pressure_mb']))  
        self.current_snow_or_rain_amount_value_txt.setText(str(self.weather_data['precip_mm']))
        self.Current_Amount_rainORsnow_txt.setText(str(self.weather_data['current_snow_or_rain_chance_text'] + ':') ) 
        self.current_condition_alert_value_txt.setText(str(self.weather_data['condition_msg']))  
        self.current_humidity_percentage_value_txt.setText(str(self.weather_data['humidity']))  
        self.current_cloud_cover_percentage_value_txt.setText(str(self.weather_data['cloud_cover']))  
        self.current_feels_like_value_txt.setText(str(self.weather_data['feelslikeTEMp_f']))  
        self.current_vis_value_txt.setText(str(self.weather_data['visibilty_miles'])) 
        self.current_uv_value_txt.setText(str(self.weather_data['uv_index']))  
        self.current_gusts_speed_value_txt.setText(str(self.weather_data['gust_mph']))  
        self.current_sunrise_value_txt.setText(str(self.weather_data['sunrise_time']))  
        self.current_sunset_value_txt.setText(str(self.weather_data['sunset_time'])) 
        self.Current_Date_value_txt.setText(str(todays_date))  
                  

        self.OneDayOut_maxTEMP_value_txt.setText(str(self.weather_data['OneDayOUT']['maxtemp_f']))  
        self.OneDayOut_minTEMP_value_txt.setText(str(self.weather_data['OneDayOUT']['mintemp_f']))    
        self.OneDayOut_wind_speed_value_txt.setText(str(self.weather_data['OneDayOUT']['maxwind_mph']))  
        self.OneDayOut_condition_alert_value_txt.setText(str(self.weather_data['OneDayOUT']['condition_msg']))  
        self.OneDayOut_snow_or_rain_chance_value_txt.setText(str(self.weather_data['OneDayOUT']['current_snow_or_rain_chance_value']))  
        self.OneDayOut_vis_value_txt.setText(str(self.weather_data['OneDayOUT']['avgvis_miles'])) 
        self.OneDayOut_change_of_rainORsnow_txt.setText(str(self.weather_data['OneDayOUT']['current_snow_or_rain_chance_text'] + ':'))
        self.OneDayOut_Date_value_txt.setText(str(self.weather_data['OneDayOUT']['date']))   
        self.OneDayOut_image_png.setPixmap((self.weather_data['OneDayOUT']['icon_URL'])) 

        self.TwoDayOut_maxTEMP_value_txt.setText(str(self.weather_data['TwoDayOUT']['maxtemp_f']))  
        self.TwoDayOut_minTEMP_value_txt.setText(str(self.weather_data['TwoDayOUT']['mintemp_f']))    
        self.TwoDayOut_wind_speed_value_txt.setText(str(self.weather_data['TwoDayOUT']['maxwind_mph']))  
        self.TwoDayOut_condition_alert_value_txt.setText(str(self.weather_data['TwoDayOUT']['condition_msg']))  
        self.TwoDayOut_snow_or_rain_chance_value_txt.setText(str(str(self.weather_data['TwoDayOUT']['current_snow_or_rain_chance_value'])))  
        self.TwoDayOut_vis_value_txt.setText(str(self.weather_data['TwoDayOUT']['avgvis_miles'])) 
        self.TwoDayOut_change_of_rainORsnow_txt.setText(str(self.weather_data['TwoDayOUT']['current_snow_or_rain_chance_text'] + ':'))
        self.TwoDayOut_Date_value_txt.setText(str(self.weather_data['TwoDayOUT']['date']))   
        self.TwoDayOut_image_png.setPixmap((self.weather_data['TwoDayOUT']['icon_URL'])) 

        self.ThreeDayOut_maxTEMP_value_txt.setText(str(self.weather_data['ThreeDayOUT']['maxtemp_f']))  
        self.ThreeDayOut_minTEMP_value_txt.setText(str(self.weather_data['ThreeDayOUT']['mintemp_f']))    
        self.ThreeDayOut_wind_speed_value_txt.setText(str(self.weather_data['ThreeDayOUT']['maxwind_mph']))  
        self.ThreeDayOut_condition_alert_value_txt.setText(str(self.weather_data['ThreeDayOUT']['condition_msg']))  
        self.ThreeDayOut_snow_or_rain_chance_value_txt.setText(str(self.weather_data['OneDayOUT']['current_snow_or_rain_chance_value']))  
        self.ThreeDayOut_vis_value_txt.setText(str(self.weather_data['ThreeDayOUT']['avgvis_miles'])) 
        self.ThreeDayOut_change_of_rainORsnow_txt.setText(str(self.weather_data['ThreeDayOUT']['current_snow_or_rain_chance_text'] + ':'))
        self.ThreeDayOut_Date_value_txt.setText(str(self.weather_data['ThreeDayOUT']['date']))   
        self.ThreeDayOut_image_png.setPixmap((self.weather_data['ThreeDayOUT']['icon_URL'])) 
         

    def add_text_to_combobox(self):
        new_text = self.combo_box.currentText()
        parts = new_text.split(', ')

        # Check if there are exactly two parts and both are integers
        if (coordinate_validations(new_text)):
            if new_text not in self.location_data:
                self.location_data.append(new_text)
                self.clear_text_function()

                # Extract latitude and longitude
                latitude, longitude = parts[0], parts[1]

                # Assuming get_weather_info and update_weather_data are functions in your class
                get_weather_info(latitude, longitude, self.weather_data)
                self.update_weather_data()
        else:
            # If the conditions are not met, connect the signal to the appropriate slot
            print("ERROR1")


    def current_selection_function(self):
        print(self.combo_box.currentText())
        text = self.combo_box.currentText()
        temp = text.split(', ')
        latitude = temp[0]
        longitude = temp[1]
        get_weather_info(latitude, longitude, self.weather_data)
        self.update_weather_data()

    def clear_text_function(self):
        self.combo_box.clearEditText()

    def exit_function(self):
        #QApplication.quit()
        pass
 

    def snowORrain_function( self,input_rain_value, input_snow_value, rain_txt, snow_txt):
        
        temp_array = [str(input_rain_value) +"_"+str(rain_txt), str(input_snow_value) +"_"+str(snow_txt)]
        temp_array.sort()
        if(input_rain_value==input_snow_value):
            temp_array = [str(input_snow_value) +"_"+str(snow_txt) , str(input_rain_value) +"_"+str(rain_txt)]
        return temp_array[1].split('_')


def format_date(input_date):
    date_obj = datetime.strptime(input_date, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%m/%d/%Y")
    return formatted_date

def get_day_of_week(input_date):
    date_obj = datetime.strptime(input_date, "%m/%d/%Y")
    day_of_week = date_obj.strftime("%A")
    return day_of_week

def subtract_one_day(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    previous_day = date_obj - timedelta(days=1)
    formatted_date = previous_day.strftime("%m/%d/%Y")
    return formatted_date
 

def image_download(URL_input, number):
  image_url = URL_input
  temp_weather_icon_path = f"weather_icon_images/temp_weatherICON{number}.png"

  # Send a GET request to the URL
  response = requests.get(image_url, stream=True)

  # Check if the request was successful (status code 200)
  if response.status_code == 200:
      # Open a local file with write-binary mode
      with open(temp_weather_icon_path, 'wb') as file:
          # Iterate over the content in chunks and write to the file
          for chunk in response.iter_content(chunk_size=128):
              file.write(chunk)

      #print(f"Image downloaded successfully as {temp_weather_icon_path}")
  else:
      print(f"Failed to download image. Status code: {response.status_code}")

def coordinate_validations(input_coordinate):
    temp = input_coordinate
    # Regular expression to match two floats separated by a comma and a space
    pattern = r'^[-+]?\d+\.\d+, ?[-+]?\d+\.\d+$'
    # Check if the string matches the pattern
    match = re.match(pattern, temp)
    if match:
        print("Valid coordinates string")
        return True
    else:
        print("Invalid coordinates string")
        return False
 
#### END up weather APP

 

class Pitch_gauge(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        
        # Load the UI file
        self.ui =loadUi('color_gauge_Pitch.ui', self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.progressBarValue(0)
   
        #self.show()
        
                 
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        ###     
        styleSheet = """
        QFrame{
        border-radius: 150px;
	    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:4, stop:{stop1} rgba(255, 255, 255, 0), stop:{stop2} rgba{color_roll}, stop:{stop3} rgba(255, 255, 255, 0), stop:{stop4} rgba(249, 249, 249, 0), stop:{stop5} rgba{color_roll}, stop:{stop6} rgba(236, 236, 236, 0));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        #value = 360           -100%  0   100 % 

        barring = arduino_map(value,-100,100,.001, .999)

        percentage_color = abs(value)

        # Calculate RGB values based on the percentage
        green = int(255 * (50 - percentage_color) / 50)
        red = int(255 * percentage_color / 50)
        blue = 0

        # Set the background color of the widget
        new_color = (red, green, blue,254)

        # GET NEW VALUES
        stop_1 = str(barring-.03)
        stop_2 = str(barring)
        stop_3 = str(barring+.03+17)
        stop_4 = str(barring-.03 +.27)
        stop_5 = str(barring +.50)
        stop_6 = str(barring+.03 +.50)
        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{stop1}", stop_1).replace("{stop2}", stop_2).replace("{stop3}", stop_3).replace("{stop4}", stop_4).replace("{stop5}", stop_5).replace("{stop6}", stop_6).replace("{color_roll}",str(new_color))
        #print("New Stylesheet:", newStylesheet)
        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circle_Progess.setStyleSheet(newStylesheet)

        self.label_precentage = self.findChild(QLabel,'label_precentage')
        self.label_precentage.setText(str(round(value,1)) )




class Roll_gauge(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        
        # Load the UI file
        self.ui =loadUi('color_gauge_ROL.ui', self)

         

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.progressBarValue(-5)
   
        #self.show()
        
                 
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        ###     
        styleSheet = """
        QFrame{
        border-radius: 150px;
	    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:4, stop:{stop1} rgba(255, 255, 255, 0), stop:{stop2} rgba{color_roll}, stop:{stop3} rgba(255, 255, 255, 0), stop:{stop4} rgba(249, 249, 249, 0), stop:{stop5} rgba{color_roll}, stop:{stop6} rgba(236, 236, 236, 0));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        #value = 360        -100%  0   100 % 

        barring = arduino_map(value,-100,100,.001, .999)

        percentage_color = abs(value)

        # Calculate RGB values based on the percentage
        green = int(255 * (50 - percentage_color) / 50)
        red = int(255 * percentage_color / 50)
        blue = 0

        # Set the background color of the widget
        new_color = (red, green, blue,254)

        # GET NEW VALUES
        stop_1 = str(barring-.03)
        stop_2 = str(barring)
        stop_3 = str(barring+.03+17)
        stop_4 = str(barring-.03 +.27)
        stop_5 = str(barring +.50)
        stop_6 = str(barring+.03 +.50)
        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{stop1}", stop_1).replace("{stop2}", stop_2).replace("{stop3}", stop_3).replace("{stop4}", stop_4).replace("{stop5}", stop_5).replace("{stop6}", stop_6).replace("{color_roll}",str(new_color))
        #print("New Stylesheet:", newStylesheet)
        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circle_Progess.setStyleSheet(newStylesheet)

        self.label_precentage = self.findChild(QLabel,'label_precentage')
        self.label_precentage.setText(str(round(value,1)) )



class compass_gauge(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        
        # Load the UI file
        self.ui =loadUi('color_gauge__compass.ui', self)

         

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.progressBarValue(270)
   
        #self.show()
        
                 
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        ###     
            ####   background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:360, stop:0.81 rgba(255, 11, 133, 0), stop:0.83 rgba(255, 0, 0, 255), stop:0.85 rgba(255, 11, 133, 0))
        styleSheet = """
        QFrame{
        	border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255,11,133,0), stop:{STOP_2} rgba(255, 0, 0, 255), stop:{STOP_3} rgba(255,11,133,0));
            
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
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{STOP_3}", stop_3)
        #print("New Stylesheet:", newStylesheet)
        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circle_Progess.setStyleSheet(newStylesheet)

        self.label_precentage = self.findChild(QLabel,'label_precentage')
        self.label_precentage.setText(str(round(value,0)) )



class color_gauge(QMainWindow):
    def __init__(self, parent: QMainWindow):
        
        QMainWindow.__init__(self)
        #self.ui = Ui_Color_Gauge()
        self.ui = loadUi('color_gauge.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #self.progressBarValue(75)
        #self.show()
        
                 
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255,11,133,0), stop:{STOP_2} rgba{color_battery});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000

        if(value>99):
            value = 99
        if(value<1):
            value = 1

        progress = (100 - value) / 100.0
        
        #color
        percentage_color = value

        # Calculate RGB values based on the percentage
        red = int(255 * (100 - percentage_color) / 100)
        green = int(255 * percentage_color / 100)
        blue = 0

        # Set the background color of the widget
        color_battery = (red, green, blue,255)
    
        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{color_battery}",str(color_battery))
        #print("New Stylesheet:", newStylesheet)
        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circle_Progess.setStyleSheet(newStylesheet)

        self.label_precentage = self.findChild(QLabel,'label_precentage')
        self.label_precentage.setText(str(value) +'%')



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
   


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        loadUi('GUI_Banshee_Command_Center.ui', self)

        self.setWindowIcon(QIcon('Banshee_logo.png'))
        self.setWindowTitle('Banshee Command Center')
        self.setWindowOpacity(0.98)


        # find child
        self.video_feed_label = self.findChild(QLabel, 'RGB_video_feed')
        self.map_viewer = self.findChild(QWebEngineView,'map')
        self.name_remove_maker = self.findChild(QLineEdit,'name_remove_maker')
        self.btn_add_marker = self.findChild(QPushButton, "add_marker_btn")
        self.btn_remove_maker = self.findChild(QPushButton,'remove_marker_btn')
        self.txt_latitude_input = self.findChild(QLineEdit,'latitude_input_TextBox')
        self.txt_longitude_input = self.findChild(QLineEdit,'longitude_input_TextBox')
        self.txt_name_add_marker = self.findChild(QLineEdit, 'name_add_maker')
        self.txt_description_add_marker = self.findChild(QLineEdit, 'description_input_text_box')
        self.Battery_Gauge_widget = self.findChild(QWidget,'Battery_Gauge_widget')
        self.Compass_Gauge_widget = self.findChild(QWidget, 'Compass_Gauge_widget')
        self.ROLL_Gauge_widget = self.findChild(QWidget,'Roll_Gauge_widget')
        self.Pitch_Gauge_widget = self.findChild(QWidget,'PITCH_Gauge_widget')
        self.WeatherAPP_location_widget = self.findChild(QWidget,'widget_weather')
        self.WeatherAPp_4_location_widget = self.findChild(QWidget,'widget_weather_4')
 
        self.Radar_widget = self.findChild(QGraphicsView,'radar_widget')
        
        # Weather app
        self.weather_widget = WeatherAPP()
        layout_weather_widget = QVBoxLayout(self.WeatherAPP_location_widget)
        layout_weather_widget.addWidget(self.weather_widget)

        # Weather app 2
        self.weather_widget2 = WeatherAPP()
        layout_weather_widget2= QVBoxLayout(self.WeatherAPp_4_location_widget)
        layout_weather_widget2.addWidget(self.weather_widget2)


        # Set up video thread
        self.video_thread = VideoThread()
        self.video_thread.frame_signal.connect(self.update_video_frame)
        self.video_thread.start()

        # Set up map thread
        self.map_thread = MapThread()
        self.map_thread.update_map_signal.connect(self.update_map)
        self.map_thread.start()
 

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
        self.RadarGaugeThread = Radar_Thread()
        self.RadarGaugeThread.update_Radar_signal.connect(self.update_radar)
        self.RadarGaugeThread.start()
   

        ## btn setup 
        self.btn_add_marker.pressed.connect(self.add_maker_btn_function)
        self.btn_remove_maker.pressed.connect(self.remove_marker)

        # Create an instance of your Battery progress bar
        self.Battery_color_gauge_w = color_gauge(QMainWindow)
        # Set up the layout and add the Battery progress bar to the widget
        layout_battery_gauge = QVBoxLayout(self.Battery_Gauge_widget)
        layout_battery_gauge.addWidget(self.Battery_color_gauge_w)

        # Create an instance of your compass progress bar
        self.Compass_color_gauge_w = compass_gauge(QMainWindow)
        # Set up the layout and add the compass progress bar to the widget
        layout_Compass_gauge = QVBoxLayout(self.Compass_Gauge_widget)
        layout_Compass_gauge.addWidget(self.Compass_color_gauge_w)

        # Create an instance of your ROLL progress bar
        self.ROLL_color_gauge_w = Roll_gauge(QMainWindow)
        # Set up the layout and add the ROLL progress bar to the widget
        layout_ROLL_gauge = QVBoxLayout(self.ROLL_Gauge_widget)
        layout_ROLL_gauge.addWidget(self.ROLL_color_gauge_w)

        
        # Create an instance of your Pitch progress bar
        self.Pitch_color_gauge_w = Pitch_gauge(QMainWindow)
        # Set up the layout and add the Pitch progress bar to the widget
        layout_Pitch_gauge = QVBoxLayout(self.Pitch_Gauge_widget)
        layout_Pitch_gauge.addWidget(self.Pitch_color_gauge_w)
        

    def update_video_frame(self, frame):
        # Update the video frame on the GUI
 
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgbFrame = cv2.resize(rgbFrame,(1080,1080))
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

            




    # Other methods...
def arduino_map(value, from_low, from_high, to_low, to_high):
    """
    Map the value from one range to another.

    Parameters:
    - value: The input value to be mapped.
    - from_low: The lower bound of the input range.
    - from_high: The upper bound of the input range.
    - to_low: The lower bound of the output range.
    - to_high: The upper bound of the output range.

    Returns:
    The mapped value.
    """
    # Ensure the value is within the input range
    value = max(from_low, min(from_high, value))

    # Map the value to the output range
    from_range = from_high - from_low
    to_range = to_high - to_low

    mapped_value = to_low + (value - from_low) * (to_range / from_range)
    return mapped_value


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
