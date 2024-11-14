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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)
import rc_Icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1535, 962)
        MainWindow.setMinimumSize(QSize(300, 340))
        icon = QIcon()
        icon.addFile(u"Icons/programmer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"QFrame{\n"
"background-color: #ededed;\n"
"border: 0px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 20))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_123 = QFrame(self.frame_9)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 20))
        self.frame_123.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_123)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_123)
        self.pages.setObjectName(u"pages")
        self.pages.setEnabled(True)
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        self.pages.setFont(font)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_55 = QVBoxLayout(self.homePage)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_129 = QFrame(self.homePage)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(0, 78))
        self.frame_129.setMaximumSize(QSize(16777215, 78))
        self.frame_129.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}	\n"
"")
        self.frame_129.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(9, 0, 9, 0)
        self.label_16 = QLabel(self.frame_129)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 60))
        self.label_16.setMaximumSize(QSize(60, 60))
        self.label_16.setPixmap(QPixmap(u":/icons/Icons/programmer.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_57.addWidget(self.label_16)

        self.label_18 = QLabel(self.frame_129)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 80))
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_18.setFont(font1)
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.label_18)


        self.verticalLayout_55.addWidget(self.frame_129)

        self.frame_24 = QFrame(self.homePage)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_24)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_24)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(16777215, 230))
        self.frame_72.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_72.setStyleSheet(u"")
        self.frame_72.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(9, -1, 50, -1)
        self.frame_148 = QFrame(self.frame_72)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMaximumSize(QSize(400, 16777215))
        self.frame_148.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_148.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_148)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.label_22 = QLabel(self.frame_148)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/icons/Icons/abaqusIcon.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_102.addWidget(self.label_22)


        self.horizontalLayout_76.addWidget(self.frame_148)

        self.label_21 = QLabel(self.frame_72)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}")
        self.label_21.setTextFormat(Qt.TextFormat.AutoText)
        self.label_21.setScaledContents(False)
        self.label_21.setWordWrap(True)
        self.label_21.setMargin(10)

        self.horizontalLayout_76.addWidget(self.label_21)


        self.verticalLayout_61.addWidget(self.frame_72)

        self.frame_74 = QFrame(self.frame_24)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_75.setSpacing(50)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(50, -1, 50, -1)
        self.frame_86 = QFrame(self.frame_74)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(450, 0))
        self.frame_86.setStyleSheet(u"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"}")
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_86)
        self.verticalLayout_98.setSpacing(15)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 30, 0, 30)
        self.frame_132 = QFrame(self.frame_86)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(-1, 9, -1, -1)
        self.label_19 = QLabel(self.frame_132)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(280, 280))
        self.label_19.setMaximumSize(QSize(280, 280))
        self.label_19.setPixmap(QPixmap(u":/icons/Icons/img01.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.label_19)


        self.verticalLayout_98.addWidget(self.frame_132)

        self.frame_146 = QFrame(self.frame_86)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(0, 180))
        self.frame_146.setMaximumSize(QSize(16777215, 180))
        self.frame_146.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_146)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(30, -1, 30, -1)
        self.label_20 = QLabel(self.frame_146)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_20.setWordWrap(True)

        self.verticalLayout_101.addWidget(self.label_20)


        self.verticalLayout_98.addWidget(self.frame_146)

        self.frame_147 = QFrame(self.frame_86)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMaximumSize(QSize(16777215, 80))
        self.frame_147.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_147.setStyleSheet(u"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"    border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	border: 0px;\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:"
                        "0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"}\n"
"\n"
"")
        self.frame_147.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(-1, -1, -1, 9)
        self.parametrizationButton = QPushButton(self.frame_147)
        self.parametrizationButton.setObjectName(u"parametrizationButton")
        self.parametrizationButton.setMinimumSize(QSize(0, 40))
        self.parametrizationButton.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_77.addWidget(self.parametrizationButton)


        self.verticalLayout_98.addWidget(self.frame_147)


        self.horizontalLayout_75.addWidget(self.frame_86)

        self.frame_90 = QFrame(self.frame_74)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(450, 0))
        self.frame_90.setStyleSheet(u"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"}")
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_90)
        self.verticalLayout_99.setSpacing(15)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 30, 0, 30)
        self.frame_149 = QFrame(self.frame_90)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(-1, 9, -1, -1)
        self.label_23 = QLabel(self.frame_149)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(280, 280))
        self.label_23.setMaximumSize(QSize(280, 280))
        self.label_23.setPixmap(QPixmap(u":/icons/Icons/img02.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_83.addWidget(self.label_23)


        self.verticalLayout_99.addWidget(self.frame_149)

        self.frame_151 = QFrame(self.frame_90)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setMinimumSize(QSize(0, 180))
        self.frame_151.setMaximumSize(QSize(16777215, 180))
        self.frame_151.setStyleSheet(u"")
        self.frame_151.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_151)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(30, -1, 30, -1)
        self.label_24 = QLabel(self.frame_151)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_24.setWordWrap(True)

        self.verticalLayout_125.addWidget(self.label_24)


        self.verticalLayout_99.addWidget(self.frame_151)

        self.frame_150 = QFrame(self.frame_90)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMaximumSize(QSize(16777215, 80))
        self.frame_150.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_150.setStyleSheet(u"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"    border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	border: 0px;\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:"
                        "0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"}\n"
"\n"
"")
        self.frame_150.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(-1, -1, -1, 9)
        self.iterationButton = QPushButton(self.frame_150)
        self.iterationButton.setObjectName(u"iterationButton")
        self.iterationButton.setEnabled(False)
        self.iterationButton.setMinimumSize(QSize(0, 40))
        self.iterationButton.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_84.addWidget(self.iterationButton)


        self.verticalLayout_99.addWidget(self.frame_150)


        self.horizontalLayout_75.addWidget(self.frame_90)

        self.frame_131 = QFrame(self.frame_74)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(450, 0))
        self.frame_131.setStyleSheet(u"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"}")
        self.frame_131.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_131)
        self.verticalLayout_127.setSpacing(15)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 30, 0, 30)
        self.frame_154 = QFrame(self.frame_131)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(-1, 9, -1, -1)
        self.label_26 = QLabel(self.frame_154)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(280, 280))
        self.label_26.setMaximumSize(QSize(280, 280))
        self.label_26.setPixmap(QPixmap(u":/icons/Icons/Screenshot 2024-09-26 111633.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_86.addWidget(self.label_26)


        self.verticalLayout_127.addWidget(self.frame_154)

        self.frame_152 = QFrame(self.frame_131)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(0, 180))
        self.frame_152.setMaximumSize(QSize(16777215, 180))
        self.frame_152.setStyleSheet(u"")
        self.frame_152.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_152)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(30, -1, 30, -1)
        self.label_25 = QLabel(self.frame_152)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_25.setWordWrap(True)

        self.verticalLayout_126.addWidget(self.label_25)


        self.verticalLayout_127.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_131)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMaximumSize(QSize(16777215, 80))
        self.frame_153.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_153.setStyleSheet(u"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"    border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	border: 0px;\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:"
                        "0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px;\n"
"}\n"
"\n"
"")
        self.frame_153.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(-1, -1, -1, 9)
        self.resultsButton = QPushButton(self.frame_153)
        self.resultsButton.setObjectName(u"resultsButton")
        self.resultsButton.setMinimumSize(QSize(0, 40))
        self.resultsButton.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_85.addWidget(self.resultsButton)


        self.verticalLayout_127.addWidget(self.frame_153)


        self.horizontalLayout_75.addWidget(self.frame_131)


        self.verticalLayout_61.addWidget(self.frame_74)


        self.verticalLayout_55.addWidget(self.frame_24)

        self.pages.addWidget(self.homePage)
        self.geometryPage = QWidget()
        self.geometryPage.setObjectName(u"geometryPage")
        self.verticalLayout_166 = QVBoxLayout(self.geometryPage)
        self.verticalLayout_166.setSpacing(0)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.frame_157 = QFrame(self.geometryPage)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_157)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 3)
        self.frame_160 = QFrame(self.frame_157)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(0, 78))
        self.frame_160.setMaximumSize(QSize(16777215, 78))
        self.frame_160.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}	\n"
"\n"
"")
        self.frame_160.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_27 = QLabel(self.frame_160)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(60, 60))
        self.label_27.setMaximumSize(QSize(60, 60))
        self.label_27.setPixmap(QPixmap(u":/icons/Icons/dimensions.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_87.addWidget(self.label_27)

        self.label_51 = QLabel(self.frame_160)
        self.label_51.setObjectName(u"label_51")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setBold(True)
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"QLabel {\n"
"        font-size: 30px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.label_51)


        self.verticalLayout_128.addWidget(self.frame_160)

        self.frame_200 = QFrame(self.frame_157)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_200)
        self.horizontalLayout_88.setSpacing(9)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(18, 18, 18, 0)
        self.frame_201 = QFrame(self.frame_200)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: #b6b6b6;\n"
"	border-radius: 15px;}")
        self.frame_201.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_201)
        self.verticalLayout_129.setSpacing(9)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_201)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #b6b6b6;}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #b6b6b6;\n"
"    background-color: #b6b6b6;}\n"
"\n"
"QTabBar::tab {\n"
"    background: #e1e1e1;\n"
"    border: 1px solid #b6b6b6;\n"
"    padding: 5px;\n"
"    color: black;\n"
"	width: 120;}\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #3498db;  /* Cor de fundo da aba selecionada */\n"
"    color: white;  /* Cor do texto da aba selecionada */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #b6b6b6;  /* Cor de fundo da aba ao passar o mouse */\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.eulerianTab = QWidget()
        self.eulerianTab.setObjectName(u"eulerianTab")
        self.verticalLayout_151 = QVBoxLayout(self.eulerianTab)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.frame_203 = QFrame(self.eulerianTab)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"    }")
        self.frame_203.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_203)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(-1, 9, -1, -1)
        self.frame_207 = QFrame(self.frame_203)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMinimumSize(QSize(0, 250))
        self.frame_207.setMaximumSize(QSize(16777215, 250))
        self.frame_207.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_207)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_208 = QFrame(self.frame_207)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_208)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(-1, 0, -1, -1)
        self.frame_209 = QFrame(self.frame_208)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMinimumSize(QSize(0, 35))
        self.frame_209.setMaximumSize(QSize(16777215, 35))
        self.frame_209.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_209)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_209)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 35))
        self.label_52.setMaximumSize(QSize(16777215, 35))
        self.label_52.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_133.addWidget(self.label_52)


        self.verticalLayout_132.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_210)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(20, -1, -1, -1)
        self.frame_211 = QFrame(self.frame_210)
        self.frame_211.setObjectName(u"frame_211")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_211.sizePolicy().hasHeightForWidth())
        self.frame_211.setSizePolicy(sizePolicy)
        self.frame_211.setMaximumSize(QSize(120, 16777215))
        self.frame_211.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_211)
        self.verticalLayout_134.setSpacing(7)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_143 = QLabel(self.frame_211)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(0, 18))
        self.label_143.setMaximumSize(QSize(16777215, 18))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semilight"])
        self.label_143.setFont(font3)
        self.label_143.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_143)

        self.label_144 = QLabel(self.frame_211)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(0, 18))
        self.label_144.setMaximumSize(QSize(16777215, 18))
        self.label_144.setFont(font3)
        self.label_144.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_144)

        self.label_153 = QLabel(self.frame_211)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(0, 18))
        self.label_153.setMaximumSize(QSize(16777215, 18))
        self.label_153.setFont(font3)
        self.label_153.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_153)

        self.label_154 = QLabel(self.frame_211)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(0, 18))
        self.label_154.setMaximumSize(QSize(16777215, 18))
        self.label_154.setFont(font3)
        self.label_154.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_154)


        self.horizontalLayout_90.addWidget(self.frame_211)

        self.frame_212 = QFrame(self.frame_210)
        self.frame_212.setObjectName(u"frame_212")
        sizePolicy.setHeightForWidth(self.frame_212.sizePolicy().hasHeightForWidth())
        self.frame_212.setSizePolicy(sizePolicy)
        self.frame_212.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_212.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_212)
        self.verticalLayout_135.setSpacing(7)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.eulerianName = QLineEdit(self.frame_212)
        self.eulerianName.setObjectName(u"eulerianName")
        self.eulerianName.setMinimumSize(QSize(0, 20))
        self.eulerianName.setMaximumSize(QSize(180, 16777215))
        self.eulerianName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianName)

        self.eulerianHeight = QLineEdit(self.frame_212)
        self.eulerianHeight.setObjectName(u"eulerianHeight")
        self.eulerianHeight.setMinimumSize(QSize(0, 20))
        self.eulerianHeight.setMaximumSize(QSize(180, 16777215))
        self.eulerianHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianHeight)

        self.eulerianWidth = QLineEdit(self.frame_212)
        self.eulerianWidth.setObjectName(u"eulerianWidth")
        self.eulerianWidth.setMinimumSize(QSize(0, 20))
        self.eulerianWidth.setMaximumSize(QSize(180, 16777215))
        self.eulerianWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianWidth)

        self.eulerianTrickness = QLineEdit(self.frame_212)
        self.eulerianTrickness.setObjectName(u"eulerianTrickness")
        self.eulerianTrickness.setMinimumSize(QSize(0, 20))
        self.eulerianTrickness.setMaximumSize(QSize(180, 16777215))
        self.eulerianTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianTrickness)


        self.horizontalLayout_90.addWidget(self.frame_212)


        self.verticalLayout_132.addWidget(self.frame_210)


        self.horizontalLayout_89.addWidget(self.frame_208)

        self.frame_213 = QFrame(self.frame_207)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_213)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(-1, 0, -1, -1)
        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMinimumSize(QSize(0, 35))
        self.frame_214.setMaximumSize(QSize(16777215, 35))
        self.frame_214.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_214)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_214)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 35))
        self.label_53.setMaximumSize(QSize(16777215, 35))
        self.label_53.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_137.addWidget(self.label_53)


        self.verticalLayout_136.addWidget(self.frame_214)

        self.frame_215 = QFrame(self.frame_213)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_91.setSpacing(20)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(20, -1, -1, -1)
        self.frame_216 = QFrame(self.frame_215)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_216)
        self.horizontalLayout_92.setSpacing(6)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_217 = QFrame(self.frame_216)
        self.frame_217.setObjectName(u"frame_217")
        sizePolicy.setHeightForWidth(self.frame_217.sizePolicy().hasHeightForWidth())
        self.frame_217.setSizePolicy(sizePolicy)
        self.frame_217.setMaximumSize(QSize(40, 16777215))
        self.frame_217.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_217)
        self.verticalLayout_138.setSpacing(7)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.frame_217)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(0, 18))
        self.label_157.setMaximumSize(QSize(16777215, 18))
        self.label_157.setFont(font3)
        self.label_157.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_157)

        self.label_158 = QLabel(self.frame_217)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMinimumSize(QSize(0, 18))
        self.label_158.setMaximumSize(QSize(16777215, 18))
        self.label_158.setFont(font3)
        self.label_158.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_158)

        self.label_169 = QLabel(self.frame_217)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMinimumSize(QSize(0, 18))
        self.label_169.setMaximumSize(QSize(16777215, 18))
        self.label_169.setFont(font3)
        self.label_169.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_169)

        self.label_170 = QLabel(self.frame_217)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMinimumSize(QSize(0, 18))
        self.label_170.setMaximumSize(QSize(16777215, 18))
        self.label_170.setFont(font3)
        self.label_170.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_170)


        self.horizontalLayout_92.addWidget(self.frame_217)

        self.frame_218 = QFrame(self.frame_216)
        self.frame_218.setObjectName(u"frame_218")
        sizePolicy.setHeightForWidth(self.frame_218.sizePolicy().hasHeightForWidth())
        self.frame_218.setSizePolicy(sizePolicy)
        self.frame_218.setMaximumSize(QSize(120, 16777215))
        self.frame_218.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_218.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_218)
        self.verticalLayout_139.setSpacing(7)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionX1 = QLineEdit(self.frame_218)
        self.eulerianPartitionX1.setObjectName(u"eulerianPartitionX1")
        self.eulerianPartitionX1.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX1)

        self.eulerianPartitionX2 = QLineEdit(self.frame_218)
        self.eulerianPartitionX2.setObjectName(u"eulerianPartitionX2")
        self.eulerianPartitionX2.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX2)

        self.eulerianPartitionX3 = QLineEdit(self.frame_218)
        self.eulerianPartitionX3.setObjectName(u"eulerianPartitionX3")
        self.eulerianPartitionX3.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX3)

        self.eulerianPartitionX4 = QLineEdit(self.frame_218)
        self.eulerianPartitionX4.setObjectName(u"eulerianPartitionX4")
        self.eulerianPartitionX4.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX4)


        self.horizontalLayout_92.addWidget(self.frame_218)


        self.horizontalLayout_91.addWidget(self.frame_216)

        self.frame_219 = QFrame(self.frame_215)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_219)
        self.horizontalLayout_93.setSpacing(6)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_220 = QFrame(self.frame_219)
        self.frame_220.setObjectName(u"frame_220")
        sizePolicy.setHeightForWidth(self.frame_220.sizePolicy().hasHeightForWidth())
        self.frame_220.setSizePolicy(sizePolicy)
        self.frame_220.setMaximumSize(QSize(40, 16777215))
        self.frame_220.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_220)
        self.verticalLayout_140.setSpacing(7)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.frame_220)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(0, 18))
        self.label_171.setMaximumSize(QSize(16777215, 18))
        self.label_171.setFont(font3)
        self.label_171.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_171)

        self.label_177 = QLabel(self.frame_220)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMinimumSize(QSize(0, 18))
        self.label_177.setMaximumSize(QSize(16777215, 18))
        self.label_177.setFont(font3)
        self.label_177.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_177)

        self.label_178 = QLabel(self.frame_220)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMinimumSize(QSize(0, 18))
        self.label_178.setMaximumSize(QSize(16777215, 18))
        self.label_178.setFont(font3)
        self.label_178.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_178)

        self.label_181 = QLabel(self.frame_220)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMinimumSize(QSize(0, 18))
        self.label_181.setMaximumSize(QSize(16777215, 18))
        self.label_181.setFont(font3)
        self.label_181.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_181)


        self.horizontalLayout_93.addWidget(self.frame_220)

        self.frame_221 = QFrame(self.frame_219)
        self.frame_221.setObjectName(u"frame_221")
        sizePolicy.setHeightForWidth(self.frame_221.sizePolicy().hasHeightForWidth())
        self.frame_221.setSizePolicy(sizePolicy)
        self.frame_221.setMaximumSize(QSize(120, 16777215))
        self.frame_221.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_221.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_221)
        self.verticalLayout_141.setSpacing(7)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionY1 = QLineEdit(self.frame_221)
        self.eulerianPartitionY1.setObjectName(u"eulerianPartitionY1")
        self.eulerianPartitionY1.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY1)

        self.eulerianPartitionY2 = QLineEdit(self.frame_221)
        self.eulerianPartitionY2.setObjectName(u"eulerianPartitionY2")
        self.eulerianPartitionY2.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY2)

        self.eulerianPartitionY3 = QLineEdit(self.frame_221)
        self.eulerianPartitionY3.setObjectName(u"eulerianPartitionY3")
        self.eulerianPartitionY3.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY3)

        self.eulerianPartitionY4 = QLineEdit(self.frame_221)
        self.eulerianPartitionY4.setObjectName(u"eulerianPartitionY4")
        self.eulerianPartitionY4.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY4)


        self.horizontalLayout_93.addWidget(self.frame_221)


        self.horizontalLayout_91.addWidget(self.frame_219)


        self.verticalLayout_136.addWidget(self.frame_215)


        self.horizontalLayout_89.addWidget(self.frame_213)


        self.verticalLayout_131.addWidget(self.frame_207)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_131.addItem(self.verticalSpacer_17)

        self.frame_222 = QFrame(self.frame_203)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setMinimumSize(QSize(0, 250))
        self.frame_222.setMaximumSize(QSize(16777215, 250))
        self.frame_222.setStyleSheet(u"")
        self.frame_222.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_222)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(9, 0, 0, 0)
        self.frame_223 = QFrame(self.frame_222)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_223)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, -1)
        self.frame_224 = QFrame(self.frame_223)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(0, 35))
        self.frame_224.setMaximumSize(QSize(16777215, 35))
        self.frame_224.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_224)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_224)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 35))
        self.label_54.setMaximumSize(QSize(16777215, 35))
        self.label_54.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_144.addWidget(self.label_54)


        self.verticalLayout_143.addWidget(self.frame_224)

        self.frame_225 = QFrame(self.frame_223)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_226 = QFrame(self.frame_225)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_226)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, -1, 12, -1)
        self.frame_227 = QFrame(self.frame_226)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_227)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(20, -1, 0, -1)
        self.frame_228 = QFrame(self.frame_227)
        self.frame_228.setObjectName(u"frame_228")
        sizePolicy.setHeightForWidth(self.frame_228.sizePolicy().hasHeightForWidth())
        self.frame_228.setSizePolicy(sizePolicy)
        self.frame_228.setMaximumSize(QSize(120, 16777215))
        self.frame_228.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_228)
        self.verticalLayout_146.setSpacing(7)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.frame_228)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 18))
        self.label_117.setMaximumSize(QSize(16777215, 18))
        self.label_117.setFont(font3)
        self.label_117.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_228)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 18))
        self.label_118.setMaximumSize(QSize(16777215, 18))
        self.label_118.setFont(font3)
        self.label_118.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_118)

        self.label_119 = QLabel(self.frame_228)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 18))
        self.label_119.setMaximumSize(QSize(16777215, 18))
        self.label_119.setFont(font3)
        self.label_119.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_119)

        self.label_120 = QLabel(self.frame_228)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 18))
        self.label_120.setMaximumSize(QSize(16777215, 18))
        self.label_120.setFont(font3)
        self.label_120.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_120)


        self.horizontalLayout_95.addWidget(self.frame_228)

        self.frame_229 = QFrame(self.frame_227)
        self.frame_229.setObjectName(u"frame_229")
        sizePolicy.setHeightForWidth(self.frame_229.sizePolicy().hasHeightForWidth())
        self.frame_229.setSizePolicy(sizePolicy)
        self.frame_229.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_229.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_229)
        self.verticalLayout_147.setSpacing(7)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.eulerianGlobalSize = QLineEdit(self.frame_229)
        self.eulerianGlobalSize.setObjectName(u"eulerianGlobalSize")
        self.eulerianGlobalSize.setMinimumSize(QSize(0, 20))
        self.eulerianGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.eulerianGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianGlobalSize)

        self.eulerianDeviationFactor = QLineEdit(self.frame_229)
        self.eulerianDeviationFactor.setObjectName(u"eulerianDeviationFactor")
        self.eulerianDeviationFactor.setMinimumSize(QSize(0, 20))
        self.eulerianDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianDeviationFactor)

        self.eulerianMininumFactor = QLineEdit(self.frame_229)
        self.eulerianMininumFactor.setObjectName(u"eulerianMininumFactor")
        self.eulerianMininumFactor.setMinimumSize(QSize(0, 20))
        self.eulerianMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianMininumFactor)

        self.eulerianOtherInfo = QLineEdit(self.frame_229)
        self.eulerianOtherInfo.setObjectName(u"eulerianOtherInfo")
        self.eulerianOtherInfo.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.eulerianOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianOtherInfo)


        self.horizontalLayout_95.addWidget(self.frame_229)


        self.verticalLayout_145.addWidget(self.frame_227)


        self.horizontalLayout_94.addWidget(self.frame_226)

        self.frame_230 = QFrame(self.frame_225)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_230)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.frame_231 = QFrame(self.frame_230)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_231)
        self.horizontalLayout_96.setSpacing(20)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(15, -1, -1, -1)
        self.frame_232 = QFrame(self.frame_231)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_232)
        self.horizontalLayout_97.setSpacing(6)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_233 = QFrame(self.frame_232)
        self.frame_233.setObjectName(u"frame_233")
        sizePolicy.setHeightForWidth(self.frame_233.sizePolicy().hasHeightForWidth())
        self.frame_233.setSizePolicy(sizePolicy)
        self.frame_233.setMaximumSize(QSize(120, 16777215))
        self.frame_233.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_233)
        self.verticalLayout_149.setSpacing(7)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_182 = QLabel(self.frame_233)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMinimumSize(QSize(0, 18))
        self.label_182.setMaximumSize(QSize(16777215, 18))
        self.label_182.setFont(font3)
        self.label_182.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_182)

        self.label_183 = QLabel(self.frame_233)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setMinimumSize(QSize(0, 18))
        self.label_183.setMaximumSize(QSize(16777215, 18))
        self.label_183.setFont(font3)
        self.label_183.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_183)

        self.label_184 = QLabel(self.frame_233)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMinimumSize(QSize(0, 18))
        self.label_184.setMaximumSize(QSize(16777215, 18))
        self.label_184.setFont(font3)
        self.label_184.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_184)

        self.label_185 = QLabel(self.frame_233)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(0, 18))
        self.label_185.setMaximumSize(QSize(16777215, 18))
        self.label_185.setFont(font3)
        self.label_185.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_185)


        self.horizontalLayout_97.addWidget(self.frame_233)

        self.frame_234 = QFrame(self.frame_232)
        self.frame_234.setObjectName(u"frame_234")
        sizePolicy.setHeightForWidth(self.frame_234.sizePolicy().hasHeightForWidth())
        self.frame_234.setSizePolicy(sizePolicy)
        self.frame_234.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_234.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_234)
        self.verticalLayout_150.setSpacing(7)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.eulerianOtherInfo_7 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_7.setObjectName(u"eulerianOtherInfo_7")
        self.eulerianOtherInfo_7.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_7.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_7)

        self.eulerianOtherInfo_8 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_8.setObjectName(u"eulerianOtherInfo_8")
        self.eulerianOtherInfo_8.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_8.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_8)

        self.eulerianOtherInfo_9 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_9.setObjectName(u"eulerianOtherInfo_9")
        self.eulerianOtherInfo_9.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_9.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_9)

        self.eulerianOtherInfo_10 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_10.setObjectName(u"eulerianOtherInfo_10")
        self.eulerianOtherInfo_10.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_10.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_10)


        self.horizontalLayout_97.addWidget(self.frame_234)


        self.horizontalLayout_96.addWidget(self.frame_232)


        self.verticalLayout_148.addWidget(self.frame_231)


        self.horizontalLayout_94.addWidget(self.frame_230)


        self.verticalLayout_143.addWidget(self.frame_225)


        self.verticalLayout_142.addWidget(self.frame_223)


        self.verticalLayout_131.addWidget(self.frame_222)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_131.addItem(self.verticalSpacer_18)

        self.eulerianWarning = QLabel(self.frame_203)
        self.eulerianWarning.setObjectName(u"eulerianWarning")
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Semilight"])
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.eulerianWarning.setFont(font4)
        self.eulerianWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.eulerianWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.eulerianWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_131.addWidget(self.eulerianWarning)

        self.verticalSpacer_19 = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_131.addItem(self.verticalSpacer_19)

        self.frame_2 = QFrame(self.frame_203)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.defautValues = QCheckBox(self.frame_2)
        self.defautValues.setObjectName(u"defautValues")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.defautValues.sizePolicy().hasHeightForWidth())
        self.defautValues.setSizePolicy(sizePolicy1)
        self.defautValues.setMaximumSize(QSize(16777215, 20))
        self.defautValues.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.defautValues)


        self.verticalLayout_131.addWidget(self.frame_2)


        self.verticalLayout_151.addWidget(self.frame_203)

        self.tabWidget.addTab(self.eulerianTab, "")
        self.chipPlayeTab = QWidget()
        self.chipPlayeTab.setObjectName(u"chipPlayeTab")
        self.chipPlayeTab.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_223 = QVBoxLayout(self.chipPlayeTab)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.frame_332 = QFrame(self.chipPlayeTab)
        self.frame_332.setObjectName(u"frame_332")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_332.sizePolicy().hasHeightForWidth())
        self.frame_332.setSizePolicy(sizePolicy2)
        self.frame_332.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"    }")
        self.frame_332.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_332.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.frame_332)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(9, 9, 0, 0)
        self.frame_333 = QFrame(self.frame_332)
        self.frame_333.setObjectName(u"frame_333")
        sizePolicy2.setHeightForWidth(self.frame_333.sizePolicy().hasHeightForWidth())
        self.frame_333.setSizePolicy(sizePolicy2)
        self.frame_333.setMinimumSize(QSize(311, 250))
        self.frame_333.setMaximumSize(QSize(16777215, 280))
        self.frame_333.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_333.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.frame_333)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(-1, 0, -1, -1)
        self.frame_334 = QFrame(self.frame_333)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMinimumSize(QSize(0, 35))
        self.frame_334.setMaximumSize(QSize(16777215, 35))
        self.frame_334.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_334)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_334)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 35))
        self.label_63.setMaximumSize(QSize(16777215, 35))
        self.label_63.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_134.addWidget(self.label_63)


        self.verticalLayout_217.addWidget(self.frame_334)

        self.frame_335 = QFrame(self.frame_333)
        self.frame_335.setObjectName(u"frame_335")
        self.frame_335.setMinimumSize(QSize(283, 180))
        self.frame_335.setMaximumSize(QSize(16777215, 16777215))
        self.frame_335.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_335.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_335.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_335)
        self.horizontalLayout_135.setSpacing(6)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(20, 9, -1, 9)
        self.frame_336 = QFrame(self.frame_335)
        self.frame_336.setObjectName(u"frame_336")
        sizePolicy2.setHeightForWidth(self.frame_336.sizePolicy().hasHeightForWidth())
        self.frame_336.setSizePolicy(sizePolicy2)
        self.frame_336.setMinimumSize(QSize(120, 0))
        self.frame_336.setStyleSheet(u"border: 0px;")
        self.frame_336.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_218 = QVBoxLayout(self.frame_336)
        self.verticalLayout_218.setSpacing(7)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_336)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 20))
        self.label_64.setMaximumSize(QSize(16777215, 18))
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_336)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 20))
        self.label_65.setMaximumSize(QSize(16777215, 18))
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_65)

        self.label_66 = QLabel(self.frame_336)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 20))
        self.label_66.setMaximumSize(QSize(16777215, 18))
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_66)

        self.label_67 = QLabel(self.frame_336)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 20))
        self.label_67.setMaximumSize(QSize(16777215, 18))
        self.label_67.setFont(font3)
        self.label_67.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_67)


        self.horizontalLayout_135.addWidget(self.frame_336)

        self.frame_337 = QFrame(self.frame_335)
        self.frame_337.setObjectName(u"frame_337")
        sizePolicy2.setHeightForWidth(self.frame_337.sizePolicy().hasHeightForWidth())
        self.frame_337.setSizePolicy(sizePolicy2)
        self.frame_337.setMinimumSize(QSize(150, 0))
        self.frame_337.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_337.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_337.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.frame_337)
        self.verticalLayout_219.setSpacing(7)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.chipName = QLineEdit(self.frame_337)
        self.chipName.setObjectName(u"chipName")
        self.chipName.setMinimumSize(QSize(0, 20))
        self.chipName.setMaximumSize(QSize(180, 16777215))
        self.chipName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipName)

        self.chipHeight = QLineEdit(self.frame_337)
        self.chipHeight.setObjectName(u"chipHeight")
        self.chipHeight.setMinimumSize(QSize(0, 20))
        self.chipHeight.setMaximumSize(QSize(180, 16777215))
        self.chipHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipHeight)

        self.chipWidth = QLineEdit(self.frame_337)
        self.chipWidth.setObjectName(u"chipWidth")
        self.chipWidth.setMinimumSize(QSize(0, 20))
        self.chipWidth.setMaximumSize(QSize(180, 16777215))
        self.chipWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipWidth)

        self.chipTrickness = QLineEdit(self.frame_337)
        self.chipTrickness.setObjectName(u"chipTrickness")
        self.chipTrickness.setMinimumSize(QSize(0, 20))
        self.chipTrickness.setMaximumSize(QSize(180, 16777215))
        self.chipTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipTrickness)


        self.horizontalLayout_135.addWidget(self.frame_337)


        self.verticalLayout_217.addWidget(self.frame_335)


        self.verticalLayout_216.addWidget(self.frame_333)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_216.addItem(self.verticalSpacer_31)

        self.frame_338 = QFrame(self.frame_332)
        self.frame_338.setObjectName(u"frame_338")
        sizePolicy2.setHeightForWidth(self.frame_338.sizePolicy().hasHeightForWidth())
        self.frame_338.setSizePolicy(sizePolicy2)
        self.frame_338.setMinimumSize(QSize(311, 221))
        self.frame_338.setMaximumSize(QSize(16777215, 280))
        self.frame_338.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_220 = QVBoxLayout(self.frame_338)
        self.verticalLayout_220.setSpacing(6)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(-1, 0, 0, 0)
        self.frame_339 = QFrame(self.frame_338)
        self.frame_339.setObjectName(u"frame_339")
        self.frame_339.setMinimumSize(QSize(0, 35))
        self.frame_339.setMaximumSize(QSize(16777215, 35))
        self.frame_339.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_339.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_339)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_339)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 35))
        self.label_68.setMaximumSize(QSize(16777215, 35))
        self.label_68.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_136.addWidget(self.label_68)


        self.verticalLayout_220.addWidget(self.frame_339)

        self.frame_340 = QFrame(self.frame_338)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setMinimumSize(QSize(283, 180))
        self.frame_340.setMaximumSize(QSize(16777215, 180))
        self.frame_340.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_340.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_340)
        self.horizontalLayout_137.setSpacing(6)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(20, 12, -1, 0)
        self.frame_341 = QFrame(self.frame_340)
        self.frame_341.setObjectName(u"frame_341")
        sizePolicy2.setHeightForWidth(self.frame_341.sizePolicy().hasHeightForWidth())
        self.frame_341.setSizePolicy(sizePolicy2)
        self.frame_341.setMinimumSize(QSize(120, 0))
        self.frame_341.setStyleSheet(u"border: 0px;")
        self.frame_341.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_341.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_221 = QVBoxLayout(self.frame_341)
        self.verticalLayout_221.setSpacing(7)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_341)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 20))
        self.label_73.setMaximumSize(QSize(16777215, 18))
        self.label_73.setFont(font3)
        self.label_73.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_341)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 20))
        self.label_74.setMaximumSize(QSize(16777215, 18))
        self.label_74.setFont(font3)
        self.label_74.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_341)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(0, 20))
        self.label_75.setMaximumSize(QSize(16777215, 18))
        self.label_75.setFont(font3)
        self.label_75.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_341)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(0, 20))
        self.label_76.setMaximumSize(QSize(16777215, 18))
        self.label_76.setFont(font3)
        self.label_76.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_76)


        self.horizontalLayout_137.addWidget(self.frame_341)

        self.frame_342 = QFrame(self.frame_340)
        self.frame_342.setObjectName(u"frame_342")
        sizePolicy2.setHeightForWidth(self.frame_342.sizePolicy().hasHeightForWidth())
        self.frame_342.setSizePolicy(sizePolicy2)
        self.frame_342.setMinimumSize(QSize(150, 0))
        self.frame_342.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_342.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_222 = QVBoxLayout(self.frame_342)
        self.verticalLayout_222.setSpacing(7)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.chipGlobalSize = QLineEdit(self.frame_342)
        self.chipGlobalSize.setObjectName(u"chipGlobalSize")
        self.chipGlobalSize.setMinimumSize(QSize(0, 20))
        self.chipGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.chipGlobalSize.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.chipGlobalSize.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.chipGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipGlobalSize)

        self.chipDeviationFactor = QLineEdit(self.frame_342)
        self.chipDeviationFactor.setObjectName(u"chipDeviationFactor")
        self.chipDeviationFactor.setMinimumSize(QSize(0, 20))
        self.chipDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.chipDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipDeviationFactor)

        self.chipMininumFactor = QLineEdit(self.frame_342)
        self.chipMininumFactor.setObjectName(u"chipMininumFactor")
        self.chipMininumFactor.setMinimumSize(QSize(0, 20))
        self.chipMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.chipMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipMininumFactor)

        self.chipOtherInfo = QLineEdit(self.frame_342)
        self.chipOtherInfo.setObjectName(u"chipOtherInfo")
        self.chipOtherInfo.setMinimumSize(QSize(0, 20))
        self.chipOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.chipOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipOtherInfo)


        self.horizontalLayout_137.addWidget(self.frame_342)


        self.verticalLayout_220.addWidget(self.frame_340)


        self.verticalLayout_216.addWidget(self.frame_338)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_216.addItem(self.verticalSpacer_29)

        self.chipWarning = QLabel(self.frame_332)
        self.chipWarning.setObjectName(u"chipWarning")
        self.chipWarning.setFont(font4)
        self.chipWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chipWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.chipWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_216.addWidget(self.chipWarning)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_216.addItem(self.verticalSpacer_30)


        self.verticalLayout_223.addWidget(self.frame_332)

        self.tabWidget.addTab(self.chipPlayeTab, "")
        self.toolTab = QWidget()
        self.toolTab.setObjectName(u"toolTab")
        self.verticalLayout_215 = QVBoxLayout(self.toolTab)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.frame_235 = QFrame(self.toolTab)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_235.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_235)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.frame_236 = QFrame(self.frame_235)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setMinimumSize(QSize(0, 250))
        self.frame_236.setMaximumSize(QSize(16777215, 250))
        self.frame_236.setStyleSheet(u"")
        self.frame_236.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_236)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(9, 0, 0, 0)
        self.frame_237 = QFrame(self.frame_236)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_237)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, -1)
        self.frame_238 = QFrame(self.frame_237)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMinimumSize(QSize(0, 35))
        self.frame_238.setMaximumSize(QSize(16777215, 35))
        self.frame_238.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_238)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_238)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 35))
        self.label_55.setMaximumSize(QSize(16777215, 35))
        self.label_55.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_155.addWidget(self.label_55)


        self.verticalLayout_154.addWidget(self.frame_238)

        self.frame_239 = QFrame(self.frame_237)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_239)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_240 = QFrame(self.frame_239)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_240)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, -1, 12, -1)
        self.frame_241 = QFrame(self.frame_240)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(20, -1, 0, -1)
        self.frame_242 = QFrame(self.frame_241)
        self.frame_242.setObjectName(u"frame_242")
        sizePolicy.setHeightForWidth(self.frame_242.sizePolicy().hasHeightForWidth())
        self.frame_242.setSizePolicy(sizePolicy)
        self.frame_242.setMaximumSize(QSize(180, 16777215))
        self.frame_242.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_242)
        self.verticalLayout_157.setSpacing(7)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.frame_242)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setMinimumSize(QSize(0, 20))
        self.label_186.setMaximumSize(QSize(16777215, 20))
        self.label_186.setFont(font3)
        self.label_186.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_186)

        self.label_187 = QLabel(self.frame_242)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setMinimumSize(QSize(0, 20))
        self.label_187.setMaximumSize(QSize(16777215, 20))
        self.label_187.setFont(font3)
        self.label_187.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_187)

        self.label_188 = QLabel(self.frame_242)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMinimumSize(QSize(0, 20))
        self.label_188.setMaximumSize(QSize(16777215, 20))
        self.label_188.setFont(font3)
        self.label_188.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_188)

        self.label_189 = QLabel(self.frame_242)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(0, 20))
        self.label_189.setMaximumSize(QSize(16777215, 20))
        self.label_189.setFont(font3)
        self.label_189.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_189)


        self.horizontalLayout_99.addWidget(self.frame_242)

        self.frame_243 = QFrame(self.frame_241)
        self.frame_243.setObjectName(u"frame_243")
        sizePolicy.setHeightForWidth(self.frame_243.sizePolicy().hasHeightForWidth())
        self.frame_243.setSizePolicy(sizePolicy)
        self.frame_243.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_243.setStyleSheet(u"")
        self.frame_243.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_243)
        self.verticalLayout_158.setSpacing(7)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.toolName = QLineEdit(self.frame_243)
        self.toolName.setObjectName(u"toolName")
        self.toolName.setMinimumSize(QSize(0, 20))
        self.toolName.setMaximumSize(QSize(180, 16777215))
        self.toolName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolName)

        self.toolTrickness = QLineEdit(self.frame_243)
        self.toolTrickness.setObjectName(u"toolTrickness")
        self.toolTrickness.setMinimumSize(QSize(0, 20))
        self.toolTrickness.setMaximumSize(QSize(180, 16777215))
        self.toolTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolTrickness)

        self.toolRakeAngle = QLineEdit(self.frame_243)
        self.toolRakeAngle.setObjectName(u"toolRakeAngle")
        self.toolRakeAngle.setMinimumSize(QSize(0, 20))
        self.toolRakeAngle.setMaximumSize(QSize(180, 16777215))
        self.toolRakeAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolRakeAngle)

        self.toolRakeDimension = QLineEdit(self.frame_243)
        self.toolRakeDimension.setObjectName(u"toolRakeDimension")
        self.toolRakeDimension.setMinimumSize(QSize(0, 20))
        self.toolRakeDimension.setMaximumSize(QSize(180, 16777215))
        self.toolRakeDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolRakeDimension)


        self.horizontalLayout_99.addWidget(self.frame_243)


        self.verticalLayout_156.addWidget(self.frame_241)


        self.horizontalLayout_98.addWidget(self.frame_240)

        self.frame_244 = QFrame(self.frame_239)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_244)
        self.verticalLayout_159.setSpacing(0)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.frame_245 = QFrame(self.frame_244)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_245)
        self.horizontalLayout_100.setSpacing(20)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(15, -1, -1, -1)
        self.frame_246 = QFrame(self.frame_245)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_246)
        self.horizontalLayout_101.setSpacing(6)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.frame_247 = QFrame(self.frame_246)
        self.frame_247.setObjectName(u"frame_247")
        sizePolicy.setHeightForWidth(self.frame_247.sizePolicy().hasHeightForWidth())
        self.frame_247.setSizePolicy(sizePolicy)
        self.frame_247.setMaximumSize(QSize(180, 16777215))
        self.frame_247.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_247)
        self.verticalLayout_160.setSpacing(7)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.label_190 = QLabel(self.frame_247)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMinimumSize(QSize(0, 20))
        self.label_190.setMaximumSize(QSize(16777215, 20))
        self.label_190.setFont(font3)
        self.label_190.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_190)

        self.label_191 = QLabel(self.frame_247)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMinimumSize(QSize(0, 20))
        self.label_191.setMaximumSize(QSize(16777215, 20))
        self.label_191.setFont(font3)
        self.label_191.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_191)

        self.label_192 = QLabel(self.frame_247)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setMinimumSize(QSize(0, 20))
        self.label_192.setMaximumSize(QSize(16777215, 20))
        self.label_192.setFont(font3)
        self.label_192.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_192)

        self.label_193 = QLabel(self.frame_247)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setMinimumSize(QSize(0, 18))
        self.label_193.setMaximumSize(QSize(16777215, 18))
        self.label_193.setFont(font3)
        self.label_193.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_193)


        self.horizontalLayout_101.addWidget(self.frame_247)

        self.frame_248 = QFrame(self.frame_246)
        self.frame_248.setObjectName(u"frame_248")
        sizePolicy.setHeightForWidth(self.frame_248.sizePolicy().hasHeightForWidth())
        self.frame_248.setSizePolicy(sizePolicy)
        self.frame_248.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_248.setStyleSheet(u"")
        self.frame_248.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_248)
        self.verticalLayout_161.setSpacing(7)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.toolClearanceAngle = QLineEdit(self.frame_248)
        self.toolClearanceAngle.setObjectName(u"toolClearanceAngle")
        self.toolClearanceAngle.setMinimumSize(QSize(0, 20))
        self.toolClearanceAngle.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolClearanceAngle)

        self.toolClearanceDimension = QLineEdit(self.frame_248)
        self.toolClearanceDimension.setObjectName(u"toolClearanceDimension")
        self.toolClearanceDimension.setMinimumSize(QSize(0, 20))
        self.toolClearanceDimension.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolClearanceDimension)

        self.toolRadius = QLineEdit(self.frame_248)
        self.toolRadius.setObjectName(u"toolRadius")
        self.toolRadius.setMinimumSize(QSize(0, 20))
        self.toolRadius.setMaximumSize(QSize(189, 16777215))
        self.toolRadius.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolRadius)

        self.label_194 = QLabel(self.frame_248)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setMinimumSize(QSize(0, 18))
        self.label_194.setMaximumSize(QSize(16777215, 18))
        self.label_194.setFont(font3)
        self.label_194.setStyleSheet(u"")

        self.verticalLayout_161.addWidget(self.label_194)


        self.horizontalLayout_101.addWidget(self.frame_248)


        self.horizontalLayout_100.addWidget(self.frame_246)


        self.verticalLayout_159.addWidget(self.frame_245)


        self.horizontalLayout_98.addWidget(self.frame_244)


        self.verticalLayout_154.addWidget(self.frame_239)


        self.verticalLayout_153.addWidget(self.frame_237)


        self.verticalLayout_152.addWidget(self.frame_236)

        self.verticalSpacer_20 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_20)

        self.frame_249 = QFrame(self.frame_235)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setMinimumSize(QSize(0, 0))
        self.frame_249.setMaximumSize(QSize(16777215, 100))
        self.frame_249.setStyleSheet(u"")
        self.frame_249.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_249)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(9, 0, 0, 0)
        self.frame_250 = QFrame(self.frame_249)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_250)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, -1)
        self.frame_251 = QFrame(self.frame_250)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(0, 35))
        self.frame_251.setMaximumSize(QSize(16777215, 35))
        self.frame_251.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_251)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_251)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 35))
        self.label_56.setMaximumSize(QSize(16777215, 35))
        self.label_56.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_102.addWidget(self.label_56)


        self.verticalLayout_163.addWidget(self.frame_251)

        self.frame_252 = QFrame(self.frame_250)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_252)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.frame_253 = QFrame(self.frame_252)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.frame_253)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 12, 0)
        self.frame_254 = QFrame(self.frame_253)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_254)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(20, -1, 0, -1)
        self.frame_255 = QFrame(self.frame_254)
        self.frame_255.setObjectName(u"frame_255")
        sizePolicy.setHeightForWidth(self.frame_255.sizePolicy().hasHeightForWidth())
        self.frame_255.setSizePolicy(sizePolicy)
        self.frame_255.setMinimumSize(QSize(180, 0))
        self.frame_255.setMaximumSize(QSize(140, 16777215))
        self.frame_255.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.frame_255)
        self.verticalLayout_202.setSpacing(7)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.label_195 = QLabel(self.frame_255)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setMinimumSize(QSize(180, 0))
        self.label_195.setMaximumSize(QSize(180, 20))
        self.label_195.setFont(font3)
        self.label_195.setStyleSheet(u"")

        self.verticalLayout_202.addWidget(self.label_195)


        self.horizontalLayout_104.addWidget(self.frame_255)

        self.frame_256 = QFrame(self.frame_254)
        self.frame_256.setObjectName(u"frame_256")
        sizePolicy.setHeightForWidth(self.frame_256.sizePolicy().hasHeightForWidth())
        self.frame_256.setSizePolicy(sizePolicy)
        self.frame_256.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_256.setStyleSheet(u"")
        self.frame_256.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.frame_256)
        self.verticalLayout_203.setSpacing(7)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.toolPartition01 = QLineEdit(self.frame_256)
        self.toolPartition01.setObjectName(u"toolPartition01")
        self.toolPartition01.setMinimumSize(QSize(0, 20))
        self.toolPartition01.setMaximumSize(QSize(180, 16777215))
        self.toolPartition01.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolPartition01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_203.addWidget(self.toolPartition01)


        self.horizontalLayout_104.addWidget(self.frame_256)


        self.verticalLayout_201.addWidget(self.frame_254)


        self.horizontalLayout_103.addWidget(self.frame_253)

        self.frame_257 = QFrame(self.frame_252)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.frame_257)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setContentsMargins(-1, 0, -1, 0)
        self.frame_258 = QFrame(self.frame_257)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_258)
        self.horizontalLayout_105.setSpacing(20)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(15, -1, -1, -1)
        self.frame_316 = QFrame(self.frame_258)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_316)
        self.horizontalLayout_106.setSpacing(6)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.frame_317 = QFrame(self.frame_316)
        self.frame_317.setObjectName(u"frame_317")
        sizePolicy.setHeightForWidth(self.frame_317.sizePolicy().hasHeightForWidth())
        self.frame_317.setSizePolicy(sizePolicy)
        self.frame_317.setMinimumSize(QSize(180, 0))
        self.frame_317.setMaximumSize(QSize(140, 16777215))
        self.frame_317.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_317.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.frame_317)
        self.verticalLayout_205.setSpacing(7)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.label_196 = QLabel(self.frame_317)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMinimumSize(QSize(180, 0))
        self.label_196.setMaximumSize(QSize(180, 20))
        self.label_196.setFont(font3)
        self.label_196.setStyleSheet(u"")

        self.verticalLayout_205.addWidget(self.label_196)


        self.horizontalLayout_106.addWidget(self.frame_317)

        self.frame_318 = QFrame(self.frame_316)
        self.frame_318.setObjectName(u"frame_318")
        sizePolicy.setHeightForWidth(self.frame_318.sizePolicy().hasHeightForWidth())
        self.frame_318.setSizePolicy(sizePolicy)
        self.frame_318.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_318.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.frame_318)
        self.verticalLayout_206.setSpacing(7)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.toolPartition02 = QLineEdit(self.frame_318)
        self.toolPartition02.setObjectName(u"toolPartition02")
        self.toolPartition02.setMinimumSize(QSize(0, 20))
        self.toolPartition02.setMaximumSize(QSize(189, 16777215))
        self.toolPartition02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_206.addWidget(self.toolPartition02)


        self.horizontalLayout_106.addWidget(self.frame_318)


        self.horizontalLayout_105.addWidget(self.frame_316)


        self.verticalLayout_204.addWidget(self.frame_258)


        self.horizontalLayout_103.addWidget(self.frame_257)


        self.verticalLayout_163.addWidget(self.frame_252)


        self.verticalLayout_162.addWidget(self.frame_250)


        self.verticalLayout_152.addWidget(self.frame_249)

        self.verticalSpacer_21 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_21)

        self.frame_319 = QFrame(self.frame_235)
        self.frame_319.setObjectName(u"frame_319")
        self.frame_319.setMinimumSize(QSize(0, 250))
        self.frame_319.setMaximumSize(QSize(16777215, 250))
        self.frame_319.setStyleSheet(u"")
        self.frame_319.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_319.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.frame_319)
        self.verticalLayout_207.setSpacing(0)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.verticalLayout_207.setContentsMargins(9, 0, 0, 0)
        self.frame_320 = QFrame(self.frame_319)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_208 = QVBoxLayout(self.frame_320)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(0, 0, 0, -1)
        self.frame_321 = QFrame(self.frame_320)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(0, 35))
        self.frame_321.setMaximumSize(QSize(16777215, 35))
        self.frame_321.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_321)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_321)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 35))
        self.label_62.setMaximumSize(QSize(16777215, 35))
        self.label_62.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_107.addWidget(self.label_62)


        self.verticalLayout_208.addWidget(self.frame_321)

        self.frame_322 = QFrame(self.frame_320)
        self.frame_322.setObjectName(u"frame_322")
        self.frame_322.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_322.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_322)
        self.horizontalLayout_108.setSpacing(0)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.frame_323 = QFrame(self.frame_322)
        self.frame_323.setObjectName(u"frame_323")
        self.frame_323.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_323.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.frame_323)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, -1, 12, -1)
        self.frame_324 = QFrame(self.frame_323)
        self.frame_324.setObjectName(u"frame_324")
        self.frame_324.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_324)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(20, -1, 0, -1)
        self.frame_325 = QFrame(self.frame_324)
        self.frame_325.setObjectName(u"frame_325")
        sizePolicy.setHeightForWidth(self.frame_325.sizePolicy().hasHeightForWidth())
        self.frame_325.setSizePolicy(sizePolicy)
        self.frame_325.setMaximumSize(QSize(180, 16777215))
        self.frame_325.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_325.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.frame_325)
        self.verticalLayout_210.setSpacing(7)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.label_197 = QLabel(self.frame_325)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setMinimumSize(QSize(0, 20))
        self.label_197.setMaximumSize(QSize(16777215, 20))
        self.label_197.setFont(font3)
        self.label_197.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_197)

        self.label_198 = QLabel(self.frame_325)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMinimumSize(QSize(0, 20))
        self.label_198.setMaximumSize(QSize(16777215, 20))
        self.label_198.setFont(font3)
        self.label_198.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_198)

        self.label_199 = QLabel(self.frame_325)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMinimumSize(QSize(0, 20))
        self.label_199.setMaximumSize(QSize(16777215, 20))
        self.label_199.setFont(font3)
        self.label_199.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_199)

        self.label_200 = QLabel(self.frame_325)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(0, 20))
        self.label_200.setMaximumSize(QSize(16777215, 20))
        self.label_200.setFont(font3)
        self.label_200.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_200)


        self.horizontalLayout_131.addWidget(self.frame_325)

        self.frame_326 = QFrame(self.frame_324)
        self.frame_326.setObjectName(u"frame_326")
        sizePolicy.setHeightForWidth(self.frame_326.sizePolicy().hasHeightForWidth())
        self.frame_326.setSizePolicy(sizePolicy)
        self.frame_326.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_326.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.frame_326)
        self.verticalLayout_211.setSpacing(7)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.toolGlobalSize = QLineEdit(self.frame_326)
        self.toolGlobalSize.setObjectName(u"toolGlobalSize")
        self.toolGlobalSize.setMinimumSize(QSize(0, 20))
        self.toolGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.toolGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolGlobalSize)

        self.toolDeviationFactor = QLineEdit(self.frame_326)
        self.toolDeviationFactor.setObjectName(u"toolDeviationFactor")
        self.toolDeviationFactor.setMinimumSize(QSize(0, 20))
        self.toolDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.toolDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolDeviationFactor)

        self.toolMinimumFactor = QLineEdit(self.frame_326)
        self.toolMinimumFactor.setObjectName(u"toolMinimumFactor")
        self.toolMinimumFactor.setMinimumSize(QSize(0, 20))
        self.toolMinimumFactor.setMaximumSize(QSize(180, 16777215))
        self.toolMinimumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolMinimumFactor)

        self.toolOthersInfo = QLineEdit(self.frame_326)
        self.toolOthersInfo.setObjectName(u"toolOthersInfo")
        self.toolOthersInfo.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo.setMaximumSize(QSize(180, 16777215))
        self.toolOthersInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolOthersInfo)


        self.horizontalLayout_131.addWidget(self.frame_326)


        self.verticalLayout_209.addWidget(self.frame_324)


        self.horizontalLayout_108.addWidget(self.frame_323)

        self.frame_327 = QFrame(self.frame_322)
        self.frame_327.setObjectName(u"frame_327")
        self.frame_327.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_327.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.frame_327)
        self.verticalLayout_212.setSpacing(0)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.frame_328 = QFrame(self.frame_327)
        self.frame_328.setObjectName(u"frame_328")
        self.frame_328.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_328.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_328)
        self.horizontalLayout_132.setSpacing(20)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(15, -1, -1, -1)
        self.frame_329 = QFrame(self.frame_328)
        self.frame_329.setObjectName(u"frame_329")
        self.frame_329.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_329)
        self.horizontalLayout_133.setSpacing(6)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.frame_330 = QFrame(self.frame_329)
        self.frame_330.setObjectName(u"frame_330")
        sizePolicy.setHeightForWidth(self.frame_330.sizePolicy().hasHeightForWidth())
        self.frame_330.setSizePolicy(sizePolicy)
        self.frame_330.setMaximumSize(QSize(180, 16777215))
        self.frame_330.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_213 = QVBoxLayout(self.frame_330)
        self.verticalLayout_213.setSpacing(7)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.label_201 = QLabel(self.frame_330)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(0, 20))
        self.label_201.setMaximumSize(QSize(16777215, 20))
        self.label_201.setFont(font3)
        self.label_201.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_201)

        self.label_202 = QLabel(self.frame_330)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMinimumSize(QSize(0, 20))
        self.label_202.setMaximumSize(QSize(16777215, 20))
        self.label_202.setFont(font3)
        self.label_202.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_202)

        self.label_203 = QLabel(self.frame_330)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMinimumSize(QSize(0, 20))
        self.label_203.setMaximumSize(QSize(16777215, 20))
        self.label_203.setFont(font3)
        self.label_203.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_203)

        self.label_204 = QLabel(self.frame_330)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setMinimumSize(QSize(0, 20))
        self.label_204.setMaximumSize(QSize(16777215, 20))
        self.label_204.setFont(font3)
        self.label_204.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_204)


        self.horizontalLayout_133.addWidget(self.frame_330)

        self.frame_331 = QFrame(self.frame_329)
        self.frame_331.setObjectName(u"frame_331")
        sizePolicy.setHeightForWidth(self.frame_331.sizePolicy().hasHeightForWidth())
        self.frame_331.setSizePolicy(sizePolicy)
        self.frame_331.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_331.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_331.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.frame_331)
        self.verticalLayout_214.setSpacing(7)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.toolOthersInfo_7 = QLineEdit(self.frame_331)
        self.toolOthersInfo_7.setObjectName(u"toolOthersInfo_7")
        self.toolOthersInfo_7.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_7.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_7)

        self.toolOthersInfo_8 = QLineEdit(self.frame_331)
        self.toolOthersInfo_8.setObjectName(u"toolOthersInfo_8")
        self.toolOthersInfo_8.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_8.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_8)

        self.toolOthersInfo_9 = QLineEdit(self.frame_331)
        self.toolOthersInfo_9.setObjectName(u"toolOthersInfo_9")
        self.toolOthersInfo_9.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_9.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_9)

        self.toolOthersInfo_10 = QLineEdit(self.frame_331)
        self.toolOthersInfo_10.setObjectName(u"toolOthersInfo_10")
        self.toolOthersInfo_10.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_10.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_10)


        self.horizontalLayout_133.addWidget(self.frame_331)


        self.horizontalLayout_132.addWidget(self.frame_329)


        self.verticalLayout_212.addWidget(self.frame_328)


        self.horizontalLayout_108.addWidget(self.frame_327)


        self.verticalLayout_208.addWidget(self.frame_322)


        self.verticalLayout_207.addWidget(self.frame_320)


        self.verticalLayout_152.addWidget(self.frame_319)

        self.verticalSpacer_27 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_27)

        self.toolWarning = QLabel(self.frame_235)
        self.toolWarning.setObjectName(u"toolWarning")
        self.toolWarning.setFont(font4)
        self.toolWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.toolWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolWarning.setWordWrap(True)

        self.verticalLayout_152.addWidget(self.toolWarning)

        self.verticalSpacer_28 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_28)


        self.verticalLayout_215.addWidget(self.frame_235)

        self.tabWidget.addTab(self.toolTab, "")
        self.assemblyTab = QWidget()
        self.assemblyTab.setObjectName(u"assemblyTab")
        self.assemblyTab.setEnabled(True)
        self.assemblyTab.setStyleSheet(u"")
        self.verticalLayout_200 = QVBoxLayout(self.assemblyTab)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.frame_263 = QFrame(self.assemblyTab)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setEnabled(True)
        self.frame_263.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_263.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_263)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(18, -1, 18, -1)
        self.frame_264 = QFrame(self.frame_263)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMinimumSize(QSize(0, 0))
        self.frame_264.setMaximumSize(QSize(16777215, 100))
        self.frame_264.setStyleSheet(u"")
        self.frame_264.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_264)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.frame_265 = QFrame(self.frame_264)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_265)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, -1)
        self.frame_266 = QFrame(self.frame_265)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMinimumSize(QSize(0, 35))
        self.frame_266.setMaximumSize(QSize(16777215, 35))
        self.frame_266.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_266)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_266)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 35))
        self.label_57.setMaximumSize(QSize(16777215, 35))
        self.label_57.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_111.addWidget(self.label_57)


        self.verticalLayout_169.addWidget(self.frame_266)

        self.frame_267 = QFrame(self.frame_265)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_267)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.frame_268 = QFrame(self.frame_267)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_268)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.frame_269 = QFrame(self.frame_268)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_269)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(20, -1, 0, -1)
        self.frame_270 = QFrame(self.frame_269)
        self.frame_270.setObjectName(u"frame_270")
        sizePolicy2.setHeightForWidth(self.frame_270.sizePolicy().hasHeightForWidth())
        self.frame_270.setSizePolicy(sizePolicy2)
        self.frame_270.setMinimumSize(QSize(40, 0))
        self.frame_270.setMaximumSize(QSize(140, 16777215))
        self.frame_270.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_270)
        self.verticalLayout_171.setSpacing(7)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.frame_270)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(30, 20))
        self.label_179.setMaximumSize(QSize(16777215, 18))
        self.label_179.setFont(font3)
        self.label_179.setStyleSheet(u"")

        self.verticalLayout_171.addWidget(self.label_179)


        self.horizontalLayout_113.addWidget(self.frame_270)

        self.frame_271 = QFrame(self.frame_269)
        self.frame_271.setObjectName(u"frame_271")
        sizePolicy.setHeightForWidth(self.frame_271.sizePolicy().hasHeightForWidth())
        self.frame_271.setSizePolicy(sizePolicy)
        self.frame_271.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_271.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_271)
        self.verticalLayout_172.setSpacing(7)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.xEulerian = QLineEdit(self.frame_271)
        self.xEulerian.setObjectName(u"xEulerian")
        self.xEulerian.setEnabled(False)
        self.xEulerian.setMinimumSize(QSize(160, 20))
        self.xEulerian.setMaximumSize(QSize(180, 16777215))
        self.xEulerian.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_172.addWidget(self.xEulerian)


        self.horizontalLayout_113.addWidget(self.frame_271)


        self.verticalLayout_170.addWidget(self.frame_269)


        self.horizontalLayout_112.addWidget(self.frame_268)

        self.frame_272 = QFrame(self.frame_267)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_272)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(-1, 0, -1, 0)
        self.frame_273 = QFrame(self.frame_272)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_114.setSpacing(20)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(15, -1, 0, -1)
        self.frame_274 = QFrame(self.frame_273)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_274)
        self.horizontalLayout_115.setSpacing(6)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_275 = QFrame(self.frame_274)
        self.frame_275.setObjectName(u"frame_275")
        sizePolicy2.setHeightForWidth(self.frame_275.sizePolicy().hasHeightForWidth())
        self.frame_275.setSizePolicy(sizePolicy2)
        self.frame_275.setMinimumSize(QSize(40, 0))
        self.frame_275.setMaximumSize(QSize(140, 16777215))
        self.frame_275.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_275)
        self.verticalLayout_174.setSpacing(7)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.label_180 = QLabel(self.frame_275)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setMinimumSize(QSize(0, 20))
        self.label_180.setMaximumSize(QSize(16777215, 18))
        self.label_180.setFont(font3)
        self.label_180.setStyleSheet(u"")

        self.verticalLayout_174.addWidget(self.label_180)


        self.horizontalLayout_115.addWidget(self.frame_275)

        self.frame_276 = QFrame(self.frame_274)
        self.frame_276.setObjectName(u"frame_276")
        sizePolicy.setHeightForWidth(self.frame_276.sizePolicy().hasHeightForWidth())
        self.frame_276.setSizePolicy(sizePolicy)
        self.frame_276.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_276.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_276)
        self.verticalLayout_175.setSpacing(7)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.yEulerian = QLineEdit(self.frame_276)
        self.yEulerian.setObjectName(u"yEulerian")
        self.yEulerian.setEnabled(False)
        self.yEulerian.setMinimumSize(QSize(160, 20))
        self.yEulerian.setMaximumSize(QSize(189, 16777215))
        self.yEulerian.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_175.addWidget(self.yEulerian)


        self.horizontalLayout_115.addWidget(self.frame_276)


        self.horizontalLayout_114.addWidget(self.frame_274)


        self.verticalLayout_173.addWidget(self.frame_273)


        self.horizontalLayout_112.addWidget(self.frame_272)


        self.verticalLayout_169.addWidget(self.frame_267)


        self.verticalLayout_168.addWidget(self.frame_265)


        self.verticalLayout_167.addWidget(self.frame_264)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_22)

        self.frame_277 = QFrame(self.frame_263)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setMinimumSize(QSize(0, 0))
        self.frame_277.setMaximumSize(QSize(16777215, 100))
        self.frame_277.setStyleSheet(u"")
        self.frame_277.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_277)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.frame_278 = QFrame(self.frame_277)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_278)
        self.verticalLayout_177.setSpacing(0)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 0, -1)
        self.frame_279 = QFrame(self.frame_278)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(0, 35))
        self.frame_279.setMaximumSize(QSize(16777215, 35))
        self.frame_279.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_279)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_279)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 20))
        self.label_58.setMaximumSize(QSize(16777215, 35))
        self.label_58.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_116.addWidget(self.label_58)


        self.verticalLayout_177.addWidget(self.frame_279)

        self.frame_280 = QFrame(self.frame_278)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_280)
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.frame_281 = QFrame(self.frame_280)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_281)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.frame_282 = QFrame(self.frame_281)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(20, -1, 0, -1)
        self.frame_283 = QFrame(self.frame_282)
        self.frame_283.setObjectName(u"frame_283")
        sizePolicy2.setHeightForWidth(self.frame_283.sizePolicy().hasHeightForWidth())
        self.frame_283.setSizePolicy(sizePolicy2)
        self.frame_283.setMinimumSize(QSize(40, 0))
        self.frame_283.setMaximumSize(QSize(140, 16777215))
        self.frame_283.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_283)
        self.verticalLayout_179.setSpacing(7)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.frame_283)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMinimumSize(QSize(0, 20))
        self.label_172.setMaximumSize(QSize(16777215, 18))
        self.label_172.setFont(font3)
        self.label_172.setStyleSheet(u"")

        self.verticalLayout_179.addWidget(self.label_172)


        self.horizontalLayout_118.addWidget(self.frame_283)

        self.frame_284 = QFrame(self.frame_282)
        self.frame_284.setObjectName(u"frame_284")
        sizePolicy.setHeightForWidth(self.frame_284.sizePolicy().hasHeightForWidth())
        self.frame_284.setSizePolicy(sizePolicy)
        self.frame_284.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_284.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frame_284)
        self.verticalLayout_180.setSpacing(7)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.xTool = QLineEdit(self.frame_284)
        self.xTool.setObjectName(u"xTool")
        self.xTool.setEnabled(False)
        self.xTool.setMinimumSize(QSize(160, 20))
        self.xTool.setMaximumSize(QSize(180, 16777215))
        self.xTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_180.addWidget(self.xTool)


        self.horizontalLayout_118.addWidget(self.frame_284)


        self.verticalLayout_178.addWidget(self.frame_282)


        self.horizontalLayout_117.addWidget(self.frame_281)

        self.frame_285 = QFrame(self.frame_280)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_285)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(-1, 0, -1, 0)
        self.frame_286 = QFrame(self.frame_285)
        self.frame_286.setObjectName(u"frame_286")
        self.frame_286.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_286.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_286)
        self.horizontalLayout_119.setSpacing(20)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(15, -1, 0, -1)
        self.frame_287 = QFrame(self.frame_286)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_287)
        self.horizontalLayout_120.setSpacing(6)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.frame_288 = QFrame(self.frame_287)
        self.frame_288.setObjectName(u"frame_288")
        sizePolicy2.setHeightForWidth(self.frame_288.sizePolicy().hasHeightForWidth())
        self.frame_288.setSizePolicy(sizePolicy2)
        self.frame_288.setMinimumSize(QSize(40, 0))
        self.frame_288.setMaximumSize(QSize(140, 16777215))
        self.frame_288.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_288)
        self.verticalLayout_182.setSpacing(7)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.label_173 = QLabel(self.frame_288)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMinimumSize(QSize(0, 20))
        self.label_173.setMaximumSize(QSize(16777215, 18))
        self.label_173.setFont(font3)
        self.label_173.setStyleSheet(u"")

        self.verticalLayout_182.addWidget(self.label_173)


        self.horizontalLayout_120.addWidget(self.frame_288)

        self.frame_289 = QFrame(self.frame_287)
        self.frame_289.setObjectName(u"frame_289")
        sizePolicy.setHeightForWidth(self.frame_289.sizePolicy().hasHeightForWidth())
        self.frame_289.setSizePolicy(sizePolicy)
        self.frame_289.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_289.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_289.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_289)
        self.verticalLayout_183.setSpacing(7)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(0, 0, 0, 0)
        self.yTool = QLineEdit(self.frame_289)
        self.yTool.setObjectName(u"yTool")
        self.yTool.setEnabled(False)
        self.yTool.setMinimumSize(QSize(160, 20))
        self.yTool.setMaximumSize(QSize(189, 16777215))
        self.yTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_183.addWidget(self.yTool)


        self.horizontalLayout_120.addWidget(self.frame_289)


        self.horizontalLayout_119.addWidget(self.frame_287)


        self.verticalLayout_181.addWidget(self.frame_286)


        self.horizontalLayout_117.addWidget(self.frame_285)


        self.verticalLayout_177.addWidget(self.frame_280)


        self.verticalLayout_176.addWidget(self.frame_278)


        self.verticalLayout_167.addWidget(self.frame_277)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_23)

        self.frame_290 = QFrame(self.frame_263)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(0, 0))
        self.frame_290.setMaximumSize(QSize(16777215, 100))
        self.frame_290.setStyleSheet(u"")
        self.frame_290.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.frame_290)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.frame_291 = QFrame(self.frame_290)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_291.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_291)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, -1)
        self.frame_292 = QFrame(self.frame_291)
        self.frame_292.setObjectName(u"frame_292")
        self.frame_292.setMinimumSize(QSize(0, 35))
        self.frame_292.setMaximumSize(QSize(16777215, 35))
        self.frame_292.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_292.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_292)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_292)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 35))
        self.label_59.setMaximumSize(QSize(16777215, 35))
        self.label_59.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_121.addWidget(self.label_59)


        self.verticalLayout_185.addWidget(self.frame_292)

        self.frame_293 = QFrame(self.frame_291)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_293)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_294 = QFrame(self.frame_293)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_294.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.frame_294)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.frame_295 = QFrame(self.frame_294)
        self.frame_295.setObjectName(u"frame_295")
        self.frame_295.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_295)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(20, -1, 0, -1)
        self.frame_296 = QFrame(self.frame_295)
        self.frame_296.setObjectName(u"frame_296")
        sizePolicy.setHeightForWidth(self.frame_296.sizePolicy().hasHeightForWidth())
        self.frame_296.setSizePolicy(sizePolicy)
        self.frame_296.setMaximumSize(QSize(220, 16777215))
        self.frame_296.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_296.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.frame_296)
        self.verticalLayout_187.setSpacing(7)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.frame_296)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(0, 20))
        self.label_159.setMaximumSize(QSize(16777215, 18))
        self.label_159.setFont(font3)
        self.label_159.setStyleSheet(u"")

        self.verticalLayout_187.addWidget(self.label_159)


        self.horizontalLayout_123.addWidget(self.frame_296)

        self.frame_297 = QFrame(self.frame_295)
        self.frame_297.setObjectName(u"frame_297")
        sizePolicy2.setHeightForWidth(self.frame_297.sizePolicy().hasHeightForWidth())
        self.frame_297.setSizePolicy(sizePolicy2)
        self.frame_297.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.frame_297.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_297.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.frame_297)
        self.verticalLayout_188.setSpacing(7)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.overWorkpiece = QLineEdit(self.frame_297)
        self.overWorkpiece.setObjectName(u"overWorkpiece")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.overWorkpiece.sizePolicy().hasHeightForWidth())
        self.overWorkpiece.setSizePolicy(sizePolicy3)
        self.overWorkpiece.setMinimumSize(QSize(160, 20))
        self.overWorkpiece.setMaximumSize(QSize(180, 16777215))
        self.overWorkpiece.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_188.addWidget(self.overWorkpiece)


        self.horizontalLayout_123.addWidget(self.frame_297)


        self.verticalLayout_186.addWidget(self.frame_295)


        self.horizontalLayout_122.addWidget(self.frame_294)

        self.frame_298 = QFrame(self.frame_293)
        self.frame_298.setObjectName(u"frame_298")
        self.frame_298.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_298.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.frame_298)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(-1, 0, -1, 0)
        self.frame_299 = QFrame(self.frame_298)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_299)
        self.horizontalLayout_124.setSpacing(20)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(15, -1, 0, -1)
        self.frame_300 = QFrame(self.frame_299)
        self.frame_300.setObjectName(u"frame_300")
        self.frame_300.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_300.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_300)
        self.horizontalLayout_125.setSpacing(6)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.frame_301 = QFrame(self.frame_300)
        self.frame_301.setObjectName(u"frame_301")
        sizePolicy.setHeightForWidth(self.frame_301.sizePolicy().hasHeightForWidth())
        self.frame_301.setSizePolicy(sizePolicy)
        self.frame_301.setMaximumSize(QSize(170, 16777215))
        self.frame_301.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.frame_301)
        self.verticalLayout_190.setSpacing(7)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.frame_301)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMinimumSize(QSize(220, 20))
        self.label_160.setMaximumSize(QSize(16777215, 18))
        self.label_160.setFont(font3)
        self.label_160.setStyleSheet(u"")

        self.verticalLayout_190.addWidget(self.label_160)


        self.horizontalLayout_125.addWidget(self.frame_301)

        self.frame_302 = QFrame(self.frame_300)
        self.frame_302.setObjectName(u"frame_302")
        sizePolicy.setHeightForWidth(self.frame_302.sizePolicy().hasHeightForWidth())
        self.frame_302.setSizePolicy(sizePolicy)
        self.frame_302.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_302.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_302.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.frame_302)
        self.verticalLayout_191.setSpacing(7)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.fromTool = QLineEdit(self.frame_302)
        self.fromTool.setObjectName(u"fromTool")
        self.fromTool.setMinimumSize(QSize(160, 20))
        self.fromTool.setMaximumSize(QSize(189, 16777215))
        self.fromTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_191.addWidget(self.fromTool)


        self.horizontalLayout_125.addWidget(self.frame_302)


        self.horizontalLayout_124.addWidget(self.frame_300)


        self.verticalLayout_189.addWidget(self.frame_299)


        self.horizontalLayout_122.addWidget(self.frame_298)


        self.verticalLayout_185.addWidget(self.frame_293)


        self.verticalLayout_184.addWidget(self.frame_291)


        self.verticalLayout_167.addWidget(self.frame_290)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_24)

        self.frame_303 = QFrame(self.frame_263)
        self.frame_303.setObjectName(u"frame_303")
        self.frame_303.setMinimumSize(QSize(0, 0))
        self.frame_303.setMaximumSize(QSize(16777215, 100))
        self.frame_303.setStyleSheet(u"")
        self.frame_303.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_303.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.frame_303)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(0, 0, 0, 0)
        self.frame_304 = QFrame(self.frame_303)
        self.frame_304.setObjectName(u"frame_304")
        self.frame_304.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_304.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.frame_304)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, -1)
        self.frame_305 = QFrame(self.frame_304)
        self.frame_305.setObjectName(u"frame_305")
        self.frame_305.setMinimumSize(QSize(0, 35))
        self.frame_305.setMaximumSize(QSize(16777215, 35))
        self.frame_305.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_305.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_305)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_305)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 35))
        self.label_60.setMaximumSize(QSize(16777215, 35))
        self.label_60.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_126.addWidget(self.label_60)


        self.verticalLayout_193.addWidget(self.frame_305)

        self.frame_306 = QFrame(self.frame_304)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_306)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_307 = QFrame(self.frame_306)
        self.frame_307.setObjectName(u"frame_307")
        self.frame_307.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_307.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.frame_307)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.frame_308 = QFrame(self.frame_307)
        self.frame_308.setObjectName(u"frame_308")
        self.frame_308.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_308)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(20, -1, 0, -1)
        self.frame_309 = QFrame(self.frame_308)
        self.frame_309.setObjectName(u"frame_309")
        sizePolicy.setHeightForWidth(self.frame_309.sizePolicy().hasHeightForWidth())
        self.frame_309.setSizePolicy(sizePolicy)
        self.frame_309.setMaximumSize(QSize(140, 16777215))
        self.frame_309.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_309.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.frame_309)
        self.verticalLayout_195.setSpacing(7)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.label_174 = QLabel(self.frame_309)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMinimumSize(QSize(0, 20))
        self.label_174.setMaximumSize(QSize(16777215, 18))
        self.label_174.setFont(font3)
        self.label_174.setStyleSheet(u"")

        self.verticalLayout_195.addWidget(self.label_174)


        self.horizontalLayout_128.addWidget(self.frame_309)

        self.frame_310 = QFrame(self.frame_308)
        self.frame_310.setObjectName(u"frame_310")
        sizePolicy.setHeightForWidth(self.frame_310.sizePolicy().hasHeightForWidth())
        self.frame_310.setSizePolicy(sizePolicy)
        self.frame_310.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_310.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_310.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.frame_310)
        self.verticalLayout_196.setSpacing(7)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.feed = QLineEdit(self.frame_310)
        self.feed.setObjectName(u"feed")
        self.feed.setMinimumSize(QSize(160, 20))
        self.feed.setMaximumSize(QSize(180, 16777215))
        self.feed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_196.addWidget(self.feed)


        self.horizontalLayout_128.addWidget(self.frame_310)


        self.verticalLayout_194.addWidget(self.frame_308)


        self.horizontalLayout_127.addWidget(self.frame_307)

        self.frame_311 = QFrame(self.frame_306)
        self.frame_311.setObjectName(u"frame_311")
        self.frame_311.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_311.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.frame_311)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(-1, 0, -1, 0)
        self.frame_312 = QFrame(self.frame_311)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_312)
        self.horizontalLayout_129.setSpacing(20)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(15, -1, 0, -1)
        self.frame_313 = QFrame(self.frame_312)
        self.frame_313.setObjectName(u"frame_313")
        self.frame_313.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_313.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_313)
        self.horizontalLayout_130.setSpacing(6)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_314 = QFrame(self.frame_313)
        self.frame_314.setObjectName(u"frame_314")
        sizePolicy.setHeightForWidth(self.frame_314.sizePolicy().hasHeightForWidth())
        self.frame_314.setSizePolicy(sizePolicy)
        self.frame_314.setMaximumSize(QSize(140, 16777215))
        self.frame_314.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.frame_314)
        self.verticalLayout_198.setSpacing(7)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_314)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 20))

        self.verticalLayout_198.addWidget(self.label_61)


        self.horizontalLayout_130.addWidget(self.frame_314)

        self.frame_315 = QFrame(self.frame_313)
        self.frame_315.setObjectName(u"frame_315")
        sizePolicy.setHeightForWidth(self.frame_315.sizePolicy().hasHeightForWidth())
        self.frame_315.setSizePolicy(sizePolicy)
        self.frame_315.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_315.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_315.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_199 = QVBoxLayout(self.frame_315)
        self.verticalLayout_199.setSpacing(7)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.timePeriod = QLineEdit(self.frame_315)
        self.timePeriod.setObjectName(u"timePeriod")
        self.timePeriod.setMinimumSize(QSize(160, 20))
        self.timePeriod.setMaximumSize(QSize(180, 16777215))
        self.timePeriod.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_199.addWidget(self.timePeriod)


        self.horizontalLayout_130.addWidget(self.frame_315)


        self.horizontalLayout_129.addWidget(self.frame_313)


        self.verticalLayout_197.addWidget(self.frame_312)


        self.horizontalLayout_127.addWidget(self.frame_311)


        self.verticalLayout_193.addWidget(self.frame_306)


        self.verticalLayout_192.addWidget(self.frame_304)


        self.verticalLayout_167.addWidget(self.frame_303)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_25)

        self.assemblyWarning = QLabel(self.frame_263)
        self.assemblyWarning.setObjectName(u"assemblyWarning")
        self.assemblyWarning.setFont(font4)
        self.assemblyWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.assemblyWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.assemblyWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_167.addWidget(self.assemblyWarning)

        self.verticalSpacer_26 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_26)


        self.verticalLayout_200.addWidget(self.frame_263)

        self.tabWidget.addTab(self.assemblyTab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_129.addWidget(self.tabWidget)

        self.frame_259 = QFrame(self.frame_201)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setMinimumSize(QSize(0, 60))
        self.frame_259.setMaximumSize(QSize(16777215, 60))
        self.frame_259.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        self.frame_259.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_259)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.frame_260 = QFrame(self.frame_259)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setMinimumSize(QSize(351, 0))
        self.frame_260.setMaximumSize(QSize(351, 81))
        self.frame_260.setStyleSheet(u"")
        self.frame_260.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_260)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.returnButton = QPushButton(self.frame_260)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setEnabled(True)
        self.returnButton.setMinimumSize(QSize(100, 36))
        self.returnButton.setMaximumSize(QSize(100, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Yu Gothic"])
        font5.setBold(True)
        self.returnButton.setFont(font5)
        self.returnButton.setStyleSheet(u"")

        self.horizontalLayout_110.addWidget(self.returnButton)

        self.applyButton = QPushButton(self.frame_260)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setEnabled(True)
        self.applyButton.setMinimumSize(QSize(100, 36))
        self.applyButton.setMaximumSize(QSize(150, 16777215))
        self.applyButton.setFont(font5)

        self.horizontalLayout_110.addWidget(self.applyButton)

        self.saveButton = QPushButton(self.frame_260)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setMinimumSize(QSize(100, 36))
        self.saveButton.setMaximumSize(QSize(150, 16777215))
        self.saveButton.setFont(font5)
        self.saveButton.setStyleSheet(u"")

        self.horizontalLayout_110.addWidget(self.saveButton)


        self.horizontalLayout_109.addWidget(self.frame_260)


        self.verticalLayout_129.addWidget(self.frame_259)


        self.horizontalLayout_88.addWidget(self.frame_201)

        self.frame_261 = QFrame(self.frame_200)
        self.frame_261.setObjectName(u"frame_261")
        sizePolicy.setHeightForWidth(self.frame_261.sizePolicy().hasHeightForWidth())
        self.frame_261.setSizePolicy(sizePolicy)
        self.frame_261.setMinimumSize(QSize(634, 645))
        self.frame_261.setStyleSheet(u"background-color: rgb(237,237,237);\n"
"border-radius: 10px;")
        self.frame_261.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_261.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_261)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.frame_262 = QFrame(self.frame_261)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"	border: 3px solid #3498db;\n"
"}")
        self.frame_262.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_262)
        self.verticalLayout_165.setSpacing(0)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(9, 0, -1, 1)
        self.plot = QFrame(self.frame_262)
        self.plot.setObjectName(u"plot")
        self.plot.setEnabled(True)
        self.plot.setMinimumSize(QSize(600, 600))
        self.plot.setStyleSheet(u"QFrame {\n"
"     border-radius: 0 px; \n"
"	 border: 0px solid #3498db;\n"
"}")
        self.plot.setFrameShape(QFrame.Shape.StyledPanel)
        self.plot.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_165.addWidget(self.plot)


        self.verticalLayout_164.addWidget(self.frame_262)


        self.horizontalLayout_88.addWidget(self.frame_261)


        self.verticalLayout_128.addWidget(self.frame_200)


        self.verticalLayout_166.addWidget(self.frame_157)

        self.pages.addWidget(self.geometryPage)
        self.iteratePage = QWidget()
        self.iteratePage.setObjectName(u"iteratePage")
        self.iteratePage.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #5e5c58;\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	border: 2px solid  #5a83c6;\n"
"}\n"
"\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/Icons/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/Icons/down.png);\n"
"	width : 12px;\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.iteratePage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_130 = QFrame(self.iteratePage)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(0, 78))
        self.frame_130.setMaximumSize(QSize(16777215, 78))
        self.frame_130.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}	\n"
"")
        self.frame_130.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_55.setSpacing(9)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(9, 0, 9, 0)
        self.label_17 = QLabel(self.frame_130)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(60, 60))
        self.label_17.setMaximumSize(QSize(60, 60))
        self.label_17.setPixmap(QPixmap(u":/icons/Icons/process.png"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_55.addWidget(self.label_17)

        self.label_4 = QLabel(self.frame_130)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 80))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_55.addWidget(self.label_4)


        self.verticalLayout_12.addWidget(self.frame_130)

        self.frame_14 = QFrame(self.iteratePage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.infoFrame = QFrame(self.frame_14)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setEnabled(True)
        self.infoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.infoFrame.setStyleSheet(u"")
        self.infoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.infoFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_7)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy4)
        self.frame_66.setMinimumSize(QSize(520, 0))
        self.frame_66.setMaximumSize(QSize(16777215, 16777215))
        self.frame_66.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"QLabel {\n"
"    font-size: 18px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"")
        self.frame_66.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_66)
        self.verticalLayout_47.setSpacing(15)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(9, 20, 9, -1)
        self.frameParameter01_11 = QFrame(self.frame_66)
        self.frameParameter01_11.setObjectName(u"frameParameter01_11")
        self.frameParameter01_11.setEnabled(True)
        self.frameParameter01_11.setMinimumSize(QSize(0, 0))
        self.frameParameter01_11.setMaximumSize(QSize(16777215, 100))
        self.frameParameter01_11.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.frameParameter01_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frameParameter01_11)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.frameParameter01_11)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(0, 40))
        self.frame_137.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(9, 0, 9, 0)
        self.label_127 = QLabel(self.frame_137)
        self.label_127.setObjectName(u"label_127")
        font6 = QFont()
        font6.setFamilies([u"Yu Gothic UI Semilight"])
        font6.setBold(True)
        self.label_127.setFont(font6)

        self.horizontalLayout_70.addWidget(self.label_127)

        self.inpPathButton = QPushButton(self.frame_137)
        self.inpPathButton.setObjectName(u"inpPathButton")
        self.inpPathButton.setMinimumSize(QSize(30, 30))
        self.inpPathButton.setMaximumSize(QSize(30, 30))
        self.inpPathButton.setStyleSheet(u"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 25px;\n"
"	font-family: \"Yu Gothic\";\n"
"	icon-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.inpPathButton.setIcon(icon1)

        self.horizontalLayout_70.addWidget(self.inpPathButton)


        self.verticalLayout_107.addWidget(self.frame_137)

        self.pathOutput = QFrame(self.frameParameter01_11)
        self.pathOutput.setObjectName(u"pathOutput")
        self.pathOutput.setFrameShape(QFrame.Shape.StyledPanel)
        self.pathOutput.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pathOutput)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.inpLabel = QLabel(self.pathOutput)
        self.inpLabel.setObjectName(u"inpLabel")
        self.inpLabel.setMinimumSize(QSize(0, 20))
        self.inpLabel.setMaximumSize(QSize(16777215, 20))
        self.inpLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.inpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.inpLabel)


        self.verticalLayout_107.addWidget(self.pathOutput)


        self.verticalLayout_47.addWidget(self.frameParameter01_11)

        self.frame_15 = QFrame(self.frame_66)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 250))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setSpacing(9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_204 = QFrame(self.frame_15)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMaximumSize(QSize(16777215, 50))
        self.frame_204.setStyleSheet(u"")
        self.frame_204.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_39 = QLabel(self.frame_204)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font6)

        self.horizontalLayout_47.addWidget(self.label_39)

        self.numberOfVariables = QComboBox(self.frame_204)
        self.numberOfVariables.addItem("")
        self.numberOfVariables.addItem("")
        self.numberOfVariables.addItem("")
        self.numberOfVariables.setObjectName(u"numberOfVariables")
        self.numberOfVariables.setMinimumSize(QSize(60, 20))
        self.numberOfVariables.setMaximumSize(QSize(60, 20))
        self.numberOfVariables.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.numberOfVariables.setStyleSheet(u"QComboBox {\n"
"	padding-left: 10px;\n"
"}")
        self.numberOfVariables.setFrame(True)

        self.horizontalLayout_47.addWidget(self.numberOfVariables)


        self.verticalLayout_14.addWidget(self.frame_204)

        self.frameParameter01 = QFrame(self.frame_15)
        self.frameParameter01.setObjectName(u"frameParameter01")
        self.frameParameter01.setEnabled(True)
        self.frameParameter01.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.frameParameter01.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frameParameter01)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.frameParameter01)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_43 = QLabel(self.frame_128)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font6)

        self.horizontalLayout_54.addWidget(self.label_43)

        self.P01 = QComboBox(self.frame_128)
        self.P01.addItem("")
        self.P01.addItem("")
        self.P01.addItem("")
        self.P01.addItem("")
        self.P01.addItem("")
        self.P01.setObjectName(u"P01")
        self.P01.setEnabled(False)
        self.P01.setMinimumSize(QSize(0, 20))
        self.P01.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_54.addWidget(self.P01)


        self.verticalLayout_100.addWidget(self.frame_128)

        self.frame_67 = QFrame(self.frameParameter01)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_44.setSpacing(10)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_44 = QLabel(self.frame_67)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_44.addWidget(self.label_44)

        self.minP01 = QLineEdit(self.frame_67)
        self.minP01.setObjectName(u"minP01")
        self.minP01.setEnabled(False)
        self.minP01.setMinimumSize(QSize(0, 20))
        self.minP01.setMaximumSize(QSize(16777215, 20))
        self.minP01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.minP01)

        self.label_45 = QLabel(self.frame_67)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_44.addWidget(self.label_45)

        self.maxP01 = QLineEdit(self.frame_67)
        self.maxP01.setObjectName(u"maxP01")
        self.maxP01.setEnabled(False)
        self.maxP01.setMinimumSize(QSize(0, 20))
        self.maxP01.setMaximumSize(QSize(16777215, 20))
        self.maxP01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.maxP01)

        self.label_46 = QLabel(self.frame_67)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_44.addWidget(self.label_46)

        self.stepP01 = QComboBox(self.frame_67)
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.addItem("")
        self.stepP01.setObjectName(u"stepP01")
        self.stepP01.setEnabled(False)
        self.stepP01.setMinimumSize(QSize(0, 20))
        self.stepP01.setMaximumSize(QSize(16777215, 20))
        self.stepP01.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stepP01.setStyleSheet(u"QComboBox {\n"
"	padding-left: 23px;\n"
"}")
        self.stepP01.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.stepP01.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_44.addWidget(self.stepP01)


        self.verticalLayout_100.addWidget(self.frame_67)


        self.verticalLayout_14.addWidget(self.frameParameter01)

        self.frameParameter01_2 = QFrame(self.frame_15)
        self.frameParameter01_2.setObjectName(u"frameParameter01_2")
        self.frameParameter01_2.setEnabled(True)
        self.frameParameter01_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.frameParameter01_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frameParameter01_2)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_155 = QFrame(self.frameParameter01_2)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setEnabled(True)
        self.frame_155.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_28 = QLabel(self.frame_155)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font6)

        self.horizontalLayout_79.addWidget(self.label_28)

        self.P02 = QComboBox(self.frame_155)
        self.P02.addItem("")
        self.P02.addItem("")
        self.P02.addItem("")
        self.P02.addItem("")
        self.P02.addItem("")
        self.P02.setObjectName(u"P02")
        self.P02.setEnabled(False)
        self.P02.setMinimumSize(QSize(0, 20))
        self.P02.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_79.addWidget(self.P02)


        self.verticalLayout_130.addWidget(self.frame_155)

        self.frame_156 = QFrame(self.frameParameter01_2)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_156)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.frame_202 = QFrame(self.frame_156)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_202)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_29 = QLabel(self.frame_202)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_46.addWidget(self.label_29)

        self.minP02 = QLineEdit(self.frame_202)
        self.minP02.setObjectName(u"minP02")
        self.minP02.setEnabled(False)
        self.minP02.setMinimumSize(QSize(0, 20))
        self.minP02.setMaximumSize(QSize(16777215, 20))
        self.minP02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_46.addWidget(self.minP02)

        self.label_31 = QLabel(self.frame_202)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_46.addWidget(self.label_31)

        self.maxP02 = QLineEdit(self.frame_202)
        self.maxP02.setObjectName(u"maxP02")
        self.maxP02.setEnabled(False)
        self.maxP02.setMinimumSize(QSize(0, 20))
        self.maxP02.setMaximumSize(QSize(16777215, 20))
        self.maxP02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_46.addWidget(self.maxP02)

        self.label_37 = QLabel(self.frame_202)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_46.addWidget(self.label_37)

        self.stepP02 = QComboBox(self.frame_202)
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.addItem("")
        self.stepP02.setObjectName(u"stepP02")
        self.stepP02.setEnabled(False)
        self.stepP02.setMinimumSize(QSize(0, 20))
        self.stepP02.setMaximumSize(QSize(16777215, 20))
        self.stepP02.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stepP02.setStyleSheet(u"QComboBox {\n"
"	padding-left: 23px;\n"
"}")
        self.stepP02.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.stepP02.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_46.addWidget(self.stepP02)


        self.horizontalLayout_80.addWidget(self.frame_202)


        self.verticalLayout_130.addWidget(self.frame_156)


        self.verticalLayout_14.addWidget(self.frameParameter01_2)


        self.verticalLayout_47.addWidget(self.frame_15)

        self.iterationWarning = QFrame(self.frame_66)
        self.iterationWarning.setObjectName(u"iterationWarning")
        self.iterationWarning.setFrameShape(QFrame.Shape.StyledPanel)
        self.iterationWarning.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.iterationWarning)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelIterationWarning = QLabel(self.iterationWarning)
        self.labelIterationWarning.setObjectName(u"labelIterationWarning")
        self.labelIterationWarning.setMinimumSize(QSize(0, 20))
        self.labelIterationWarning.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font-size: 12px;")
        self.labelIterationWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelIterationWarning)


        self.verticalLayout_47.addWidget(self.iterationWarning)

        self.frame_13 = QFrame(self.frame_66)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.applyIteration = QPushButton(self.frame_13)
        self.applyIteration.setObjectName(u"applyIteration")
        self.applyIteration.setMinimumSize(QSize(50, 36))
        self.applyIteration.setMaximumSize(QSize(115, 16777215))
        self.applyIteration.setFont(font5)

        self.horizontalLayout_7.addWidget(self.applyIteration)


        self.verticalLayout_47.addWidget(self.frame_13)


        self.horizontalLayout_4.addWidget(self.frame_66)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.simulationSetup = QFrame(self.infoFrame)
        self.simulationSetup.setObjectName(u"simulationSetup")
        self.simulationSetup.setMinimumSize(QSize(0, 250))
        self.simulationSetup.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"QLabel {\n"
"    font-size: 18px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.simulationSetup.setFrameShape(QFrame.Shape.StyledPanel)
        self.simulationSetup.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.simulationSetup)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frameParameter01_12 = QFrame(self.simulationSetup)
        self.frameParameter01_12.setObjectName(u"frameParameter01_12")
        self.frameParameter01_12.setEnabled(True)
        self.frameParameter01_12.setMinimumSize(QSize(0, 0))
        self.frameParameter01_12.setMaximumSize(QSize(16777215, 100))
        self.frameParameter01_12.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"")
        self.frameParameter01_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frameParameter01_12)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frameParameter01_12)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 40))
        self.frame_138.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(9, 0, 9, 0)
        self.label_128 = QLabel(self.frame_138)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font6)

        self.horizontalLayout_71.addWidget(self.label_128)

        self.coreLabel = QLabel(self.frame_138)
        self.coreLabel.setObjectName(u"coreLabel")
        self.coreLabel.setMinimumSize(QSize(0, 20))
        self.coreLabel.setMaximumSize(QSize(100, 20))
        self.coreLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.coreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_71.addWidget(self.coreLabel)


        self.verticalLayout_108.addWidget(self.frame_138)

        self.frame_12 = QFrame(self.frameParameter01_12)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.label_129 = QLabel(self.frame_12)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font6)

        self.horizontalLayout_6.addWidget(self.label_129)

        self.numberSimulation = QLabel(self.frame_12)
        self.numberSimulation.setObjectName(u"numberSimulation")
        self.numberSimulation.setMinimumSize(QSize(0, 20))
        self.numberSimulation.setMaximumSize(QSize(100, 20))
        self.numberSimulation.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.numberSimulation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.numberSimulation)


        self.verticalLayout_108.addWidget(self.frame_12)


        self.verticalLayout_15.addWidget(self.frameParameter01_12)

        self.frame_5 = QFrame(self.simulationSetup)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_343 = QFrame(self.frame_5)
        self.frame_343.setObjectName(u"frame_343")
        self.frame_343.setMaximumSize(QSize(16777215, 50))
        self.frame_343.setStyleSheet(u"")
        self.frame_343.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_343.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_343)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_69 = QLabel(self.frame_343)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font6)

        self.horizontalLayout_56.addWidget(self.label_69)

        self.numberofPararelSimulations = QComboBox(self.frame_343)
        self.numberofPararelSimulations.addItem("")
        self.numberofPararelSimulations.setObjectName(u"numberofPararelSimulations")
        self.numberofPararelSimulations.setMinimumSize(QSize(60, 20))
        self.numberofPararelSimulations.setMaximumSize(QSize(60, 20))
        self.numberofPararelSimulations.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.numberofPararelSimulations.setStyleSheet(u"QComboBox {\n"
"	padding-left: 10px;\n"
"}")
        self.numberofPararelSimulations.setFrame(True)

        self.horizontalLayout_56.addWidget(self.numberofPararelSimulations)


        self.verticalLayout_10.addWidget(self.frame_343)

        self.frame_139 = QFrame(self.frame_5)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_70 = QLabel(self.frame_139)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font6)

        self.horizontalLayout_69.addWidget(self.label_70)

        self.core = QComboBox(self.frame_139)
        self.core.addItem("")
        self.core.setObjectName(u"core")
        self.core.setMinimumSize(QSize(60, 20))
        self.core.setMaximumSize(QSize(60, 20))
        self.core.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.core.setStyleSheet(u"QComboBox {\n"
"	padding-left: 10px;\n"
"}")
        self.core.setFrame(True)

        self.horizontalLayout_69.addWidget(self.core)


        self.verticalLayout_10.addWidget(self.frame_139)


        self.verticalLayout_15.addWidget(self.frame_5)


        self.verticalLayout_13.addWidget(self.simulationSetup)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.buttonsFrame = QFrame(self.infoFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setMinimumSize(QSize(0, 60))
        self.buttonsFrame.setMaximumSize(QSize(16777215, 60))
        self.buttonsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        self.buttonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_206 = QFrame(self.buttonsFrame)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMinimumSize(QSize(0, 0))
        self.frame_206.setMaximumSize(QSize(351, 81))
        self.frame_206.setStyleSheet(u"")
        self.frame_206.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.returnIterationButton = QPushButton(self.frame_206)
        self.returnIterationButton.setObjectName(u"returnIterationButton")
        self.returnIterationButton.setEnabled(True)
        self.returnIterationButton.setMinimumSize(QSize(50, 36))
        self.returnIterationButton.setMaximumSize(QSize(115, 16777215))
        self.returnIterationButton.setFont(font5)
        self.returnIterationButton.setStyleSheet(u"")

        self.horizontalLayout_82.addWidget(self.returnIterationButton)

        self.saveAndRunButton = QPushButton(self.frame_206)
        self.saveAndRunButton.setObjectName(u"saveAndRunButton")
        self.saveAndRunButton.setMinimumSize(QSize(50, 36))
        self.saveAndRunButton.setMaximumSize(QSize(115, 16777215))
        self.saveAndRunButton.setFont(font5)

        self.horizontalLayout_82.addWidget(self.saveAndRunButton)


        self.horizontalLayout_81.addWidget(self.frame_206)


        self.verticalLayout_13.addWidget(self.buttonsFrame)


        self.horizontalLayout_5.addWidget(self.infoFrame)

        self.frame_481 = QFrame(self.frame_14)
        self.frame_481.setObjectName(u"frame_481")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_481.sizePolicy().hasHeightForWidth())
        self.frame_481.setSizePolicy(sizePolicy5)
        self.frame_481.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"	border: 3px solid #3498db;\n"
"}")
        self.frame_481.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_481.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_316 = QVBoxLayout(self.frame_481)
        self.verticalLayout_316.setSpacing(0)
        self.verticalLayout_316.setObjectName(u"verticalLayout_316")
        self.verticalLayout_316.setContentsMargins(9, 0, -1, 1)
        self.plotResults = QFrame(self.frame_481)
        self.plotResults.setObjectName(u"plotResults")
        self.plotResults.setMinimumSize(QSize(600, 600))
        self.plotResults.setStyleSheet(u"QFrame {\n"
"     border-radius: 0 px; \n"
"	 border: 0px solid #3498db;\n"
"}")
        self.plotResults.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotResults.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_316.addWidget(self.plotResults)


        self.horizontalLayout_5.addWidget(self.frame_481)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.frame_73 = QFrame(self.iteratePage)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy6)
        self.frame_73.setMinimumSize(QSize(0, 0))
        self.frame_73.setMaximumSize(QSize(16777215, 16777215))
        self.frame_73.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_73)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.frame_73)

        self.pages.addWidget(self.iteratePage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.resultsPage.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #5e5c58;\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	border: 2px solid  #5a83c6;\n"
"}\n"
"\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/Icons/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/Icons/down.png);\n"
"	width : 12px;\n"
"}\n"
"\n"
"")
        self.vboxLayout = QVBoxLayout(self.resultsPage)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.resultsPage)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(0, 78))
        self.frame_140.setMaximumSize(QSize(16777215, 78))
        self.frame_140.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"}	\n"
"")
        self.frame_140.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_159.setSpacing(9)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(9, 0, 9, 0)
        self.label_136 = QLabel(self.frame_140)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(60, 60))
        self.label_136.setMaximumSize(QSize(60, 60))
        self.label_136.setPixmap(QPixmap(u":/icons/Icons/process.png"))
        self.label_136.setScaledContents(True)

        self.horizontalLayout_159.addWidget(self.label_136)

        self.label_7 = QLabel(self.frame_140)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 80))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_159.addWidget(self.label_7)


        self.vboxLayout.addWidget(self.frame_140)

        self.frame_80 = QFrame(self.resultsPage)
        self.frame_80.setObjectName(u"frame_80")
        sizePolicy6.setHeightForWidth(self.frame_80.sizePolicy().hasHeightForWidth())
        self.frame_80.setSizePolicy(sizePolicy6)
        self.frame_80.setMinimumSize(QSize(0, 0))
        self.frame_80.setMaximumSize(QSize(16777215, 16777215))
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_80)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)

        self.vboxLayout.addWidget(self.frame_80)

        self.frame_16 = QFrame(self.resultsPage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_484 = QFrame(self.frame_16)
        self.frame_484.setObjectName(u"frame_484")
        sizePolicy5.setHeightForWidth(self.frame_484.sizePolicy().hasHeightForWidth())
        self.frame_484.setSizePolicy(sizePolicy5)
        self.frame_484.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"     background-color: rgb(182, 182, 182);\n"
"     border-radius: 15px; \n"
"	border: 3px solid #3498db;\n"
"}")
        self.frame_484.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_484.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_319 = QVBoxLayout(self.frame_484)
        self.verticalLayout_319.setSpacing(0)
        self.verticalLayout_319.setObjectName(u"verticalLayout_319")
        self.verticalLayout_319.setContentsMargins(9, 0, -1, 1)
        self.plotResult = QFrame(self.frame_484)
        self.plotResult.setObjectName(u"plotResult")
        self.plotResult.setMinimumSize(QSize(600, 600))
        self.plotResult.setStyleSheet(u"QFrame {\n"
"     border-radius: 0 px; \n"
"	 border: 0px solid #3498db;\n"
"}")
        self.plotResult.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotResult.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_319.addWidget(self.plotResult)


        self.horizontalLayout_16.addWidget(self.frame_484)

        self.infoFrame_4 = QFrame(self.frame_16)
        self.infoFrame_4.setObjectName(u"infoFrame_4")
        self.infoFrame_4.setEnabled(True)
        self.infoFrame_4.setMaximumSize(QSize(16777215, 16777215))
        self.infoFrame_4.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"QLabel {\n"
"    font-size: 18px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"")
        self.infoFrame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.infoFrame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.infoFrame_4)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.infoFrame_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_17.setSpacing(9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_28)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy4.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy4)
        self.frame_84.setMinimumSize(QSize(450, 0))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setStyleSheet(u"")
        self.frame_84.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_84)
        self.verticalLayout_64.setSpacing(15)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(9, 20, 9, -1)
        self.frameParameter01_21 = QFrame(self.frame_84)
        self.frameParameter01_21.setObjectName(u"frameParameter01_21")
        self.frameParameter01_21.setEnabled(True)
        self.frameParameter01_21.setMinimumSize(QSize(0, 0))
        self.frameParameter01_21.setMaximumSize(QSize(16777215, 100))
        self.frameParameter01_21.setStyleSheet(u"")
        self.frameParameter01_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frameParameter01_21)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.frame_176 = QFrame(self.frameParameter01_21)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(0, 40))
        self.frame_176.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(9, 0, 9, 0)
        self.label_137 = QLabel(self.frame_176)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font6)

        self.horizontalLayout_160.addWidget(self.label_137)

        self.importResultsButton = QPushButton(self.frame_176)
        self.importResultsButton.setObjectName(u"importResultsButton")
        self.importResultsButton.setMinimumSize(QSize(30, 30))
        self.importResultsButton.setMaximumSize(QSize(30, 30))
        self.importResultsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 25px;\n"
"	font-family: \"Yu Gothic\";\n"
"	icon-size: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        self.importResultsButton.setIcon(icon1)

        self.horizontalLayout_160.addWidget(self.importResultsButton)


        self.verticalLayout_115.addWidget(self.frame_176)

        self.pathOutput_4 = QFrame(self.frameParameter01_21)
        self.pathOutput_4.setObjectName(u"pathOutput_4")
        self.pathOutput_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.pathOutput_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.pathOutput_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, -1, 9, -1)
        self.pathResultsLabel = QLabel(self.pathOutput_4)
        self.pathResultsLabel.setObjectName(u"pathResultsLabel")
        self.pathResultsLabel.setMinimumSize(QSize(0, 20))
        self.pathResultsLabel.setMaximumSize(QSize(16777215, 20))
        self.pathResultsLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pathResultsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.pathResultsLabel)


        self.verticalLayout_115.addWidget(self.pathOutput_4)


        self.verticalLayout_64.addWidget(self.frameParameter01_21)

        self.frameParameter01_24 = QFrame(self.frame_84)
        self.frameParameter01_24.setObjectName(u"frameParameter01_24")
        self.frameParameter01_24.setEnabled(True)
        self.frameParameter01_24.setMinimumSize(QSize(0, 0))
        self.frameParameter01_24.setMaximumSize(QSize(16777215, 100))
        self.frameParameter01_24.setStyleSheet(u"")
        self.frameParameter01_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frameParameter01_24)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.frame_178 = QFrame(self.frameParameter01_24)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 40))
        self.frame_178.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(9, 0, 9, 0)
        self.label_141 = QLabel(self.frame_178)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font6)

        self.horizontalLayout_161.addWidget(self.label_141)


        self.verticalLayout_117.addWidget(self.frame_178)

        self.pathOutput_8 = QFrame(self.frameParameter01_24)
        self.pathOutput_8.setObjectName(u"pathOutput_8")
        self.pathOutput_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.pathOutput_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.pathOutput_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(9, -1, 9, -1)
        self.odbFiles = QComboBox(self.pathOutput_8)
        self.odbFiles.addItem("")
        self.odbFiles.addItem("")
        self.odbFiles.setObjectName(u"odbFiles")
        self.odbFiles.setEnabled(True)
        self.odbFiles.setMinimumSize(QSize(0, 20))
        self.odbFiles.setMaximumSize(QSize(16777215, 20))
        self.odbFiles.setStyleSheet(u"padding: 15px;")

        self.verticalLayout_29.addWidget(self.odbFiles)


        self.verticalLayout_117.addWidget(self.pathOutput_8)


        self.verticalLayout_64.addWidget(self.frameParameter01_24)

        self.resultsInfoLabel = QFrame(self.frame_84)
        self.resultsInfoLabel.setObjectName(u"resultsInfoLabel")
        self.resultsInfoLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.resultsInfoLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.resultsInfoLabel)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_354 = QFrame(self.resultsInfoLabel)
        self.frame_354.setObjectName(u"frame_354")
        self.frame_354.setEnabled(True)
        self.frame_354.setMinimumSize(QSize(0, 80))
        self.frame_354.setMaximumSize(QSize(16777215, 150))
        self.frame_354.setStyleSheet(u"")
        self.frame_354.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_354.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_354)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_138 = QLabel(self.frame_354)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font6)

        self.verticalLayout.addWidget(self.label_138)

        self.typeOfAnalisys = QComboBox(self.frame_354)
        self.typeOfAnalisys.addItem("")
        self.typeOfAnalisys.addItem("")
        self.typeOfAnalisys.addItem("")
        self.typeOfAnalisys.setObjectName(u"typeOfAnalisys")
        self.typeOfAnalisys.setEnabled(True)
        self.typeOfAnalisys.setMinimumSize(QSize(0, 20))
        self.typeOfAnalisys.setMaximumSize(QSize(16777215, 20))
        self.typeOfAnalisys.setStyleSheet(u"padding: 15px;")

        self.verticalLayout.addWidget(self.typeOfAnalisys)


        self.verticalLayout_7.addWidget(self.frame_354)

        self.rfFrame = QFrame(self.resultsInfoLabel)
        self.rfFrame.setObjectName(u"rfFrame")
        self.rfFrame.setMinimumSize(QSize(0, 80))
        self.rfFrame.setMaximumSize(QSize(16777215, 150))
        self.rfFrame.setStyleSheet(u"")
        self.rfFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rfFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.rfFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_140 = QLabel(self.rfFrame)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font6)

        self.verticalLayout_9.addWidget(self.label_140)

        self.typeRF = QComboBox(self.rfFrame)
        self.typeRF.addItem("")
        self.typeRF.setObjectName(u"typeRF")
        self.typeRF.setEnabled(True)
        self.typeRF.setMinimumSize(QSize(0, 20))
        self.typeRF.setMaximumSize(QSize(16777215, 20))
        self.typeRF.setStyleSheet(u"padding: 15px;")

        self.verticalLayout_9.addWidget(self.typeRF)


        self.verticalLayout_7.addWidget(self.rfFrame)


        self.verticalLayout_64.addWidget(self.resultsInfoLabel)

        self.frame_29 = QFrame(self.frame_84)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 250))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_29)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frameParameter01_22 = QFrame(self.frame_29)
        self.frameParameter01_22.setObjectName(u"frameParameter01_22")
        self.frameParameter01_22.setEnabled(True)
        self.frameParameter01_22.setStyleSheet(u"")
        self.frameParameter01_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frameParameter01_22)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_28.addWidget(self.frameParameter01_22)

        self.frameParameter01_23 = QFrame(self.frame_29)
        self.frameParameter01_23.setObjectName(u"frameParameter01_23")
        self.frameParameter01_23.setEnabled(True)
        self.frameParameter01_23.setStyleSheet(u"")
        self.frameParameter01_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameParameter01_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_226 = QVBoxLayout(self.frameParameter01_23)
        self.verticalLayout_226.setSpacing(0)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.verticalLayout_226.setContentsMargins(0, 0, 0, 0)
        self.frame_179 = QFrame(self.frameParameter01_23)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_226.addWidget(self.frame_179)


        self.verticalLayout_28.addWidget(self.frameParameter01_23)


        self.verticalLayout_64.addWidget(self.frame_29)


        self.horizontalLayout_17.addWidget(self.frame_84)


        self.verticalLayout_26.addWidget(self.frame_28)

        self.dataFrame = QFrame(self.infoFrame_4)
        self.dataFrame.setObjectName(u"dataFrame")
        self.dataFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dataFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dataFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_177 = QFrame(self.dataFrame)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_139 = QLabel(self.frame_177)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font6)

        self.horizontalLayout_162.addWidget(self.label_139)


        self.verticalLayout_3.addWidget(self.frame_177)

        self.pathOutput_5 = QFrame(self.dataFrame)
        self.pathOutput_5.setObjectName(u"pathOutput_5")
        self.pathOutput_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.pathOutput_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.pathOutput_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.label_149 = QLabel(self.pathOutput_5)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout.addWidget(self.label_149)

        self.inpLabel_5 = QLabel(self.pathOutput_5)
        self.inpLabel_5.setObjectName(u"inpLabel_5")
        self.inpLabel_5.setMinimumSize(QSize(0, 20))
        self.inpLabel_5.setMaximumSize(QSize(16777215, 20))
        self.inpLabel_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"    font-size: 12px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.inpLabel_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.inpLabel_5)


        self.verticalLayout_3.addWidget(self.pathOutput_5)


        self.verticalLayout_26.addWidget(self.dataFrame)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_6)

        self.frame_357 = QFrame(self.infoFrame_4)
        self.frame_357.setObjectName(u"frame_357")
        self.frame_357.setMinimumSize(QSize(0, 60))
        self.frame_357.setMaximumSize(QSize(16777215, 60))
        self.frame_357.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(108, 166, 240, 255), stop:1 rgba(85, 122, 187, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"	font-family: \"Yu Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b3b3b3; \n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));\n"
"    border: 2px solid #55aaff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}")
        self.frame_357.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_357.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.frame_357)
        self.horizontalLayout_170.setSpacing(0)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.frame_358 = QFrame(self.frame_357)
        self.frame_358.setObjectName(u"frame_358")
        self.frame_358.setMinimumSize(QSize(0, 0))
        self.frame_358.setMaximumSize(QSize(351, 81))
        self.frame_358.setStyleSheet(u"")
        self.frame_358.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_358.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_171 = QHBoxLayout(self.frame_358)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.returnResultsButton = QPushButton(self.frame_358)
        self.returnResultsButton.setObjectName(u"returnResultsButton")
        self.returnResultsButton.setEnabled(True)
        self.returnResultsButton.setMinimumSize(QSize(50, 36))
        self.returnResultsButton.setMaximumSize(QSize(115, 16777215))
        self.returnResultsButton.setFont(font5)
        self.returnResultsButton.setStyleSheet(u"")

        self.horizontalLayout_171.addWidget(self.returnResultsButton)

        self.saveAndRunButton_4 = QPushButton(self.frame_358)
        self.saveAndRunButton_4.setObjectName(u"saveAndRunButton_4")
        self.saveAndRunButton_4.setMinimumSize(QSize(50, 36))
        self.saveAndRunButton_4.setMaximumSize(QSize(115, 16777215))
        self.saveAndRunButton_4.setFont(font5)

        self.horizontalLayout_171.addWidget(self.saveAndRunButton_4)

        self.exportFigureButton = QPushButton(self.frame_358)
        self.exportFigureButton.setObjectName(u"exportFigureButton")
        self.exportFigureButton.setEnabled(True)
        self.exportFigureButton.setMinimumSize(QSize(50, 36))
        self.exportFigureButton.setMaximumSize(QSize(115, 16777215))
        self.exportFigureButton.setFont(font5)
        self.exportFigureButton.setStyleSheet(u"")

        self.horizontalLayout_171.addWidget(self.exportFigureButton)


        self.horizontalLayout_170.addWidget(self.frame_358)


        self.verticalLayout_26.addWidget(self.frame_357)


        self.horizontalLayout_16.addWidget(self.infoFrame_4)


        self.vboxLayout.addWidget(self.frame_16)

        self.pages.addWidget(self.resultsPage)

        self.verticalLayout_44.addWidget(self.pages)

        self.label_15 = QLabel(self.frame_123)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"color: rgba(97, 97, 97, 97);\n"
"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_44.addWidget(self.label_15)


        self.verticalLayout_8.addWidget(self.frame_123)


        self.verticalLayout_6.addWidget(self.frame_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Abaqus/Python", None))
        self.label_16.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ABAQUS ANALYSIS", None))
        self.label_22.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" color:#ededed;\">. .</span> The software is designed to simplify the parametrization and analysis of numerical simulations using Abaqus, offering an efficient and intuitive approach to the simulation process. It features three main functions: first, it enables rapid parametrization of turning simulations through an intuitive interface with adjustable predefined parameters. Second, it supports iteration over different values and the generation of output files in INP or CAE formats after initial setup. Finally, it provides detailed post-processing of simulation data, allowing users to analyze and visualize results with advanced tools for effective data interpretation.</p></body></html>", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" color:#b6b6b6;\">. .</span><span style=\" font-weight:700;\">Fast parametrization of turning simulations.</span> This tool provides an intuitive interface where predefined parameters are made available to ease the initial setup. Users have the flexibility to adjust these parameters according to their specific needs.</p></body></html>", None))
        self.parametrizationButton.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" color:#b6b6b6;\">. .</span><span style=\" font-weight:700; color:#000000;\">I</span><span style=\" font-weight:700;\">teration over values and generation of output files</span>. After the initial configuration, it's possible iterate over different values and define output files in INP or CAE formats. This function facilitates the management of multiple simulation scenarios by allowing detailed adjustments and iterations.</p></body></html>", None))
        self.iterationButton.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_26.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" color:#b6b6b6;\">. .</span><span style=\" font-weight:700;\">Detailed post-processing of simulation data</span>. Once the simulations are executed, this tool assists in analyzing the results by providing advanced resources for visualizing and interpreting the generated data. This enables users to efficiently explore and understand the outcomes of the simulations.</p></body></html>", None))
        self.resultsButton.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_27.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"GEOMETRY SETTINGS", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm):", None))
        self.eulerianName.setText("")
        self.eulerianName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.eulerianHeight.setText("")
        self.eulerianHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianWidth.setText("")
        self.eulerianWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianTrickness.setText("")
        self.eulerianTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Partition Position", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"X3:", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"X4:", None))
        self.eulerianPartitionX1.setText("")
        self.eulerianPartitionX1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX2.setText("")
        self.eulerianPartitionX2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX3.setText("")
        self.eulerianPartitionX3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX4.setText("")
        self.eulerianPartitionX4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Y3:", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Y4:", None))
        self.eulerianPartitionY1.setText("")
        self.eulerianPartitionY1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY2.setText("")
        self.eulerianPartitionY2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY3.setText("")
        self.eulerianPartitionY3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY4.setText("")
        self.eulerianPartitionY4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianGlobalSize.setText("")
        self.eulerianGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianDeviationFactor.setText("")
        self.eulerianDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianMininumFactor.setText("")
        self.eulerianMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianOtherInfo.setText("")
        self.eulerianOtherInfo.setPlaceholderText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianOtherInfo_7.setText("")
        self.eulerianOtherInfo_7.setPlaceholderText("")
        self.eulerianOtherInfo_8.setText("")
        self.eulerianOtherInfo_8.setPlaceholderText("")
        self.eulerianOtherInfo_9.setText("")
        self.eulerianOtherInfo_9.setPlaceholderText("")
        self.eulerianOtherInfo_10.setText("")
        self.eulerianOtherInfo_10.setPlaceholderText("")
        self.eulerianWarning.setText("")
        self.defautValues.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eulerianTab), QCoreApplication.translate("MainWindow", u"Eulerian", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm): ", None))
        self.chipName.setText("")
        self.chipName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.chipHeight.setText("")
        self.chipHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipWidth.setText("")
        self.chipWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipTrickness.setText("")
        self.chipTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.chipGlobalSize.setText("")
        self.chipGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipDeviationFactor.setText("")
        self.chipDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipMininumFactor.setText("")
        self.chipMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipOtherInfo.setText("")
        self.chipOtherInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chipPlayeTab), QCoreApplication.translate("MainWindow", u"Chip Plate", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm):", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Rake Angle:", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Rake Dimension (mm):", None))
        self.toolName.setText("")
        self.toolName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.toolTrickness.setText("")
        self.toolTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeAngle.setText("")
        self.toolRakeAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeDimension.setText("")
        self.toolRakeDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Clerance Angle:", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Clearance Dimension (mm):", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.label_193.setText("")
        self.toolClearanceAngle.setText("")
        self.toolClearanceAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolClearanceDimension.setText("")
        self.toolClearanceDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRadius.setText("")
        self.toolRadius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_194.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Partition Information", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Size Partition 01:", None))
        self.toolPartition01.setText("")
        self.toolPartition01.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Size Partiton 02", None))
        self.toolPartition02.setText("")
        self.toolPartition02.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolGlobalSize.setText("")
        self.toolGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolDeviationFactor.setText("")
        self.toolDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolMinimumFactor.setText("")
        self.toolMinimumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo.setText("")
        self.toolOthersInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolOthersInfo_7.setText("")
        self.toolOthersInfo_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_8.setText("")
        self.toolOthersInfo_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_9.setText("")
        self.toolOthersInfo_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_10.setText("")
        self.toolOthersInfo_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolTab), QCoreApplication.translate("MainWindow", u"Tool", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setTabWhatsThis(self.tabWidget.indexOf(self.toolTab), QCoreApplication.translate("MainWindow", u"yyyyyyyyyyyyyyy", None))
#endif // QT_CONFIG(whatsthis)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Eulerian Position", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.xEulerian.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.xEulerian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.yEulerian.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.yEulerian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Tool Position", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.xTool.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.xTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.yTool.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.yTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Chip Plate Position", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Clearance Over Workpiece (mm):", None))
        self.overWorkpiece.setText("")
        self.overWorkpiece.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Distance From Tool (mm):", None))
        self.fromTool.setText("")
        self.fromTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Others Informations", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Depth of cut (mm):", None))
        self.feed.setText("")
        self.feed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Time Period:", None))
        self.timePeriod.setText("")
        self.timePeriod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.assemblyWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assemblyTab), QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Materials", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Boundary Conditions", None))
        self.returnButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_17.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PARAMETER ITERATION", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Select the directory to save the files", None))
        self.inpPathButton.setText("")
        self.inpLabel.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Select the number of Iteration?", None))
        self.numberOfVariables.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.numberOfVariables.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.numberOfVariables.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.numberOfVariables.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Select the parameter:", None))
        self.P01.setItemText(0, "")
        self.P01.setItemText(1, QCoreApplication.translate("MainWindow", u"Feed", None))
        self.P01.setItemText(2, QCoreApplication.translate("MainWindow", u"Rake Angle", None))
        self.P01.setItemText(3, QCoreApplication.translate("MainWindow", u"Clearance Angle", None))
        self.P01.setItemText(4, QCoreApplication.translate("MainWindow", u"Time Period", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Steps:", None))
        self.stepP01.setItemText(0, "")
        self.stepP01.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.stepP01.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.stepP01.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.stepP01.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.stepP01.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.stepP01.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.stepP01.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.stepP01.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.stepP01.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.stepP01.setCurrentText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Select the parameter:", None))
        self.P02.setItemText(0, "")
        self.P02.setItemText(1, QCoreApplication.translate("MainWindow", u"Feed", None))
        self.P02.setItemText(2, QCoreApplication.translate("MainWindow", u"Clearance Angle", None))
        self.P02.setItemText(3, QCoreApplication.translate("MainWindow", u"Rake Angle", None))
        self.P02.setItemText(4, QCoreApplication.translate("MainWindow", u"Time Period", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Steps:", None))
        self.stepP02.setItemText(0, "")
        self.stepP02.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.stepP02.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.stepP02.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.stepP02.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.stepP02.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.stepP02.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.stepP02.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.stepP02.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.stepP02.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.stepP02.setCurrentText("")
        self.labelIterationWarning.setText("")
        self.applyIteration.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Cores Available:", None))
        self.coreLabel.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Number of Simulations:", None))
        self.numberSimulation.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"How many simulations to run at the same time?", None))
        self.numberofPararelSimulations.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.numberofPararelSimulations.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Cores by simulation:", None))
        self.core.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.core.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.returnIterationButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.saveAndRunButton.setText(QCoreApplication.translate("MainWindow", u"Save and Run", None))
        self.label_136.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Select the directory with the ODB file", None))
        self.importResultsButton.setText("")
        self.pathResultsLabel.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Select the files", None))
        self.odbFiles.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.odbFiles.setItemText(1, QCoreApplication.translate("MainWindow", u"All", None))

        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Type of analysis:", None))
        self.typeOfAnalisys.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.typeOfAnalisys.setItemText(1, QCoreApplication.translate("MainWindow", u"NT11", None))
        self.typeOfAnalisys.setItemText(2, QCoreApplication.translate("MainWindow", u"RF", None))

        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Select the RF:", None))
        self.typeRF.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Steady State Value:", None))
        self.inpLabel_5.setText("")
        self.returnResultsButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.saveAndRunButton_4.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.exportFigureButton.setText(QCoreApplication.translate("MainWindow", u"Export Figure", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior", None))
    # retranslateUi

