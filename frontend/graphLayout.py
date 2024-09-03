from imports import *

class Graph_Layout():
    def __init__(self):
        super(Graph_Layout, self).__init__()

    # Create the plot areas for different pages and set up the canvases.
    def createPlotAreas(self):
        self.figTool, self.axTool, self.canvasTool = Graph_Layout.setCanvas(self, self.ui.plotToolArea)
        self.figChip, self.axChip, self.canvasChip = Graph_Layout.setCanvas(self, self.ui.plotChipPlateArea)
        self.figAssembly, self.axAssembly, self.canvasAssembly = Graph_Layout.setCanvas(self, self.ui.plotAssemblyArea)
        self.figEulerian, self.axEulerian, self.canvasEulerian = Graph_Layout.setCanvas(self, self.ui.plotEulerianArea)


    # Set up a canvas and axis for the given plot area
    def setCanvas(self, plot_area):
        fig, ax = plt.subplots()
        ax.axis(False)
        ax = fig.add_subplot(111, projection='3d')
        ax.set_axis_off()
        fig.set_facecolor((182/255, 182/255, 182/255))
        ax.set_facecolor((182/255, 182/255, 182/255))
        canvas = FigureCanvas(fig)
        canvas.setGeometry(plot_area.contentsRect())
        canvas.setParent(plot_area)
        return fig, ax, canvas


    # Resize the canvas based on the current page
    def resize(self):
        page_mappings = {
            1: (self.canvasEulerian, self.axEulerian, self.ui.plotEulerianArea),
            2: (self.canvasTool, self.axTool, self.ui.plotToolArea),
            3: (self.canvasAssembly, self.axAssembly, self.ui.plotAssemblyArea),
            4: (self.canvasChip, self.axChip, self.ui.plotChipPlateArea)}

        page_index = self.ui.pages.currentIndex()
        if page_index in page_mappings:
            canvas, axis, plot_area = page_mappings[page_index]
            size = plot_area.size()
            canvas.setGeometry(0, 0, size.width(), size.height())
            axis.figure.tight_layout()
            canvas.draw()


    # Set up the axis limits, view, and aspect ratio for the current page.
    def axisLayout(self, geometry):
        if geometry == "ChipPlate":
            xlim = [0, float(self.ui.chipWidth.text())]
            ylim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            zlim = [-0.1*float(self.ui.chipWidth.text()), 0.1*float(self.ui.chipWidth.text())]
            elev, azim, boxAspect = [30, 40, [1, 1, 1]]
            axis, fig, canvas = [self.axChip, self.figChip, self.canvasChip]

        elif geometry == "Eulerian":
            xlim = [-(float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2, float(self.ui.eulerianWidth.text()) + (float(self.ui.eulerianHeight.text())-float(self.ui.eulerianWidth.text()))/2]
            ylim = [0, float(self.ui.eulerianHeight.text())]
            zlim = [0, float(self.ui.eulerianHeight.text())]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]
            axis, fig, canvas = [self.axEulerian, self.figEulerian, self.canvasEulerian]

        elif geometry == "Tool":
            clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
            rakeFaceDimension = float(self.ui.toolRakeDimension.text())
            bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))
            space = (rakeFaceDimension*np.cos(bottom_angle_rad)-clearanceFaceDimension*np.cos(bottom_angle_rad))/2

            xlim = [-space, clearanceFaceDimension*np.cos(bottom_angle_rad)+space]
            ylim = [0, rakeFaceDimension*np.cos(bottom_angle_rad)]
            zlim = [-(rakeFaceDimension*np.cos(bottom_angle_rad)/10), (rakeFaceDimension*np.cos(bottom_angle_rad)/10)]
            elev, azim, boxAspect = [90, 270, [1, 1, 1]]
            axis, fig, canvas = [self.axTool, self.figTool, self.canvasTool]

        elif geometry == "Assembly":
            xlim = [0.5, 6]
            ylim = [0.5, 6]
            zlim = [0.5, 6]
            elev, azim, boxAspect = [0, -90, [1, 1, 1]]
            axis, fig, canvas = [self.axAssembly, self.figAssembly, self.canvasAssembly]

        axis.set_xlim(xlim)
        axis.set_ylim(ylim)
        axis.set_zlim(zlim)
        axis.set_axis_off()
        axis.view_init(elev=elev, azim=azim)
        axis.set_box_aspect(boxAspect)
        fig.tight_layout()
        canvas.draw()



