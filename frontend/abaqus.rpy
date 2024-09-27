# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by adam-ua769pu3t3n7k4o on Fri Sep 27 08:50:30 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.55729, 1.55556), width=229.233, 
    height=154.311)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile(
    'S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/geometryAndAssembly/main.py', 
    __main__.__dict__)
#: The model "restartMode" has been created.
#: The model "dataInput-simulation-with-rakeAngle-10_0" has been created.
#: 123
#: The interaction property "chip-plate-contact" has been created.
#: The interaction property "self-contact" has been created.
#: The interaction property "tool-chip-contact" has been created.
#: The interaction "contact" has been created.
#: The model "dataInput-simulation-with-rakeAngle-12_0" has been created.
#: 123
#: The interaction property "chip-plate-contact" has been created.
#: The interaction property "self-contact" has been created.
#: The interaction property "tool-chip-contact" has been created.
#: The interaction "contact" has been created.
#: The model "dataInput-simulation-with-rakeAngle-8_0" has been created.
#: 123
#: The interaction property "chip-plate-contact" has been created.
#: The interaction property "self-contact" has been created.
#: The interaction property "tool-chip-contact" has been created.
#: The interaction "contact" has been created.
#* *** Error: File open failed (utl_File: CreateFile in OpenWrite)
#* error: The process cannot access the file because it is being used by 
#* another process.
#* 
#* file: C:\Users\adam-ua769pu3t3n7k4o\Music\CAEFiless\simulation_CAE.cae
#* File 
#* "S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/geometryAndAssembly/main.py", 
#* line 86, in <module>
#*     model = Main()
#* File 
#* "S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/geometryAndAssembly/main.py", 
#* line 23, in __init__
#*     Main.createGeometryAndAssembly(self)
#* File 
#* "S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/geometryAndAssembly/main.py", 
#* line 84, in createGeometryAndAssembly
#*     mdb.saveAs(pathName='simulation_CAE')
