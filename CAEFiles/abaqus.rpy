# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by adam-ua769pu3t3n7k4o on Tue Sep  3 13:30:44 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=240.134368896484, 
    height=263.822235107422)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('simulation_CAE.cae')
#: The model database "S:\Junior\Abaqus+Python\PythonScriptforAbaqus\CAEFiles\simulation_CAE.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['dataInput-simulation-with-feed-0_01-rakeAngle-8_0'].parts['ChipPlate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['dataInput-simulation-with-feed-0_01-rakeAngle-10_0'].parts['ChipPlate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['dataInput-simulation-with-feed-0_01-rakeAngle-10_0'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5636, 
    farPlane=22.7379, width=8.75485, height=6.48735, cameraPosition=(15.3933, 
    9.70676, 12.5379), cameraUpVector=(-0.26004, 0.740952, -0.619169), 
    cameraTarget=(3.32999, 3.26173, -0.153131))
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.0196, 
    farPlane=21.1735, width=9.63012, height=7.13592, cameraPosition=(12.777, 
    3.63042, 15.9316), cameraUpVector=(0.0696132, 0.891416, -0.447808), 
    cameraTarget=(3.33101, 3.2641, -0.154456))
a = mdb.models['dataInput-simulation-with-feed-0_05-rakeAngle-12_0'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
