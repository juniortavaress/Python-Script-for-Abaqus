from AuxFiles.imports import *
from AuxFiles.dictionaries import GetDictionary
from AuxFiles.generalFunctions import AuxFunctions

class ResultsDatas():
    def __init__(self):
        super(ResultsDatas, self).__init__()

    def folders_paths(self):
        # Opens a file dialog for the user to select a folder where results (ODB files) will be saved
        self.path_to_odb_file = QFileDialog.getExistingDirectory(self)

        if self.path_to_odb_file:
            ResultsDatas.layout_manager_for_results_page(self, 'style')

            # Saves the selected folder path to a JSON file
            data = AuxFunctions.open_dict('dict', self.path_datas_input)
            data["paths"] = {"path_to_odb_file": self.path_to_odb_file}
            AuxFunctions.save_dict(self.path_datas_input, data)

            # Initiates the worker thread and loads available ODB files
            AuxFunctions.thread_manager_for_inp_simulation_and_results(self, 'Results')
            ResultsDatas.load_odb(self)


    def load_odb(self):
        # Loads available ODB files from the selected folder and populates the UI dropdown
        self.odb_files_list = [f[:-4] for f in os.listdir(self.path_to_odb_file) if f.endswith('.odb')]
        self.ui.odbFiles.addItems(self.odb_files_list)


    def get_graph(self, task):
        # Handles the logic for plotting graphs based on selected analysis type and ODB file
        odb_name = self.ui.odbFiles.currentText()
        analysis = self.ui.typeOfAnalisys.currentText()

        # Try to clean the plot area
        AuxFunctions.clean_plot_area(self, self.ax_Result, self.canvas_Result)

        # If a specific ODB file and analysis type are selected, plot the graph for that file
        if odb_name not in ['None', 'All'] and analysis != 'None':
            file_name = f'datas{analysis}{odb_name}.pkl'
            self.path_file_results_plk = os.path.join(self.path_datas_result, file_name)
            ResultsDatas.graph_manager(self, odb_name)

        # If 'All' ODB files are selected, plot graphs for all available ODB files
        elif odb_name == 'All' and analysis != 'None':
            for index, file in enumerate(self.odb_files_list):
                file_name = f'datas{analysis}{file}.pkl'
                self.path_file_results_plk = os.path.join(self.path_datas_result, file_name)
                ResultsDatas.graph_manager(self, file, index)


    def graph_manager(self, labelname, index = None):
        # Load data from the .pkl file and get the color based on the provides index
        datas = AuxFunctions.open_dict('plk', self.path_file_results_plk)
        color = GetDictionary.get_colors(self, index)

        # Check if the analysis type is 'NT11' and plot the graph
        if self.ui.typeOfAnalisys.currentText() == 'NT11':
            times, temperatures = datas[0], datas[1]
            ResultsDatas.set_graph_datas_and_axis(self, times, temperatures, color, labelname, 'Time (s)', 'Temperature (C)', 'Temperature vs Node Time')

        # Check if the analysis type is 'RF' and plot the graph
        elif self.ui.typeOfAnalisys.currentText() == 'RF' and self.ui.typeRF.currentText() != 'None':
            if self.ui.typeRF.currentText() in ['RF1', 'RF2', 'RF3']:
                data_rf1, data_rf2, data_rf3 = datas[0], datas[1], datas[2]
                GRAPH_MAPPINGS = {'RF1':  [data_rf1[0], data_rf1[1], 'RF1 vs Time'], 'RF2':  [data_rf2[0], data_rf2[1], 'RF2 vs Time'], 'RF3':  [data_rf3[0], data_rf3[1], 'RF3 vs Time']}
                x, y, title = GRAPH_MAPPINGS[self.ui.typeRF.currentText()]
                ResultsDatas.set_graph_datas_and_axis(self, x, y, color, labelname, 'Time (s)', 'Reaction Force (N)', title)
            else:
                if self.ui.odbFiles.currentText() != 'All':
                    labels = ['RF1', 'RF2', 'RF3']
                    colors = ['r', '#003366', '#8b5ea7']
                    for data, color, label in zip(datas, colors, labels):
                        ResultsDatas.set_graph_datas_and_axis(self, data[0], data[1], color, label, 'Time (s)', 'Reaction Force (N)', 'RF vs Time')


    def set_graph_datas_and_axis(self, x, y, color, labelname, xlabel, ylabel, title):
        # Plot the data with the specified line style, color, label, and line width
        self.ax_Result.plot(x, y, linestyle='-', color=color, label=labelname, linewidth=1.0)
        # Set graph layout and redraw the graph
        self.ax_Result.set_xlabel(xlabel)
        self.ax_Result.set_ylabel(ylabel)
        self.ax_Result.set_title(title)
        self.ax_Result.legend()
        self.ax_Result.axis(True)
        self.ax_Result.grid(False)
        self.fig_Result.tight_layout()
        self.canvas_Result.draw()


    # Manages the layout updates based on user selections
    def layout_manager_for_results_page(self, task):
        if task == 'odbFiles':
            self.ui.typeOfAnalisys.setCurrentIndex(0)
            self.ui.typeRF.setCurrentIndex(0)
            self.ui.rfFrame.hide()
            self.ui.dataFrame.hide()

        elif task == 'typeOfAnalisys':
            self.ui.typeRF.setCurrentIndex(0)
            if self.ui.typeOfAnalisys.currentText() == 'NT11':
                self.ui.dataFrame.show()
                self.ui.rfFrame.hide()
            elif self.ui.typeOfAnalisys.currentText() == 'RF':
                self.ui.rfFrame.show()
                self.ui.typeRF.currentIndexChanged.disconnect()
                self.ui.typeRF.clear()
                self.ui.typeRF.addItems(['None', 'RF1', 'RF2', 'RF3']) if self.ui.odbFiles.currentText() == 'All' else self.ui.typeRF.addItems(['None', 'All', 'RF1', 'RF2', 'RF3'])
                self.ui.dataFrame.hide() if self.ui.typeRF.currentText() == 'All' else self.ui.dataFrame.show()
                self.ui.typeRF.currentIndexChanged.connect(lambda: ResultsDatas.get_graph(self, 'typeRF'))

        elif task == 'typeRF':
            self.ui.dataFrame.hide() if self.ui.typeRF.currentText() == 'All' else self.ui.dataFrame.show()

        elif task == 'style':
            self.ui.typeOfAnalisys.setEnabled(True)
            self.ui.pathResultsLabel.setText(self.path_to_odb_file)


    # Functions to export the results graph
    def save_figure(self):
        img_name_and_path, _ = QFileDialog.getSaveFileName(self, "Salvar Gráfico", "", "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        self.fig_Result.savefig(img_name_and_path) if img_name_and_path else None
