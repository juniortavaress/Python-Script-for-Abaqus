import os
import json
from abaqus import *
from abaqusConstants import *
import numpy as np
from part import *
from material import *
from section import *
from assembly import *
# from step import *
from interaction import *
# from load import *
from mesh import *
# from optimization import *
# from job import *
# from sketch import *
from visualization import *
from connectorBehavior import *


work_directory = 'S:\Junior\Abaqus+Python\PythonScriptforAbaqus\\backend2'
os.chdir(work_directory)

class Main():
    def __init__(self):
        # Loading data from JSON and creating the model
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)
        ModelName = str(data['generalInformation']['modelName'])
        mdb.Model(modelType=STANDARD_EXPLICIT, name=ModelName)

        try:
            del mdb.models['Model-1']
        except:
            print('except')
            pass

        from materials import Materials
        from createChipPlate import ChipPlateModel
        from createEulerian import EulerianModel
        from createTool import ToolModel
        from assemblyAndSimulation import AssemblyModel

        Materials('ab')     

        data = 50

        path = 'S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/iterationDatas'

        for files in os.listdir(path):
            with open(os.path.join(path, files), 'r') as file:
                data = json.load(file)
            print('djgsdhjkjkhjkh', files[:-5])


            ChipPlateModel(data)
            EulerianModel(data)
            ToolModel(data)
            AssemblyModel(data, files[:-5])
            
model = Main()







