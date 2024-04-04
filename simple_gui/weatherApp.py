import requests
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic 
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
from utilities import format_date, get_day_of_week, subtract_one_day, image_download, coordinate_validations

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
    api_key = "2f6b8642f0744741a93160512232412"
    get_current_weather(api_key, latitude, longitude ,weather_data)
    get_forecast_weather(api_key, latitude, longitude ,weather_data)
 
    print(weather_data)
 
class WeatherAPP(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        uic.loadUi('./ui/weatherAPP_ui.ui', self)
        
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