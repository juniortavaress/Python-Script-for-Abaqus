from AuxFiles.imports import *
from Form.ui_form import Ui_MainWindow
from AuxFiles.callbackButtons import ButtonsCallback
import rc_Icons

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread = None
        ButtonsCallback.add_path(self)
        ButtonsCallback.start(self)
        ButtonsCallback.activate_buttons(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

