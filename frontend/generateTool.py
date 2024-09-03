from imports import *
from pageLayout import Page_Layout
from graphLayout import Graph_Layout

class Tool():
    def __init__(self):
        super(Tool, self).__init__()


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
        tool_faces = FacesGenerator.toolDatas(self, "Tool")
        self.axTool.add_collection3d(Poly3DCollection(tool_faces, facecolors='#48bca6', linewidths=1, edgecolors='white', alpha=0.8))
        # Set up plot layout
        Graph_Layout.axisLayout(self, "Tool")
        Graph_Layout.resize(self)
        self.ui.toolFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        try:
            with open(self.path_datas_input, 'r') as json_file:
                data = json.load(json_file)
        except:
            data = {"generalInformation": {"modelName": "PythonModel"}}

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

        with open(self.path_datas_input, 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.toolFinish.setEnabled(False)
        self.ui.assemblyButton.setEnabled(True)
        self.ui.toolButton.setChecked(True)
