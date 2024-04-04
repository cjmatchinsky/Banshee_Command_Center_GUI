# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_gaugewRWFCK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Color_Gauge(object):
    def setupUi(self, Color_Gauge):
        if Color_Gauge.objectName():
            Color_Gauge.setObjectName(u"Color_Gauge")
        Color_Gauge.resize(337, 336)
        self.centralwidget = QWidget(Color_Gauge)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circleProgressBAR_Base = QFrame(self.centralwidget)
        self.circleProgressBAR_Base.setObjectName(u"circleProgressBAR_Base")
        self.circleProgressBAR_Base.setGeometry(QRect(10, 10, 320, 320))
        self.circleProgressBAR_Base.setFrameShape(QFrame.NoFrame)
        self.circleProgressBAR_Base.setFrameShadow(QFrame.Raised)
        self.circle_Progess = QFrame(self.circleProgressBAR_Base)
        self.circle_Progess.setObjectName(u"circle_Progess")
        self.circle_Progess.setGeometry(QRect(10, 10, 300, 300))
        self.circle_Progess.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 11, 133, 0), stop:0.750 rgba(85, 170, 255, 255))\n"
"}")
        self.circle_Progess.setFrameShape(QFrame.StyledPanel)
        self.circle_Progess.setFrameShadow(QFrame.Raised)
        self.circle_background = QFrame(self.circleProgressBAR_Base)
        self.circle_background.setObjectName(u"circle_background")
        self.circle_background.setGeometry(QRect(10, 10, 300, 300))
        self.circle_background.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127,120);\n"
"}")
        self.circle_background.setFrameShape(QFrame.StyledPanel)
        self.circle_background.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circleProgressBAR_Base)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.container)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-20, 0, 311, 131))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255); background-color: none;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_precentage = QLabel(self.container)
        self.label_precentage.setObjectName(u"label_precentage")
        self.label_precentage.setGeometry(QRect(-40, 60, 371, 181))
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(35)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_precentage.setFont(font1)
        self.label_precentage.setStyleSheet(u"color: rgb(255, 255, 255); background-color: none;")
        self.label_precentage.setAlignment(Qt.AlignCenter)
        self.circle_background.raise_()
        self.circle_Progess.raise_()
        self.container.raise_()
        Color_Gauge.setCentralWidget(self.centralwidget)

        self.retranslateUi(Color_Gauge)

        QMetaObject.connectSlotsByName(Color_Gauge)
    # setupUi

    def retranslateUi(self, Color_Gauge):
        Color_Gauge.setWindowTitle(QCoreApplication.translate("Color_Gauge", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("Color_Gauge", u"<html><head/><body><p><span style=\" font-weight:600; color:#9b9bff;\">Battery Life</span></p></body></html>", None))
        self.label_precentage.setText(QCoreApplication.translate("Color_Gauge", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400; color:#f0f0ff;\">0</span><span style=\" font-weight:400; color:#f0f0ff; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi

