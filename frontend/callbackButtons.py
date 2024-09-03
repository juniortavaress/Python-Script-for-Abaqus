from imports import *
from generateTool import Tool
from pageLayout import Page_Layout
from generateAssembly import Assembly
from generateEulerian import Eulerian
from generateChipPlate import ChipPlate
from iterationDatas import Iteration_Datas
from setAndSaveDefautDatas import DataInicialization

class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    def actions(self):
        # General Actions
        DataInicialization.getPaths(self)
        DataInicialization.getDafautDatas(self)
        self.ui.defautValues.stateChanged.connect(lambda: DataInicialization.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: DataInicialization.saveInfos(self) if self.ui.defautValues.isChecked() else None)


        self.ui.applyIteration.clicked.connect(lambda: Iteration_Datas.run(self))
        self.ui.parametrizationButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None, None))

        # Chip Plate Actions
        self.ui.chipPlateApply.clicked.connect(lambda: ChipPlate.setInfo(self))
        self.ui.chipPlateFinish.clicked.connect(lambda: ChipPlate.saveInfos(self))
        self.ui.returnChipPlate.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.chipPlateButton, False))
        self.ui.chipPlateFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.chipPlateButton, True))
        self.ui.chipPlateButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 4, self.ui.chipPlateFinish, False))

        # Eulerian Actions
        self.ui.eulerianApply.clicked.connect(lambda: Eulerian.setInfo(self))
        self.ui.eulerianFinish.clicked.connect(lambda: Eulerian.saveInfos(self))
        self.ui.returnEulerian.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.eulerianButton, False))
        self.ui.eulerianFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.eulerianButton, True))
        self.ui.eulerianButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 1, self.ui.eulerianFinish, False))

        # Tool Actions
        self.ui.toolApply.clicked.connect(lambda: Tool.setInfo(self))
        self.ui.toolFinish.clicked.connect(lambda: Tool.saveInfos(self))
        self.ui.returnTool.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.toolButton, False))
        self.ui.toolFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.toolButton, True))
        self.ui.toolButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 2, self.ui.toolFinish, False))

        # Assembly Actions
        self.ui.assemblyApply.clicked.connect(lambda: Assembly.setInfo(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Assembly.saveInfos(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.assemblyButton, True))
        self.ui.returnAssembly.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.assemblyButton, False))
        self.ui.assemblyButton.clicked.connect(lambda: Assembly.setInfo(self))
        self.ui.assemblyButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 3, self.ui.assemblyFinish, False))

        # Iteration Actions
        self.ui.iterateButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 5, self.ui.iterateButton, False))
        self.ui.returnIteration.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, self.ui.iterateButton, False))
        self.ui.numberOfVariables.currentIndexChanged.connect(lambda: Page_Layout.setIterationVariablesEnabled(self))
        self.ui.applyIteration.clicked.connect(lambda: Iteration_Datas.saveIterationInfo(self))



