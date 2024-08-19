import json
import matplotlib.pyplot as plt

from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Eulerian():
    def __init__(self):
        super(Eulerian, self).__init__()


    def setDefautInfos(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Extract information from the loaded JSON data
        self.PartName = str(data['eulerianData']['createPartInformation']['Name'])
        self.Width = data['eulerianData']['createPartInformation']['Width']
        self.Height = data['eulerianData']['createPartInformation']['Height']
        self.Trickness = data['eulerianData']['createPartInformation']['Trickness']
        self.x_points = data['eulerianData']['createParticionInformation']['x_points']
        self.y_points = data['eulerianData']['createParticionInformation']['y_points']
        self.GlobalSize = data['eulerianData']['createMeshInformation']['globalSize']
        self.DeviationFactor = data['eulerianData']['createMeshInformation']['deviationFactor']
        self.MinSizeFactor = data['eulerianData']['createMeshInformation']['minSizeFactor']


        # Check if the default information checkbox is selected and set the UI elements with the extracted data, if checkbox is selected
        if self.ui.eulerianDefaut.isChecked():
            self.ui.eulerianName.setText(self.PartName)
            self.ui.eulerianHeight.setText(str(self.Height))
            self.ui.eulerianWidth.setText(str(self.Width))
            self.ui.eulerianTrickness.setText(str(self.Trickness))
            self.ui.eulerianGlobalSize.setText(str(self.GlobalSize))
            self.ui.eulerianMininumFactor.setText(str(self.MinSizeFactor))
            self.ui.eulerianDeviationFactor.setText(str(self.DeviationFactor))
            self.ui.eulerianPartitionX1.setText(str(self.x_points[0]))
            self.ui.eulerianPartitionX2.setText(str(self.x_points[1]))
            self.ui.eulerianPartitionX3.setText(str(self.x_points[2]))
            self.ui.eulerianPartitionX4.setText(str(self.x_points[3]))
            self.ui.eulerianPartitionY1.setText(str(self.y_points[0]))
            self.ui.eulerianPartitionY2.setText(str(self.y_points[1]))
            self.ui.eulerianPartitionY3.setText(str(self.y_points[2]))
            self.ui.eulerianPartitionY4.setText(str(self.y_points[3]))
            self.ui.eulerianOtherInfo.setText("defaut")
            self.ui.eulerianOtherInfo_2.setText("defaut")
            self.ui.eulerianOtherInfo_3.setText("defaut")
            self.ui.eulerianOtherInfo_4.setText("defaut")
            self.ui.eulerianOtherInfo_5.setText("defaut")

        # Clear the UI elements if default information checkbox is not selected
        else:
            self.ui.eulerianName.setText("")
            self.ui.eulerianHeight.setText("")
            self.ui.eulerianWidth.setText("")
            self.ui.eulerianTrickness.setText("")
            self.ui.eulerianGlobalSize.setText("")
            self.ui.eulerianMininumFactor.setText("")
            self.ui.eulerianDeviationFactor.setText("")
            self.ui.eulerianPartitionX1.setText("")
            self.ui.eulerianPartitionX2.setText("")
            self.ui.eulerianPartitionX3.setText("")
            self.ui.eulerianPartitionX4.setText("")
            self.ui.eulerianPartitionY1.setText("")
            self.ui.eulerianPartitionY2.setText("")
            self.ui.eulerianPartitionY3.setText("")
            self.ui.eulerianPartitionY4.setText("")
            self.ui.eulerianOtherInfo.setText("")
            self.ui.eulerianOtherInfo_2.setText("")
            self.ui.eulerianOtherInfo_3.setText("")
            self.ui.eulerianOtherInfo_4.setText("")
            self.ui.eulerianOtherInfo_5.setText("")


    def setInfo(self, widget):
        print("setEulerianInfo")
        # Initialize a flag to track if all required information is provided
        all_Infos = True

        # List of names for the QLineEdit widgets that need to be checked
        allInfos = ["eulerianName", "eulerianHeight", "eulerianWidth", "eulerianTrickness", "eulerianGlobalSize", "eulerianDeviationFactor", "eulerianMininumFactor", "eulerianPartitionX1",
                    "eulerianPartitionX2", "eulerianPartitionX3", "eulerianPartitionX4", "eulerianPartitionY1", "eulerianPartitionY2", "eulerianPartitionY3", "eulerianPartitionY4"]
        numericalInfos = allInfos[1:]


        # Iterate over each widget name in the list
        # Find the QLineEdit widget by its object name
        # Check if the text in the QLineEdit widget is empty
        # If the text is empty, set the flag to False and display a warning message
        for info in allInfos:
            lineEdit = widget.findChild(QLineEdit, info)
            if not lineEdit.text().strip():
                all_Infos = False
                self.ui.eulerianWarning.setText("Set all parameters")
                QTimer.singleShot(4000, lambda: self.ui.eulerianWarning.setText(""))

        if lineEdit.text().strip():
            for info in numericalInfos:
                lineEdit = widget.findChild(QLineEdit, info)
                try:
                    float(lineEdit.text())
                except:
                    all_Infos = False
                    self.ui.eulerianWarning.setText("The parameter '" + info + "' must be a number value")
                    QTimer.singleShot(4000, lambda: self.ui.eulerianWarning.setText(""))

        # If all required information is provided, generate the 3D graph
        # If not all information is provided, clear the previous plot
        if all_Infos:
            Eulerian.plot3dGraph(self)
            self.ui.eulerianWarning.setText("")
        else:
            self.axEulerian.clear()
            self.axEulerian.set_axis_off()
            self.canvasEulerian.draw()


    def plot3dGraph(self):
        # Clear the existing plot on the axes
        self.axEulerian.clear()
        self.axEulerian.axis(False)

        # Defining the dimensions of the bar
        width = float(self.ui.eulerianWidth.text())
        trickness = float(self.ui.eulerianTrickness.text())
        height = float(self.ui.eulerianHeight.text())

        # Defining the vertices of the cuboid (bar)
        vertices = [[0, 0, 0],
                    [width, 0, 0],
                    [width, trickness, 0],
                    [0, trickness, 0],
                    [0, 0, height],
                    [width, 0, height],
                    [width, trickness, height],
                    [0, trickness, height]]

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
            self.axEulerian.plot([x_val, x_val], [trickness, trickness], [0, height], 'b-')
            self.axEulerian.plot([x_val, x_val], [0, trickness], [0, 0], 'b-')
            self.axEulerian.plot([x_val, x_val], [0, trickness], [height, height], 'b-')

        # Linhas horizontais
        for y_val in y_values:
            self.axEulerian.plot([0, 0], [0, trickness], [y_val, y_val], 'b-')
            self.axEulerian.plot([width, width], [0, trickness], [y_val, y_val], 'b-')
            self.axEulerian.plot([0, width], [0, 0], [y_val, y_val], 'b-')
            self.axEulerian.plot([0, width], [trickness, trickness], [y_val, y_val], 'b-')

        self.axEulerian.set_box_aspect([6, 6, 6])

        # Setting the axis limits
        self.axEulerian.set_xlim([-(height-width)/2, width + (height-width)/2])
        self.axEulerian.set_ylim([0, 0.1*height])
        self.axEulerian.set_zlim([0, height])

        # Remove axis lines, tick labels, and axis labels
        self.axEulerian.set_axis_off()  # Turn off tahe axis
        self.axEulerian.view_init(elev=0, azim=-90)

        # Redraw the canvas to reflect the new plot
        self.axEulerian.set_facecolor((237/255, 237/255, 237/255))
        self.canvasEulerian.draw()
        Page_Layout.resize(self)
        self.ui.eulerianFinish.setEnabled(True)


    def saveInfos(self):
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        data['eulerianData']['createPartInformation']['Name'] = self.ui.eulerianName.text()
        data['eulerianData']['createPartInformation']['Width'] = float(self.ui.eulerianWidth.text())
        data['eulerianData']['createPartInformation']['Height'] = float(self.ui.eulerianHeight.text())
        data['eulerianData']['createPartInformation']['Trickness'] = float(self.ui.eulerianTrickness.text())
        data['eulerianData']['createMeshInformation']['globalSize'] = float(self.ui.eulerianGlobalSize.text())
        data['eulerianData']['createMeshInformation']['deviationFactor'] = float(self.ui.eulerianDeviationFactor.text())
        data['eulerianData']['createMeshInformation']['minSizeFactor'] = float(self.ui.eulerianMininumFactor.text())
        data['eulerianData']['createParticionInformation']['x_points'] = [float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())]
        data['eulerianData']['createParticionInformation']['y_points'] = [float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())]

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.eulerianFinish.setEnabled(False)

