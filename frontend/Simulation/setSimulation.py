from AuxFiles.imports import *
from Simulation.managerThread import WorkerThread


class RunSimulation():
    def __init__(self):
        super(RunSimulation, self).__init__()

    # Initializes parameters required for the simulation
    def get_parameters_for_simulation(self):
        RunSimulation.get_available_cores(self)
        QTimer.singleShot(150, lambda: RunSimulation.get_number_of_simulation(self))

    # Gets the number of available CPU cores that are below a usage threshold
    def get_available_cores(self):
        psutil.cpu_percent(percpu=True)
        QTimer.singleShot(100, lambda: RunSimulation._calculate_available_cores(self))

    # Helper function to calculate available CPU cores
    def _calculate_available_cores(self):
        threshold = 8
        cpu_percentages = psutil.cpu_percent(percpu=True)
        num_physical_cores = psutil.cpu_count(logical=False)
        self.availableCores = sum(1 for i, usage in enumerate(cpu_percentages) if usage < threshold and i < num_physical_cores)
        self.ui.coreLabel.setText(str(self.availableCores))

    # Counts the number of simulation files and updates the UI accordingly
    def get_number_of_simulation(self):
        files = [f for f in os.listdir(self.path_folder_simulation_datas) if os.path.isfile(os.path.join(self.path_folder_simulation_datas, f))]
        number_of_files = len(files)
        self.ui.numberSimulation.setText(str(number_of_files))
        self.ui.numberofPararelSimulations.clear()
        max_simulations = min(number_of_files, self.availableCores)
        [self.ui.numberofPararelSimulations.addItem(str(x)) for x in range(1, max_simulations +1)]

    # Calculate how many cores are assigned to each simulation
    def core_by_simulation(self):
        try:
            self.numberFiles = int(self.ui.numberofPararelSimulations.currentText())
            self.core_by_simulation = int(self.availableCores/self.numberFiles)
            self.ui.core.clear()
            [self.ui.core.addItem(str(x)) for x in range(1, self.core_by_simulation+1)]
        except Exception as e:
            pass

    # Start the worker thread to manage the simulation process
    def call_thread_for_simulation(self):
        if self.core_by_simulation and self.numberFiles:
            self.worker = WorkerThread(self, self.ui, 'Simulation')
            self.worker.finished.connect(lambda: RunSimulation.get_odb_files(self))

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
            self.ui.infoFrame.setEnabled(True)
        else:
            print('Simulation setup is incomplete')

    # This function is part of the process of organizing and cleaning the files resulting from simulations
    def get_odb_files(self):
        inp_dir = os.path.join(self.path_to_save_files,  'INPFiles')
        odb_dir = os.path.join(self.path_to_save_files,  'ODBFiles')
        os.makedirs(odb_dir) if not os.path.exists(odb_dir) else None

        for filename in os.listdir(inp_dir):
            path = os.path.join(inp_dir, filename)
            if os.path.isfile(path):
                if not (filename.endswith('.inp') or filename.endswith('.odb')):
                    os.remove(path)
                elif filename.endswith('.odb'):
                    shutil.move(path, os.path.join(odb_dir, filename))
            elif os.path.isdir(path):
                os.rmdir(path)

