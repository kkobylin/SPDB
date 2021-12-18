import math


class Node:
    def __init__(self, id, x, y, label):
        self.id = id
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
        self.second_order_local_mean = 0

    def calculate_local_statistics(self):
        number_of_edges = len(self.edges)

        for edge in self.edges:
            self.local_mean += edge.calculate_length() / number_of_edges

        sum_st_dev = 0
        for edge in self.edges:
            sum_st_dev += (self.local_mean - edge.calculate_length()) ** 2
        self.local_st_dev = math.sqrt(sum_st_dev / number_of_edges)

    def calculate_relative_statistics(self, mean_st_dev):
        self.relative_st_dev = self.local_st_dev / mean_st_dev

    def split_edges(self, mean_st_dev):
        for edge in self.edges:
            edge_length = edge.calculate_length()
            if self.local_mean - mean_st_dev > edge_length:
                self.short_edges.add(edge)
            elif self.local_mean + mean_st_dev < edge_length:
                self.long_edges.add(edge)
            else:
                self.other_edges.add(edge)

    def hide_long_and_short_edges(self):
        for edge in set.union(self.short_edges, self.long_edges):
            edge.hide_edge()

    def propagate_prediction(self):
        for edge in self.edges:
            other_node = edge.find_other_node(self)
            if other_node.prediction is None and edge.visible:
                other_node.prediction = self.prediction
                other_node.propagate_prediction()

    def restore_short_edges_and_predict(self, cluster_strength):
        biggest_cluster_prediction = [-1]
        biggest_cluster_strength = -1
        # Finding biggest cluster
        for edge in self.short_edges:
            other_node = edge.find_other_node(self)
            pred = other_node.prediction
            stre = cluster_strength.get(pred)
            if pred not in biggest_cluster_prediction and stre > biggest_cluster_strength and stre > 1:
                biggest_cluster_prediction = [pred]
                biggest_cluster_strength = cluster_strength.get(pred)
            elif pred not in biggest_cluster_prediction and stre == biggest_cluster_strength and stre > 1:
                biggest_cluster_prediction.append(pred)

        # If two or more equal cluster, find the shortest path
        shortest_length = None
        best_prediction = self.prediction
        if len(biggest_cluster_prediction) > 1:
            for edge in self.short_edges:
                other_node = edge.find_other_node(self)
                pred = other_node.prediction
                length = edge.calculate_length()
                if pred in biggest_cluster_prediction and (shortest_length is None or length < shortest_length):
                    best_prediction = pred
                    shortest_length = length
        else:
            best_prediction = best_prediction if biggest_cluster_prediction[0] == -1 else biggest_cluster_prediction[0]

        # Restore edges to best cluster
        cluster_strength[self.prediction] -= 1
        self.prediction = best_prediction
        cluster_strength[self.prediction] += 1

        for edge in self.edges:
            other_node = edge.find_other_node(self)
            if other_node.prediction == best_prediction and edge not in self.long_edges:
                edge.restore_edge()
            else:
                edge.hide_edge()

    def detect_second_order_inconsistency(self, mean_st_dev):
        second_order_edges = set()
        visible_edges = (edge for edge in self.edges if edge.visible)
        second_order_edges.update(visible_edges)
        for edge in visible_edges:
            other_node = edge.find_other_node(self)
            second_order_edges.update(edge for edge in other_node.edges if edge.visible)

        number_of_edges = len(second_order_edges)
        for edge in second_order_edges:
            self.second_order_local_mean += edge.calculate_length() / number_of_edges

        for edge in visible_edges:
            if edge.calculate_length() > self.second_order_local_mean + mean_st_dev:
                edge.hide_edge()



