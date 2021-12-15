from scipy.spatial import Delaunay
import AlgorithmUtils
from Edge import Edge


class Autoclust:
    def __init__(self, nodes):
        self.nodes = nodes
        self.coordinates = AlgorithmUtils.convert_nodes_to_array_of_coordinates(nodes)
        self.mean_std_dev = 0
        self.short_edges = set()
        self.long_edges = set()
        self.other_edges = set()
        self.cluster_strength = dict()

    def get_edges_from_triangulation(self):
        tri_result = Delaunay(self.coordinates)
        triangles = tri_result.simplices
        for triangle in triangles:
            point1 = self.nodes[triangle[0]]
            point2 = self.nodes[triangle[1]]
            point3 = self.nodes[triangle[2]]
            point1.edges.update([Edge(point2), Edge(point3)])
            point2.edges.update([Edge(point1), Edge(point3)])
            point3.edges.update([Edge(point1), Edge(point2)])

        return self.nodes

    def calculate_statistics(self):
        sum_local_st_dev = 0
        for node in self.nodes:
            node.calculate_local_statistics()
            sum_local_st_dev += node.local_st_dev
        self.mean_std_dev = sum_local_st_dev / len(self.nodes)

        for node in self.nodes:
            node.calculate_relative_statistics(self.mean_std_dev)

        return self.nodes

    def split_edges(self):
        for node in self.nodes:
            node.split_edges(self.mean_std_dev)
            self.short_edges.update(node.short_edges)
            self.long_edges.update(node.long_edges)
            self.other_edges.update(node.other_edges)

        return self.nodes

    def hide_long_and_short_edges(self):
        for node in self.nodes:
            node.hide_long_and_short_edges()

    def predict_clusters(self):
        cluster_nr = 0
        for node in self.nodes:
            if node.prediction is None:
                node.prediction = cluster_nr
                cluster_nr += 1
                node.propagate_prediction()
            self.add_one_to_cluster_strength(node.prediction)

        return self.nodes

    def add_one_to_cluster_strength(self, prediction):
        strength = self.cluster_strength.get(prediction)

        if strength is None:
            self.cluster_strength[prediction] = 1
        else:
            self.cluster_strength[prediction] += 1

    def restore_short_edges(self):
        for node in self.nodes:
            if len(node.short_edges) != 0:
                node.restore_short_edges(self.cluster_strength)






