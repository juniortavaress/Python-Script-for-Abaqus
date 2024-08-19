import numpy as np
import matplotlib.pyplot as plt
from pageLayout import Page_Layout
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Graphs():
    def __init__(self):
        super(Graphs, self).__init__()

    def eulerianGraph3D(self):
        # Clear the existing plot on the axes
        self.axEulerian.clear()
        self.axEulerian.axis(False)

        # Defining the dimensions of the bar
        height = 5
        width = 0.02
        length = 3.8

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
        faces = [[vertices[j] for j in [0, 1, 2, 3]],
                 [vertices[j] for j in [4, 5, 6, 7]],
                 [vertices[j] for j in [0, 1, 5, 4]],
                 [vertices[j] for j in [2, 3, 7, 6]],
                 [vertices[j] for j in [1, 2, 6, 5]],
                 [vertices[j] for j in [4, 7, 3, 0]]]

        # Create a 3D subplot within the existing figure
        self.axEulerian = self.figEulerian.add_subplot(111, projection='3d')

        # Creating the Poly3DCollection from the faces
        self.axEulerian.add_collection3d(Poly3DCollection(faces, facecolors='lightblue', linewidths=1, edgecolors='grey', alpha=0.5))

        x_values = [1.5, 2.7, 3.0, 3.3]
        y_values = [2.8, 1.3, 1.23, 1.1]

        # Linhas verticais
        for x_val in x_values:
            self.axEulerian.plot([x_val, x_val], [0, 0], [0, height], 'b-')
            self.axEulerian.plot([x_val, x_val], [width, width], [0, height], 'b-')
            self.axEulerian.plot([x_val, x_val], [0, width], [0, 0], 'b-')
            self.axEulerian.plot([x_val, x_val], [0, width], [height, height], 'b-')

        # Linhas horizontais
        for y_val in y_values:
            self.axEulerian.plot([0, 0], [0, width], [y_val, y_val], 'b-')
            self.axEulerian.plot([length, length], [0, width], [y_val, y_val], 'b-')
            self.axEulerian.plot([0, length], [0, 0], [y_val, y_val], 'b-')
            self.axEulerian.plot([0, length], [width, width], [y_val, y_val], 'b-')

        self.axEulerian.set_box_aspect([length, width, height])

        # Setting the axis limits
        self.axEulerian.set_xlim([0, 6])
        self.axEulerian.set_ylim([0, 6])
        self.axEulerian.set_zlim([0, 6])

        # Remove axis lines, tick labels, and axis labels
        self.axEulerian.set_axis_off()  # Turn off the axis
        self.axEulerian.view_init(elev=0, azim=-90)

        # Redraw the canvas to reflect the new plot
        self.axEulerian.set_facecolor((237/255, 237/255, 237/255))
        self.canvasEulerian.draw()
        Page_Layout.resize(self)

    def toolGraph3D(self):
        # Clear the existing plot on the axes
        self.axTool.clear()
        self.axTool.axis(False)
        # Defining the dimensions of the bar
        clearanceFaceDimension = 3.35  # Length in mm
        rakeFaceDimension = 5.3
        Trickness = 0.02  # Width in mm
        height = 0.01  # Height in mm

        left_angle_rad = np.radians(12)
        bottom_angle_rad = np.radians(3)

        # Defining the vertices of the cuboid (bar)
        print(clearanceFaceDimension*np.cos(bottom_angle_rad))

        vertices = [[0, 0, 0],
                    [0, 0, Trickness],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), 0],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), Trickness],
                    [rakeFaceDimension*np.sin(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad), 0],
                    [rakeFaceDimension*np.sin(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad), Trickness],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad), 0],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad), Trickness]
        ]


        # Defining the faces of the cuboid using the vertices
        faces = [[vertices[0], vertices[1], vertices[3], vertices[2]],  # Bottom face
                 [vertices[4], vertices[5], vertices[7], vertices[6]],  # Top face
                 [vertices[0], vertices[1], vertices[5], vertices[4]],  # Left face
                 [vertices[2], vertices[3], vertices[6], vertices[7]],  # Right face
                 [vertices[0], vertices[2], vertices[6], vertices[4]],  # Front face
                 [vertices[1], vertices[3], vertices[7], vertices[5]]]  # Back face

        # Create a 3D subplot within the existing figure
        self.axTool = self.figTool.add_subplot(111, projection='3d')

        # Creating the Poly3DCollection from the faces
        self.axTool.add_collection3d(Poly3DCollection(faces, facecolors='black', linewidths=1, edgecolors='grey', alpha=0.8))

        # # Setting the axis limits
        self.axTool.set_xlim([0, 5])
        self.axTool.set_ylim([0, 5])
        self.axTool.set_zlim([0, 1])

        # Remove axis lines, tick labels, and axis labels
        self.axTool.set_axis_off()  # Turn off the axis
        self.axTool.view_init(elev=90, azim=270)

        # Redraw the canvas to reflect the new plot
        self.axTool.set_facecolor((237/255, 237/255, 237/255))
        self.canvasTool.draw()
        Page_Layout.resize(self)
