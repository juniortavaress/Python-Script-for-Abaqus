from generateTool import Tool
from pageLayout import Page_Layout
from generateAssembly import Assembly
from generateEulerian import Eulerian
from generateChipPlate import ChipPlate
from PySide6 import QtCore, QtGui, QtWidgets


class ButtonsCallback():
    def __init__(self):
        super(ButtonsCallback, self).__init__()

    def actions(self):
        # General Actions

        # Chip Plate Actions
        ChipPlate.init(self)
        self.ui.chipPlateApply.clicked.connect(lambda: ChipPlate.setInfo(self))
        self.ui.chipPlateFinish.clicked.connect(lambda: ChipPlate.saveInfos(self))
        self.ui.chipPlateFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0))
        self.ui.chipPlateDefaut.stateChanged.connect(lambda: ChipPlate.setDefautInfos(self))
        self.ui.chipPlateButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 4))

        # Eulerian Actions
        Eulerian.init(self)
        self.ui.eulerianApply.clicked.connect(lambda: Eulerian.setInfo(self))
        self.ui.eulerianFinish.clicked.connect(lambda: Eulerian.saveInfos(self))
        self.ui.eulerianFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0))
        self.ui.eulerianDefaut.stateChanged.connect(lambda: Eulerian.setDefautInfos(self))
        self.ui.eulerianButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 1))

        # Tool Actions
        Tool.init(self)
        self.ui.toolApply.clicked.connect(lambda: Tool.setInfo(self))
        self.ui.toolFinish.clicked.connect(lambda: Tool.saveInfos(self))
        self.ui.toolFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0))
        self.ui.toolDefaut.stateChanged.connect(lambda: Tool.setDefautInfos(self))
        self.ui.toolButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 2))

        # Assembly Actions
        Assembly.init(self)
        self.ui.assemblyApply.clicked.connect(lambda: Assembly.setInfo(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Assembly.saveInfos(self))
        self.ui.assemblyFinish.clicked.connect(lambda: Page_Layout.pageNumber(self, 0))
        self.ui.assemblyDefaut.stateChanged.connect(lambda: Assembly.setDefautInfos(self))
        self.ui.assemblyButton.clicked.connect(lambda: Page_Layout.pageNumber(self, 3))





