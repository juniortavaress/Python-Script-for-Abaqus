from imports import *
from pageLayout import Page_Layout

class Iteration_Datas():
    def __init__(self):
        super(Iteration_Datas, self).__init__()

    def saveIterationInfo(self):
        self.all_infos = True
        with open(self.path_defaut_datas_input, 'r') as json_file:
                data = json.load(json_file)

        self.iteration_info = {
            "Feed": {"activated": False, "min": 0, "max": 0, "step": 0},
            "rakeAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
            "clearanceAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
            "timePeriod": {"activated": False, "min": 0, "max": 0, "step": 0}}

        values = [[self.ui.P01, self.ui.minP01, self.ui.maxP01, self.ui.stepP01], [self.ui.P02, self.ui.minP02, self.ui.maxP02, self.ui.stepP02]]
        values = [values[0]] if self.ui.numberOfVariables.currentText() == "1" else values

        for value in values:
            key, info = Iteration_Datas.getInfo(self, value[0], value[1], value[2], value[3])
            if key:
                self.iteration_info[key] = info
            else:
                self.all_infos = False

        if self.all_infos:  # Verifica se todas as informações são válidas
            Page_Layout.pageNumber(self, 0, self.ui.iterateButton, True)
            Iteration_Datas.saveValuestoSimulation(self)


    def getInfo(self, combobox, min, max, step):
        value = combobox.currentText()
        try:
            if value == "Feed":
                return "Feed", {"activated": True, "min": float(min.text()), "max": float(max.text()), "step": int(step.currentText())}
            elif value == "Rake Angle":
                return "rakeAngle", {"activated": True, "min": float(min.text()), "max": float(max.text()), "step": int(step.currentText())}
            elif value == "Clearance Angle":
                return "clearanceAngle", {"activated": True, "min": float(min.text()), "max": float(max.text()), "step": int(step.currentText())}
            elif value == "Time Period":
                return "timePeriod", {"activated": True, "min": float(min.text()), "max": float(max.text()), "step": int(step.currentText())}
            else:
                self.ui.iterationWarning.show()
                self.ui.labelIterationWarning.setText('Select a parameter')
                QTimer.singleShot(3000, lambda: self.ui.iterationWarning.hide())
        except ValueError as e:
            self.ui.iterationWarning.show()
            self.ui.labelIterationWarning.setText('The parameters min, max and step must be a number')
            QTimer.singleShot(3000, lambda: self.ui.iterationWarning.hide())
        return None, None


    def saveValuestoSimulation(self):
        path = 'S:\Junior\Abaqus+Python\PythonScriptforAbaqus\data\simulationDatas'
        try:
            for file in os.listdir(path):
                pathFile = os.path.join(path, file)
                os.remove(pathFile)
        except:
            os.makedirs(path)


        # Abrir e carregar o JSON existente
        with open(self.path_datas_input, 'r') as json_file:
            data = json.load(json_file)

        # Função para atualizar valores em uma lista ou valor único
        def update_value(key, default_value):
            if self.iteration_info[key]['activated'] == True:
                step = self.iteration_info[key]['step']
                max_val = self.iteration_info[key]['max']
                min_val = self.iteration_info[key]['min']
                return np.linspace(min_val, max_val, num=step).tolist()
            return [default_value]

        # Atualizar os valores necessários
        feed = update_value('Feed', float(self.ui.feed.text()))
        timePeriod = update_value('timePeriod', float(self.ui.timePeriod.text()))
        rakeAngle = update_value('rakeAngle', float(self.ui.toolRakeAngle.text()))
        clearanceAngle = update_value('clearanceAngle', float(self.ui.toolClearanceAngle.text()))

        # Gerar todas as combinações possíveis
        combinations = list(itertools.product(feed, timePeriod, clearanceAngle, rakeAngle))


        for combination in combinations:
            list_identifiers = []
            if isinstance(feed, list) and len(feed) > 1:
                list_identifiers.append("feed")
                value = str(combination[0]).replace('.', '_')
                list_identifiers.append(value)
            if isinstance(timePeriod, list) and len(timePeriod) > 1:
                list_identifiers.append("timePeriod")
                value = str(combination[1]).replace('.', '_')
                list_identifiers.append(value)
            if isinstance(clearanceAngle, list) and len(clearanceAngle) > 1:
                list_identifiers.append("clearanceAngle")
                value = str(combination[2]).replace('.', '_')
                list_identifiers.append(value)
            if isinstance(rakeAngle, list) and len(rakeAngle) > 1:
                list_identifiers.append("rakeAngle")
                value = str(combination[3]).replace('.', '_')
                list_identifiers.append(value)


            try:
                name = 'dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1]) + '-' + list_identifiers[2] + '-' + str(list_identifiers[3])
                pathName = os.path.join(self.main_path, 'data/simulationDatas/dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1]) + '-' + list_identifiers[2] + '-' + str(list_identifiers[3]) + '.json')
            except:
                name = 'dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1])
                pathName = os.path.join(self.main_path, 'data/simulationDatas/dataInput-simulation-with-' + list_identifiers[0] + '-' + str(list_identifiers[1]) + '.json')

            data['generalInformation']['modelName'] = name
            data["assemblyAndSimulationData"]["toolPosition"]["feed"] = combination[0]
            data["assemblyAndSimulationData"]["toolPosition"]["timePeriod"] = combination[1]
            data["toolData"]["createPartInformation"]["clearanceAngle"] = combination[2]
            data["toolData"]["createPartInformation"]["rakeAngle"] = combination[3]


            with open(pathName, 'w') as json_file:
                json.dump(data, json_file, indent=4)


    def run(self):
        QTimer.singleShot(3000, lambda: Iteration_Datas.runAbaqus(self))

    def runAbaqus(self):
        from backend.script import runBackend
        # pass
        runBackend()



