from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from utilities import arduino_map

class Pitch_gauge(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        
        # Load the UI file
        self.ui =loadUi('ui/color_gauge_Pitch.ui', self)

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
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:4, 
                stop:{stop1} rgba(255, 255, 255, 0), 
                stop:{stop2} rgba{color_roll}, 
                stop:{stop3} rgba(255, 255, 255, 0), 
                stop:{stop4} rgba(249, 249, 249, 0), 
                stop:{stop5} rgba{color_roll}, 
                stop:{stop6} rgba(236, 236, 236, 0));
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
        self.ui =loadUi('ui/color_gauge_ROL.ui', self)

         

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
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:4, 
                stop:{stop1} rgba(255, 255, 255, 0), 
                stop:{stop2} {color_roll}, 
                stop:{stop3} rgba(255, 255, 255, 0), 
                stop:{stop4} rgba(249, 249, 249, 0), 
                stop:{stop5} {color_roll}, 
                stop:{stop6} rgba(236, 236, 236, 0));
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
        self.ui =loadUi('ui/color_gauge__compass.ui', self)

         

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
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:{STOP_1} rgba(255,11,133,0), 
                stop:{STOP_2} rgba(255, 0, 0, 255), 
                stop:{STOP_3} rgba(255,11,133,0));
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
        self.ui = loadUi('ui/color_gauge.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #self.progressBarValue(75)
        #self.show()
        
                 
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:{STOP_1} rgba(255,11,133,0), 
                stop:{STOP_2} rgba{color_battery});
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