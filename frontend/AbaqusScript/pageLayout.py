import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


# Basically defines which buttons are available depending on the user's interaction

class Page_Layout():
    def __init__(self):
        super(Page_Layout, self).__init__()


    def createPlotAreas(self):
        # background_color = (237/255, 237/255, 237/255)

        self.figTool, self.axTool, self.canvasTool = Page_Layout.setCanvas(self, self.ui.plotToolArea)
        self.figChip, self.axChip, self.canvasChip = Page_Layout.setCanvas(self, self.ui.plotChipPlateArea)
        self.figAssembly, self.axAssembly, self.canvasAssembly = Page_Layout.setCanvas(self, self.ui.plotAssemblyArea)
        self.figEulerian, self.axEulerian, self.canvasEulerian = Page_Layout.setCanvas(self, self.ui.plotEulerianArea)


    def setCanvas(self, plot_area):
        fig, ax = plt.subplots()
        ax.axis(False)
        fig.set_facecolor((237/255, 237/255, 237/255))
        canvas = FigureCanvas(fig)
        canvas.setGeometry(plot_area.contentsRect())
        canvas.setParent(plot_area)
        return fig, ax, canvas





    def resize(self):
        # Get the current dimensions of the 'Plot' frame at the time the function is called
        # Set the position and size of the canvas (x, y, width, height) to match the 'Plot' frame
        # Automatically adjust the layout of the figure relative to the canvas and axis (ax)
        # Redraw the plot
        size = self.ui.plotChipPlateArea.size()
        self.canvasChip.setGeometry(0, 0, size.width(), size.height())
        self.axChip.figure.tight_layout()
        self.canvasChip.draw()

        size = self.ui.plotEulerianArea.size()
        self.canvasEulerian.setGeometry(0, 0, size.width(), size.height())
        self.axEulerian.figure.tight_layout()
        self.canvasEulerian.draw()

        size = self.ui.plotToolArea.size()
        self.canvasTool.setGeometry(0, 0, size.width(), size.height())
        self.axTool.figure.tight_layout()
        self.canvasTool.draw()


    def createGeometry(self, page):
        self.setMinimumSize(1500, 850)
        self.showMaximized()
        if page == "Eulerian":
            self.ui.pages.setCurrentIndex(1)
            Page_Layout.resize(self)
        elif page == "Chip Plate":
            self.ui.pages.setCurrentIndex(4)
            Page_Layout.resize(self)
        elif page == "Tool":
            self.ui.pages.setCurrentIndex(2)
            Page_Layout.resize(self)
        elif page == "Assembly":
            self.ui.pages.setCurrentIndex(3)
            Page_Layout.resize(self)


    def initialPage(self):
        self.setMinimumSize(300, 364)
        self.ui.pages.setCurrentIndex(0)
        self.resize(300, 364)
