from AuxFiles.imports import *
from Simulation.setSimulation import RunSimulation
from AuxFiles.dictionaries import GetDictionary
from AuxFiles.generalFunctions import AuxFunctions
from Simulation.managerThread import WorkerThread

class IterationDatas():
    def __init__(self):
        super(IterationDatas, self).__init__()

    # Opens a file dialog for the user to select a folder to save the files
    def folders_paths(self):
        self.path_to_save_files = QFileDialog.getExistingDirectory(self, "Select a folder to save the files")
        self.ui.inpLabel.setText(self.path_to_save_files)

        with open(self.path_datas_input, 'r+') as json_file:
            data = json.load(json_file)
            data["paths"] = {"pathOutputFiles": self.path_to_save_files}
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()


    # Collects simulation parameters and calls functions to run the simulation.
    def save_simulation_infos(self):
        iteration_info = GetDictionary.iteration_info(self)
        parameters = GetDictionary.iteration_parameters(self)
        if self.ui.numberOfVariables.currentText() != "None":
            for parameter in parameters:
                key, info = IterationDatas.get_info(self, parameter[0], parameter[1], parameter[2], parameter[3])
                iteration_info[key] = info
                setup = IterationDatas.save_iteration(self, iteration_info) if key != None else None
            IterationDatas.generate_inp_files(self) if setup else None
        else:
            IterationDatas.save_single_datas(self)


    # Fetches the selected parameter info from the combobox and validates user inputs.
    def get_info(self, combobox, min, max, step):
        parameter_map = {"Feed": "Feed", "Rake Angle": "rakeAngle", "Clearance Angle": "clearanceAngle", "Time Period": "timePeriod"}
        parameter = parameter_map.get(combobox.currentText())
        if parameter:
            try:
                return parameter, {"activated": True, "min": float(min.text()), "max": float(max.text()), "step": int(step.currentText())}
            except:
                AuxFunctions.warning(self, self.ui.labelIterationWarning, 'The parameters min, max and step must be a number')
                return None, None
        else:
            AuxFunctions.warning(self, self.ui.labelIterationWarning, 'Select a parameter')
            return None, None


    # Saves the iteration setup and generates all combinations of the simulation parameters.
    def save_iteration(self, iteration_info):
        setup = True
        AuxFunctions.clean_and_create_folder(self, self.path_folder_simulation_datas)
        data = AuxFunctions.open_dict('dict', self.path_datas_input)

        # Updates parameters with the given values or default
        feed = IterationDatas.update_parameters_values(self, iteration_info, 'Feed', float(self.ui.feed.text()))
        timePeriod = IterationDatas.update_parameters_values(self, iteration_info, 'timePeriod', float(self.ui.timePeriod.text()))
        rakeAngle = IterationDatas.update_parameters_values(self, iteration_info, 'rakeAngle', float(self.ui.toolRakeAngle.text()))
        clearanceAngle = IterationDatas.update_parameters_values(self, iteration_info, 'clearanceAngle', float(self.ui.toolClearanceAngle.text()))

        # Iterates over all combinations, builds file names, and saves data for each simulation
        combinations = list(itertools.product(feed, timePeriod, clearanceAngle, rakeAngle))

        for combination in combinations:
            list_identifiers = []
            params = [('feed', feed, 0), ('timePeriod', timePeriod, 1), ('clearanceAngle', clearanceAngle, 2), ('rakeAngle', rakeAngle, 3)]
            for name, param, index in params:
                if isinstance(param, list) and len(param) > 1:
                    list_identifiers.append(name)
                    value = str(combination[index]).replace('.', '_')
                    list_identifiers.append(value)

            try:
                name = 'dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1]) + '-' + list_identifiers[2] + '-' + str(list_identifiers[3])
                pathName = os.path.join(self.main_path, 'data/simulationDatas/' + name + '.json')
            except:
                name = 'dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1])
                pathName = os.path.join(self.main_path, 'data/simulationDatas/' + name + '.json')

            # Updates the JSON data structure with the current combination
            data['generalInformation']['modelName'] = name
            data["assemblyAndSimulationData"]["toolPosition"]["feed"] = combination[0]
            data["assemblyAndSimulationData"]["stepsAndHistoryInformation"]["timePeriod"] = combination[1]
            data["toolData"]["createPartInformation"]["clearanceAngle"] = combination[2]
            data["toolData"]["createPartInformation"]["rakeAngle"] = combination[3]
            AuxFunctions.save_dict(pathName, data)
        return setup


    # Disables the GUI buttons, checks for a valid folder, and runs the simulation process.
    def generate_inp_files(self):
        if self.ui.inpLabel.text() != "":
            QTimer.singleShot(50, lambda: IterationDatas.call_thread_for_inp_files(self))
        else:
            self.ui.iterationWarning.show()
            AuxFunctions.warning(self, self.ui.labelIterationWarning, 'Select a folder')


    # Updates parameter values based on the iteration information or returns the default value.
    def update_parameters_values(self, iteration_info, key, default_value):
        if iteration_info[key]['activated'] == True:
            step = iteration_info[key]['step']
            max_val = iteration_info[key]['max']
            min_val = iteration_info[key]['min']
            return np.linspace(min_val, max_val, num=step).tolist()
        return [default_value]


    # Saves data for a single simulation (no parameter combinations) and runs the simulation.
    def save_single_datas(self):
        AuxFunctions.clean_and_create_folder(self, self.path_folder_simulation_datas)
        data = AuxFunctions.open_dict('dict', self.path_datas_input)
        data['generalInformation']['modelName'] = 'SingleSimulation'
        pathName = os.path.join(self.main_path, 'data/simulationDatas/SingleSimulation.json')
        AuxFunctions.save_dict(pathName, data)
        IterationDatas.generate_inp_files(self)


    # Executes the Abaqus simulation via the backend script and re-enables the buttons when done.
    def call_thread_for_inp_files(self):
        self.ui.infoFrame.setEnabled(False)
        self.worker = WorkerThread(self, self.ui, 'INPFiles')

        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()

        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.thread_manager)
        self.thread.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()



