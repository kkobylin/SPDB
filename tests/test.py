import Painter
from Autoclust import Autoclust
from Edge import Edge
from Node import Node
# Test na usuniecie krawedzi do Node4 i predictCluster
node1 = Node(1, 1, 1)
node2 = Node(1, 5, 2)
node3 = Node(5, 5, 3)
node4 = Node(5, 1, 4)
node5 = Node(3, 3, 5)

node1.edges.update([Edge(node2), Edge(node3)])
node2.edges.update([Edge(node1), Edge(node4), Edge(node5)])
node3.edges.update([Edge(node1), Edge(node4), Edge(node5)])
node4.edges.update([Edge(node2), Edge(node3)])
node5.edges.update([Edge(node2), Edge(node3)])

nodes = [node1, node2, node3, node4, node5]

node4.long_edges.update(node4.edges)

autoclust = Autoclust(nodes)
autoclust.hide_long_and_short_edges()
nodes = autoclust.predict_clusters()

Painter.draw_points_by_prediction(nodes)
