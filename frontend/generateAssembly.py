from imports import *
from pageLayout import Page_Layout
from graphLayout import Graph_Layout
from generateEulerian import Eulerian

class Assembly():
    def __init__(self):
        super(Assembly, self).__init__()

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
        chip_faces = FacesGenerator.chipPlateDatas(self, self.xChipPlatePosition, 0, self.zChipPlatePosition)
        self.axAssembly.add_collection3d(Poly3DCollection(chip_faces, facecolors='black', linewidth=1, edgecolors='black', alpha=1))

        # Create Eulerian
        eulerian_faces = FacesGenerator.eulerianDatas(self)
        Eulerian.createPartitionEulerian(self, self.axAssembly)
        self.axAssembly.add_collection3d(Poly3DCollection(eulerian_faces, facecolors='#48bca6', linewidths=0.8, edgecolors='black', alpha=0.2))

        # Create Tool
        self.ui.xTool.setText(str(x))
        self.ui.yTool.setText(str(partitions))
        tool_faces = FacesGenerator.toolDatas(self, "assembly")
        self.axAssembly.add_collection3d(Poly3DCollection(tool_faces, facecolors='#01dcdc', linewidth=0.5, edgecolors='black', alpha=1))

        # Set up plot layout
        Graph_Layout.axisLayout(self, "Assembly")
        Graph_Layout.resize(self)
        self.ui.assemblyFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        try:
            with open(self.path_datas_input, 'r') as json_file:
                data = json.load(json_file)
        except:
            data = {"generalInformation": {"modelName": "PythonModel"}}

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


        with open(self.path_datas_input, 'w') as file:
            json.dump(data, file, indent=4)


        try:
            for file in os.listdir(self.paht_folder_simulation_datas):
                pathFile = os.path.join(self.paht_folder_simulation_datas, file)
                os.remove(pathFile)
        except:
            os.makedirs(self.paht_folder_simulation_datas)

        with open(self.path_datas_single_simulation, 'w') as file:
            json.dump(data, file, indent=4)


        self.ui.assemblyFinish.setEnabled(False)
        self.ui.iterateButton.setEnabled(True)
        self.ui.assemblyButton.setChecked(True)

