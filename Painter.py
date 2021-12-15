import matplotlib.pyplot as plt
from Color import Color
import mplcursors


def format_set(nodes, cluster_strength):
    formatted_set = {"x": [], "y": [], "label": [], "prediction": []}
    for node in nodes:
        formatted_set['x'].append(node.x)
        formatted_set['y'].append(node.y)
        formatted_set['label'].append(node.label)
        if cluster_strength is not None and cluster_strength[node.prediction] <= 1:
            formatted_set['prediction'].append(-1)
        else:
            formatted_set['prediction'].append(node.prediction)

    return formatted_set


def draw_points_by_label(nodes, cluster_strength) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["label"])
    # plt.savefig('ByLabel.png')

    mplcursors.cursor()
    plt.show()


def draw_points(nodes, cluster_strength) -> None:
    # fig, ax = plt.subplots()
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"])

    mplcursors.cursor()
    plt.show()


def draw_nodes_with_edges(nodes, edges, cluster_strength):
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"], c=Color.green.value)
    for edge in edges:
        if edge.visible:
            plt.plot([edge.node1.x, edge.node2.x], [edge.node1.y, edge.node2.y], c=Color.blue.value, linewidth=0.5)

    mplcursors.cursor()
    plt.show()


def draw_points_by_prediction_with_edges(nodes, edges, cluster_strength) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["prediction"])
    for edge in edges:
        if edge.visible:
            plt.plot([edge.node1.x, edge.node2.x], [edge.node1.y, edge.node2.y], c=Color.blue.value, linewidth=0.5)

    mplcursors.cursor()
    plt.show()
