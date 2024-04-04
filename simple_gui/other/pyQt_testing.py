
import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QWidget

class MainWindow(QMainWindow):

    def __init__(self, *args, **Kwargs):
        super(MainWindow, self).__init__(*args, **Kwargs)

        self.setGeometry(100,100,3650,2000)
        self.setWindowTitle('Banshee Command Center')
        self.setWindowIcon(QIcon('Banshee_logo.png'))
        self.setFixedSize(3650,2000)
        self.setWindowOpacity(0.95)
        self.setStyleSheet('background-color: rgb(90, 98, 99)	')
        
        self.create_buttons()

    def create_buttons(self):
        btn1 = QPushButton("Click ME!" , self)
        #btn1 = setText("testing")
        btn1.setGeometry(300,300,500,500)
        btn1.setIcon(QIcon('banshee_logo.png'))
        btn1.clicked.connect(self.clicked_btn)

        btn2 = QPushButton("Click2", self)
        btn2.setGeometry(1000,1000,500,500)
        btn2.clicked.connect(self.clicked_btn2)


    def clicked_btn(self):
        print('btn')
         
    
    def clicked_btn2(self):
        print('btn22')
         
       
  
  

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())