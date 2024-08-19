import json
import numpy as np
import matplotlib.pyplot as plt

from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Tool():
    def __init__(self):
        super(Tool, self).__init__()

    def setDefautInfos(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Extract information from the loaded JSON data
        self.PartName = str(data['toolData']['createPartInformation']['Name'])
        self.Trickness = data['toolData']['createPartInformation']['Trickness']
        self.ClearanceAngles = data['toolData']['createPartInformation']['clearanceAngle']
        self.RakeAngle = data['toolData']['createPartInformation']['rakeAngle']
        self.ClearanceFace = data['toolData']['createPartInformation']['clearanceFaceDimension']
        self.RakeFace = data['toolData']['createPartInformation']['rakeFaceDimension']
        self.Radius = data['toolData']['createPartInformation']['Radius']
        self.Partition01 = data['toolData']['createPartitionInformation']['partition01']
        self.Partition02 = data['toolData']['createPartitionInformation']['partition02']
        self.GlobalSize = data['toolData']['createMeshInformation']['globalSize']
        self.DeviationFactor = data['toolData']['createMeshInformation']['deviationFactor']
        self.MinSizeFactor = data['toolData']['createMeshInformation']['minSizeFactor']


        # Check if the default information checkbox is selected and set the UI elements with the extracted data, if checkbox is selected
        if self.ui.toolDefaut.isChecked():
            self.ui.toolName.setText(self.PartName)
            self.ui.toolTrickness.setText(str(self.Trickness))
            self.ui.toolRakeAngle.setText(str(self.RakeAngle))
            self.ui.toolRakeDimension.setText(str(self.RakeFace))
            self.ui.toolClearanceAngle.setText(str(self.ClearanceAngles))
            self.ui.toolClearanceDimension.setText(str(self.ClearanceFace))
            self.ui.toolRadius.setText(str(self.Radius))
            self.ui.toolPartition01.setText(str(self.Partition01))
            self.ui.toolPartition02.setText(str(self.Partition02))
            self.ui.toolGlobalSize.setText(str(self.GlobalSize))
            self.ui.toolMinimumFactor.setText(str(self.MinSizeFactor))
            self.ui.toolDeviationFactor.setText(str(self.DeviationFactor))
            self.ui.toolOthersInfo.setText("defaut")
            self.ui.toolOthersInfo_2.setText("defaut")
            self.ui.toolOthersInfo_3.setText("defaut")
            self.ui.toolOthersInfo_4.setText("defaut")
            self.ui.toolOthersInfo_5.setText("defaut")

        # Clear the UI elements if default information checkbox is not selected
        else:
            self.ui.toolName.setText("")
            self.ui.toolTrickness.setText("")
            self.ui.toolRakeAngle.setText("")
            self.ui.toolRakeDimension.setText("")
            self.ui.toolClearanceAngle.setText("")
            self.ui.toolClearanceDimension.setText("")
            self.ui.toolRadius.setText("")
            self.ui.toolPartition01.setText("")
            self.ui.toolPartition02.setText("")
            self.ui.toolGlobalSize.setText("")
            self.ui.toolMinimumFactor.setText("")
            self.ui.toolDeviationFactor.setText("")
            self.ui.toolOthersInfo.setText("")
            self.ui.toolOthersInfo_2.setText("")
            self.ui.toolOthersInfo_3.setText("")
            self.ui.toolOthersInfo_4.setText("")
            self.ui.toolOthersInfo_5.setText("")


    def setInfo(self, widget):
        # Initialize a flag to track if all required information is provided
        all_Infos = True

        # List of names for the QLineEdit widgets that need to be checked
        allInfos = ["toolName", "toolTrickness", "toolRakeAngle", "toolRakeDimension", "toolClearanceAngle", "toolClearanceDimension",
                    "toolRadius", "toolPartition01", "toolPartition02", "toolGlobalSize", "toolDeviationFactor", "toolMinimumFactor"]

        numericalInfos = allInfos[1:]

        # Iterate over each widget name in the list
        # Find the QLineEdit widget by its object name
        # Check if the text in the QLineEdit widget is empty
        # If the text is empty, set the flag to False and display a warning message
        for info in allInfos:
            lineEdit = widget.findChild(QLineEdit, info)
            if not lineEdit.text().strip():
                all_Infos = False
                self.ui.toolWarning.setText("Set all parameters")
                QTimer.singleShot(4000, lambda: self.ui.toolWarning.setText(""))

        if lineEdit.text().strip():
            for info in numericalInfos:
                lineEdit = widget.findChild(QLineEdit, info)
                try:
                    float(lineEdit.text())
                except:
                    all_Infos = False
                    self.ui.toolWarning.setText("The parameter '" + info + "' must be a number value")
                    QTimer.singleShot(4000, lambda: self.ui.toolWarning.setText(""))

        # If all required information is provided, generate the 3D graph
        # If not all information is provided, clear the previous plot
        if all_Infos:
            Tool.plot3dGraph(self)
            self.ui.toolWarning.setText("")
        else:
            self.axTool.clear()
            self.axTool.set_axis_off()
            self.canvasTool.draw()


    def plot3dGraph(self):
        # Clear the existing plot on the axes
        self.axTool.clear()
        self.axTool.axis(False)
        # Defining the dimensions of the bar

        clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
        rakeFaceDimension = float(self.ui.toolRakeDimension.text())
        Trickness = float(self.ui.toolTrickness.text())
        left_angle_rad = np.radians(float(self.ui.toolRakeAngle.text()))
        bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))

        # Defining the vertices of the cuboid (bar)
        vertices = [[0, 0, 0],
                    [0, 0, Trickness],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), 0],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), Trickness],
                    [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                    [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                    [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness]
        ]


        # Defining the faces of the cuboid using the vertices
        faces = []
        verticesSets = [[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 6, 7], [0, 2, 6, 4], [1, 3, 7, 5]]
        for verticeSet in verticesSets:
            face = [vertices[j] for j in verticeSet]
            faces.append(face)

        # Create a 3D subplot within the existing figure
        self.axTool = self.figTool.add_subplot(111, projection='3d')

        # Creating the Poly3DCollection from the faces
        self.axTool.add_collection3d(Poly3DCollection(faces, facecolors='lightblue', linewidths=1, edgecolors='grey', alpha=0.8))

        self.axTool.set_box_aspect([rakeFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(bottom_angle_rad)])

        # # Setting the axis limits
        space = (rakeFaceDimension*np.cos(bottom_angle_rad)-clearanceFaceDimension*np.cos(bottom_angle_rad))/2
        self.axTool.set_xlim(-space, clearanceFaceDimension*np.cos(bottom_angle_rad)+space)
        self.axTool.set_ylim([0, rakeFaceDimension*np.cos(bottom_angle_rad)])
        self.axTool.set_zlim([-(rakeFaceDimension*np.cos(bottom_angle_rad)/10), (rakeFaceDimension*np.cos(bottom_angle_rad)/10)])

        # Remove axis lines, tick labels, and axis labels
        self.axTool.set_axis_off()  # Turn off the axis
        self.axTool.view_init(elev=90, azim=270)

        # Redraw the canvas to reflect the new plot
        self.axTool.set_facecolor((237/255, 237/255, 237/255))
        self.canvasTool.draw()
        Page_Layout.resize(self)
        self.ui.toolFinish.setEnabled(True)



    def saveInfos(self):
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        data['toolData']['createPartInformation']['Name'] = self.ui.toolName.text()
        data['toolData']['createPartInformation']['Trickness'] = float(self.ui.toolTrickness.text())
        data['toolData']['createPartInformation']['clearanceAngle'] = float(self.ui.toolClearanceAngle.text())
        data['toolData']['createPartInformation']['rakeAngle'] = float(self.ui.toolRakeAngle.text())
        data['toolData']['createPartInformation']['clearanceFaceDimension'] = float(self.ui.toolClearanceDimension.text())
        data['toolData']['createPartInformation']['rakeFaceDimension'] = float(self.ui.toolRakeDimension.text())
        data['toolData']['createPartInformation']['Radius'] = float(self.ui.toolRadius.text())
        data['toolData']['createPartitionInformation']['partition01'] = float(self.ui.toolPartition01.text())
        data['toolData']['createPartitionInformation']['partition02'] = float(self.ui.toolPartition02.text())
        data['toolData']['createMeshInformation']['globalSize'] = float(self.ui.toolGlobalSize.text())
        data['toolData']['createMeshInformation']['deviationFactor'] = float(self.ui.toolDeviationFactor.text())
        data['toolData']['createMeshInformation']['minSizeFactor'] = float(self.ui.toolMinimumFactor.text())

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.toolFinish.setEnabled(False)

