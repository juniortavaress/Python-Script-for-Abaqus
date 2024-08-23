import json
import numpy as np
import matplotlib.pyplot as plt

from vectors import Vectors
from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from generateEulerian import Eulerian
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Assembly():
    def __init__(self):
        super(Assembly, self).__init__()

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def init(self):
        path = 'S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json'
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        self.assembly_elements = {self.ui.overWorkpiece: str(data['assemblyAndSimulationData']['chipPlatePosition']['clearanceOverWorkpiece']),
                                  self.ui.fromTool: str(data['assemblyAndSimulationData']['chipPlatePosition']['distanceFromTool']),
                                  self.ui.xTool: str(data['assemblyAndSimulationData']['toolPosition']['xPosition']),
                                  self.ui.yTool: str(data['assemblyAndSimulationData']['toolPosition']['yPosition']),
                                  self.ui.feed: str(data['assemblyAndSimulationData']['toolPosition']['feed']),
                                  self.ui.timePeriod: str(data['assemblyAndSimulationData']['stepsAndHistoryInformation']['timePeriod'])}


    # Update the UI elements based on the checkbox state
    def setDefautInfos(self):
        for key, value in self.assembly_elements.items():
            key.setText(value if self.ui.assemblyDefaut.isChecked() else "")


    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def setInfo(self):
        all_Infos = Page_Layout.setGeneralInfos(self, 3)
        if all_Infos:
            self.axAssembly.clear()
            Assembly.plot3DGraph(self)
            self.ui.assemblyWarning.setText("")
        else:
            self.axAssembly.clear()
            self.axAssembly.set_axis_off()
            self.canvasAssembly.draw()


    # Plot graph
    def plot3DGraph(self):
        # Create Chip Plate
        partitions = sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)[1]
        x = sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())])[2]
        self.xChipPlatePosition = x - float(self.ui.chipWidth.text()) - float(self.ui.fromTool.text())
        self.zChipPlatePosition = partitions + float(self.ui.overWorkpiece.text())
        chip_faces = Vectors.chipPlateDatas(self, self.xChipPlatePosition, 0, self.zChipPlatePosition)
        self.axAssembly.add_collection3d(Poly3DCollection(chip_faces, facecolors='black', linewidth=1, edgecolors='black', alpha=1))

        # Create Eulerian
        eulerian_faces = Vectors.eulerianDatas(self)
        Eulerian.createPartitionEulerian(self, self.axAssembly)
        self.axAssembly.add_collection3d(Poly3DCollection(eulerian_faces, facecolors='lightblue', linewidths=0.8, edgecolors='black', alpha=0.2))

        # Create Tool
        self.ui.xTool.setText(str(x))
        self.ui.yTool.setText(str(partitions))
        tool_faces = Vectors.toolDatas(self, "assembly")
        self.axAssembly.add_collection3d(Poly3DCollection(tool_faces, facecolors='#01dcdc', linewidth=0.5, edgecolors='black', alpha=1))

        # Set up plot layout
        Graph_Layout.axisLayout(self, "Assembly")
        Graph_Layout.resize(self)
        self.ui.assemblyFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)

        data["assemblyAndSimulationData"] = {
                                            "chipPlatePosition": {
                                                "clearanceOverWorkpiece": float(self.ui.overWorkpiece.text()),
                                                "distanceFromTool": float(self.ui.fromTool.text())
                                                },
                                            "toolPosition": {
                                                "xPosition": float(self.ui.xTool.text()),
                                                "yPosition": float(self.ui.yTool.text()),
                                                "feed": float(self.ui.feed.text())
                                                },
                                            "stepsAndHistoryInformation": {
                                                "timePeriod": float(self.ui.timePeriod.text())
                                                }
                                            }

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.assemblyFinish.setEnabled(False)
        self.ui.iterateButton.setEnabled(True)
        self.ui.assemblyButton.setChecked(True)

