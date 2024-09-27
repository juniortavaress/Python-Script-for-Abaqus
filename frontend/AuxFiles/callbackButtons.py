from AuxFiles.imports import *
from Layout.pageLayout import PageLayout
from Layout.graphLayout import GraphLayout
from Geometry.getGeometry import GetGeometry
from Results.resultsDatas import ResultsDatas
from AuxFiles.generalFunctions import AuxFunctions
from Simulation.setSimulation import RunSimulation
from Simulation.iterationDatas import IterationDatas
from Datas.setAndSaveDefautDatas import DataInicialization


class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    # Adding main and backend paths to sys.path
    def add_path(self):
        current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.main_path = os.path.dirname(os.path.dirname(current_directory))
        sys.path.append(self.main_path) if self.main_path not in sys.path else None
        pathFiles = [os.path.join(self.main_path, 'backend\\runSimulation'), os.path.join(self.main_path, 'backend\\getResults')]
        for pathFile in pathFiles:
            sys.path.append(pathFile) if pathFile not in sys.path else None

    # Initializing plot areas and loading data paths
    def start(self):
        self.ui.tabWidget.setCurrentIndex(0)
        AuxFunctions.change_page_number(self, 0)
        self.ax_geometry, self.fig_geometry, self.canvas_geometry = GraphLayout.create_plot_areas(self, self.ui.plot, '3d')
        self.ax_Result, self.fig_Result, self.canvas_Result = GraphLayout.create_plot_areas(self, self.ui.plotResult)
        self.resizeEvent = lambda event: GraphLayout.resize(self)
        DataInicialization.get_paths(self)
        DataInicialization.get_defaut_datas(self)

    # Activating the interface buttons
    def activate_buttons(self):
        # Home Page
        self.ui.parametrizationButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 1))
        self.ui.iterationButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 2))
        self.ui.resultsButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 3))

        # Geometry Page
        self.ui.returnButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 0))
        self.ui.defautValues.stateChanged.connect(lambda: DataInicialization.set_defaut_infos(self))
        self.ui.applyButton.clicked.connect(lambda: GetGeometry.set_info(self))
        self.ui.tabWidget.currentChanged.connect(lambda: GetGeometry.set_info(self))
        self.ui.saveButton.clicked.connect(lambda: GetGeometry.save_infos(self))

        # Iteration Page
        self.ui.returnIterationButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 0))
        self.ui.inpPathButton.clicked.connect(lambda: IterationDatas.folders_paths(self))
        self.ui.numberOfVariables.currentIndexChanged.connect(lambda: PageLayout.set_iteration_variables_enabled(self))
        self.ui.applyIteration.clicked.connect(lambda: IterationDatas.save_simulation_infos(self))
        self.ui.applyIteration.clicked.connect(lambda: RunSimulation.get_parameters_for_simulation(self))
        self.ui.numberofPararelSimulations.currentIndexChanged.connect(lambda: RunSimulation.core_by_simulation(self))
        self.ui.saveAndRunButton.clicked.connect(lambda: RunSimulation.call_thread_for_simulation(self))

        # Results Page
        self.ui.rfFrame.hide()
        self.ui.dataFrame.hide()
        self.ui.importResultsButton.clicked.connect(lambda: ResultsDatas.folders_paths(self))
        self.ui.typeOfAnalisys.currentIndexChanged.connect(lambda: ResultsDatas.layout_manager_for_results_page(self, 'typeOfAnalisys'))
        self.ui.typeRF.currentIndexChanged.connect(lambda: ResultsDatas.layout_manager_for_results_page(self, 'typeRF'))
        self.ui.odbFiles.currentIndexChanged.connect(lambda: ResultsDatas.layout_manager_for_results_page(self, 'odbFiles'))
        self.ui.odbFiles.currentIndexChanged.connect(lambda: ResultsDatas.get_graph(self, 'odbFiles'))
        self.ui.typeOfAnalisys.currentIndexChanged.connect(lambda: ResultsDatas.get_graph(self, 'typeOfAnalisys'))
        self.ui.typeRF.currentIndexChanged.connect(lambda: ResultsDatas.get_graph(self, 'typeRF'))
        self.ui.returnResultsButton.clicked.connect(lambda: AuxFunctions.change_page_number(self, 0))
        self.ui.exportFigureButton.clicked.connect(lambda: ResultsDatas.save_figure(self))

