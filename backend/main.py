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



work_directory = 'S:\Junior\Abaqus+Python\PythonScriptforAbaqus\INPFiles'
os.chdir(work_directory)

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


files = ['datas', 'materials', 'createChipPlate', 'createTool', 'createEulerian', 'assemblyAndSimulation']
# files = ['createChipPlate']

for file in files:
    with open('S:\\Junior\Abaqus+Python\\PythonScriptforAbaqus\\backend\\' + file + '.py') as m:
        exec(m.read())

