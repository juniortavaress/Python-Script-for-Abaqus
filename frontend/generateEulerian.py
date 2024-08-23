import json
import matplotlib.pyplot as plt

from vectors import Vectors
from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Eulerian():
    def __init__(self):
        super(Eulerian, self).__init__()

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def init(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        self.eulerian_elements = {self.ui.eulerianName: str(data['eulerianData']['createPartInformation']['Name']),
                             self.ui.eulerianWidth: str(data['eulerianData']['createPartInformation']['Width']),
                             self.ui.eulerianHeight: str(data['eulerianData']['createPartInformation']['Height']),
                             self.ui.eulerianTrickness: str(data['eulerianData']['createPartInformation']['Trickness']),
                             self.ui.eulerianPartitionX1: str(data['eulerianData']['createParticionInformation']['x_points'][0]),
                             self.ui.eulerianPartitionX2: str(data['eulerianData']['createParticionInformation']['x_points'][1]),
                             self.ui.eulerianPartitionX3: str(data['eulerianData']['createParticionInformation']['x_points'][2]),
                             self.ui.eulerianPartitionX4: str(data['eulerianData']['createParticionInformation']['x_points'][3]),
                             self.ui.eulerianPartitionY1: str(data['eulerianData']['createParticionInformation']['y_points'][0]),
                             self.ui.eulerianPartitionY2: str(data['eulerianData']['createParticionInformation']['y_points'][1]),
                             self.ui.eulerianPartitionY3: str(data['eulerianData']['createParticionInformation']['y_points'][2]),
                             self.ui.eulerianPartitionY4: str(data['eulerianData']['createParticionInformation']['y_points'][3]),
                             self.ui.eulerianGlobalSize: str(data['eulerianData']['createMeshInformation']['globalSize']),
                             self.ui.eulerianDeviationFactor: str(data['eulerianData']['createMeshInformation']['deviationFactor']),
                             self.ui.eulerianMininumFactor: str(data['eulerianData']['createMeshInformation']['minSizeFactor'])}


    # Update the UI elements based on the checkbox state
    def setDefautInfos(self):
        for key, value in self.eulerian_elements.items():
                 key.setText(value if self.ui.eulerianDefaut.isChecked() else "")


    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def setInfo(self):
        all_Infos = Page_Layout.setGeneralInfos(self, 1)
        if all_Infos:
            self.axEulerian.clear()
            Eulerian.plot3dGraph(self)
            self.ui.eulerianWarning.setText("")
        else:
            self.axEulerian.clear()
            self.axEulerian.set_axis_off()
            self.canvasEulerian.draw()


    # Plot graph
    def plot3dGraph(self):
        # Set up 3D plot
        eulerian_faces = Vectors.eulerianDatas(self)
        Eulerian.createPartitionEulerian(self, self.axEulerian)
        self.axEulerian.add_collection3d(Poly3DCollection(eulerian_faces, facecolors='lightblue', linewidths=1, edgecolors='grey', alpha=0.5))
        # Set up plot layout
        Graph_Layout.axisLayout(self, "Eulerian")
        Graph_Layout.resize(self)
        self.ui.eulerianFinish.setEnabled(True)


    # Generate eulerian partitions
    def createPartitionEulerian(self, axis):
        # Define positions for vertical and horizontal lines on the plot
        x_values = [float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())]
        y_values = [float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())]

        # Plot vertical partitions
        for x_val in x_values:
            axis.plot([x_val, x_val], [0, 0], [0, float(self.ui.eulerianHeight.text())], 'b-')
            axis.plot([x_val, x_val], [float(self.ui.eulerianTrickness.text()), float(self.ui.eulerianTrickness.text())], [0, float(self.ui.eulerianHeight.text())], 'b-')
            axis.plot([x_val, x_val], [0, float(self.ui.eulerianTrickness.text())], [0, 0], 'b-')
            axis.plot([x_val, x_val], [0, float(self.ui.eulerianTrickness.text())], [float(self.ui.eulerianHeight.text()), float(self.ui.eulerianHeight.text())], 'b-')

        # Plot horizontal partitions
        for y_val in y_values:
            axis.plot([0, 0], [0, float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'b-')
            axis.plot([float(self.ui.eulerianWidth.text()), float(self.ui.eulerianWidth.text())], [0, float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'b-')
            axis.plot([0, float(self.ui.eulerianWidth.text())], [0, 0], [y_val, y_val], 'b-')
            axis.plot([0, float(self.ui.eulerianWidth.text())], [float(self.ui.eulerianTrickness.text()), float(self.ui.eulerianTrickness.text())], [y_val, y_val], 'b-')


    # Save the user inputs
    def saveInfos(self):
        try:
            with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
                data = json.load(json_file)
        except:
            data = {"generalInformation": {"modelName": "PythonModel"}}

        data ["eulerianData"] = {
                                "createPartInformation": {
                                    "Name": self.ui.eulerianName.text(),
                                    "Width": float(self.ui.eulerianWidth.text()),
                                    "Trickness": float(self.ui.eulerianTrickness.text()),
                                    "Height": float(self.ui.eulerianHeight.text())
                                    },
                                "createParticionInformation": {
                                    "x_points": sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())]),
                                    "y_points": sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)
                                    },
                                "createMeshInformation": {
                                    "globalSize": float(self.ui.eulerianGlobalSize.text()),
                                    "deviationFactor": float(self.ui.eulerianDeviationFactor.text()),
                                    "minSizeFactor": float(self.ui.eulerianMininumFactor.text())
                                    }
                                }

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.eulerianFinish.setEnabled(False)
        self.ui.chipPlateButton.setEnabled(True)
        self.ui.eulerianButton.setChecked(True)
