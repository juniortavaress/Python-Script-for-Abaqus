from imports import *
from pageLayout import Page_Layout
from graphLayout import Graph_Layout

class ChipPlate():
    def __init__(self):
        super(ChipPlate, self).__init__()


    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def setInfo(self):
        all_Infos = Page_Layout.setGeneralInfos(self, 4)
        if all_Infos:
            self.axChip.clear()
            ChipPlate.plot3dGraph(self)
            self.ui.chipWarning.setText("")
        else:
            self.axChip.clear()
            self.axChip.set_axis_off()
            self.canvasChip.draw()


    # Plot graph
    def plot3dGraph(self):
        # Set up 3D plot
        chip_faces = FacesGenerator.chipPlateDatas(self, 0, 0, 0)
        self.axChip.add_collection3d(Poly3DCollection(chip_faces, facecolors='#48bca6', linewidth=1, edgecolors='white', alpha=0.8))
        # Set up plot layout
        Graph_Layout.axisLayout(self, 'ChipPlate')
        Graph_Layout.resize(self)
        self.ui.chipPlateFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        try:
            with open(self.path_datas_input, 'r') as json_file:
                data = json.load(json_file)
        except:
            data = {"generalInformation": {"modelName": "PythonModel"}}


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

        with open(self.path_datas_input, 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.chipPlateFinish.setEnabled(False)
        self.ui.toolButton.setEnabled(True)
        self.ui.chipPlateButton.setChecked(True)


