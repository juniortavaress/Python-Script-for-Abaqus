# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1602, 848)
        MainWindow.setMinimumSize(QSize(300, 340))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"Icons/programmer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QFrame{\n"
"background-color: rgb(243, 243, 243);\n"
"border: 0px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setMaximumSize(QSize(16777215, 16777215))
        self.initialPage = QWidget()
        self.initialPage.setObjectName(u"initialPage")
        self.initialPage.setMinimumSize(QSize(0, 0))
        self.initialPage.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.initialPage)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_4 = QFrame(self.initialPage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(220, 16777215))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QPushButton {\n"
"        background-color: #cccccc; /* Cor de fundo do bot\u00e3o */\n"
"        color: #333333; /* Cor do texto */\n"
"        border: 2px solid #999999; /* Borda */\n"
"        border-radius: 5px; /* Bordas arredondadas */\n"
"        padding: 10px; /* Espa\u00e7amento interno */\n"
"        font-size: 16px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #b3b3b3; /* Cor de fundo ao passar o mouse */\n"
"        border: 2px solid #55aaff; /* Borda ao passar o mouse */\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: #999999; /* Cor de fundo quando pressionado */\n"
"        border: 2px solid #444444; /* Borda quando pressionado */\n"
"    }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.eulerianButton = QPushButton(self.frame)
        self.eulerianButton.setObjectName(u"eulerianButton")
        self.eulerianButton.setMinimumSize(QSize(0, 50))
        self.eulerianButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.eulerianButton)

        self.chipPlateButton = QPushButton(self.frame)
        self.chipPlateButton.setObjectName(u"chipPlateButton")
        self.chipPlateButton.setEnabled(True)
        self.chipPlateButton.setMinimumSize(QSize(0, 50))
        self.chipPlateButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.chipPlateButton)

        self.toolButton = QPushButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(True)
        self.toolButton.setMinimumSize(QSize(0, 50))
        self.toolButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.toolButton)

        self.assemblyButton = QPushButton(self.frame)
        self.assemblyButton.setObjectName(u"assemblyButton")
        self.assemblyButton.setEnabled(True)
        self.assemblyButton.setMinimumSize(QSize(0, 50))
        self.assemblyButton.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.assemblyButton)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.pages.addWidget(self.initialPage)
        self.eulerianPage = QWidget()
        self.eulerianPage.setObjectName(u"eulerianPage")
        self.eulerianPage.setMinimumSize(QSize(1263, 735))
        self.eulerianPage.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.eulerianPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.eulerianPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 3)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 78))
        self.frame_5.setMaximumSize(QSize(16777215, 78))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 60))
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setPixmap(QPixmap(u"Icons/3d.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"        font-size: 30px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.frame_30 = QFrame(self.frame_8)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 250))
        self.frame_30.setMaximumSize(QSize(16777215, 250))
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_31)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.frame_41 = QFrame(self.frame_31)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 35))
        self.frame_41.setMaximumSize(QSize(16777215, 35))
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_41)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_41)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 35))
        self.label_32.setMaximumSize(QSize(16777215, 35))
        self.label_32.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_19.addWidget(self.label_32)


        self.verticalLayout_18.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_31)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, -1, -1)
        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy2)
        self.frame_45.setMaximumSize(QSize(120, 16777215))
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_45)
        self.verticalLayout_29.setSpacing(7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.frame_45)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 18))
        self.label_121.setMaximumSize(QSize(16777215, 18))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semilight"])
        self.label_121.setFont(font2)
        self.label_121.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_121)

        self.label_122 = QLabel(self.frame_45)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(0, 18))
        self.label_122.setMaximumSize(QSize(16777215, 18))
        self.label_122.setFont(font2)
        self.label_122.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_122)

        self.label_123 = QLabel(self.frame_45)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 18))
        self.label_123.setMaximumSize(QSize(16777215, 18))
        self.label_123.setFont(font2)
        self.label_123.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_45)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 18))
        self.label_124.setMaximumSize(QSize(16777215, 18))
        self.label_124.setFont(font2)
        self.label_124.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.label_124)


        self.horizontalLayout_17.addWidget(self.frame_45)

        self.frame_53 = QFrame(self.frame_42)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy2.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy2)
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_53)
        self.verticalLayout_33.setSpacing(7)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.eulerianName = QLineEdit(self.frame_53)
        self.eulerianName.setObjectName(u"eulerianName")
        self.eulerianName.setMinimumSize(QSize(0, 18))
        self.eulerianName.setMaximumSize(QSize(180, 16777215))
        self.eulerianName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.eulerianName)

        self.eulerianHeight = QLineEdit(self.frame_53)
        self.eulerianHeight.setObjectName(u"eulerianHeight")
        self.eulerianHeight.setMinimumSize(QSize(0, 18))
        self.eulerianHeight.setMaximumSize(QSize(180, 16777215))
        self.eulerianHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.eulerianHeight)

        self.eulerianWidth = QLineEdit(self.frame_53)
        self.eulerianWidth.setObjectName(u"eulerianWidth")
        self.eulerianWidth.setMinimumSize(QSize(0, 18))
        self.eulerianWidth.setMaximumSize(QSize(180, 16777215))
        self.eulerianWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.eulerianWidth)

        self.eulerianTrickness = QLineEdit(self.frame_53)
        self.eulerianTrickness.setObjectName(u"eulerianTrickness")
        self.eulerianTrickness.setMinimumSize(QSize(0, 18))
        self.eulerianTrickness.setMaximumSize(QSize(180, 16777215))
        self.eulerianTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.eulerianTrickness)


        self.horizontalLayout_17.addWidget(self.frame_53)


        self.verticalLayout_18.addWidget(self.frame_42)


        self.horizontalLayout_26.addWidget(self.frame_31)

        self.frame_54 = QFrame(self.frame_30)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_54)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 0, -1, -1)
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 35))
        self.frame_55.setMaximumSize(QSize(16777215, 35))
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_55)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_55)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 35))
        self.label_33.setMaximumSize(QSize(16777215, 35))
        self.label_33.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_35.addWidget(self.label_33)


        self.verticalLayout_34.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, -1, -1)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy2.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy2)
        self.frame_58.setMaximumSize(QSize(40, 16777215))
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_58)
        self.verticalLayout_36.setSpacing(7)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_145 = QLabel(self.frame_58)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(0, 18))
        self.label_145.setMaximumSize(QSize(16777215, 18))
        self.label_145.setFont(font2)
        self.label_145.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_58)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(0, 18))
        self.label_146.setMaximumSize(QSize(16777215, 18))
        self.label_146.setFont(font2)
        self.label_146.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.label_146)

        self.label_147 = QLabel(self.frame_58)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(0, 18))
        self.label_147.setMaximumSize(QSize(16777215, 18))
        self.label_147.setFont(font2)
        self.label_147.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.label_147)

        self.label_148 = QLabel(self.frame_58)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(0, 18))
        self.label_148.setMaximumSize(QSize(16777215, 18))
        self.label_148.setFont(font2)
        self.label_148.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.label_148)


        self.horizontalLayout_23.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy2.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy2)
        self.frame_59.setMaximumSize(QSize(120, 16777215))
        self.frame_59.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_59)
        self.verticalLayout_37.setSpacing(7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionX1 = QLineEdit(self.frame_59)
        self.eulerianPartitionX1.setObjectName(u"eulerianPartitionX1")
        self.eulerianPartitionX1.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionX1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.eulerianPartitionX1)

        self.eulerianPartitionX2 = QLineEdit(self.frame_59)
        self.eulerianPartitionX2.setObjectName(u"eulerianPartitionX2")
        self.eulerianPartitionX2.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionX2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.eulerianPartitionX2)

        self.eulerianPartitionX3 = QLineEdit(self.frame_59)
        self.eulerianPartitionX3.setObjectName(u"eulerianPartitionX3")
        self.eulerianPartitionX3.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionX3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.eulerianPartitionX3)

        self.eulerianPartitionX4 = QLineEdit(self.frame_59)
        self.eulerianPartitionX4.setObjectName(u"eulerianPartitionX4")
        self.eulerianPartitionX4.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionX4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.eulerianPartitionX4)


        self.horizontalLayout_23.addWidget(self.frame_59)


        self.horizontalLayout_22.addWidget(self.frame_57)

        self.frame_60 = QFrame(self.frame_56)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy2.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy2)
        self.frame_61.setMaximumSize(QSize(40, 16777215))
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_61)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_149 = QLabel(self.frame_61)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(0, 18))
        self.label_149.setMaximumSize(QSize(16777215, 18))
        self.label_149.setFont(font2)
        self.label_149.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.label_149)

        self.label_150 = QLabel(self.frame_61)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(0, 18))
        self.label_150.setMaximumSize(QSize(16777215, 18))
        self.label_150.setFont(font2)
        self.label_150.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.label_150)

        self.label_151 = QLabel(self.frame_61)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(0, 18))
        self.label_151.setMaximumSize(QSize(16777215, 18))
        self.label_151.setFont(font2)
        self.label_151.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.label_151)

        self.label_152 = QLabel(self.frame_61)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(0, 18))
        self.label_152.setMaximumSize(QSize(16777215, 18))
        self.label_152.setFont(font2)
        self.label_152.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.label_152)


        self.horizontalLayout_25.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_60)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy2.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy2)
        self.frame_62.setMaximumSize(QSize(120, 16777215))
        self.frame_62.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setSpacing(7)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionY1 = QLineEdit(self.frame_62)
        self.eulerianPartitionY1.setObjectName(u"eulerianPartitionY1")
        self.eulerianPartitionY1.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionY1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.eulerianPartitionY1)

        self.eulerianPartitionY2 = QLineEdit(self.frame_62)
        self.eulerianPartitionY2.setObjectName(u"eulerianPartitionY2")
        self.eulerianPartitionY2.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionY2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.eulerianPartitionY2)

        self.eulerianPartitionY3 = QLineEdit(self.frame_62)
        self.eulerianPartitionY3.setObjectName(u"eulerianPartitionY3")
        self.eulerianPartitionY3.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionY3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.eulerianPartitionY3)

        self.eulerianPartitionY4 = QLineEdit(self.frame_62)
        self.eulerianPartitionY4.setObjectName(u"eulerianPartitionY4")
        self.eulerianPartitionY4.setMinimumSize(QSize(0, 18))
        self.eulerianPartitionY4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.eulerianPartitionY4)


        self.horizontalLayout_25.addWidget(self.frame_62)


        self.horizontalLayout_22.addWidget(self.frame_60)


        self.verticalLayout_34.addWidget(self.frame_56)


        self.horizontalLayout_26.addWidget(self.frame_54)


        self.verticalLayout_9.addWidget(self.frame_30)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 250))
        self.frame_11.setMaximumSize(QSize(16777215, 250))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_11)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.frame_28 = QFrame(self.frame_16)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 35))
        self.frame_28.setMaximumSize(QSize(16777215, 35))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_28)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_28)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 35))
        self.label_30.setMaximumSize(QSize(16777215, 35))
        self.label_30.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_15.addWidget(self.label_30)


        self.verticalLayout_10.addWidget(self.frame_28)

        self.frame_52 = QFrame(self.frame_16)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_52)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 12, -1)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, 0, -1)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setMaximumSize(QSize(120, 16777215))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_116 = QLabel(self.frame_25)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 18))
        self.label_116.setMaximumSize(QSize(16777215, 18))
        self.label_116.setFont(font2)
        self.label_116.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_116)

        self.label_113 = QLabel(self.frame_25)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 18))
        self.label_113.setMaximumSize(QSize(16777215, 18))
        self.label_113.setFont(font2)
        self.label_113.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_113)

        self.label_115 = QLabel(self.frame_25)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(0, 18))
        self.label_115.setMaximumSize(QSize(16777215, 18))
        self.label_115.setFont(font2)
        self.label_115.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_115)

        self.label_114 = QLabel(self.frame_25)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 18))
        self.label_114.setMaximumSize(QSize(16777215, 18))
        self.label_114.setFont(font2)
        self.label_114.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_114)


        self.horizontalLayout_9.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy2.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy2)
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.eulerianGlobalSize = QLineEdit(self.frame_26)
        self.eulerianGlobalSize.setObjectName(u"eulerianGlobalSize")
        self.eulerianGlobalSize.setMinimumSize(QSize(0, 18))
        self.eulerianGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.eulerianGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.eulerianGlobalSize)

        self.eulerianDeviationFactor = QLineEdit(self.frame_26)
        self.eulerianDeviationFactor.setObjectName(u"eulerianDeviationFactor")
        self.eulerianDeviationFactor.setMinimumSize(QSize(0, 18))
        self.eulerianDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.eulerianDeviationFactor)

        self.eulerianMininumFactor = QLineEdit(self.frame_26)
        self.eulerianMininumFactor.setObjectName(u"eulerianMininumFactor")
        self.eulerianMininumFactor.setMinimumSize(QSize(0, 18))
        self.eulerianMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.eulerianMininumFactor)

        self.eulerianOtherInfo = QLineEdit(self.frame_26)
        self.eulerianOtherInfo.setObjectName(u"eulerianOtherInfo")
        self.eulerianOtherInfo.setMinimumSize(QSize(0, 18))
        self.eulerianOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.eulerianOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.eulerianOtherInfo)


        self.horizontalLayout_9.addWidget(self.frame_26)


        self.verticalLayout_11.addWidget(self.frame_23)


        self.horizontalLayout_24.addWidget(self.frame_22)

        self.frame_27 = QFrame(self.frame_52)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_27)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, -1, -1, -1)
        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_38)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy2.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy2)
        self.frame_32.setMaximumSize(QSize(120, 16777215))
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_32)
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_137 = QLabel(self.frame_32)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(0, 18))
        self.label_137.setMaximumSize(QSize(16777215, 18))
        self.label_137.setFont(font2)
        self.label_137.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.label_137)

        self.label_138 = QLabel(self.frame_32)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(0, 18))
        self.label_138.setMaximumSize(QSize(16777215, 18))
        self.label_138.setFont(font2)
        self.label_138.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.label_138)

        self.label_139 = QLabel(self.frame_32)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(0, 18))
        self.label_139.setMaximumSize(QSize(16777215, 18))
        self.label_139.setFont(font2)
        self.label_139.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.label_139)

        self.label_140 = QLabel(self.frame_32)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 18))
        self.label_140.setMaximumSize(QSize(16777215, 18))
        self.label_140.setFont(font2)
        self.label_140.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.label_140)


        self.horizontalLayout_16.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_38)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy2.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy2)
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_33)
        self.verticalLayout_26.setSpacing(7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.eulerianOtherInfo_2 = QLineEdit(self.frame_33)
        self.eulerianOtherInfo_2.setObjectName(u"eulerianOtherInfo_2")
        self.eulerianOtherInfo_2.setMinimumSize(QSize(0, 18))
        self.eulerianOtherInfo_2.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.eulerianOtherInfo_2)

        self.eulerianOtherInfo_3 = QLineEdit(self.frame_33)
        self.eulerianOtherInfo_3.setObjectName(u"eulerianOtherInfo_3")
        self.eulerianOtherInfo_3.setMinimumSize(QSize(0, 18))
        self.eulerianOtherInfo_3.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.eulerianOtherInfo_3)

        self.eulerianOtherInfo_4 = QLineEdit(self.frame_33)
        self.eulerianOtherInfo_4.setObjectName(u"eulerianOtherInfo_4")
        self.eulerianOtherInfo_4.setMinimumSize(QSize(0, 18))
        self.eulerianOtherInfo_4.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.eulerianOtherInfo_4)

        self.eulerianOtherInfo_5 = QLineEdit(self.frame_33)
        self.eulerianOtherInfo_5.setObjectName(u"eulerianOtherInfo_5")
        self.eulerianOtherInfo_5.setMinimumSize(QSize(0, 18))
        self.eulerianOtherInfo_5.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.eulerianOtherInfo_5)


        self.horizontalLayout_16.addWidget(self.frame_33)


        self.horizontalLayout_10.addWidget(self.frame_38)


        self.verticalLayout_14.addWidget(self.frame_29)


        self.horizontalLayout_24.addWidget(self.frame_27)


        self.verticalLayout_10.addWidget(self.frame_52)


        self.verticalLayout_27.addWidget(self.frame_16)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_13)

        self.eulerianWarning = QLabel(self.frame_8)
        self.eulerianWarning.setObjectName(u"eulerianWarning")
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semilight"])
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.eulerianWarning.setFont(font3)
        self.eulerianWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.eulerianWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.eulerianWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.eulerianWarning)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.frame_86 = QFrame(self.frame_8)
        self.frame_86.setObjectName(u"frame_86")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_86.sizePolicy().hasHeightForWidth())
        self.frame_86.setSizePolicy(sizePolicy3)
        self.frame_86.setMaximumSize(QSize(16777215, 20))
        self.frame_86.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_86)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(9, 0, 0, 0)
        self.eulerianDefaut = QCheckBox(self.frame_86)
        self.eulerianDefaut.setObjectName(u"eulerianDefaut")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.eulerianDefaut.sizePolicy().hasHeightForWidth())
        self.eulerianDefaut.setSizePolicy(sizePolicy4)
        self.eulerianDefaut.setMaximumSize(QSize(16777215, 20))
        self.eulerianDefaut.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_55.addWidget(self.eulerianDefaut)


        self.verticalLayout_9.addWidget(self.frame_86)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 60))
        self.frame_10.setMaximumSize(QSize(16777215, 60))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(351, 0))
        self.frame_7.setMaximumSize(QSize(351, 81))
        self.frame_7.setStyleSheet(u"QPushButton {\n"
"        background-color: #cccccc; /* Cor de fundo do bot\u00e3o */\n"
"        color: #333333; /* Cor do texto */\n"
"        border: 2px solid #999999; /* Borda */\n"
"        border-radius: 5px; /* Bordas arredondadas */\n"
"        font-size: 15px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #b3b3b3; /* Cor de fundo ao passar o mouse */\n"
"        border: 2px solid #55aaff; /* Borda ao passar o mouse */\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: #999999; /* Cor de fundo quando pressionado */\n"
"        border: 2px solid #444444; /* Borda quando pressionado */\n"
"    }")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.eulerianApply = QPushButton(self.frame_7)
        self.eulerianApply.setObjectName(u"eulerianApply")
        self.eulerianApply.setMinimumSize(QSize(100, 30))
        self.eulerianApply.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic"])
        font4.setBold(False)
        self.eulerianApply.setFont(font4)

        self.horizontalLayout_4.addWidget(self.eulerianApply)

        self.eulerianFinish = QPushButton(self.frame_7)
        self.eulerianFinish.setObjectName(u"eulerianFinish")
        self.eulerianFinish.setEnabled(False)
        self.eulerianFinish.setMinimumSize(QSize(100, 30))
        self.eulerianFinish.setMaximumSize(QSize(150, 16777215))
        self.eulerianFinish.setFont(font4)
        self.eulerianFinish.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.eulerianFinish)


        self.horizontalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.plotEulerianArea = QFrame(self.frame_6)
        self.plotEulerianArea.setObjectName(u"plotEulerianArea")
        sizePolicy2.setHeightForWidth(self.plotEulerianArea.sizePolicy().hasHeightForWidth())
        self.plotEulerianArea.setSizePolicy(sizePolicy2)
        self.plotEulerianArea.setMinimumSize(QSize(634, 645))
        self.plotEulerianArea.setStyleSheet(u"background-color: rgb(237,237,237);\n"
"border-radius: 10px;")
        self.plotEulerianArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotEulerianArea.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_66 = QFrame(self.plotEulerianArea)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setGeometry(QRect(130, 330, 120, 391))
        self.frame_66.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.plotEulerianArea)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.pages.addWidget(self.eulerianPage)
        self.toolPage = QWidget()
        self.toolPage.setObjectName(u"toolPage")
        self.verticalLayout_62 = QVBoxLayout(self.toolPage)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.toolPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_12)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 3)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 78))
        self.frame_13.setMaximumSize(QSize(16777215, 78))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 60))
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setPixmap(QPixmap(u"Icons/3d.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"QLabel {\n"
"        font-size: 30px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)


        self.verticalLayout_28.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 10, 0, 0)
        self.frame_37 = QFrame(self.frame_14)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"}\n"
"")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_37)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 0, -1, -1)
        self.frame_94 = QFrame(self.frame_37)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 250))
        self.frame_94.setMaximumSize(QSize(16777215, 250))
        self.frame_94.setStyleSheet(u"")
        self.frame_94.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_94)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(9, 0, 0, 0)
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_95)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, -1)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 35))
        self.frame_96.setMaximumSize(QSize(16777215, 35))
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_96)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_96)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 35))
        self.label_36.setMaximumSize(QSize(16777215, 35))
        self.label_36.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_65.addWidget(self.label_36)


        self.verticalLayout_64.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_95)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_98)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, -1, 12, -1)
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(20, -1, 0, -1)
        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName(u"frame_100")
        sizePolicy2.setHeightForWidth(self.frame_100.sizePolicy().hasHeightForWidth())
        self.frame_100.setSizePolicy(sizePolicy2)
        self.frame_100.setMaximumSize(QSize(140, 16777215))
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_100)
        self.verticalLayout_67.setSpacing(7)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_129 = QLabel(self.frame_100)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(0, 18))
        self.label_129.setMaximumSize(QSize(16777215, 18))
        self.label_129.setFont(font2)
        self.label_129.setStyleSheet(u"")

        self.verticalLayout_67.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_100)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(0, 18))
        self.label_130.setMaximumSize(QSize(16777215, 18))
        self.label_130.setFont(font2)
        self.label_130.setStyleSheet(u"")

        self.verticalLayout_67.addWidget(self.label_130)

        self.label_131 = QLabel(self.frame_100)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(0, 18))
        self.label_131.setMaximumSize(QSize(16777215, 18))
        self.label_131.setFont(font2)
        self.label_131.setStyleSheet(u"")

        self.verticalLayout_67.addWidget(self.label_131)

        self.label_132 = QLabel(self.frame_100)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(0, 18))
        self.label_132.setMaximumSize(QSize(16777215, 18))
        self.label_132.setFont(font2)
        self.label_132.setStyleSheet(u"")

        self.verticalLayout_67.addWidget(self.label_132)


        self.horizontalLayout_38.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_99)
        self.frame_101.setObjectName(u"frame_101")
        sizePolicy2.setHeightForWidth(self.frame_101.sizePolicy().hasHeightForWidth())
        self.frame_101.setSizePolicy(sizePolicy2)
        self.frame_101.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_101)
        self.verticalLayout_68.setSpacing(7)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.toolName = QLineEdit(self.frame_101)
        self.toolName.setObjectName(u"toolName")
        self.toolName.setMinimumSize(QSize(0, 18))
        self.toolName.setMaximumSize(QSize(180, 16777215))
        self.toolName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.toolName)

        self.toolTrickness = QLineEdit(self.frame_101)
        self.toolTrickness.setObjectName(u"toolTrickness")
        self.toolTrickness.setMinimumSize(QSize(0, 18))
        self.toolTrickness.setMaximumSize(QSize(180, 16777215))
        self.toolTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.toolTrickness)

        self.toolRakeAngle = QLineEdit(self.frame_101)
        self.toolRakeAngle.setObjectName(u"toolRakeAngle")
        self.toolRakeAngle.setMinimumSize(QSize(0, 18))
        self.toolRakeAngle.setMaximumSize(QSize(180, 16777215))
        self.toolRakeAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.toolRakeAngle)

        self.toolRakeDimension = QLineEdit(self.frame_101)
        self.toolRakeDimension.setObjectName(u"toolRakeDimension")
        self.toolRakeDimension.setMinimumSize(QSize(0, 18))
        self.toolRakeDimension.setMaximumSize(QSize(180, 16777215))
        self.toolRakeDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_68.addWidget(self.toolRakeDimension)


        self.horizontalLayout_38.addWidget(self.frame_101)


        self.verticalLayout_66.addWidget(self.frame_99)


        self.horizontalLayout_37.addWidget(self.frame_98)

        self.frame_102 = QFrame(self.frame_97)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_102)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_103 = QFrame(self.frame_102)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_39.setSpacing(20)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(15, -1, -1, -1)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_40.setSpacing(6)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        sizePolicy2.setHeightForWidth(self.frame_105.sizePolicy().hasHeightForWidth())
        self.frame_105.setSizePolicy(sizePolicy2)
        self.frame_105.setMaximumSize(QSize(140, 16777215))
        self.frame_105.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_105)
        self.verticalLayout_70.setSpacing(7)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_161 = QLabel(self.frame_105)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMinimumSize(QSize(0, 18))
        self.label_161.setMaximumSize(QSize(16777215, 18))
        self.label_161.setFont(font2)
        self.label_161.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.label_161)

        self.label_162 = QLabel(self.frame_105)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMinimumSize(QSize(0, 18))
        self.label_162.setMaximumSize(QSize(16777215, 18))
        self.label_162.setFont(font2)
        self.label_162.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.label_162)

        self.label_163 = QLabel(self.frame_105)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMinimumSize(QSize(0, 18))
        self.label_163.setMaximumSize(QSize(16777215, 18))
        self.label_163.setFont(font2)
        self.label_163.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.label_163)

        self.label_164 = QLabel(self.frame_105)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMinimumSize(QSize(0, 18))
        self.label_164.setMaximumSize(QSize(16777215, 18))
        self.label_164.setFont(font2)
        self.label_164.setStyleSheet(u"")

        self.verticalLayout_70.addWidget(self.label_164)


        self.horizontalLayout_40.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        sizePolicy2.setHeightForWidth(self.frame_106.sizePolicy().hasHeightForWidth())
        self.frame_106.setSizePolicy(sizePolicy2)
        self.frame_106.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_106)
        self.verticalLayout_71.setSpacing(7)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.toolClearanceAngle = QLineEdit(self.frame_106)
        self.toolClearanceAngle.setObjectName(u"toolClearanceAngle")
        self.toolClearanceAngle.setMinimumSize(QSize(0, 18))
        self.toolClearanceAngle.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_71.addWidget(self.toolClearanceAngle)

        self.toolClearanceDimension = QLineEdit(self.frame_106)
        self.toolClearanceDimension.setObjectName(u"toolClearanceDimension")
        self.toolClearanceDimension.setMinimumSize(QSize(0, 18))
        self.toolClearanceDimension.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_71.addWidget(self.toolClearanceDimension)

        self.toolRadius = QLineEdit(self.frame_106)
        self.toolRadius.setObjectName(u"toolRadius")
        self.toolRadius.setMinimumSize(QSize(0, 18))
        self.toolRadius.setMaximumSize(QSize(189, 16777215))
        self.toolRadius.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_71.addWidget(self.toolRadius)

        self.label_165 = QLabel(self.frame_106)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMinimumSize(QSize(0, 18))
        self.label_165.setMaximumSize(QSize(16777215, 18))
        self.label_165.setFont(font2)
        self.label_165.setStyleSheet(u"")

        self.verticalLayout_71.addWidget(self.label_165)


        self.horizontalLayout_40.addWidget(self.frame_106)


        self.horizontalLayout_39.addWidget(self.frame_104)


        self.verticalLayout_69.addWidget(self.frame_103)


        self.horizontalLayout_37.addWidget(self.frame_102)


        self.verticalLayout_64.addWidget(self.frame_97)


        self.verticalLayout_63.addWidget(self.frame_95)


        self.verticalLayout_40.addWidget(self.frame_94)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_4)

        self.frame_88 = QFrame(self.frame_37)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 0))
        self.frame_88.setMaximumSize(QSize(16777215, 100))
        self.frame_88.setStyleSheet(u"")
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_88)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(9, 0, 0, 0)
        self.frame_108 = QFrame(self.frame_88)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_108)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, -1)
        self.frame_109 = QFrame(self.frame_108)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 35))
        self.frame_109.setMaximumSize(QSize(16777215, 35))
        self.frame_109.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_109)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 35))
        self.label_35.setMaximumSize(QSize(16777215, 35))
        self.label_35.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_28.addWidget(self.label_35)


        self.verticalLayout_59.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.frame_108)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_111)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 12, 0)
        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(20, -1, 0, -1)
        self.frame_113 = QFrame(self.frame_112)
        self.frame_113.setObjectName(u"frame_113")
        sizePolicy2.setHeightForWidth(self.frame_113.sizePolicy().hasHeightForWidth())
        self.frame_113.setSizePolicy(sizePolicy2)
        self.frame_113.setMaximumSize(QSize(140, 16777215))
        self.frame_113.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_113)
        self.verticalLayout_74.setSpacing(7)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.frame_113)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(0, 18))
        self.label_133.setMaximumSize(QSize(16777215, 18))
        self.label_133.setFont(font2)
        self.label_133.setStyleSheet(u"")

        self.verticalLayout_74.addWidget(self.label_133)


        self.horizontalLayout_29.addWidget(self.frame_113)

        self.frame_114 = QFrame(self.frame_112)
        self.frame_114.setObjectName(u"frame_114")
        sizePolicy2.setHeightForWidth(self.frame_114.sizePolicy().hasHeightForWidth())
        self.frame_114.setSizePolicy(sizePolicy2)
        self.frame_114.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_114)
        self.verticalLayout_75.setSpacing(7)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.toolPartition01 = QLineEdit(self.frame_114)
        self.toolPartition01.setObjectName(u"toolPartition01")
        self.toolPartition01.setMinimumSize(QSize(0, 18))
        self.toolPartition01.setMaximumSize(QSize(180, 16777215))
        self.toolPartition01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_75.addWidget(self.toolPartition01)


        self.horizontalLayout_29.addWidget(self.frame_114)


        self.verticalLayout_73.addWidget(self.frame_112)


        self.horizontalLayout_41.addWidget(self.frame_111)

        self.frame_115 = QFrame(self.frame_110)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_115)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(-1, 0, -1, 0)
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_42.setSpacing(20)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(15, -1, -1, -1)
        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName(u"frame_118")
        sizePolicy2.setHeightForWidth(self.frame_118.sizePolicy().hasHeightForWidth())
        self.frame_118.setSizePolicy(sizePolicy2)
        self.frame_118.setMaximumSize(QSize(140, 16777215))
        self.frame_118.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_118)
        self.verticalLayout_77.setSpacing(7)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_141 = QLabel(self.frame_118)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(0, 18))
        self.label_141.setMaximumSize(QSize(16777215, 18))
        self.label_141.setFont(font2)
        self.label_141.setStyleSheet(u"")

        self.verticalLayout_77.addWidget(self.label_141)


        self.horizontalLayout_43.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_117)
        self.frame_119.setObjectName(u"frame_119")
        sizePolicy2.setHeightForWidth(self.frame_119.sizePolicy().hasHeightForWidth())
        self.frame_119.setSizePolicy(sizePolicy2)
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_119)
        self.verticalLayout_78.setSpacing(7)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.toolPartition02 = QLineEdit(self.frame_119)
        self.toolPartition02.setObjectName(u"toolPartition02")
        self.toolPartition02.setMinimumSize(QSize(0, 18))
        self.toolPartition02.setMaximumSize(QSize(189, 16777215))
        self.toolPartition02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_78.addWidget(self.toolPartition02)


        self.horizontalLayout_43.addWidget(self.frame_119)


        self.horizontalLayout_42.addWidget(self.frame_117)


        self.verticalLayout_76.addWidget(self.frame_116)


        self.horizontalLayout_41.addWidget(self.frame_115)


        self.verticalLayout_59.addWidget(self.frame_110)


        self.verticalLayout_53.addWidget(self.frame_108)


        self.verticalLayout_40.addWidget(self.frame_88)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)

        self.frame_76 = QFrame(self.frame_37)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 250))
        self.frame_76.setMaximumSize(QSize(16777215, 250))
        self.frame_76.setStyleSheet(u"")
        self.frame_76.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_76)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(9, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_77)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, -1)
        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 35))
        self.frame_78.setMaximumSize(QSize(16777215, 35))
        self.frame_78.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_78)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 35))
        self.label_34.setMaximumSize(QSize(16777215, 35))
        self.label_34.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_27.addWidget(self.label_34)


        self.verticalLayout_52.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_77)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_80)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, -1, 12, -1)
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, -1, 0, -1)
        self.frame_39 = QFrame(self.frame_81)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy2.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy2)
        self.frame_39.setMaximumSize(QSize(120, 16777215))
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_39)
        self.verticalLayout_41.setSpacing(7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_134 = QLabel(self.frame_39)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(0, 18))
        self.label_134.setMaximumSize(QSize(16777215, 18))
        self.label_134.setFont(font2)
        self.label_134.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.label_134)

        self.label_135 = QLabel(self.frame_39)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(0, 18))
        self.label_135.setMaximumSize(QSize(16777215, 18))
        self.label_135.setFont(font2)
        self.label_135.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.label_135)

        self.label_136 = QLabel(self.frame_39)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(0, 18))
        self.label_136.setMaximumSize(QSize(16777215, 18))
        self.label_136.setFont(font2)
        self.label_136.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.label_136)

        self.label_142 = QLabel(self.frame_39)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(0, 18))
        self.label_142.setMaximumSize(QSize(16777215, 18))
        self.label_142.setFont(font2)
        self.label_142.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.label_142)


        self.horizontalLayout_15.addWidget(self.frame_39)

        self.frame_83 = QFrame(self.frame_81)
        self.frame_83.setObjectName(u"frame_83")
        sizePolicy2.setHeightForWidth(self.frame_83.sizePolicy().hasHeightForWidth())
        self.frame_83.setSizePolicy(sizePolicy2)
        self.frame_83.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_83)
        self.verticalLayout_57.setSpacing(7)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.toolGlobalSize = QLineEdit(self.frame_83)
        self.toolGlobalSize.setObjectName(u"toolGlobalSize")
        self.toolGlobalSize.setMinimumSize(QSize(0, 18))
        self.toolGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.toolGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_57.addWidget(self.toolGlobalSize)

        self.toolDeviationFactor = QLineEdit(self.frame_83)
        self.toolDeviationFactor.setObjectName(u"toolDeviationFactor")
        self.toolDeviationFactor.setMinimumSize(QSize(0, 18))
        self.toolDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.toolDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_57.addWidget(self.toolDeviationFactor)

        self.toolMinimumFactor = QLineEdit(self.frame_83)
        self.toolMinimumFactor.setObjectName(u"toolMinimumFactor")
        self.toolMinimumFactor.setMinimumSize(QSize(0, 18))
        self.toolMinimumFactor.setMaximumSize(QSize(180, 16777215))
        self.toolMinimumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_57.addWidget(self.toolMinimumFactor)

        self.toolOthersInfo = QLineEdit(self.frame_83)
        self.toolOthersInfo.setObjectName(u"toolOthersInfo")
        self.toolOthersInfo.setMinimumSize(QSize(0, 18))
        self.toolOthersInfo.setMaximumSize(QSize(180, 16777215))
        self.toolOthersInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_57.addWidget(self.toolOthersInfo)


        self.horizontalLayout_15.addWidget(self.frame_83)


        self.verticalLayout_54.addWidget(self.frame_81)


        self.horizontalLayout_32.addWidget(self.frame_80)

        self.frame_84 = QFrame(self.frame_79)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_84)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(15, -1, -1, -1)
        self.frame_87 = QFrame(self.frame_85)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_107 = QFrame(self.frame_87)
        self.frame_107.setObjectName(u"frame_107")
        sizePolicy2.setHeightForWidth(self.frame_107.sizePolicy().hasHeightForWidth())
        self.frame_107.setSizePolicy(sizePolicy2)
        self.frame_107.setMaximumSize(QSize(140, 16777215))
        self.frame_107.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_107)
        self.verticalLayout_72.setSpacing(7)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_125 = QLabel(self.frame_107)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 18))
        self.label_125.setMaximumSize(QSize(16777215, 18))
        self.label_125.setFont(font2)
        self.label_125.setStyleSheet(u"")

        self.verticalLayout_72.addWidget(self.label_125)

        self.label_126 = QLabel(self.frame_107)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(0, 18))
        self.label_126.setMaximumSize(QSize(16777215, 18))
        self.label_126.setFont(font2)
        self.label_126.setStyleSheet(u"")

        self.verticalLayout_72.addWidget(self.label_126)

        self.label_127 = QLabel(self.frame_107)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 18))
        self.label_127.setMaximumSize(QSize(16777215, 18))
        self.label_127.setFont(font2)
        self.label_127.setStyleSheet(u"")

        self.verticalLayout_72.addWidget(self.label_127)

        self.label_128 = QLabel(self.frame_107)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(0, 18))
        self.label_128.setMaximumSize(QSize(16777215, 18))
        self.label_128.setFont(font2)
        self.label_128.setStyleSheet(u"")

        self.verticalLayout_72.addWidget(self.label_128)


        self.horizontalLayout_34.addWidget(self.frame_107)

        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        sizePolicy2.setHeightForWidth(self.frame_89.sizePolicy().hasHeightForWidth())
        self.frame_89.setSizePolicy(sizePolicy2)
        self.frame_89.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_89)
        self.verticalLayout_60.setSpacing(7)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.toolOthersInfo_2 = QLineEdit(self.frame_89)
        self.toolOthersInfo_2.setObjectName(u"toolOthersInfo_2")
        self.toolOthersInfo_2.setMinimumSize(QSize(0, 18))
        self.toolOthersInfo_2.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.toolOthersInfo_2)

        self.toolOthersInfo_5 = QLineEdit(self.frame_89)
        self.toolOthersInfo_5.setObjectName(u"toolOthersInfo_5")
        self.toolOthersInfo_5.setMinimumSize(QSize(0, 18))
        self.toolOthersInfo_5.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.toolOthersInfo_5)

        self.toolOthersInfo_3 = QLineEdit(self.frame_89)
        self.toolOthersInfo_3.setObjectName(u"toolOthersInfo_3")
        self.toolOthersInfo_3.setMinimumSize(QSize(0, 18))
        self.toolOthersInfo_3.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.toolOthersInfo_3)

        self.toolOthersInfo_4 = QLineEdit(self.frame_89)
        self.toolOthersInfo_4.setObjectName(u"toolOthersInfo_4")
        self.toolOthersInfo_4.setMinimumSize(QSize(0, 18))
        self.toolOthersInfo_4.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.toolOthersInfo_4)


        self.horizontalLayout_34.addWidget(self.frame_89)


        self.horizontalLayout_33.addWidget(self.frame_87)


        self.verticalLayout_58.addWidget(self.frame_85)


        self.horizontalLayout_32.addWidget(self.frame_84)


        self.verticalLayout_52.addWidget(self.frame_79)


        self.verticalLayout_51.addWidget(self.frame_77)


        self.verticalLayout_40.addWidget(self.frame_76)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_14)

        self.toolWarning = QLabel(self.frame_37)
        self.toolWarning.setObjectName(u"toolWarning")
        self.toolWarning.setFont(font3)
        self.toolWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.toolWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.toolWarning)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_6)

        self.frame_90 = QFrame(self.frame_37)
        self.frame_90.setObjectName(u"frame_90")
        sizePolicy3.setHeightForWidth(self.frame_90.sizePolicy().hasHeightForWidth())
        self.frame_90.setSizePolicy(sizePolicy3)
        self.frame_90.setMaximumSize(QSize(16777215, 20))
        self.frame_90.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_90)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(9, 0, 0, 0)
        self.toolDefaut = QCheckBox(self.frame_90)
        self.toolDefaut.setObjectName(u"toolDefaut")
        sizePolicy4.setHeightForWidth(self.toolDefaut.sizePolicy().hasHeightForWidth())
        self.toolDefaut.setSizePolicy(sizePolicy4)
        self.toolDefaut.setMaximumSize(QSize(16777215, 20))
        self.toolDefaut.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_61.addWidget(self.toolDefaut)


        self.verticalLayout_40.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_37)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 60))
        self.frame_91.setMaximumSize(QSize(16777215, 60))
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(351, 0))
        self.frame_92.setMaximumSize(QSize(351, 81))
        self.frame_92.setStyleSheet(u"QPushButton {\n"
"        background-color: #cccccc; /* Cor de fundo do bot\u00e3o */\n"
"        color: #333333; /* Cor do texto */\n"
"        border: 2px solid #999999; /* Borda */\n"
"        border-radius: 5px; /* Bordas arredondadas */\n"
"        font-size: 15px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #b3b3b3; /* Cor de fundo ao passar o mouse */\n"
"        border: 2px solid #55aaff; /* Borda ao passar o mouse */\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: #999999; /* Cor de fundo quando pressionado */\n"
"        border: 2px solid #444444; /* Borda quando pressionado */\n"
"    }")
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.toolApply = QPushButton(self.frame_92)
        self.toolApply.setObjectName(u"toolApply")
        self.toolApply.setMinimumSize(QSize(100, 30))
        self.toolApply.setMaximumSize(QSize(150, 16777215))
        self.toolApply.setFont(font4)

        self.horizontalLayout_36.addWidget(self.toolApply)

        self.toolFinish = QPushButton(self.frame_92)
        self.toolFinish.setObjectName(u"toolFinish")
        self.toolFinish.setEnabled(False)
        self.toolFinish.setMinimumSize(QSize(100, 30))
        self.toolFinish.setMaximumSize(QSize(150, 16777215))
        self.toolFinish.setFont(font4)
        self.toolFinish.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.toolFinish)


        self.horizontalLayout_35.addWidget(self.frame_92)


        self.verticalLayout_40.addWidget(self.frame_91)


        self.horizontalLayout_11.addWidget(self.frame_37)

        self.plotToolArea = QFrame(self.frame_14)
        self.plotToolArea.setObjectName(u"plotToolArea")
        sizePolicy2.setHeightForWidth(self.plotToolArea.sizePolicy().hasHeightForWidth())
        self.plotToolArea.setSizePolicy(sizePolicy2)
        self.plotToolArea.setMinimumSize(QSize(634, 645))
        self.plotToolArea.setStyleSheet(u"background-color: rgb(237,237,237);\n"
"border-radius: 10px;")
        self.plotToolArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotToolArea.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_67 = QFrame(self.plotToolArea)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setGeometry(QRect(150, 90, 281, 351))
        self.frame_67.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.plotToolArea)


        self.verticalLayout_28.addWidget(self.frame_14)


        self.verticalLayout_62.addWidget(self.frame_12)

        self.pages.addWidget(self.toolPage)
        self.assemblyPage = QWidget()
        self.assemblyPage.setObjectName(u"assemblyPage")
        self.verticalLayout_45 = QVBoxLayout(self.assemblyPage)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.assemblyPage)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_40)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, -1, -1, 3)
        self.frame_63 = QFrame(self.frame_40)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 78))
        self.frame_63.setMaximumSize(QSize(16777215, 78))
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_7 = QLabel(self.frame_63)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 60))
        self.label_7.setMaximumSize(QSize(60, 60))
        self.label_7.setPixmap(QPixmap(u"Icons/dimensions.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_7)

        self.label_11 = QLabel(self.frame_63)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel {\n"
"        font-size: 30px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_11)


        self.verticalLayout_42.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_40)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 10, 0, 0)
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"}\n"
"")
        self.frame_65.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_65)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(-1, 10, -1, 10)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_11)

        self.frame_161 = QFrame(self.frame_65)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(0, 0))
        self.frame_161.setMaximumSize(QSize(16777215, 100))
        self.frame_161.setStyleSheet(u"")
        self.frame_161.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_161)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(9, 0, 0, 0)
        self.frame_162 = QFrame(self.frame_161)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_162)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, -1)
        self.frame_163 = QFrame(self.frame_162)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(0, 35))
        self.frame_163.setMaximumSize(QSize(16777215, 35))
        self.frame_163.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_163)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 35))
        self.label_40.setMaximumSize(QSize(16777215, 35))
        self.label_40.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_60.addWidget(self.label_40)


        self.verticalLayout_104.addWidget(self.frame_163)

        self.frame_164 = QFrame(self.frame_162)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_165)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 12, 0)
        self.frame_166 = QFrame(self.frame_165)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(20, -1, 0, -1)
        self.frame_167 = QFrame(self.frame_166)
        self.frame_167.setObjectName(u"frame_167")
        sizePolicy3.setHeightForWidth(self.frame_167.sizePolicy().hasHeightForWidth())
        self.frame_167.setSizePolicy(sizePolicy3)
        self.frame_167.setMinimumSize(QSize(40, 0))
        self.frame_167.setMaximumSize(QSize(140, 16777215))
        self.frame_167.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_167)
        self.verticalLayout_106.setSpacing(7)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_175 = QLabel(self.frame_167)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMinimumSize(QSize(30, 18))
        self.label_175.setMaximumSize(QSize(16777215, 18))
        self.label_175.setFont(font2)
        self.label_175.setStyleSheet(u"")

        self.verticalLayout_106.addWidget(self.label_175)


        self.horizontalLayout_62.addWidget(self.frame_167)

        self.frame_168 = QFrame(self.frame_166)
        self.frame_168.setObjectName(u"frame_168")
        sizePolicy2.setHeightForWidth(self.frame_168.sizePolicy().hasHeightForWidth())
        self.frame_168.setSizePolicy(sizePolicy2)
        self.frame_168.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_168.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_168)
        self.verticalLayout_107.setSpacing(7)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_159 = QLineEdit(self.frame_168)
        self.lineEdit_159.setObjectName(u"lineEdit_159")
        self.lineEdit_159.setMinimumSize(QSize(0, 18))
        self.lineEdit_159.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_159.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_107.addWidget(self.lineEdit_159)


        self.horizontalLayout_62.addWidget(self.frame_168)


        self.verticalLayout_105.addWidget(self.frame_166)


        self.horizontalLayout_61.addWidget(self.frame_165)

        self.frame_169 = QFrame(self.frame_164)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_169)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(-1, 0, -1, 0)
        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_63.setSpacing(20)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(15, -1, -1, -1)
        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_64.setSpacing(6)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_172 = QFrame(self.frame_171)
        self.frame_172.setObjectName(u"frame_172")
        sizePolicy3.setHeightForWidth(self.frame_172.sizePolicy().hasHeightForWidth())
        self.frame_172.setSizePolicy(sizePolicy3)
        self.frame_172.setMinimumSize(QSize(40, 0))
        self.frame_172.setMaximumSize(QSize(140, 16777215))
        self.frame_172.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_172)
        self.verticalLayout_109.setSpacing(7)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_176 = QLabel(self.frame_172)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMinimumSize(QSize(0, 18))
        self.label_176.setMaximumSize(QSize(16777215, 18))
        self.label_176.setFont(font2)
        self.label_176.setStyleSheet(u"")

        self.verticalLayout_109.addWidget(self.label_176)


        self.horizontalLayout_64.addWidget(self.frame_172)

        self.frame_173 = QFrame(self.frame_171)
        self.frame_173.setObjectName(u"frame_173")
        sizePolicy2.setHeightForWidth(self.frame_173.sizePolicy().hasHeightForWidth())
        self.frame_173.setSizePolicy(sizePolicy2)
        self.frame_173.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_173.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_173)
        self.verticalLayout_110.setSpacing(7)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_160 = QLineEdit(self.frame_173)
        self.lineEdit_160.setObjectName(u"lineEdit_160")
        self.lineEdit_160.setMinimumSize(QSize(0, 18))
        self.lineEdit_160.setMaximumSize(QSize(189, 16777215))
        self.lineEdit_160.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_110.addWidget(self.lineEdit_160)


        self.horizontalLayout_64.addWidget(self.frame_173)


        self.horizontalLayout_63.addWidget(self.frame_171)


        self.verticalLayout_108.addWidget(self.frame_170)


        self.horizontalLayout_61.addWidget(self.frame_169)


        self.verticalLayout_104.addWidget(self.frame_164)


        self.verticalLayout_103.addWidget(self.frame_162)


        self.verticalLayout_43.addWidget(self.frame_161)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_7)

        self.frame_174 = QFrame(self.frame_65)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMinimumSize(QSize(0, 0))
        self.frame_174.setMaximumSize(QSize(16777215, 100))
        self.frame_174.setStyleSheet(u"")
        self.frame_174.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_174)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(9, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_175)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, -1)
        self.frame_176 = QFrame(self.frame_175)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(0, 35))
        self.frame_176.setMaximumSize(QSize(16777215, 35))
        self.frame_176.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_176)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 35))
        self.label_41.setMaximumSize(QSize(16777215, 35))
        self.label_41.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_65.addWidget(self.label_41)


        self.verticalLayout_111.addWidget(self.frame_176)

        self.frame_177 = QFrame(self.frame_175)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_178 = QFrame(self.frame_177)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_178)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 12, 0)
        self.frame_179 = QFrame(self.frame_178)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(20, -1, 0, -1)
        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        sizePolicy3.setHeightForWidth(self.frame_180.sizePolicy().hasHeightForWidth())
        self.frame_180.setSizePolicy(sizePolicy3)
        self.frame_180.setMinimumSize(QSize(40, 0))
        self.frame_180.setMaximumSize(QSize(140, 16777215))
        self.frame_180.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_180)
        self.verticalLayout_113.setSpacing(7)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.frame_180)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMinimumSize(QSize(0, 18))
        self.label_166.setMaximumSize(QSize(16777215, 18))
        self.label_166.setFont(font2)
        self.label_166.setStyleSheet(u"")

        self.verticalLayout_113.addWidget(self.label_166)


        self.horizontalLayout_67.addWidget(self.frame_180)

        self.frame_181 = QFrame(self.frame_179)
        self.frame_181.setObjectName(u"frame_181")
        sizePolicy2.setHeightForWidth(self.frame_181.sizePolicy().hasHeightForWidth())
        self.frame_181.setSizePolicy(sizePolicy2)
        self.frame_181.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_181.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_181)
        self.verticalLayout_114.setSpacing(7)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_125 = QLineEdit(self.frame_181)
        self.lineEdit_125.setObjectName(u"lineEdit_125")
        self.lineEdit_125.setMinimumSize(QSize(0, 18))
        self.lineEdit_125.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_125.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_114.addWidget(self.lineEdit_125)


        self.horizontalLayout_67.addWidget(self.frame_181)


        self.verticalLayout_112.addWidget(self.frame_179)


        self.horizontalLayout_66.addWidget(self.frame_178)

        self.frame_182 = QFrame(self.frame_177)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_182)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(-1, 0, -1, 0)
        self.frame_183 = QFrame(self.frame_182)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_183)
        self.horizontalLayout_68.setSpacing(20)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(15, -1, -1, -1)
        self.frame_184 = QFrame(self.frame_183)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_69.setSpacing(6)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        sizePolicy3.setHeightForWidth(self.frame_185.sizePolicy().hasHeightForWidth())
        self.frame_185.setSizePolicy(sizePolicy3)
        self.frame_185.setMinimumSize(QSize(40, 0))
        self.frame_185.setMaximumSize(QSize(140, 16777215))
        self.frame_185.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_185)
        self.verticalLayout_116.setSpacing(7)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_167 = QLabel(self.frame_185)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMinimumSize(QSize(0, 18))
        self.label_167.setMaximumSize(QSize(16777215, 18))
        self.label_167.setFont(font2)
        self.label_167.setStyleSheet(u"")

        self.verticalLayout_116.addWidget(self.label_167)


        self.horizontalLayout_69.addWidget(self.frame_185)

        self.frame_186 = QFrame(self.frame_184)
        self.frame_186.setObjectName(u"frame_186")
        sizePolicy2.setHeightForWidth(self.frame_186.sizePolicy().hasHeightForWidth())
        self.frame_186.setSizePolicy(sizePolicy2)
        self.frame_186.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_186.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_186)
        self.verticalLayout_117.setSpacing(7)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_126 = QLineEdit(self.frame_186)
        self.lineEdit_126.setObjectName(u"lineEdit_126")
        self.lineEdit_126.setMinimumSize(QSize(0, 18))
        self.lineEdit_126.setMaximumSize(QSize(189, 16777215))
        self.lineEdit_126.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_117.addWidget(self.lineEdit_126)


        self.horizontalLayout_69.addWidget(self.frame_186)


        self.horizontalLayout_68.addWidget(self.frame_184)


        self.verticalLayout_115.addWidget(self.frame_183)


        self.horizontalLayout_66.addWidget(self.frame_182)


        self.verticalLayout_111.addWidget(self.frame_177)


        self.verticalLayout_79.addWidget(self.frame_175)


        self.verticalLayout_43.addWidget(self.frame_174)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_10)

        self.frame_133 = QFrame(self.frame_65)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 0))
        self.frame_133.setMaximumSize(QSize(16777215, 100))
        self.frame_133.setStyleSheet(u"")
        self.frame_133.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_133)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(9, 0, 0, 0)
        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_134)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, -1)
        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 35))
        self.frame_135.setMaximumSize(QSize(16777215, 35))
        self.frame_135.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_135)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 35))
        self.label_38.setMaximumSize(QSize(16777215, 35))
        self.label_38.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_48.addWidget(self.label_38)


        self.verticalLayout_88.addWidget(self.frame_135)

        self.frame_136 = QFrame(self.frame_134)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.frame_136)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_137)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 12, 0)
        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(20, -1, 0, -1)
        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        sizePolicy2.setHeightForWidth(self.frame_139.sizePolicy().hasHeightForWidth())
        self.frame_139.setSizePolicy(sizePolicy2)
        self.frame_139.setMaximumSize(QSize(200, 16777215))
        self.frame_139.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_139)
        self.verticalLayout_90.setSpacing(7)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_155 = QLabel(self.frame_139)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(0, 18))
        self.label_155.setMaximumSize(QSize(16777215, 18))
        self.label_155.setFont(font2)
        self.label_155.setStyleSheet(u"")

        self.verticalLayout_90.addWidget(self.label_155)


        self.horizontalLayout_50.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.frame_138)
        self.frame_140.setObjectName(u"frame_140")
        sizePolicy3.setHeightForWidth(self.frame_140.sizePolicy().hasHeightForWidth())
        self.frame_140.setSizePolicy(sizePolicy3)
        self.frame_140.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.frame_140.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_140.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_140)
        self.verticalLayout_91.setSpacing(7)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_119 = QLineEdit(self.frame_140)
        self.lineEdit_119.setObjectName(u"lineEdit_119")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_119.sizePolicy().hasHeightForWidth())
        self.lineEdit_119.setSizePolicy(sizePolicy5)
        self.lineEdit_119.setMinimumSize(QSize(0, 18))
        self.lineEdit_119.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_119.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_91.addWidget(self.lineEdit_119)


        self.horizontalLayout_50.addWidget(self.frame_140)


        self.verticalLayout_89.addWidget(self.frame_138)


        self.horizontalLayout_49.addWidget(self.frame_137)

        self.frame_141 = QFrame(self.frame_136)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_141)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(-1, 0, -1, 0)
        self.frame_142 = QFrame(self.frame_141)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_51.setSpacing(20)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(15, -1, -1, -1)
        self.frame_143 = QFrame(self.frame_142)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_52.setSpacing(6)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_144 = QFrame(self.frame_143)
        self.frame_144.setObjectName(u"frame_144")
        sizePolicy2.setHeightForWidth(self.frame_144.sizePolicy().hasHeightForWidth())
        self.frame_144.setSizePolicy(sizePolicy2)
        self.frame_144.setMaximumSize(QSize(140, 16777215))
        self.frame_144.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_144)
        self.verticalLayout_93.setSpacing(7)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.frame_144)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMinimumSize(QSize(0, 18))
        self.label_156.setMaximumSize(QSize(16777215, 18))
        self.label_156.setFont(font2)
        self.label_156.setStyleSheet(u"")

        self.verticalLayout_93.addWidget(self.label_156)


        self.horizontalLayout_52.addWidget(self.frame_144)

        self.frame_145 = QFrame(self.frame_143)
        self.frame_145.setObjectName(u"frame_145")
        sizePolicy2.setHeightForWidth(self.frame_145.sizePolicy().hasHeightForWidth())
        self.frame_145.setSizePolicy(sizePolicy2)
        self.frame_145.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_145.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_145)
        self.verticalLayout_94.setSpacing(7)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_120 = QLineEdit(self.frame_145)
        self.lineEdit_120.setObjectName(u"lineEdit_120")
        self.lineEdit_120.setMinimumSize(QSize(0, 18))
        self.lineEdit_120.setMaximumSize(QSize(189, 16777215))
        self.lineEdit_120.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_94.addWidget(self.lineEdit_120)


        self.horizontalLayout_52.addWidget(self.frame_145)


        self.horizontalLayout_51.addWidget(self.frame_143)


        self.verticalLayout_92.addWidget(self.frame_142)


        self.horizontalLayout_49.addWidget(self.frame_141)


        self.verticalLayout_88.addWidget(self.frame_136)


        self.verticalLayout_56.addWidget(self.frame_134)


        self.verticalLayout_43.addWidget(self.frame_133)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_8)

        self.frame_187 = QFrame(self.frame_65)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setMinimumSize(QSize(0, 0))
        self.frame_187.setMaximumSize(QSize(16777215, 100))
        self.frame_187.setStyleSheet(u"")
        self.frame_187.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_187)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(9, 0, 0, 0)
        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.frame_188)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, -1)
        self.frame_189 = QFrame(self.frame_188)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setMinimumSize(QSize(0, 35))
        self.frame_189.setMaximumSize(QSize(16777215, 35))
        self.frame_189.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_189)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 35))
        self.label_42.setMaximumSize(QSize(16777215, 35))
        self.label_42.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_70.addWidget(self.label_42)


        self.verticalLayout_118.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_188)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_191 = QFrame(self.frame_190)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_191)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 12, 0)
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(20, -1, 0, -1)
        self.frame_193 = QFrame(self.frame_192)
        self.frame_193.setObjectName(u"frame_193")
        sizePolicy2.setHeightForWidth(self.frame_193.sizePolicy().hasHeightForWidth())
        self.frame_193.setSizePolicy(sizePolicy2)
        self.frame_193.setMaximumSize(QSize(140, 16777215))
        self.frame_193.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_193)
        self.verticalLayout_120.setSpacing(7)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_168 = QLabel(self.frame_193)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMinimumSize(QSize(0, 18))
        self.label_168.setMaximumSize(QSize(16777215, 18))
        self.label_168.setFont(font2)
        self.label_168.setStyleSheet(u"")

        self.verticalLayout_120.addWidget(self.label_168)


        self.horizontalLayout_72.addWidget(self.frame_193)

        self.frame_194 = QFrame(self.frame_192)
        self.frame_194.setObjectName(u"frame_194")
        sizePolicy2.setHeightForWidth(self.frame_194.sizePolicy().hasHeightForWidth())
        self.frame_194.setSizePolicy(sizePolicy2)
        self.frame_194.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_194.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_194)
        self.verticalLayout_121.setSpacing(7)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_127 = QLineEdit(self.frame_194)
        self.lineEdit_127.setObjectName(u"lineEdit_127")
        self.lineEdit_127.setMinimumSize(QSize(0, 18))
        self.lineEdit_127.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_127.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_121.addWidget(self.lineEdit_127)


        self.horizontalLayout_72.addWidget(self.frame_194)


        self.verticalLayout_119.addWidget(self.frame_192)


        self.horizontalLayout_71.addWidget(self.frame_191)

        self.frame_195 = QFrame(self.frame_190)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_195)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(-1, 0, -1, 0)
        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_73.setSpacing(20)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(15, -1, -1, -1)
        self.frame_197 = QFrame(self.frame_196)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_74.setSpacing(6)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_198 = QFrame(self.frame_197)
        self.frame_198.setObjectName(u"frame_198")
        sizePolicy2.setHeightForWidth(self.frame_198.sizePolicy().hasHeightForWidth())
        self.frame_198.setSizePolicy(sizePolicy2)
        self.frame_198.setMaximumSize(QSize(140, 16777215))
        self.frame_198.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_198)
        self.verticalLayout_123.setSpacing(7)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_74.addWidget(self.frame_198)

        self.frame_199 = QFrame(self.frame_197)
        self.frame_199.setObjectName(u"frame_199")
        sizePolicy2.setHeightForWidth(self.frame_199.sizePolicy().hasHeightForWidth())
        self.frame_199.setSizePolicy(sizePolicy2)
        self.frame_199.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_199.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_199)
        self.verticalLayout_124.setSpacing(7)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_74.addWidget(self.frame_199)


        self.horizontalLayout_73.addWidget(self.frame_197)


        self.verticalLayout_122.addWidget(self.frame_196)


        self.horizontalLayout_71.addWidget(self.frame_195)


        self.verticalLayout_118.addWidget(self.frame_190)


        self.verticalLayout_80.addWidget(self.frame_188)


        self.verticalLayout_43.addWidget(self.frame_187)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_9)

        self.frame_157 = QFrame(self.frame_65)
        self.frame_157.setObjectName(u"frame_157")
        sizePolicy3.setHeightForWidth(self.frame_157.sizePolicy().hasHeightForWidth())
        self.frame_157.setSizePolicy(sizePolicy3)
        self.frame_157.setMaximumSize(QSize(16777215, 20))
        self.frame_157.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.frame_157.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_157)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(9, 0, 0, 0)
        self.chipPlateDefaut_5 = QCheckBox(self.frame_157)
        self.chipPlateDefaut_5.setObjectName(u"chipPlateDefaut_5")
        sizePolicy4.setHeightForWidth(self.chipPlateDefaut_5.sizePolicy().hasHeightForWidth())
        self.chipPlateDefaut_5.setSizePolicy(sizePolicy4)
        self.chipPlateDefaut_5.setMaximumSize(QSize(16777215, 20))
        self.chipPlateDefaut_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_102.addWidget(self.chipPlateDefaut_5)


        self.verticalLayout_43.addWidget(self.frame_157)

        self.frame_158 = QFrame(self.frame_65)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(0, 60))
        self.frame_158.setMaximumSize(QSize(16777215, 60))
        self.frame_158.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.frame_158)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(351, 0))
        self.frame_159.setMaximumSize(QSize(351, 81))
        self.frame_159.setStyleSheet(u"QPushButton {\n"
"        background-color: #cccccc; /* Cor de fundo do bot\u00e3o */\n"
"        color: #333333; /* Cor do texto */\n"
"        border: 2px solid #999999; /* Borda */\n"
"        border-radius: 5px; /* Bordas arredondadas */\n"
"        font-size: 15px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #b3b3b3; /* Cor de fundo ao passar o mouse */\n"
"        border: 2px solid #55aaff; /* Borda ao passar o mouse */\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: #999999; /* Cor de fundo quando pressionado */\n"
"        border: 2px solid #444444; /* Borda quando pressionado */\n"
"    }")
        self.frame_159.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.assemblyApply = QPushButton(self.frame_159)
        self.assemblyApply.setObjectName(u"assemblyApply")
        self.assemblyApply.setMinimumSize(QSize(100, 30))
        self.assemblyApply.setMaximumSize(QSize(150, 16777215))
        self.assemblyApply.setFont(font4)

        self.horizontalLayout_59.addWidget(self.assemblyApply)

        self.assemblyFinish = QPushButton(self.frame_159)
        self.assemblyFinish.setObjectName(u"assemblyFinish")
        self.assemblyFinish.setMinimumSize(QSize(100, 30))
        self.assemblyFinish.setMaximumSize(QSize(150, 16777215))
        self.assemblyFinish.setFont(font4)
        self.assemblyFinish.setStyleSheet(u"")

        self.horizontalLayout_59.addWidget(self.assemblyFinish)


        self.horizontalLayout_58.addWidget(self.frame_159)


        self.verticalLayout_43.addWidget(self.frame_158)


        self.horizontalLayout_31.addWidget(self.frame_65)

        self.plotAssemblyArea = QFrame(self.frame_64)
        self.plotAssemblyArea.setObjectName(u"plotAssemblyArea")
        sizePolicy2.setHeightForWidth(self.plotAssemblyArea.sizePolicy().hasHeightForWidth())
        self.plotAssemblyArea.setSizePolicy(sizePolicy2)
        self.plotAssemblyArea.setMinimumSize(QSize(634, 645))
        self.plotAssemblyArea.setStyleSheet(u"background-color: rgb(237,237,237);\n"
"border-radius: 10px;")
        self.plotAssemblyArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotAssemblyArea.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_31.addWidget(self.plotAssemblyArea)


        self.verticalLayout_42.addWidget(self.frame_64)


        self.verticalLayout_45.addWidget(self.frame_40)

        self.pages.addWidget(self.assemblyPage)
        self.chipPlatePage = QWidget()
        self.chipPlatePage.setObjectName(u"chipPlatePage")
        self.verticalLayout_4 = QVBoxLayout(self.chipPlatePage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.chipPlatePage)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 3)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 78))
        self.frame_17.setMaximumSize(QSize(16777215, 78))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(60, 60))
        self.label_8.setMaximumSize(QSize(60, 60))
        self.label_8.setPixmap(QPixmap(u"Icons/3d.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel {\n"
"        font-size: 30px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_9)


        self.verticalLayout_16.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 10, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(500, 16777215))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(20, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy3.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy3)
        self.frame_20.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setMinimumSize(QSize(311, 221))
        self.frame_21.setMaximumSize(QSize(16777215, 280))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.frame_46 = QFrame(self.frame_21)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 35))
        self.frame_46.setMaximumSize(QSize(16777215, 35))
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_46)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_46)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 35))
        self.label_10.setMaximumSize(QSize(16777215, 35))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_10)


        self.verticalLayout_21.addWidget(self.frame_46)

        self.frame_34 = QFrame(self.frame_21)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(283, 180))
        self.frame_34.setMaximumSize(QSize(16777215, 180))
        self.frame_34.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 0, -1, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy3.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy3)
        self.frame_35.setMinimumSize(QSize(130, 0))
        self.frame_35.setStyleSheet(u"border: 0px;")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_35)
        self.verticalLayout_22.setSpacing(7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_35)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 18))
        self.label_47.setMaximumSize(QSize(16777215, 18))
        self.label_47.setFont(font2)
        self.label_47.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_35)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 18))
        self.label_48.setMaximumSize(QSize(16777215, 18))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.label_48)

        self.label_49 = QLabel(self.frame_35)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 18))
        self.label_49.setMaximumSize(QSize(16777215, 18))
        self.label_49.setFont(font2)
        self.label_49.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.label_49)

        self.label_50 = QLabel(self.frame_35)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 18))
        self.label_50.setMaximumSize(QSize(16777215, 18))
        self.label_50.setFont(font2)
        self.label_50.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.label_50)


        self.horizontalLayout_14.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy3.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy3)
        self.frame_36.setMinimumSize(QSize(150, 0))
        self.frame_36.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border: 0px;\n"
"}")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_36)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.chipName = QLineEdit(self.frame_36)
        self.chipName.setObjectName(u"chipName")
        self.chipName.setMinimumSize(QSize(0, 18))
        self.chipName.setMaximumSize(QSize(180, 16777215))
        self.chipName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.chipName)

        self.chipHeight = QLineEdit(self.frame_36)
        self.chipHeight.setObjectName(u"chipHeight")
        self.chipHeight.setMinimumSize(QSize(0, 18))
        self.chipHeight.setMaximumSize(QSize(180, 16777215))
        self.chipHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.chipHeight)

        self.chipWidth = QLineEdit(self.frame_36)
        self.chipWidth.setObjectName(u"chipWidth")
        self.chipWidth.setMinimumSize(QSize(0, 18))
        self.chipWidth.setMaximumSize(QSize(180, 16777215))
        self.chipWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.chipWidth)

        self.chipTrickness = QLineEdit(self.frame_36)
        self.chipTrickness.setObjectName(u"chipTrickness")
        self.chipTrickness.setMinimumSize(QSize(0, 18))
        self.chipTrickness.setMaximumSize(QSize(180, 16777215))
        self.chipTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.chipTrickness)


        self.horizontalLayout_14.addWidget(self.frame_36)


        self.verticalLayout_21.addWidget(self.frame_34)


        self.verticalLayout_24.addWidget(self.frame_21)

        self.frame_47 = QFrame(self.frame_20)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy3.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy3)
        self.frame_47.setMinimumSize(QSize(311, 221))
        self.frame_47.setMaximumSize(QSize(16777215, 280))
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_47)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 35))
        self.frame_48.setMaximumSize(QSize(16777215, 35))
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_48)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 35))
        self.label_13.setMaximumSize(QSize(16777215, 35))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_20.addWidget(self.label_13)


        self.verticalLayout_30.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_47)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(283, 180))
        self.frame_49.setMaximumSize(QSize(16777215, 180))
        self.frame_49.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 0, -1, 0)
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy3.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy3)
        self.frame_50.setMinimumSize(QSize(130, 0))
        self.frame_50.setStyleSheet(u"border: 0px;")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_50)
        self.verticalLayout_31.setSpacing(7)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.frame_50)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 18))
        self.label_69.setMaximumSize(QSize(16777215, 18))
        self.label_69.setFont(font2)
        self.label_69.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_69)

        self.label_70 = QLabel(self.frame_50)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 18))
        self.label_70.setMaximumSize(QSize(16777215, 18))
        self.label_70.setFont(font2)
        self.label_70.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_70)

        self.label_71 = QLabel(self.frame_50)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 18))
        self.label_71.setMaximumSize(QSize(16777215, 18))
        self.label_71.setFont(font2)
        self.label_71.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_71)

        self.label_72 = QLabel(self.frame_50)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 18))
        self.label_72.setMaximumSize(QSize(16777215, 18))
        self.label_72.setFont(font2)
        self.label_72.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_72)


        self.horizontalLayout_21.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy3.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy3)
        self.frame_51.setMinimumSize(QSize(150, 0))
        self.frame_51.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border: 0px;\n"
"}")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_51)
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.chipGlobalSize = QLineEdit(self.frame_51)
        self.chipGlobalSize.setObjectName(u"chipGlobalSize")
        self.chipGlobalSize.setMinimumSize(QSize(0, 18))
        self.chipGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.chipGlobalSize.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.chipGlobalSize.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.chipGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.chipGlobalSize)

        self.chipDeviationFactor = QLineEdit(self.frame_51)
        self.chipDeviationFactor.setObjectName(u"chipDeviationFactor")
        self.chipDeviationFactor.setMinimumSize(QSize(0, 18))
        self.chipDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.chipDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.chipDeviationFactor)

        self.chipMininumFactor = QLineEdit(self.frame_51)
        self.chipMininumFactor.setObjectName(u"chipMininumFactor")
        self.chipMininumFactor.setMinimumSize(QSize(0, 18))
        self.chipMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.chipMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.chipMininumFactor)

        self.chipOtherInfo = QLineEdit(self.frame_51)
        self.chipOtherInfo.setObjectName(u"chipOtherInfo")
        self.chipOtherInfo.setMinimumSize(QSize(0, 18))
        self.chipOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.chipOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.chipOtherInfo)


        self.horizontalLayout_21.addWidget(self.frame_51)


        self.verticalLayout_30.addWidget(self.frame_49)


        self.verticalLayout_24.addWidget(self.frame_47)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer)

        self.chipWarning = QLabel(self.frame_20)
        self.chipWarning.setObjectName(u"chipWarning")
        self.chipWarning.setFont(font3)
        self.chipWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chipWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.chipWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.chipWarning)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_12)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 30))
        self.frame_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_24)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.chipPlateDefaut = QCheckBox(self.frame_24)
        self.chipPlateDefaut.setObjectName(u"chipPlateDefaut")
        sizePolicy4.setHeightForWidth(self.chipPlateDefaut.sizePolicy().hasHeightForWidth())
        self.chipPlateDefaut.setSizePolicy(sizePolicy4)
        self.chipPlateDefaut.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_25.addWidget(self.chipPlateDefaut)


        self.verticalLayout_24.addWidget(self.frame_24)


        self.verticalLayout_17.addWidget(self.frame_20)

        self.frame_43 = QFrame(self.frame_19)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 60))
        self.frame_43.setMaximumSize(QSize(16777215, 60))
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(351, 0))
        self.frame_44.setMaximumSize(QSize(351, 81))
        self.frame_44.setStyleSheet(u"QPushButton {\n"
"        background-color: #cccccc; /* Cor de fundo do bot\u00e3o */\n"
"        color: #333333; /* Cor do texto */\n"
"        border: 2px solid #999999; /* Borda */\n"
"        border-radius: 5px; /* Bordas arredondadas */\n"
"        font-size: 15px; /* Tamanho da fonte */\n"
"		font-family: \"Yu Gothic\"; /* Fam\u00edlia da fonte */\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #b3b3b3; /* Cor de fundo ao passar o mouse */\n"
"        border: 2px solid #55aaff; /* Borda ao passar o mouse */\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: #999999; /* Cor de fundo quando pressionado */\n"
"        border: 2px solid #444444; /* Borda quando pressionado */\n"
"    }")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.chipPlateApply = QPushButton(self.frame_44)
        self.chipPlateApply.setObjectName(u"chipPlateApply")
        self.chipPlateApply.setMinimumSize(QSize(100, 30))
        self.chipPlateApply.setMaximumSize(QSize(150, 16777215))
        self.chipPlateApply.setFont(font4)

        self.horizontalLayout_19.addWidget(self.chipPlateApply)

        self.chipPlateFinish = QPushButton(self.frame_44)
        self.chipPlateFinish.setObjectName(u"chipPlateFinish")
        self.chipPlateFinish.setEnabled(False)
        self.chipPlateFinish.setMinimumSize(QSize(100, 30))
        self.chipPlateFinish.setMaximumSize(QSize(150, 16777215))
        self.chipPlateFinish.setFont(font4)
        self.chipPlateFinish.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.chipPlateFinish)


        self.horizontalLayout_18.addWidget(self.frame_44)


        self.verticalLayout_17.addWidget(self.frame_43)


        self.horizontalLayout_13.addWidget(self.frame_19)

        self.plotChipPlateArea = QFrame(self.frame_18)
        self.plotChipPlateArea.setObjectName(u"plotChipPlateArea")
        sizePolicy2.setHeightForWidth(self.plotChipPlateArea.sizePolicy().hasHeightForWidth())
        self.plotChipPlateArea.setSizePolicy(sizePolicy2)
        self.plotChipPlateArea.setMinimumSize(QSize(634, 600))
        self.plotChipPlateArea.setStyleSheet(u"background-color: rgb(237,237,237);\n"
"border-radius: 10px;")
        self.plotChipPlateArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotChipPlateArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.plotChipPlateArea)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_13.addWidget(self.plotChipPlateArea)


        self.verticalLayout_16.addWidget(self.frame_18)


        self.verticalLayout_4.addWidget(self.frame_15)

        self.pages.addWidget(self.chipPlatePage)

        self.verticalLayout_7.addWidget(self.pages)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 20))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_7.addWidget(self.frame_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Script", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SIMULATION DATAS", None))
        self.eulerianButton.setText(QCoreApplication.translate("MainWindow", u"Eulerian", None))
        self.chipPlateButton.setText(QCoreApplication.translate("MainWindow", u"Chip Plate", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.assemblyButton.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EULERIAN GEOMETRY", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Part Informartion", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Trickness:", None))
        self.eulerianName.setText("")
        self.eulerianName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.eulerianHeight.setText("")
        self.eulerianHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianWidth.setText("")
        self.eulerianWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianTrickness.setText("")
        self.eulerianTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Partition Position", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"X3:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"X4:", None))
        self.eulerianPartitionX1.setText("")
        self.eulerianPartitionX1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX2.setText("")
        self.eulerianPartitionX2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX3.setText("")
        self.eulerianPartitionX3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX4.setText("")
        self.eulerianPartitionX4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Y3:", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Y4:", None))
        self.eulerianPartitionY1.setText("")
        self.eulerianPartitionY1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY2.setText("")
        self.eulerianPartitionY2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY3.setText("")
        self.eulerianPartitionY3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY4.setText("")
        self.eulerianPartitionY4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianGlobalSize.setText("")
        self.eulerianGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianDeviationFactor.setText("")
        self.eulerianDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianMininumFactor.setText("")
        self.eulerianMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianOtherInfo.setText("")
        self.eulerianOtherInfo.setPlaceholderText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianOtherInfo_2.setText("")
        self.eulerianOtherInfo_2.setPlaceholderText("")
        self.eulerianOtherInfo_3.setText("")
        self.eulerianOtherInfo_3.setPlaceholderText("")
        self.eulerianOtherInfo_4.setText("")
        self.eulerianOtherInfo_4.setPlaceholderText("")
        self.eulerianOtherInfo_5.setText("")
        self.eulerianOtherInfo_5.setPlaceholderText("")
        self.eulerianWarning.setText("")
        self.eulerianDefaut.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.eulerianApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.eulerianFinish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TOOL GEOMETRY", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Trickness:", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Rake Angle:", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Rake Dimension:", None))
        self.toolName.setText("")
        self.toolName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.toolTrickness.setText("")
        self.toolTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeAngle.setText("")
        self.toolRakeAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeDimension.setText("")
        self.toolRakeDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Clerance Angle:", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Clearance Dimension:", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.label_164.setText("")
        self.toolClearanceAngle.setText("")
        self.toolClearanceAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolClearanceDimension.setText("")
        self.toolClearanceDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRadius.setText("")
        self.toolRadius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_165.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Partition Information", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Size Partition 01:", None))
        self.toolPartition01.setText("")
        self.toolPartition01.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Size Partiton 02", None))
        self.toolPartition02.setText("")
        self.toolPartition02.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolGlobalSize.setText("")
        self.toolGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolDeviationFactor.setText("")
        self.toolDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolMinimumFactor.setText("")
        self.toolMinimumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo.setText("")
        self.toolOthersInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolOthersInfo_2.setText("")
        self.toolOthersInfo_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_5.setText("")
        self.toolOthersInfo_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_3.setText("")
        self.toolOthersInfo_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_4.setText("")
        self.toolOthersInfo_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolWarning.setText("")
        self.toolDefaut.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.toolApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.toolFinish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_7.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Eulerian Position", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lineEdit_159.setText("")
        self.lineEdit_159.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lineEdit_160.setText("")
        self.lineEdit_160.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Tool Position", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.lineEdit_125.setText("")
        self.lineEdit_125.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.lineEdit_126.setText("")
        self.lineEdit_126.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Chip Plate Position", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Clearance Over Workpiece:", None))
        self.lineEdit_119.setText("")
        self.lineEdit_119.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Distance From Tool:", None))
        self.lineEdit_120.setText("")
        self.lineEdit_120.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"General Positions", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Feed:", None))
        self.lineEdit_127.setText("")
        self.lineEdit_127.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipPlateDefaut_5.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.assemblyApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.assemblyFinish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CHIP PLATE GEOMETRY", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Part Informartion", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Trickness:", None))
        self.chipName.setText("")
        self.chipName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.chipHeight.setText("")
        self.chipHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipWidth.setText("")
        self.chipWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipTrickness.setText("")
        self.chipTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.chipGlobalSize.setText("")
        self.chipGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a size", None))
        self.chipDeviationFactor.setText("")
        self.chipDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a size", None))
        self.chipMininumFactor.setText("")
        self.chipMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a size", None))
        self.chipOtherInfo.setText("")
        self.chipOtherInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a size", None))
        self.chipWarning.setText("")
        self.chipPlateDefaut.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.chipPlateApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.chipPlateFinish.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior", None))
    # retranslateUi

