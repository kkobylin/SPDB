import unittest

from Edge import Edge
from Node import Node


class NodeTest(unittest.TestCase):
    def test_restore_short_edges(self):
        # given
        node1 = Node(1, 1, 1)
        node2 = Node(1, 5, 2)
        node3 = Node(5, 5, 3)
        node4 = Node(5, 1, 4)
        node5 = Node(3, 3, 5)

        node1.prediction = 1
        node2.prediction = 2
        node3.prediction = 3
        node4.prediction = 2
        node5.prediction = 3

        node1.short_edges.update([Edge(node2), Edge(node3)])
        node1.other_edges.update([Edge(node4), Edge(node5)])
        node2.edges.update([Edge(node1)])
        node3.edges.update([Edge(node1)])
        node4.edges.update([Edge(node1)])
        node5.edges.update([Edge(node1)])
        for edge in set.union(node1.short_edges, node2.edges, node3.edges):
            edge.visible = False

        cluster_strength = {
            1: 1,
            2: 2,
            3: 6
        }

        # when
        node1.restore_short_edges_and_predict(cluster_strength)
        # then
        ## Zmiana predykcji
        self.assertEqual(node1.prediction, 3)
        ## Update slownika
        self.assertEqual(cluster_strength[1], 0)
        self.assertEqual(cluster_strength[3], 7)
        ## Update krawedzi
        for short_edge in node1.short_edges:
            if short_edge.node == node2:
                self.assertEqual(False, short_edge.visible)
            if short_edge.node == node3:
                self.assertEqual(True, short_edge.visible)

        for edge in node1.other_edges:
            if edge.node == node4:
                self.assertEqual(False, edge.visible)
            if edge.node == node5:
                self.assertEqual(True, edge.visible)

        for edge in set.union(node2.edges, node4.edges):
            self.assertEqual(False, edge.visible)
        for edge in set.union(node3.edges, node5.edges):
            self.assertEqual(True, edge.visible)

    def test_detect_second_order_inconsistency(self):
        # given
        node1 = Node(1, 1, 1)
        node2 = Node(1, 5, 2)
        node3 = Node(5, 5, 3)
        node4 = Node(5, 1, 4)

        node1.edges.update([Edge(node2)])
        node2.edges.update([Edge(node1), Edge(node3), Edge(node4)])

        # when
        second_order_edges = node1.edges
        for edge in node1.edges:
            other_node = edge.find_other_node(node1)
            second_order_edges.update(other_node.edges)

        self.assertEqual(3, len(second_order_edges))


if __name__ == '__main__':
            unittest.main()