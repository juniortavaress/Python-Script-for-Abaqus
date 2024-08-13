# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ui_form import Ui_MainWindow
from pageLayout import Page_Layout

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCanvas()
        self.chipPlateGraph()

        self.resizeEvent = lambda event: Page_Layout.resize(self)


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
        Page_Layout.resize(self)

    def chipPlateGraph(self):
        # Clear the existing plot on the axes
        self.ax.clear()
        self.ax.axis(False)
        # Defining the dimensions of the bar
        length = 200000  # Length in mm
        width = 10  # Width in mm
        height = 10  # Height in mm

        # Defining the vertices of the cuboid (bar)
        vertices = [[0, 0, 0],
                    [length, 0, 0],
                    [length, width, 0],
                    [0, width, 0],
                    [0, 0, height],
                    [length, 0, height],
                    [length, width, height],
                    [0, width, height]]

        # Defining the faces of the cuboid using the vertices
        faces = [[vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom face
                 [vertices[7], vertices[6], vertices[2], vertices[3]],  # Top face
                 [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left face
                 [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
                 [vertices[0], vertices[1], vertices[2], vertices[3]],  # Front face
                 [vertices[4], vertices[5], vertices[6], vertices[7]]]  # Back face

        # Create a 3D subplot within the existing figure
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Creating the Poly3DCollection from the faces
        self.ax.add_collection3d(Poly3DCollection(faces, facecolors='black', linewidths=1, edgecolors='grey', alpha=0.8))

        # Setting the axis limits
        self.ax.set_xlim([-50, length + 50])
        self.ax.set_ylim([-30, 30])
        self.ax.set_zlim([-30, 30])

        # Remove axis lines, tick labels, and axis labels
        self.ax.set_axis_off()  # Turn off the axis

        # Redraw the canvas to reflect the new plot

        self.ax.set_facecolor((237/255, 237/255, 237/255))  # Cor de fundo do eixo
        self.canvas.draw()
        Page_Layout.resize(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
