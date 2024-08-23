import json
import matplotlib.pyplot as plt

from vectors import Vectors
from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas





class ChipPlate():
    def __init__(self):
        super(ChipPlate, self).__init__()

    # Load data from JSON and store UI elements and corresponding values in a dictionary
    def init(self):
        path = 'S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json'
        with open(path, 'r') as json_file:
            data = json.load(json_file)

        # Store UI elements and corresponding values in a dictionary
        self.chip_elements = {self.ui.chipName: str(data['chipPlateData']['createPartInformation']['Name']),
                         self.ui.chipHeight: str(data['chipPlateData']['createPartInformation']['Height']),
                         self.ui.chipWidth: str(data['chipPlateData']['createPartInformation']['Width']),
                         self.ui.chipTrickness: str(data['chipPlateData']['createPartInformation']['Trickness']),
                         self.ui.chipGlobalSize: str(data['chipPlateData']['createMeshInformation']['globalSize']),
                         self.ui.chipMininumFactor: str(data['chipPlateData']['createMeshInformation']['minSizeFactor']),
                         self.ui.chipDeviationFactor: str(data['chipPlateData']['createMeshInformation']['deviationFactor']),
                         self.ui.chipOtherInfo: "defaut"}


    # Update the UI elements based on the checkbox state
    def setDefautInfos(self):
        for key, value in self.chip_elements.items():
            key.setText(value if self.ui.chipPlateDefaut.isChecked() else "")


    # Get info from GUI and if all required information is provided, generate the 3D graph, otherwise clear the previous plot
    def setInfo(self):
        # If all required information is provided, generate the 3D graph, otherwise clear the previous plot
        all_Infos = Page_Layout.setGeneralInfos(self, 4)
        if all_Infos:
            ChipPlate.plot3dGraph(self)
            self.ui.chipWarning.setText("")
        else:
            self.axChip.clear()
            self.axChip.set_axis_off()
            self.canvasChip.draw()


    # Plot graph
    def plot3dGraph(self):
        # Set up 3D plot
        chip_faces = Vectors.chipPlateDatas(self, 0, 0, 0)
        self.axChip.add_collection3d(Poly3DCollection(chip_faces, facecolors='lightblue', linewidth=1, edgecolors='grey', alpha=0.8))
        # Set up plot layout
        Page_Layout.axisLayout(self, 'ChipPlate')
        Page_Layout.resize(self)
        self.ui.chipPlateFinish.setEnabled(True)


    # Save the user inputs
    def saveInfos(self):
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        data['chipPlateData']['createPartInformation']['Name'] = self.ui.chipName.text()
        data['chipPlateData']['createPartInformation']['Width'] = float(self.ui.chipWidth.text())
        data['chipPlateData']['createPartInformation']['Height'] = float(self.ui.chipHeight.text())
        data['chipPlateData']['createPartInformation']['Trickness'] = float(self.ui.chipTrickness.text())
        data['chipPlateData']['createMeshInformation']['globalSize'] = float(self.ui.chipGlobalSize.text())
        data['chipPlateData']['createMeshInformation']['deviationFactor'] = float(self.ui.chipDeviationFactor.text())
        data['chipPlateData']['createMeshInformation']['minSizeFactor'] = float(self.ui.chipMininumFactor.text())

        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.ui.chipPlateFinish.setEnabled(False)

