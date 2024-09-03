# -*- coding: utf-8 -*-
""" Define o terminal cd C:\ temp e usa o comando abaqus cae noGUI=S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/main.py """
import os
import inspect

current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
main_directory = os.path.dirname(current_directory)
work_directory = os.chdir(current_directory)

from imports import *

print('current directory', current_directory)
print('main directory', main_directory)
print('work directory', work_directory)

class Main():
    def __init__(self):

        mdb.Model(modelType=STANDARD_EXPLICIT, name='restartMode')
        for model_name in list(mdb.models.keys()):
            if model_name != 'restartMode':
                del mdb.models[model_name]

        for job_name in list(mdb.jobs.keys()):
            del mdb.jobs[job_name]
        
        path_INP = os.path.join(main_directory, 'INPFiles')
        path_CAE = os.path.join(main_directory, 'CAEFiles')
        folders = [path_INP, path_CAE]

        for folder in folders:
            try:   
                for file in os.listdir(folder):
                    pathFile = os.path.join(path_INP, file)
                    os.remove(pathFile)
            except:
                if not os.path.exists(folder):
                    os.makedirs(folder)

        from materials import Materials
        from createChipPlate import ChipPlateModel
        from createEulerian import EulerianModel
        from createTool import ToolModel
        from assemblyAndSimulation import AssemblyModel

        path_simulation_datas = os.path.join(main_directory, 'data/simulationDatas')
        for files in os.listdir(path_simulation_datas):
            with open(os.path.join(path_simulation_datas, files), 'r') as file:
                data = json.load(file)

            ModelName = str(data['generalInformation']['modelName'])
            mdb.Model(modelType=STANDARD_EXPLICIT, name=ModelName)

            Materials(ModelName) 
            ChipPlateModel(data)
            EulerianModel(data)
            ToolModel(data)
            AssemblyModel(data, path_INP, path_CAE, files[10:-5])

        del mdb.models['restartMode']

        os.chdir(path_CAE)
        mdb.saveAs(pathName='simulation_CAE')
            
model = Main()







