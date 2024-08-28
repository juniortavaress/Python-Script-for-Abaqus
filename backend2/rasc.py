# -*- coding: utf-8 -*-
import os
import json
import numpy as np
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *


work_directory = r'S:\\Junior\\Abaqus+Python\\PythonScriptforAbaqus'
os.chdir(work_directory)




files1 = ['datas', 'materials', 'createChipPlate', 'createTool', 'createEulerian', 'assemblyAndSimulation']
files1 = ['datas', 'materials']

for file in files1:
    with open(r'S:\\Junior\\Abaqus+Python\\PythonScriptforAbaqus\\backend\\' + file + '.py') as m:
        exec(m.read())


class Main():
    def __init__(self):
        
        with open('S:/Junior/Abaqus+Python/PythonScriptforAbaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)
        ModelName = str(data['generalInformation']['modelName'])
        self.model = mdb.Model(modelType=STANDARD_EXPLICIT, name=ModelName)
    
        Main.test(self)

    def test(self):
        import sys
        sys.path.append(r'S:\\Junior\\Abaqus+Python\\PythonScriptforAbaqus\\backend')

        from assemblyAndSimulation import AssemblyModel
        from createChipPlate import ChipPlateModel

        chip_plate_model = ChipPlateModel()
        chip_plate_model.teste(self.model)

    
model = Main()



 





