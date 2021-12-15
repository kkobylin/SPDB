from Node import Node


class Edge:
    def __init__(self, node: Node):
        self.node = node
        self.visible = True

    def hide_edge(self, x, y):
        self.visible = False
        corresponding_edge = [edge for edge in self.node.edges if edge.node.x == x and edge.node.y == y]
        corresponding_edge[0].visible = False

    def restore_edge(self, x, y):
        self.visible = True
        corresponding_edge = [edge for edge in self.node.edges if edge.node.x == x and edge.node.y == y]
        corresponding_edge[0].visible = True

    def __eq__(self, obj):
        return obj.node == self.node

    def __hash__(self):
        return hash(self.node)
