import sys

from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from callbackButtons import ButtonsCallback
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

import rc_Icons

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ButtonsCallback.actions(self)
        Page_Layout.pageNumber(self, 0, None)
        Graph_Layout.createPlotAreas(self)
        self.resizeEvent = lambda event: Graph_Layout.resize(self)

        self.ui.iterationWarning.hide()
        # self.ui.pages.setCurrentIndex(0)
        # Page_Layout.pageNumber(self, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
