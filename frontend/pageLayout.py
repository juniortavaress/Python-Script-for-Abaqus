from imports import *
from graphLayout import Graph_Layout

class Page_Layout():
    def __init__(self):
        super(Page_Layout, self).__init__()

    # Change the page view based on the provided page name
    def pageNumber(self, page, button, action):
        if page == 0 or page == 5:
            self.setMinimumSize(420, 450)
            self.ui.pages.setCurrentIndex(page)
            self.resize(420, 450)
            Page_Layout.centerWindow(self)
            button.setChecked(action) if button else None
        elif page == 6:
            self.setMinimumSize(1500, 850)
            self.showMaximized()
            self.ui.pages.setCurrentIndex(page)
        else:
            button.setEnabled(action) if button else None
            self.setMinimumSize(1500, 850)
            self.showMaximized()
            self.ui.pages.setCurrentIndex(page)
            Graph_Layout.resize(self)


    def setGeneralInfos(self, page):
        all_Infos = True

        all_infos_widgets_chip = {'Name': self.ui.chipName, 'Height': self.ui.chipHeight, 'Width': self.ui.chipWidth, 'Trickness': self.ui.chipTrickness,
                                  'Global Size': self.ui.chipGlobalSize, 'Deviation Factor': self.ui.chipDeviationFactor, 'Minimum Factor': self.ui.chipMininumFactor}

        all_infos_widgets_eulerian = {'Name': self.ui.eulerianName, 'Height': self.ui.eulerianHeight, 'Width': self.ui.eulerianWidth, 'Trickness': self.ui.eulerianTrickness,
                                      'Global Size': self.ui.eulerianGlobalSize, 'Deviation Factor': self.ui.eulerianDeviationFactor, 'Minimum Factor': self.ui.eulerianMininumFactor,
                                      'X1': self.ui.eulerianPartitionX1, 'X2': self.ui.eulerianPartitionX2, 'X3': self.ui.eulerianPartitionX3, 'X4': self.ui.eulerianPartitionX4,
                                      'Y1': self.ui.eulerianPartitionY1, 'Y2': self.ui.eulerianPartitionY2, 'Y3': self.ui.eulerianPartitionY2, 'Y4': self.ui.eulerianPartitionY4,}


        all_infos_widgets_tool = {'Name': self.ui.toolName, 'Trickness': self.ui.toolTrickness,'Rake Angle': self.ui.toolRakeAngle, 'Rake Dimension': self.ui.toolRakeDimension,
                                  'Clearance Angle': self.ui.toolClearanceAngle, 'Clearance Dimension': self.ui.toolClearanceDimension, 'Radius': self.ui.toolRadius,
                                  'Partition 01': self.ui.toolPartition01, 'Partition 02': self.ui.toolPartition02, 'Global Size': self.ui.toolGlobalSize,
                                  'Deviation Factor': self.ui.toolDeviationFactor, 'Minimum Factor': self.ui.toolMinimumFactor}


        all_infos_widgets_assembly = {'Clearance Over Workpiece': self.ui.overWorkpiece, 'Distance From Tool': self.ui.fromTool, 'Tool Position (X)': self.ui.xTool, 'Tool Position (Y)': self.ui.yTool,
                                      'Feed': self.ui.feed, 'Time Period': self.ui.timePeriod}

        page_mappings = {
            1: (all_infos_widgets_eulerian, self.ui.eulerianWarning, self.ui.eulerianName, self.ui.eulerianFinish),
            2: (all_infos_widgets_tool, self.ui.toolWarning, self.ui.toolName, self.ui.toolFinish),
            3: (all_infos_widgets_assembly, self.ui.assemblyWarning, 'defaut', self.ui.assemblyFinish),
            4: (all_infos_widgets_chip, self.ui.chipWarning, self.ui.chipName, self.ui.chipPlateFinish)}

        all_infos_widgets, warning, non_numerical_label, button = page_mappings[page]

        # Validate that all required fields are filled with the right info
        for key, info in all_infos_widgets.items():
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
                    warning.setText("The parameter " + key + "\n must be a number value with dot as decimal separator!")
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

    def saveInfos(self):
        self.ui.chipPlateFinish.setEnabled(True)
        self.ui.eulerianFinish.setEnabled(True)
        self.ui.toolFinish.setEnabled(True)
        self.ui.assemblyFinish.setEnabled(True)

    def setIterationVariablesEnabled(self):
        if self.ui.numberOfVariables.currentIndex() == 1:
            self.ui.P01.setEnabled(True)
            self.ui.minP01.setEnabled(True)
            self.ui.maxP01.setEnabled(True)
            self.ui.stepP01.setEnabled(True)
            self.ui.P02.setEnabled(False)
            self.ui.minP02.setEnabled(False)
            self.ui.maxP02.setEnabled(False)
            self.ui.stepP02.setEnabled(False)
        elif self.ui.numberOfVariables.currentIndex() == 2:
            self.ui.P01.setEnabled(True)
            self.ui.minP01.setEnabled(True)
            self.ui.maxP01.setEnabled(True)
            self.ui.stepP01.setEnabled(True)
            self.ui.P02.setEnabled(True)
            self.ui.minP02.setEnabled(True)
            self.ui.maxP02.setEnabled(True)
            self.ui.stepP02.setEnabled(True)
        else:
            self.ui.P01.setEnabled(False)
            self.ui.minP01.setEnabled(False)
            self.ui.maxP01.setEnabled(False)
            self.ui.stepP01.setEnabled(False)
            self.ui.P02.setEnabled(False)
            self.ui.minP02.setEnabled(False)
            self.ui.maxP02.setEnabled(False)
            self.ui.stepP02.setEnabled(False)


