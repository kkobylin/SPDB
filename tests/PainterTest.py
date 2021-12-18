import unittest

import Painter
from Node import Node


class PainterTest(unittest.TestCase):
    def test_get_non_solo_label(self):
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
        nodes = [node1, node2, node3, node4, node5]

        cluster_strength = {
            1: 1,
            2: 2,
            3: 2
        }

        Painter.draw_points_by_prediction(nodes, cluster_strength)
