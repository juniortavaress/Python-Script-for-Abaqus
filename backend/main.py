import json
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

import os
work_directory = 'S:\Junior\Abaqus+Python\PythonScriptforAbaqus\INPFiles'
os.chdir(work_directory)

mdb.Model(modelType=STANDARD_EXPLICIT, name='PythonModel')

try:
    del mdb.models['Model-1']
except:
    print('except')
    pass

files = ['datas', 'materials', 'createChipPlate', 'createTool', 'createEulerian', 'assemblyAndSimulation']
# files = ['createEulerian']
for file in files:
    with open('S:\\Junior\Abaqus+Python\\PythonScriptforAbaqus\\backend\\' + file + '.py') as m:
        exec(m.read())

