import numpy as np


def convert_nodes_to_array_of_coordinates(nodes):
    coordinates = []
    for node in nodes:
        point = [node.x, node.y]
        coordinates.append(point)
    return np.array(coordinates)