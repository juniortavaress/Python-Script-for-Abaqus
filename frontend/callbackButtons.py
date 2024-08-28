from generateTool import Tool
from pageLayout import Page_Layout
from generateAssembly import Assembly
from generateEulerian import Eulerian
from generateChipPlate import ChipPlate
from PySide6 import QtCore, QtGui, QtWidgets

from iterationDatas import Iteration_Datas

class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    def actions(self):
        # General Actions
        self.ui.defautValues.stateChanged.connect(lambda: Tool.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Eulerian.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: ChipPlate.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Page_Layout.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Assembly.setDefautInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Tool.saveInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Assembly.saveInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Eulerian.saveInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: ChipPlate.saveInfos(self))
        self.ui.defautValues.stateChanged.connect(lambda: Page_Layout.saveInfos(self))

        # Chip Plate Actions
        ChipPlate.init(self)
        self.ui.chipPlateApply.clicked.connect(lambda: ChipPlate.setInfo(self))
        self.ui.chipPlateFinish.clicked.connect(lambda: ChipPlate.saveInfos(self))
        self.ui.returnChipPlate.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        self.ui.chipPlateFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))

        self.ui.chipPlateButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 4, self.ui.chipPlateFinish))

        # Eulerian Actions
        Eulerian.init(self)
        self.ui.eulerianApply.clicked.connect(lambda: Eulerian.setInfo(self))
        self.ui.eulerianFinish.clicked.connect(lambda: Eulerian.saveInfos(self))
        self.ui.returnEulerian.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        self.ui.eulerianFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))

        self.ui.eulerianButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 1, self.ui.eulerianFinish))

        # Tool Actions
        Tool.init(self)
        self.ui.toolApply.clicked.connect(lambda: Tool.setInfo(self))
        self.ui.toolFinish.clicked.connect(lambda: Tool.saveInfos(self))
        self.ui.returnTool.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        self.ui.toolFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))

        self.ui.toolButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 2, self.ui.toolFinish))

        # Assembly Actions
        Assembly.init(self)
        self.ui.assemblyApply.clicked.connect(lambda: Assembly.setInfo(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Assembly.saveInfos(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        self.ui.returnAssembly.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))

        self.ui.assemblyButton.clicked.connect(lambda: Assembly.setInfo(self))
        self.ui.assemblyButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 3, self.ui.assemblyFinish))


        # Iteration Actions
        self.ui.iterateButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 5, None))
        self.ui.returnIteration.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        # self.ui.applyIteration.clicked.connect(lambda: Page_Layout.pageNumber(self, 0, None))
        self.ui.numberOfVariables.currentIndexChanged.connect(lambda: Page_Layout.setIterationVariablesEnabled(self))
        self.ui.applyIteration.clicked.connect(lambda: Iteration_Datas.saveIterationInfo(self))


