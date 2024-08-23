import json
import numpy as np
import matplotlib.pyplot as plt

from vectors import Vectors
from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Tool():
    def __init__(self):
        super(Tool, self).__init__()

    def init(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Extract information from the loaded JSON data
        self.tool_elements = {self.ui.toolName: str(data['toolData']['createPartInformation']['Name']),
                         self.ui.toolTrickness: str(data['toolData']['createPartInformation']['Trickness']),
                         self.ui.toolClearanceAngle: str(data['toolData']['createPartInformation']['clearanceAngle']),
                         self.ui.toolRakeAngle: str(data['toolData']['createPartInformation']['rakeAngle']),
                         self.ui.toolClearanceDimension: str(data['toolData']['createPartInformation']['clearanceFaceDimension']),
                         self.ui.toolRakeDimension: str(data['toolData']['createPartInformation']['rakeFaceDimension']),
                         self.ui.toolRadius: str(data['toolData']['createPartInformation']['Radius']),
                         self.ui.toolPartition01: str(data['toolData']['createPartitionInformation']['partition01']),
                         self.ui.toolPartition02: str(data['toolData']['createPartitionInformation']['partition02']),
                         self.ui.toolGlobalSize: str(data['toolData']['createMeshInformation']['globalSize']),
                         self.ui.toolDeviationFactor: str(data['toolData']['createMeshInformation']['deviationFactor']),
                         self.ui.toolMinimumFactor: str(data['toolData']['createMeshInformation']['minSizeFactor'])}


    # Update the UI elements based on the checkbox state
    def setDefautInfos(self):
        for key, value in self.tool_elements.items():
            key.setText(value if self.ui.toolDefaut.isChecked() else "")


    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def setInfo(self):
        all_Infos = Page_Layout.setGeneralInfos(self, 2)
        if all_Infos:
            self.axTool.clear()
            Tool.plot3dGraph(self)
            self.ui.toolWarning.setText("")
        else:
            self.axTool.clear()
            self.axTool.set_axis_off()
            self.canvasTool.draw()


    # Plot graph
    def plot3dGraph(self):
        # Set up 3D plot
        tool_faces = Vectors.toolDatas(self, "Tool")
        self.axTool.add_collection3d(Poly3DCollection(tool_faces, facecolors='lightblue', linewidths=1, edgecolors='grey', alpha=0.8))
        # Set up plot layout
        Graph_Layout.axisLayout(self, "Tool")
        Graph_Layout.resize(self)
        self.ui.toolFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)

        data["toolData"] = {
                            "createPartInformation": {
                                "Name": self.ui.toolName.text(),
                                "Trickness": float(self.ui.toolTrickness.text()),
                                "clearanceAngle": float(self.ui.toolClearanceAngle.text()),
                                "rakeAngle": float(self.ui.toolRakeAngle.text()),
                                "clearanceFaceDimension": float(self.ui.toolClearanceDimension.text()),
                                "rakeFaceDimension": float(self.ui.toolRakeDimension.text()),
                                "Radius": float(self.ui.toolRadius.text()),
                                },
                            "createPartitionInformation": {
                                "partition01": float(self.ui.toolPartition01.text()),
                                "partition02": float(self.ui.toolPartition02.text())
                                },
                            "createMeshInformation": {
                                "globalSize": float(self.ui.toolGlobalSize.text()),
                                "deviationFactor": float(self.ui.toolDeviationFactor.text()),
                                "minSizeFactor": float(self.ui.toolMinimumFactor.text()),
                                "radiusMeshSize": 0.01,
                                "noseBiasMaxMeshSize": 0.06,
                                "partition02MeshSize": 0.1,
                                "noseBiasMinMeshSize": 0.01
                                }
                            }

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.toolFinish.setEnabled(False)
        self.ui.assemblyButton.setEnabled(True)
        self.ui.toolButton.setChecked(True)
