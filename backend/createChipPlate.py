class ChipPlateModel():
    def __init__(self):
        # Create the chip plate model 
        self.dataInput()
        self.createPart()
        self.createSetsandSections()
        self.createMesh()

    def dataInput(self):
        # Load data from JSON
        with open('S:/Junior/Abaqus+Python/Python Script for Abaqus/data/dataInput.json', 'r') as json_file:
            data = json.load(json_file)

        # Calling Model
        self.ModelName = str(data['generalInformation']['modelName'])
        self.m = mdb.models[self.ModelName]

        # Defining Variables
        self.PartName = str(data['chipPlateData']['createPartInformation']['Name'])
        self.Width = data['chipPlateData']['createPartInformation']['Width']
        self.Height = data['chipPlateData']['createPartInformation']['Height']
        self.Trickness = data['chipPlateData']['createPartInformation']['Trickness']
        self.ReferenceSetName = str(data['chipPlateData']['createSetsandSectionsInformation']['referenceSetName'])
        self.DomainSetName = str(data['chipPlateData']['createSetsandSectionsInformation']['domainSetName'])
        self.SectionName = str(data['chipPlateData']['createSetsandSectionsInformation']['sectionName'])
        self.ElementType = str(data['chipPlateData']['createMeshInformation']['elemCode'])
        self.ElementLibrary = str(data['chipPlateData']['createMeshInformation']['elemLibrary'])
        self.GlobalSize = data['chipPlateData']['createMeshInformation']['globalSize']
        self.DeviationFactor = data['chipPlateData']['createMeshInformation']['deviationFactor']
        self.MinSizeFactor = data['chipPlateData']['createMeshInformation']['minSizeFactor']

    def createPart(self):
        # Creating the Chip Plate
        self.s = self.m.ConstrainedSketch(name='sketchChipPlate', sheetSize=200.0)
        self.s.rectangle(point1=(0.0, 0.0), point2=(self.Width, self.Height))
        self.p = self.m.Part(dimensionality=THREE_D, name=self.PartName, type=DEFORMABLE_BODY)
        self.p.BaseSolidExtrude(depth=self.Trickness, sketch=self.s)   

    def createSetsandSections(self):
        # Defining the Reference Point
        self.p.ReferencePoint(point=self.m.parts[self.PartName].InterestingPoint(self.m.parts[self.PartName].edges[1], MIDDLE))
        # Creating RP Set
        self.p.Set(name=self.ReferenceSetName, referencePoints=(self.p.referencePoints[2], ))
        # Creating Domain Set - Without RF
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#1 ]', ), ), name=self.DomainSetName)
        # Creating Sections
        self.m.HomogeneousSolidSection(material='WG-300', name=self.SectionName, thickness=None)
        self.p.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=self.p.sets[self.DomainSetName], sectionName=self.SectionName, thicknessAssignment=FROM_SECTION)
        # Creating Surfaces
        self.p.Surface(name='ChipPlateSurface', side1Faces=self.p.faces.getSequenceFromMask(('[#3f ]', ), ))

    def createMesh(self):
        # Creating Mesh
        self.p.setElementType(elemTypes=(ElemType(
            elemCode=self.ElementType, elemLibrary=self.ElementLibrary, secondOrderAccuracy=OFF, kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
            distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=EXPLICIT), 
            ElemType(elemCode=C3D4, elemLibrary=EXPLICIT)), regions=(self.p.cells.getSequenceFromMask(('[#1 ]', ), ), ))
        self.p.seedPart(deviationFactor=self.DeviationFactor, minSizeFactor=self.MinSizeFactor, size=self.GlobalSize)   # size is the same then global size
        self.p.generateMesh()

# Instantiate the class
model = ChipPlateModel()

