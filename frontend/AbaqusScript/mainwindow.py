import sys

from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow

from pageLayout import Page_Layout
from callbackButtons import ButtonsCallback


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ButtonsCallback.actions(self)
        Page_Layout.initialPage(self)
        Page_Layout.createPlotAreas(self)

        self.ui.pages.setCurrentIndex(0)
        self.resizeEvent = lambda event: Page_Layout.resize(self)

        self.ui.chipPlateApply.clicked.connect(lambda: self.createImage("Chip Plate"))
        self.ui.eulerianApply.clicked.connect(lambda: self.createImage("Eulerian"))
        self.ui.assemblyApply.clicked.connect(lambda: self.createImage("Assembly"))
        self.ui.toolApply.clicked.connect(lambda: self.createImage("Tool"))


    def createImage(self, page):
        from generateTool import Tool
        from generateEulerian import Eulerian
        from generateChipPlate import ChipPlate
        if page == "Eulerian":
            Eulerian.setInfo(self, widget)
        elif page == "Chip Plate":
            ChipPlate.setInfo(self, widget)
        elif page == "Tool":
            Tool.setInfo(self, widget)
        elif page == "Assembly":
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
