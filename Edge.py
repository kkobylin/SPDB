from Node import Node
import math


class Edge:
    def __init__(self, id, node1: Node, node2: Node):
        self.id = id
        self.node1 = node1
        self.node2 = node2
        self.visible = True
        
    def calculate_length(self):
        return math.sqrt((self.node1.x - self.node2.x) ** 2 + (self.node1.y - self.node2.y) ** 2)

    def hide_edge(self):
        self.visible = False
        # corresponding_edge = [edge for edge in self.node.edges if edge.node.x == x and edge.node.y == y]
        # corresponding_edge[0].visible = False

    def restore_edge(self):
        self.visible = True
        # corresponding_edge = [edge for edge in self.node.edges if edge.node.x == x and edge.node.y == y]
        # corresponding_edge[0].visible = True

    def find_other_node(self, node: Node) -> Node:
        if node == self.node1:
            return self.node2
        else:
            return self.node1

    def __eq__(self, obj):
        return obj.node1 == self.node1 and obj.node2 == self.node2 or obj.node1 == self.node2 and obj.node2 == self.node1

    def __hash__(self):
        return hash(hash(self.node1) * hash(self.node2))
