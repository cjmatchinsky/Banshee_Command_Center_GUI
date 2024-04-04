 #########################################################

import sys
import platform
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

# GUI FILE
from ui_color_gauge import Ui_Color_Gauge
global counter
counter = 98 
import time
class color_gauge(QMainWindow):
    def __init__(self, parent: QMainWindow):
        
        QMainWindow.__init__(self)
        #self.ui = Ui_Color_Gauge()
        self.ui = uic.loadUi('color_gauge.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        global counter

        self.progressBarValue(counter)
 

        self.show()

    ## DEF PROGRESS BAR VALUE
    ########################################################################
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

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circle_Progess.setStyleSheet(newStylesheet)

        self.label_precentage = self.findChild(QLabel,'label_precentage')
        self.label_precentage.setText(str(value) +'%')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = color_gauge(QMainWindow)
    
    sys.exit(app.exec_())