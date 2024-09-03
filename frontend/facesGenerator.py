import numpy as np

class FacesGenerator():
    def __init__(self):
        super(FacesGenerator, self).__init__()

    # Generate chip plate faces from vertices and combinations
    def chipPlateDatas(self, x, y, z):
        chip_width = float(self.ui.chipWidth.text())
        chip_thickness = float(self.ui.chipTrickness.text())
        chip_height = float(self.ui.chipHeight.text())

        vertices_combinations = [[0, 1, 5, 4], [7, 6, 2, 3], [0, 3, 7, 4], [1, 2, 6, 5], [0, 1, 2, 3], [4, 5, 6, 7]]
        chip_vertices = [
            [0 + x, 0 + y, 0 + z], [chip_width + x, 0 + y, 0 + z],
            [chip_width + x, chip_thickness + y, 0 + z], [0 + x, chip_thickness + y, 0 + z],
            [0 + x, 0 + y, chip_height + z], [chip_width + x, 0 + y, chip_height + z],
            [chip_width + x, chip_thickness + y, chip_height + z], [0 + x, chip_thickness + y, chip_height + z]]

        chip_faces = FacesGenerator.getFaces(self, chip_vertices, vertices_combinations)
        return chip_faces


    # Generate eulerian faces from vertices and combinations
    def eulerianDatas(self):
        eulerian_width = float(self.ui.eulerianWidth.text())
        eulerian_thickness = float(self.ui.eulerianTrickness.text())
        eulerian_height = float(self.ui.eulerianHeight.text())

        vertices_combinations = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]]
        eulerian_vertices = [
            [0, 0, 0], [eulerian_width, 0, 0],
            [eulerian_width, eulerian_thickness, 0], [0, eulerian_thickness, 0],
            [0, 0, eulerian_height], [eulerian_width, 0, eulerian_height],
            [eulerian_width, eulerian_thickness, eulerian_height], [0, eulerian_thickness, eulerian_height]]

        eulerian_faces = FacesGenerator.getFaces(self, eulerian_vertices, vertices_combinations)
        return eulerian_faces


    # Generate tool faces from vertices and combinations
    def toolDatas(self, page):
        clearanceFaceDimension = float(self.ui.toolClearanceDimension.text())
        rakeFaceDimension = float(self.ui.toolRakeDimension.text())
        Trickness = float(self.ui.toolTrickness.text())
        left_angle_rad = np.radians(float(self.ui.toolRakeAngle.text()))
        bottom_angle_rad = np.radians(float(self.ui.toolClearanceAngle.text()))

        vertices_combinations = [[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 6, 7], [0, 2, 6, 4], [1, 3, 7, 5]]

        if page == "Tool":
            tool_vertices = [[0, 0, 0],[0, 0, Trickness],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), 0],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), clearanceFaceDimension*np.sin(bottom_angle_rad), Trickness],
                        [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                        [rakeFaceDimension*np.sin(left_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), 0],
                        [clearanceFaceDimension*np.cos(bottom_angle_rad), rakeFaceDimension*np.cos(left_angle_rad), Trickness]]
        else:
            x = sorted([float(self.ui.eulerianPartitionX1.text()), float(self.ui.eulerianPartitionX2.text()), float(self.ui.eulerianPartitionX3.text()), float(self.ui.eulerianPartitionX4.text())])[2]
            z = sorted([float(self.ui.eulerianPartitionY1.text()), float(self.ui.eulerianPartitionY2.text()), float(self.ui.eulerianPartitionY3.text()), float(self.ui.eulerianPartitionY4.text())], reverse=True)[1]
            feed = float(self.ui.feed.text())
            tool_vertices = [
                [0 + x, 0, 0 + z - feed],
                [0 + x, Trickness, 0 + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, 0, clearanceFaceDimension * np.sin(bottom_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, Trickness, clearanceFaceDimension * np.sin(bottom_angle_rad) + z - feed],
                [rakeFaceDimension * np.sin(left_angle_rad) + x, 0, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [rakeFaceDimension * np.sin(left_angle_rad) + x, Trickness, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, 0, rakeFaceDimension * np.cos(left_angle_rad) + z - feed],
                [clearanceFaceDimension * np.cos(bottom_angle_rad) + x, Trickness, rakeFaceDimension * np.cos(left_angle_rad) + z - feed]]

        tool_faces = FacesGenerator.getFaces(self, tool_vertices, vertices_combinations)
        return tool_faces


    # Define faces for the geometry using the vertices
    def getFaces(self, vertices, vertex_combinations):
        faces = []
        for vertex_set in vertex_combinations:
            face = [vertices[j] for j in vertex_set]
            faces.append(face)
        return faces












