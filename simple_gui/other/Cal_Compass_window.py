from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

import qdarktheme
 



class Cal_compass_Dialog_window_CLASS(QDialog):
    def __init__(self, *args, **Kwargs):
        super(Cal_compass_Dialog_window_CLASS, self).__init__(*args, **Kwargs)
        loadUi('Cal_compass_window.ui',self)
        self.setWindowIcon(QIcon('Banshee_logo.png'))
        self.setWindowTitle('Calibraion of Compass')
        self.setWindowOpacity(0.91)
        # define and find child name in ui file


