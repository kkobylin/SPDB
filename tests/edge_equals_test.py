from Edge import Edge
from Node import Node

node1 = Node(1, 1, 1)
node2 = Node(1, 5, 2)

# node1.edges.update([Edge(node2)])
# node2.edges.update([Edge(node1)])

edge_set = set()
edge_set.update([Edge(node1), Edge(node1)])
assert(len(edge_set) == 1)
