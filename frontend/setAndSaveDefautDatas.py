from imports import *
from generateEulerian import Eulerian
from generateTool import Tool
from generateChipPlate import ChipPlate
from generateAssembly import Assembly

class DataInicialization():
    def __init__(self):
        super(DataInicialization, self).__init__()

    def getPaths(self):
        self.path_datas_input = os.path.join(self.main_path,  'data/dataInput.json')
        self.path_defaut_datas_input = os.path.join(self.main_path,  'data/dataDefautInput.json')
        self.paht_folder_simulation_datas =os.path.join(self.main_path, 'data/simulationDatas')
        self.path_datas_single_simulation = os.path.join(self.main_path,  'data/simulationDatas/dataInput_singleSimulation.json')

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def getDafautDatas(self):
        with open(self.path_defaut_datas_input, 'r') as json_file:
            data = json.load(json_file)

        self.chip_elements = {self.ui.chipName: str(data['chipPlateData']['createPartInformation']['Name']),
                              self.ui.chipHeight: str(data['chipPlateData']['createPartInformation']['Height']),
                              self.ui.chipWidth: str(data['chipPlateData']['createPartInformation']['Width']),
                              self.ui.chipTrickness: str(data['chipPlateData']['createPartInformation']['Trickness']),
                              self.ui.chipGlobalSize: str(data['chipPlateData']['createMeshInformation']['globalSize']),
                              self.ui.chipMininumFactor: str(data['chipPlateData']['createMeshInformation']['minSizeFactor']),
                              self.ui.chipDeviationFactor: str(data['chipPlateData']['createMeshInformation']['deviationFactor']),
                              self.ui.chipOtherInfo: "defaut"}

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

        self.assembly_elements = {self.ui.overWorkpiece: str(data['assemblyAndSimulationData']['chipPlatePosition']['clearanceOverWorkpiece']),
                                  self.ui.fromTool: str(data['assemblyAndSimulationData']['chipPlatePosition']['distanceFromTool']),
                                  self.ui.xTool: str(data['assemblyAndSimulationData']['toolPosition']['xPosition']),
                                  self.ui.yTool: str(data['assemblyAndSimulationData']['toolPosition']['yPosition']),
                                  self.ui.feed: str(data['assemblyAndSimulationData']['toolPosition']['feed']),
                                  self.ui.timePeriod: str(data['assemblyAndSimulationData']['stepsAndHistoryInformation']['timePeriod'])}


    # Update the UI elements based on the checkbox state
    def setDefautInfos(self):
        Value = True if self.ui.defautValues.isChecked() else False
        self.ui.eulerianButton.setChecked(Value)
        self.ui.chipPlateButton.setEnabled(Value)
        self.ui.chipPlateButton.setChecked(Value)
        self.ui.toolButton.setEnabled(Value)
        self.ui.toolButton.setChecked(Value)
        self.ui.assemblyButton.setEnabled(Value)
        self.ui.assemblyButton.setChecked(Value)
        self.ui.iterateButton.setEnabled(Value)

        elements = [self.chip_elements, self.tool_elements, self.eulerian_elements, self.assembly_elements]
        for element in elements:
            for key, value in element.items():
                key.setText(value if self.ui.defautValues.isChecked() else "")

        if self.ui.defautValues.isChecked():
            Eulerian.setInfo(self)
            ChipPlate.setInfo(self)
            Tool.setInfo(self)
            Assembly.setInfo(self)

        else:
            elements = [[self.ui.returnEulerian, self.axEulerian, self.canvasEulerian],
                        [self.ui.returnChipPlate, self.axChip, self.canvasChip],
                        [self.ui.returnTool, self.axTool, self.canvasTool],
                        [self.ui.returnAssembly, self.axAssembly, self.canvasAssembly]]

            for element in elements:
                element[0].setEnabled(True)
                element[1].clear()
                element[1].set_axis_off()
                element[2].draw()


    # Save the user inputs
    def saveInfos(self):
        try:
            with open(self.path_datas_input, 'r') as json_file:
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
        self.ui.eulerianFinish.setEnabled(False)
        self.ui.returnEulerian.setEnabled(False)
        self.ui.eulerianButton.setChecked(True)
        self.ui.chipPlateButton.setEnabled(True)

        data["chipPlateData"] = {
                                "createPartInformation": {
                                    "Name": self.ui.chipName.text(),
                                    "Width": float(self.ui.chipWidth.text()),
                                    "Trickness": float(self.ui.chipTrickness.text()),
                                    "Height": float(self.ui.chipHeight.text())
                                    },
                                "createMeshInformation": {
                                    "globalSize": float(self.ui.chipGlobalSize.text()),
                                    "deviationFactor": float(self.ui.chipDeviationFactor.text()),
                                    "minSizeFactor": float(self.ui.chipMininumFactor.text())
                                    }
                                }
        self.ui.chipPlateFinish.setEnabled(False)
        self.ui.returnChipPlate.setEnabled(False)
        self.ui.chipPlateButton.setChecked(True)
        self.ui.toolButton.setEnabled(True)

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
        self.ui.toolFinish.setEnabled(False)
        self.ui.returnTool.setEnabled(False)
        self.ui.toolButton.setChecked(True)
        self.ui.assemblyButton.setEnabled(True)

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
        self.ui.assemblyFinish.setEnabled(False)
        self.ui.returnAssembly.setEnabled(False)
        self.ui.assemblyButton.setChecked(True)
        self.ui.iterateButton.setEnabled(True)

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








