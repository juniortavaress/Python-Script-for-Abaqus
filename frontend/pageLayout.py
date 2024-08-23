from PySide6.QtGui import QScreen
from PySide6.QtCore import QTimer
from graphLayout import Graph_Layout
from PySide6.QtWidgets import QApplication

class Page_Layout():
    def __init__(self):
        super(Page_Layout, self).__init__()

    # Change the page view based on the provided page name
    def pageNumber(self, page):
        if page == 0:
            self.setMinimumSize(380, 400)
            self.ui.pages.setCurrentIndex(0)
            self.resize(380, 400)
            Page_Layout.centerWindow(self)
        else:
            self.setMinimumSize(1500, 850)
            self.showMaximized()
            self.ui.pages.setCurrentIndex(page)
            Graph_Layout.resize(self)


    def setGeneralInfos(self, page):
        all_Infos = True
        all_infos_widgets_chip = [self.ui.chipName, self.ui.chipHeight, self.ui.chipWidth, self.ui.chipTrickness, self.ui.chipGlobalSize, self.ui.chipDeviationFactor, self.ui.chipMininumFactor]
        all_infos_widgets_eulerian = [self.ui.eulerianName, self.ui.eulerianHeight, self.ui.eulerianWidth, self.ui.eulerianTrickness, self.ui.eulerianGlobalSize, self.ui.eulerianDeviationFactor, self.ui.eulerianMininumFactor, self.ui.eulerianPartitionX1, self.ui.eulerianPartitionX2, self.ui.eulerianPartitionX3, self.ui.eulerianPartitionX4, self.ui.eulerianPartitionY1, self.ui.eulerianPartitionY2, self.ui.eulerianPartitionY3, self.ui.eulerianPartitionY4]
        all_infos_widgets_tool = [self.ui.toolName, self.ui.toolTrickness, self.ui.toolRakeAngle, self.ui.toolRakeDimension, self.ui.toolClearanceAngle, self.ui.toolClearanceDimension, self.ui.toolRadius, self.ui.toolPartition01, self.ui.toolPartition02, self.ui.toolGlobalSize, self.ui.toolDeviationFactor, self.ui.toolMinimumFactor]
        all_infos_widgets_assembly = [self.ui.overWorkpiece, self.ui.fromTool, self.ui.xTool, self.ui.yTool, self.ui.feed, self.ui.timePeriod]

        page_mappings = {
            1: (all_infos_widgets_eulerian, self.ui.eulerianWarning, self.ui.eulerianName, self.ui.eulerianFinish),
            2: (all_infos_widgets_tool, self.ui.toolWarning, self.ui.toolName, self.ui.toolFinish),
            3: (all_infos_widgets_assembly, self.ui.assemblyWarning, 'defaut', self.ui.assemblyFinish),
            4: (all_infos_widgets_chip, self.ui.chipWarning, self.ui.chipName, self.ui.chipPlateFinish)}

        page_index = self.ui.pages.currentIndex()
        all_infos_widgets, warning, non_numerical_label, button = page_mappings[page_index]

        # Validate that all required fields are filled with the right info
        for info in all_infos_widgets:
            if not info.text().strip():
                all_Infos = False
                warning.setText("Set all parameters")
                QTimer.singleShot(4000, lambda: warning.setText(""))
                button.setEnabled(False)
                break
            elif info.text().strip() and info != non_numerical_label:
                try:
                    float(info.text())
                except:
                    all_Infos = False
                    warning.setText("The parameter '" + info.objectName() + "' must be a number value")
                    QTimer.singleShot(4000, lambda: warning.setText(""))
                    button.setEnabled(False)
        return all_Infos


    def centerWindow(self):
        # Obtain the geometry of the window, including the title bar
        qr = self.frameGeometry()
        # Get the geometry of the screen
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        # Calculate the center of the screen
        cp = screen.center()
        # Move the center of the window's geometry to the center of the screen
        qr.moveCenter(cp)
        # Move the top-left corner of the window to align with the adjusted geometry
        self.move(qr.topLeft())
