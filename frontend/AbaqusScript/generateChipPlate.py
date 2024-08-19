import json
import matplotlib.pyplot as plt

from PySide6.QtCore import QTimer
from pageLayout import Page_Layout
from PySide6.QtWidgets import QLineEdit
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class ChipPlate():
    def __init__(self):
        super(ChipPlate, self).__init__()


    def setDefautInfos(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Store UI elements and corresponding values in a dictionary
        chip_elements = {self.ui.chipName: str(data['chipPlateData']['createPartInformation']['Name']),
                         self.ui.chipHeight: str(data['chipPlateData']['createPartInformation']['Height']),
                         self.ui.chipWidth: str(data['chipPlateData']['createPartInformation']['Width']),
                         self.ui.chipTrickness: str(data['chipPlateData']['createPartInformation']['Trickness']),
                         self.ui.chipGlobalSize: str(data['chipPlateData']['createMeshInformation']['globalSize']),
                         self.ui.chipMininumFactor: str(data['chipPlateData']['createMeshInformation']['minSizeFactor']),
                         self.ui.chipDeviationFactor: str(data['chipPlateData']['createMeshInformation']['deviationFactor']),
                         self.ui.chipOtherInfo: "defaut"}

        # Update the UI elements based on the checkbox state
        for key, value in chip_elements.items():
            key.setText(value if self.ui.chipPlateDefaut.isChecked() else "")


    def setInfo(self, widget):
        # Initialize a flag to track if all required information is provided
        all_Infos = True

        # List of names for the QLineEdit widgets that need to be checked
        allInfos = ["chipName", "chipHeight", "chipWidth", "chipTrickness", "chipGlobalSize", "chipDeviationFactor", "chipMininumFactor"]
        numericalInfos = ["chipHeight", "chipWidth", "chipTrickness", "chipGlobalSize", "chipDeviationFactor", "chipMininumFactor"]

        # Iterate over each widget name in the list
        # Find the QLineEdit widget by its object name
        # Check if the text in the QLineEdit widget is empty
        # If the text is empty, set the flag to False and display a warning message
        for info in allInfos:
            lineEdit = widget.findChild(QLineEdit, info)
            if not lineEdit.text().strip():
                all_Infos = False
                self.ui.chipWarning.setText("Set all parameters")
                QTimer.singleShot(4000, lambda: self.ui.chipWarning.setText(""))

        if lineEdit.text().strip():
            for info in numericalInfos:
                lineEdit = widget.findChild(QLineEdit, info)
                try:
                    float(lineEdit.text())
                except:
                    all_Infos = False
                    self.ui.chipWarning.setText("The parameter '" + info + "' must be a number value")
                    QTimer.singleShot(4000, lambda: self.ui.chipWarning.setText(""))

        # If all required information is provided, generate the 3D graph
        # If not all information is provided, clear the previous plot
        if all_Infos:
            print('chegou')
            ChipPlate.plot3dGraph(self)
            self.ui.chipWarning.setText("")
        else:
            self.axChip.clear()
            self.axChip.set_axis_off()
            self.canvasChip.draw()


    def plot3dGraph(self):
          # Clear the existing plot on the axes
          self.axChip.clear()
          self.axChip.axis(False)

          # Define the dimensions of the chip plate
          width = float(self.ui.chipWidth.text())
          trickness = float(self.ui.chipTrickness.text())
          height = float(self.ui.chipHeight.text())

          # Defining the vertices of the geometry
          vertices = [[0, 0, 0],
                      [width, 0, 0],
                      [width, trickness, 0],
                      [0, trickness, 0],
                      [0, 0, height],
                      [width, 0, height],
                      [width, trickness, height],
                      [0, trickness, height]]

          # Defining the faces of the geometry using the vertices
          faces = [[vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom face
                   [vertices[7], vertices[6], vertices[2], vertices[3]],  # Top face
                   [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left face
                   [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
                   [vertices[0], vertices[1], vertices[2], vertices[3]],  # Front face
                   [vertices[4], vertices[5], vertices[6], vertices[7]]]  # Back face

          # Create a 3D subplot within the existing figure
          self.axChip = self.figChip.add_subplot(111, projection='3d')

          # Creating the Poly3DCollection from the faces
          self.axChip.add_collection3d(Poly3DCollection(faces, facecolors='lightblue', linewidth=1, edgecolors='grey', alpha=0.8))

          # Setting the axis limits and remove axis lines, tick labels, and axis labels
          self.axChip.set_xlim([0, width])
          self.axChip.set_ylim([-0.1*width, 0.1*width])
          self.axChip.set_zlim([-0.1*width, 0.1*width])
          self.axChip.set_axis_off()  # Turn off the axis
          self.axChip.view_init(elev=30, azim=45)

          # Redraw the canvas to reflect the new plot
          self.axChip.set_facecolor((237/255, 237/255, 237/255))
          self.figChip.tight_layout()
          self.canvasChip.draw()
          Page_Layout.resize(self)
          self.ui.chipPlateFinish.setEnabled(True)


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

