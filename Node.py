import math


class Node:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
        self.prediction = None
        self.edges = set()
        self.short_edges = set()
        self.long_edges = set()
        self.other_edges = set()
        self.local_mean = 0
        self.local_st_dev = 0
        self.relative_st_dev = 0

    def calculate_local_statistics(self):
        number_of_edges = len(self.edges)

        for edge in self.edges:
            self.local_mean += self.calculate_edge_length(edge) / number_of_edges

        sum_st_dev = 0
        for edge in self.edges:
            sum_st_dev += (self.local_mean - self.calculate_edge_length(edge)) ** 2
        self.local_st_dev = math.sqrt(sum_st_dev / number_of_edges)

    def calculate_relative_statistics(self, mean_st_dev):
        self.relative_st_dev = self.local_st_dev / mean_st_dev

    def calculate_edge_length(self, edge):
        return math.sqrt((self.x - edge.node.x) ** 2 + (self.y - edge.node.y) ** 2)

    def split_edges(self, mean_st_dev):
        for edge in self.edges:
            edge_length = self.calculate_edge_length(edge)
            if self.local_mean - mean_st_dev > edge_length:
                self.short_edges.add(edge)
            elif self.local_mean + mean_st_dev < edge_length:
                self.long_edges.add(edge)
            else:
                self.other_edges.add(edge)

    def hide_long_and_short_edges(self):
        for edge in set.union(self.short_edges, self.long_edges):
            edge.hide_edge(self.x, self.y)

    def propagate_prediction(self):
        for edge in self.edges:
            if edge.node.prediction is None and edge.visible:
                edge.node.prediction = self.prediction
                edge.node.propagate_prediction()

    def restore_short_edges(self, cluster_strength):
        biggest_cluster_prediction = [-1]
        biggest_cluster_strength = -1
        # Finding biggest cluster
        for edge in self.short_edges:
            pred = edge.node.prediction
            if pred not in biggest_cluster_prediction and cluster_strength.get(pred) > biggest_cluster_strength:
                biggest_cluster_prediction = [pred]
                biggest_cluster_strength = cluster_strength.get(edge.node.prediction)
            elif pred not in biggest_cluster_prediction and cluster_strength.get(pred) == biggest_cluster_strength:
                biggest_cluster_prediction.append(pred)

        # If two or more equal cluster, find the shortest path
        shortest_length = None
        best_prediction = -1
        if len(biggest_cluster_prediction) > 1:
            for edge in self.short_edges:
                pred = edge.node.prediction
                length = self.calculate_edge_length(edge)
                if pred in biggest_cluster_prediction and (shortest_length is None or length < shortest_length):
                    best_prediction = pred
                    shortest_length = length
        else:
            best_prediction = biggest_cluster_prediction[0]

        # Restore edges to best cluster
        cluster_strength[self.prediction] -= 1
        self.prediction = best_prediction
        cluster_strength[self.prediction] += 1

        for edge in set.union(self.short_edges, self.other_edges):
            if edge.node.prediction == best_prediction:
                edge.restore_edge(self.x, self.y)
            else:
                edge.hide_edge(self.x, self.y)


