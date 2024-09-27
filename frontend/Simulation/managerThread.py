import sys
import subprocess
from PySide6.QtCore import QObject, Signal

class WorkerThread(QObject):
    finished = Signal(str)
    # Constructor method for initializing the thread worker
    # self is the self.worker in this file
    def __init__(self, widget, ui, file):
        super().__init__()
        self.main = widget
        self.ui = ui
        self.file = file

    # Manages the thread execution and handles the action
    def thread_manager(self):
        message = self.run_action()
        self.on_abaqus_finished(message)

    # Determines which action to take based on the 'file' value
    def run_action(self):
        action_map = {'INPFiles': self.generate_inp_files, 'Simulation': self.run_simulation, 'Results': self.read_results}
        return action_map[self.file]() if self.file in action_map else f'Unknown action: {self.file} (managerThread.py)'

    # Generates INP files by running an Abaqus command
    def generate_inp_files(self):
        try:
            abaqus_command = r'abaqus cae noGUI=S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/geometryAndAssembly/main.py'
            result = subprocess.run(abaqus_command, shell=True, check=True)
            return 'INP files were successful generated (managerThread.py)'
        except Exception as e:
            return f'Error to generate INP: {str(e)} (managerThread.py)'

    # Runs the simulation using parallel execution
    def run_simulation(self):
        from pararelSimulation import PararelSimulation
        try:
            self.ui.infoFrame.setEnabled(False)
            self.number_of_cores = self.ui.core.currentText()
            self.path_to_save_files = self.main.path_to_save_files
            self.numberFiles = self.main.numberFiles
            PararelSimulation.startSimulation(self)
            return 'Simulation were successful generated (managerThread.py)'
        except Exception as e:
            return f'Error to run the simulation: {str(e)} (managerThread.py)'

    # Reads and processes the results after the simulation
    def read_results(self):
        from mainResults import getResults
        try:
            self.ui.resultsInfoLabel.setEnabled(False)
            getResults.startResults(self.main)
            return 'Reading of results was successful (managerThread.py)'
        except Exception as e:
            return f'Error to read the results: {str(e)} (managerThread.py)'

    # Handles actions after Abaqus or the simulation has finished running
    def on_abaqus_finished(self, message):
        print(f'--> MESSAGE: {message}')

        if message[:3] == 'INP':
            self.ui.infoFrame.setEnabled(True)

        elif message[:7] == 'Reading':
            self.ui.resultsInfoLabel.setEnabled(True)

        elif message[:10] == 'Simulation':
            self.ui.infoFrame.setEnabled(True)


