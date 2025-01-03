# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by adam-ua769pu3t3n7k4o on Mon Dec  2 08:58:53 2024
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
    's:/Junior/abaqus-with-python/gui-interface-abaqus-with-python/backend/geometryAndAssembly/main.py', 
    __main__.__dict__)
#: The model "restartMode" has been created.
#: The model "dataInput-simulation-with-rakeAngle-6_0" has been created.
#: 123
#: The interaction property "chip-plate-contact" has been created.
#: The interaction property "self-contact" has been created.
#: The interaction property "tool-chip-contact" has been created.
#: The interaction "contact" has been created.
#: The model "dataInput-simulation-with-rakeAngle-7_0" has been created.
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
#: The model database has been saved to "C:\Users\adam-ua769pu3t3n7k4o\Downloads\CAEFiless\simulation_CAE.cae".
print 'RT script done'
#: RT script done
