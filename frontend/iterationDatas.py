import json
import itertools

import numpy as np
from pageLayout import Page_Layout
from PySide6.QtCore import QTimer

class Iteration_Datas():
    def __init__(self):
        super(Iteration_Datas, self).__init__()


    def saveIterationInfo(self):
        self.all_infos = True
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataDefautInput.json', 'r') as json_file:
                data = json.load(json_file)

        iteration_info = {
            "Feed": {"activated": False, "min": 0, "max": 0, "step": 0},
            "rakeAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
            "clearanceAngle": {"activated": False, "min": 0, "max": 0, "step": 0},
            "timePeriod": {"activated": False, "min": 0, "max": 0, "step": 0}}

        values = [[self.ui.P01, self.ui.minP01, self.ui.maxP01, self.ui.stepP01], [self.ui.P02, self.ui.minP02, self.ui.maxP02, self.ui.stepP02]]
        values = [values[0]] if self.ui.numberOfVariables.currentText() == "1" else values
        for value in values:
            key, info = Iteration_Datas.getInfo(self, value[0], value[1], value[2], value[3])
            if key:
                data["iterationInformation"][key] = info
            else:
                self.all_infos = False

        if self.all_infos:  # Verifica se todas as informações são válidas
            with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'w') as file:
                json.dump(data, file, indent=4)
            Page_Layout.pageNumber(self, 0, None)

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
        except ValueError as e:
            self.ui.iterationWarning.show()
            QTimer.singleShot(3000, lambda: self.ui.iterationWarning.hide())
        return None, None


    def saveValuestoSimulation(self):
        # Abrir e carregar o JSON existente
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Função para atualizar valores em uma lista ou valor único
        def update_value(key, default_value):
            if data['iterationInformation'][key]['activated'] == True:
                step = data['iterationInformation'][key]['step']
                max_val = data['iterationInformation'][key]['max']
                min_val = data['iterationInformation'][key]['min']
                return np.linspace(min_val, max_val, num=step).tolist()
            return [default_value]

        # Atualizar os valores necessários
        feed = update_value('Feed', float(self.ui.feed.text()))
        timePeriod = update_value('timePeriod', float(self.ui.timePeriod.text()))
        rakeAngle = update_value('rakeAngle', float(self.ui.toolRakeAngle.text()))
        clearanceAngle = update_value('clearanceAngle', float(self.ui.toolClearanceAngle.text()))

        print('feed', feed)
        print('timePeriod', timePeriod)
        print('rakeAngle', rakeAngle)
        print('clearanceAngle', clearanceAngle)

        # Gerar todas as combinações possíveis
        combinations = list(itertools.product(feed, timePeriod, clearanceAngle, rakeAngle))

        # Exibir as combinações
        n = 0
        for combination in combinations:
            print(combination)
            n += 1
            data["assemblyAndSimulationData"]["toolPosition"]["feed"] = combination[0]
            data["assemblyAndSimulationData"]["toolPosition"]["timePeriod"] = combination[1]
            data["toolData"]["createPartInformation"]["clearanceAngle"] = combination[2]
            data["toolData"]["createPartInformation"]["rakeAngle"] = combination[3]

            with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/iterationDatas/dataInput_' + str(n) + '.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)










