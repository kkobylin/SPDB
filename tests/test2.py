from Autoclust import Autoclust
from Edge import Edge
from Node import Node

node1 = Node(1, 1, 1)
node2 = Node(2, 2, 2)

node1.edges.add(Edge(node2))
node1.short_edges.add(Edge(node2))

for edge in node1.edges:
    edge.node.label = 1

for edge in node1.short_edges:
    assert(edge.node.label == 1)

found_edge = [edge for edge in node1.edges if edge.node.x == 2 and edge.node.y == 2]
