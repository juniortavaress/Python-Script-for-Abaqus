import json

dataInput = {
    "generalInformation": {
        "modelName": "PythonModel",
    },

    "chipPlateData": {
        "createPartInformation": {
            "Name": "ChipPlate",
            "Width": 1.5,
            "Height": 0.01,
            "Trickness": 0.02
        },
        "createSetsandSectionsInformation": {
            "referenceSetName": "PlateRP",
            "domainSetName": "PlateDomain",
            "sectionName": "ChipPlateSection",
        },
        "createMeshInformation": {
            "elemCode": "C3D8R",
            "elemLibrary": "EXPLICIT",
            "globalSize": 0.01,
            "deviationFactor": 0.1,
            "minSizeFactor": 0.1
        }
    },

    "toolData": {
        "createPartInformation": {
            "Name": "Tool", 
            "Trickness": 0.02, 
            "clearanceAngle": 3.0, 
            "Radius": 0.08, 
            "clearanceFaceDimension": 3.35, 
            "rakeAngle": 12.0, 
            "rakeFaceDimension": 5.3
        },
        "createPartitionInformation": {
            "partition01": 1.5,
            "partition02": 1.14,
            "sectionName": "ToolSection"
        },
        "createMeshInformation": {
            "globalSize": 0.1,
            "deviationFactor": 0.1,
            "minSizeFactor": 0.1,
            "radiusMeshSize": 0.01,
            "noseBiasMaxMeshSize": 0.06, 
            "noseBiasMinMeshSize": 0.01,
            "partition02MeshSize": 0.1
        }
    },
    
    "eulerianData": {
        "createPartInformation": {
            "Name": "Eulerian",
            "Height": 5.0,
            "Width": 3.8,
            "Trickness": 0.02
        },
        "createParticionInformation":{
            "x_points": [1.5, 2.7, 3.0, 3.3],
            "y_points": [2.8, 1.3, 1.23, 1.1],
        },
        "createSetsandSectionsInformation": {
            "eulerDomainSet": "EulerDomain",
            "kssDomain": "KssDomain",
            "workpieceBottom": "WorkpieceBottom",
            "workpieceDomain": "WorkpieceDomain",
            "sectionName": "EulerSection"
        },

        "createMeshInformation": {
            "elemCode": "EC3D8RT",
            "elemLibrary": "EXPLICIT",
            "globalSize": 0.2,
            "deviationFactor": 0.1,
            "minSizeFactor": 0.1
        }
    },

    "assemblyAndSimulationData": {
        "chipPlatePosition": {
            "clearanceOverWorkpiece": 0.05,
            "distanceFromTool": 0.2
        },
        "toolPosition":{
            "xPosition": 3.0,
            "yPosition": 1.3,
            "feed": 0.05
        },
        "stepsAndHistoryInformation":{
            "stepName": "CuttingStep",
            "timePeriod": 0.03
        }
    }
}


# Path to the json file
file_path = "S:/Junior/Abaqus+Python/Python Script for Abaqus/data/dataInput.json"

# Saving the dict to the json file
with open(file_path, 'w') as json_file:
    json.dump(dataInput, json_file, indent=4)


