from imports import *
from ui_form import Ui_MainWindow
from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from callbackButtons import ButtonsCallback

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.main_path = os.path.dirname(current_directory)
        sys.path.append(self.main_path) if self.main_path not in sys.path else None

        ButtonsCallback.actions(self)
        Page_Layout.pageNumber(self, 0, None, None)
        Page_Layout.pageNumber(self, 6, None, None)
        Graph_Layout.createPlotAreas(self)
        self.resizeEvent = lambda event: Graph_Layout.resize(self)
        self.ui.iterationWarning.hide()

        # print('\nVariaveis')
        # atributos = vars(self)
        # for nome, valor in atributos.items():
        #     print(f"{nome}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
