from pageLayout import Page_Layout
from generateEulerian import Eulerian
from generateChipPlate import ChipPlate
from generateTool import Tool



class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()



    def actions(self):
        # Chip Plate Actions
        self.ui.chipPlateFinish.clicked.connect(lambda: Page_Layout.initialPage(self))
        self.ui.chipPlateFinish.clicked.connect(lambda: ChipPlate.saveInfos(self))
        self.ui.chipPlateButton.clicked.connect(lambda: Page_Layout.createGeometry(self, "Chip Plate"))
        self.ui.chipPlateDefaut.stateChanged.connect(lambda: ChipPlate.setDefautInfos(self))

        # Eulerian Actions
        self.ui.eulerianFinish.clicked.connect(lambda: Page_Layout.initialPage(self))
        self.ui.eulerianFinish.clicked.connect(lambda: Eulerian.saveInfos(self))
        self.ui.eulerianButton.clicked.connect(lambda: Page_Layout.createGeometry(self, "Eulerian"))
        self.ui.eulerianDefaut.stateChanged.connect(lambda: Eulerian.setDefautInfos(self))

        # Tool Actions
        self.ui.toolFinish.clicked.connect(lambda: Page_Layout.initialPage(self))
        self.ui.toolFinish.clicked.connect(lambda: Tool.saveInfos(self))
        self.ui.toolButton.clicked.connect(lambda: Page_Layout.createGeometry(self, "Tool"))
        self.ui.toolDefaut.stateChanged.connect(lambda: Tool.setDefautInfos(self))

        # Assembly Actions
        self.ui.assemblyFinish.clicked.connect(lambda: Page_Layout.initialPage(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Page_Layout.initialPage(self))
        self.ui.assemblyButton.clicked.connect(lambda: Page_Layout.createGeometry(self, "Assembly"))



