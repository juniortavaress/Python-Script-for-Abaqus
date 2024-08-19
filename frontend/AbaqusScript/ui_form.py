# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1648, 871)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 20, -1, -1)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setFrameShadow(QFrame.Shadow.Plain)
        self.label_2.setPixmap(QPixmap(u"Icons/computing.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_44 = QFrame(self.frame_4)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_44)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 250))
        self.frame_45.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_45)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(15, 15, 15, 9)
        self.label_43 = QLabel(self.frame_45)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 20))
        self.label_43.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_43, 0, 0, 1, 1)

        self.line_9 = QFrame(self.frame_45)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMaximumSize(QSize(16777215, 1))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_9, 1, 0, 1, 1)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(16777215, 180))
        self.frame_46.setStyleSheet(u"border: 0px solid;")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(80, 0))
        self.frame_47.setStyleSheet(u"border: 0px;")
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_47)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_47)
        self.label_48.setObjectName(u"label_48")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semilight"])
        font1.setPointSize(13)
        self.label_48.setFont(font1)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_9.addWidget(self.label_48)

        self.label_49 = QLabel(self.frame_47)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_9.addWidget(self.label_49)

        self.label_50 = QLabel(self.frame_47)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_9.addWidget(self.label_50)

        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_9.addWidget(self.label_51)


        self.horizontalLayout_13.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(150, 0))
        self.frame_48.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_48)
        self.verticalLayout_30.setSpacing(7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_32 = QLineEdit(self.frame_48)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.lineEdit_32)

        self.lineEdit_37 = QLineEdit(self.frame_48)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.lineEdit_37)

        self.lineEdit_38 = QLineEdit(self.frame_48)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.lineEdit_38)

        self.lineEdit_39 = QLineEdit(self.frame_48)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.lineEdit_39)


        self.horizontalLayout_13.addWidget(self.frame_48)


        self.gridLayout_6.addWidget(self.frame_46, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_45, 0, 0, 1, 1)

        self.frame_61 = QFrame(self.frame_44)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 250))
        self.frame_61.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_61)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(15, 15, 15, 9)
        self.label_66 = QLabel(self.frame_61)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 20))
        self.label_66.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_66)

        self.line_12 = QFrame(self.frame_61)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMaximumSize(QSize(16777215, 1))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_39.addWidget(self.line_12)

        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 180))
        self.frame_62.setStyleSheet(u"border: 0px solid;")
        self.frame_62.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_63 = QFrame(self.frame_62)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"border: 0px;")
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_63)
        self.verticalLayout_40.setSpacing(7)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_63)
        self.label_67.setObjectName(u"label_67")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semilight"])
        font2.setPointSize(12)
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_40.addWidget(self.label_67)

        self.label_68 = QLabel(self.frame_63)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font2)
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_40.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_63)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font2)
        self.label_69.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_40.addWidget(self.label_69)


        self.horizontalLayout_18.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_62)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_64.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_64)
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_52 = QLineEdit(self.frame_64)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_52)

        self.lineEdit_53 = QLineEdit(self.frame_64)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_53)

        self.lineEdit_54 = QLineEdit(self.frame_64)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_54)


        self.horizontalLayout_18.addWidget(self.frame_64)


        self.verticalLayout_39.addWidget(self.frame_62)


        self.gridLayout_5.addWidget(self.frame_61, 1, 1, 1, 1)

        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(16777215, 250))
        self.frame_49.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_49)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(15, 15, 15, 9)
        self.label_52 = QLabel(self.frame_49)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 20))
        self.label_52.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_52)

        self.line_10 = QFrame(self.frame_49)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMaximumSize(QSize(16777215, 1))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_10)

        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 180))
        self.frame_50.setStyleSheet(u"border: 0px;")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(16777215, 16777215))
        self.frame_51.setStyleSheet(u"border: 0px solid;")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(30, 0))
        self.frame_52.setStyleSheet(u"border: 0px;")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_52)
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_52)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_32.addWidget(self.label_53)

        self.label_54 = QLabel(self.frame_52)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)
        self.label_54.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_32.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_52)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font1)
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_32.addWidget(self.label_55)

        self.label_56 = QLabel(self.frame_52)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font1)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_32.addWidget(self.label_56)


        self.horizontalLayout_15.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_53)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_40 = QLineEdit(self.frame_53)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.lineEdit_40)

        self.lineEdit_41 = QLineEdit(self.frame_53)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.lineEdit_41)

        self.lineEdit_42 = QLineEdit(self.frame_53)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.lineEdit_42)

        self.lineEdit_43 = QLineEdit(self.frame_53)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.lineEdit_43)


        self.horizontalLayout_15.addWidget(self.frame_53)


        self.horizontalLayout_14.addWidget(self.frame_51)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(16777215, 16777215))
        self.frame_54.setStyleSheet(u"border: 0px solid;")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(30, 0))
        self.frame_55.setStyleSheet(u"border: 0px;")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_55)
        self.verticalLayout_34.setSpacing(7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_55)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_34.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_55)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)
        self.label_58.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_34.addWidget(self.label_58)

        self.label_59 = QLabel(self.frame_55)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_34.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_55)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_34.addWidget(self.label_60)


        self.horizontalLayout_16.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_56)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_44 = QLineEdit(self.frame_56)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMaxLength(32767)
        self.lineEdit_44.setFrame(True)
        self.lineEdit_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.lineEdit_44)

        self.lineEdit_45 = QLineEdit(self.frame_56)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.lineEdit_45)

        self.lineEdit_46 = QLineEdit(self.frame_56)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.lineEdit_46)

        self.lineEdit_47 = QLineEdit(self.frame_56)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_35.addWidget(self.lineEdit_47)


        self.horizontalLayout_16.addWidget(self.frame_56)


        self.horizontalLayout_14.addWidget(self.frame_54)


        self.verticalLayout_31.addWidget(self.frame_50)


        self.gridLayout_5.addWidget(self.frame_49, 0, 1, 1, 1)

        self.frame_57 = QFrame(self.frame_44)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 250))
        self.frame_57.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_57)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(15, 15, 15, 9)
        self.label_61 = QLabel(self.frame_57)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(16777215, 20))
        self.label_61.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_61)

        self.line_11 = QFrame(self.frame_57)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMaximumSize(QSize(16777215, 1))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_36.addWidget(self.line_11)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(16777215, 180))
        self.frame_58.setStyleSheet(u"border: 0px solid;")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        font3 = QFont()
        font3.setPointSize(12)
        self.frame_59.setFont(font3)
        self.frame_59.setStyleSheet(u"border: 0px;")
        self.frame_59.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_59)
        self.verticalLayout_37.setSpacing(7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_59)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font2)
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_37.addWidget(self.label_62)

        self.label_63 = QLabel(self.frame_59)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font2)
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_37.addWidget(self.label_63)

        self.label_64 = QLabel(self.frame_59)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_37.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_59)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_37.addWidget(self.label_65)


        self.horizontalLayout_17.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_60)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_48 = QLineEdit(self.frame_60)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.lineEdit_48)

        self.lineEdit_49 = QLineEdit(self.frame_60)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.lineEdit_49)

        self.lineEdit_50 = QLineEdit(self.frame_60)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.lineEdit_50)

        self.lineEdit_51 = QLineEdit(self.frame_60)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.lineEdit_51)


        self.horizontalLayout_17.addWidget(self.frame_60)


        self.verticalLayout_36.addWidget(self.frame_58)


        self.gridLayout_5.addWidget(self.frame_57, 1, 0, 1, 1)

        self.plotChipPlateArea_2 = QFrame(self.frame_44)
        self.plotChipPlateArea_2.setObjectName(u"plotChipPlateArea_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotChipPlateArea_2.sizePolicy().hasHeightForWidth())
        self.plotChipPlateArea_2.setSizePolicy(sizePolicy)
        self.plotChipPlateArea_2.setMinimumSize(QSize(800, 0))
        self.plotChipPlateArea_2.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);")
        self.plotChipPlateArea_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotChipPlateArea_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_5.addWidget(self.plotChipPlateArea_2, 2, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.frame_44)

        self.plotChipPlateArea = QFrame(self.frame_4)
        self.plotChipPlateArea.setObjectName(u"plotChipPlateArea")
        sizePolicy.setHeightForWidth(self.plotChipPlateArea.sizePolicy().hasHeightForWidth())
        self.plotChipPlateArea.setSizePolicy(sizePolicy)
        self.plotChipPlateArea.setMinimumSize(QSize(800, 0))
        self.plotChipPlateArea.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);")
        self.plotChipPlateArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotChipPlateArea.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_6 = QFrame(self.plotChipPlateArea)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(120, 130, 120, 241))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.plotChipPlateArea)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_23 = QFrame(self.page_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(270, 110, 703, 398))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_23)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_24)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 15, 15, 9)
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)

        self.line_5 = QFrame(self.frame_24)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 16777215))
        self.frame_25.setStyleSheet(u"border: 0px solid;")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(80, 0))
        self.frame_26.setStyleSheet(u"border: 0px;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_26)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_26)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_8.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_26)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_8.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_26)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_8.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_8.addWidget(self.label_28)


        self.horizontalLayout_7.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(150, 0))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_27)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_17 = QLineEdit(self.frame_27)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.frame_27)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineEdit_18)

        self.lineEdit_19 = QLineEdit(self.frame_27)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.frame_27)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.lineEdit_20)


        self.horizontalLayout_7.addWidget(self.frame_27)


        self.gridLayout_4.addWidget(self.frame_25, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)

        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_28)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(15, 15, 15, 9)
        self.label_29 = QLabel(self.frame_28)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 20))
        self.label_29.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_29)

        self.line_6 = QFrame(self.frame_28)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_6)

        self.frame_43 = QFrame(self.frame_28)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"border: 0px;")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_29 = QFrame(self.frame_43)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setStyleSheet(u"border: 0px solid;")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(30, 0))
        self.frame_30.setStyleSheet(u"border: 0px;")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_30)
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_30)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_20.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_30)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_20.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_30)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_20.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_30)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_20.addWidget(self.label_33)


        self.horizontalLayout_8.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_31)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_21 = QLineEdit(self.frame_31)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_21)

        self.lineEdit_22 = QLineEdit(self.frame_31)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_22)

        self.lineEdit_23 = QLineEdit(self.frame_31)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_23)

        self.lineEdit_24 = QLineEdit(self.frame_31)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_24)


        self.horizontalLayout_8.addWidget(self.frame_31)


        self.horizontalLayout_12.addWidget(self.frame_29)

        self.frame_40 = QFrame(self.frame_43)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 16777215))
        self.frame_40.setStyleSheet(u"border: 0px solid;")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(30, 0))
        self.frame_41.setStyleSheet(u"border: 0px;")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_41)
        self.verticalLayout_28.setSpacing(7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_41)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_28.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_41)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_28.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_41)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_28.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_41)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_28.addWidget(self.label_47)


        self.horizontalLayout_11.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_42)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_33 = QLineEdit(self.frame_42)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMaxLength(32767)
        self.lineEdit_33.setFrame(True)
        self.lineEdit_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_33)

        self.lineEdit_34 = QLineEdit(self.frame_42)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_34)

        self.lineEdit_35 = QLineEdit(self.frame_42)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_35)

        self.lineEdit_36 = QLineEdit(self.frame_42)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_36)


        self.horizontalLayout_11.addWidget(self.frame_42)


        self.horizontalLayout_12.addWidget(self.frame_40)


        self.verticalLayout_19.addWidget(self.frame_43)


        self.gridLayout_3.addWidget(self.frame_28, 0, 1, 1, 1)

        self.frame_32 = QFrame(self.frame_23)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_32)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 15, 15, 9)
        self.label_34 = QLabel(self.frame_32)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_34)

        self.line_7 = QFrame(self.frame_32)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 1))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line_7)

        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setStyleSheet(u"border: 0px solid;")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFont(font3)
        self.frame_34.setStyleSheet(u"border: 0px;")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_34)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_34)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_23.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_34)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_23.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_34)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_34)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_23.addWidget(self.label_38)


        self.horizontalLayout_9.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_35)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_25 = QLineEdit(self.frame_35)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_25)

        self.lineEdit_26 = QLineEdit(self.frame_35)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_26)

        self.lineEdit_27 = QLineEdit(self.frame_35)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_27)

        self.lineEdit_28 = QLineEdit(self.frame_35)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_28)


        self.horizontalLayout_9.addWidget(self.frame_35)


        self.verticalLayout_22.addWidget(self.frame_33)


        self.gridLayout_3.addWidget(self.frame_32, 1, 0, 1, 1)

        self.frame_36 = QFrame(self.frame_23)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(15, 15, 15, 9)
        self.label_39 = QLabel(self.frame_36)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 20))
        self.label_39.setStyleSheet(u"border: 0px solid rgba(214, 214, 214, 150);")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_39)

        self.line_8 = QFrame(self.frame_36)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_25.addWidget(self.line_8)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setStyleSheet(u"border: 0px solid;")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"border: 0px;")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_38)
        self.verticalLayout_26.setSpacing(7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_38)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_26.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_38)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_26.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_38)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font2)
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;")

        self.verticalLayout_26.addWidget(self.label_42)


        self.horizontalLayout_10.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgba(214, 214, 214, 150);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_39)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_29 = QLineEdit(self.frame_39)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.lineEdit_29)

        self.lineEdit_30 = QLineEdit(self.frame_39)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.lineEdit_30)

        self.lineEdit_31 = QLineEdit(self.frame_39)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.lineEdit_31)


        self.horizontalLayout_10.addWidget(self.frame_39)


        self.verticalLayout_25.addWidget(self.frame_37)


        self.gridLayout_3.addWidget(self.frame_36, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 540, 311, 41))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"    QComboBox {\n"
"        border: 1px solid #666666; /* Borda do comboBox */\n"
"        border-radius: 5px; /* Cantos arredondados */\n"
"        padding: 5px 10px; /* Espa\u00e7amento interno */\n"
"        background-color: #353535; /* Cor de fundo */\n"
"        color: #FFFFFF; /* Cor do texto */\n"
"    }\n"
"\n"
"    QComboBox::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 20px; /* Largura do bot\u00e3o de dropdown */\n"
"        border-left: 1px solid #666666; /* Borda esquerda do bot\u00e3o de dropdown */\n"
"        background-color: #4c4c4c; /* Cor de fundo do bot\u00e3o de dropdown */\n"
"        border-top-right-radius: 5px; /* Canto superior direito arredondado */\n"
"        border-bottom-right-radius: 5px; /* Canto inferior direito arredondado */\n"
"    }\n"
"\n"
"    QComboBox::down-arrow {\n"
"        image: url(:/Icons/down_arrow.png); /* Imagem do \u00edcone de seta para baixo */\n"
"    }\n"
"\n"
"    QComboBox QAbstrac"
                        "tItemView {\n"
"        border: 1px solid #666666; /* Borda da lista suspensa */\n"
"        selection-background-color: #4c4c4c; /* Cor de fundo dos itens selecionados */\n"
"        selection-color: #FFFFFF; /* Cor do texto dos itens selecionados */\n"
"        background-color: #353535; /* Cor de fundo da lista suspensa */\n"
"        color: #FFFFFF; /* Cor do texto dos itens */\n"
"    }")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EULERIAN", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"GEOMETRY INFORMATION", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Trickness:", None))
        self.lineEdit_32.setText("")
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.lineEdit_37.setText("")
        self.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.lineEdit_38.setText("")
        self.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.lineEdit_39.setText("")
        self.lineEdit_39.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"MESH INFORMATION", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Min Size Factor", None))
        self.lineEdit_52.setText("")
        self.lineEdit_52.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mesh global size", None))
        self.lineEdit_53.setText("")
        self.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainWindow", u"deviation factor", None))
        self.lineEdit_54.setText("")
        self.lineEdit_54.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minimum size", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"PARTITION INFORMATIOR", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"X3:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"X4:", None))
        self.lineEdit_40.setText("")
        self.lineEdit_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_41.setText("")
        self.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_42.setText("")
        self.lineEdit_42.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_43.setText("")
        self.lineEdit_43.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Y3:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Y4:", None))
        self.lineEdit_44.setInputMask("")
        self.lineEdit_44.setText("")
        self.lineEdit_44.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_45.setText("")
        self.lineEdit_45.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_46.setText("")
        self.lineEdit_46.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_47.setText("")
        self.lineEdit_47.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"SET AND SECTIONS INFORMATION", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Domain 01:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Domain 02:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Domain 03:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Domain 04:", None))
        self.lineEdit_48.setText("")
        self.lineEdit_48.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_49.setText("")
        self.lineEdit_49.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_50.setText("")
        self.lineEdit_50.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_51.setText("")
        self.lineEdit_51.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"GEOMETRY INFORMATION", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Trickness:", None))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"PARTITION INFORMATIOR", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"X3:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"X4:", None))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_23.setText("")
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_24.setText("")
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Y3:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Y4:", None))
        self.lineEdit_33.setInputMask("")
        self.lineEdit_33.setText("")
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_34.setText("")
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_35.setText("")
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.lineEdit_36.setText("")
        self.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a position", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"SET AND SECTIONS INFORMATION", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Domain 01:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Domain 02:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Domain 03:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Domain 04:", None))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_26.setText("")
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_27.setText("")
        self.lineEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.lineEdit_28.setText("")
        self.lineEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"domain name", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"MESH INFORMATION", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Min Size Factor", None))
        self.lineEdit_29.setText("")
        self.lineEdit_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mesh global size", None))
        self.lineEdit_30.setText("")
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"deviation factor", None))
        self.lineEdit_31.setText("")
        self.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minimum size", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a part", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Eulerian", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Tool", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Chip Plate", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the part", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior", None))
    # retranslateUi

