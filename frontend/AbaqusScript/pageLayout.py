import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Basically defines which buttons are available depending on the user's interaction
class Page_Layout():
    def __init__(self):
        super(Page_Layout, self).__init__()



    def setCanvas(self):
        # Create the 'figure' where the plot will be drawn, and its axis
        # Turn off the axis to hide it when opening the interface
        # Set the background color of the plot
        # Create the canvas -> essentially a widget used to plot graphs in PyQt
        # Set the canvas to occupy the entire space of the Plot frame
        # Set the "parent" of the canvas, which is where the canvas will be placed
        self.fig, self.ax = plt.subplots()
        self.ax.axis(False)
        self.fig.set_facecolor((237/255, 237/255, 237/255))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setGeometry(self.ui.plotArea.contentsRect())
        self.canvas.setParent(self.ui.plotArea)


    def resize(self):
        # Get the current dimensions of the 'Plot' frame at the time the function is called
        # Set the position and size of the canvas (x, y, width, height) to match the 'Plot' frame
        # Automatically adjust the layout of the figure relative to the canvas and axis (ax)
        # Redraw the plot
        size = self.ui.plotArea.size()
        self.canvas.setGeometry(0, 0, size.width(), size.height())
        self.ax.figure.tight_layout()
        self.canvas.draw()
