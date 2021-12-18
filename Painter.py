import matplotlib.pyplot as plt
from Color import Color
import mplcursors

save_fig = None
colors = ["k", "tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink",
          "tab:olive", "tab:cyan", "tab:gray", "yellow", "greenyellow", "blue", "navy", "royalblue",
          "silver", "tomato", "palegreen", "olive", "khaki", "tan", "seagreen", "violet", "skyblue"]


def format_set(nodes, cluster_strength):
    formatted_set = {"x": [], "y": [], "label": [], "prediction": []}
    non_solo_labels_dict = dict()
    non_solo_next_label = 1

    for node in nodes:
        formatted_set['x'].append(node.x)
        formatted_set['y'].append(node.y)
        formatted_set['label'].append(colors[int(node.label)])

        if cluster_strength is not None and cluster_strength[node.prediction] <= 1:  # Solo nodes
            formatted_set['prediction'].append(colors[0])
        elif node.prediction is not None:
            # Get number of cluster for cluster node
            label = non_solo_labels_dict.get(node.prediction)
            if label is None:
                label = non_solo_next_label
                non_solo_next_label += 1
                non_solo_labels_dict[node.prediction] = label
            # Get color for given cluster
            if label < 24:
                formatted_set['prediction'].append(colors[label])
            else:
                formatted_set['prediction'].append(colors[24])

    return formatted_set


def draw_points_by_label(nodes, cluster_strength, filename) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["label"])

    save_figure(filename)
    mplcursors.cursor()
    plt.show()


def draw_points(nodes, cluster_strength, filename) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"])

    save_figure(filename)
    mplcursors.cursor()
    plt.show()


def draw_nodes_with_edges(nodes, edges, cluster_strength, filename):
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"], c=Color.green.value)
    for edge in edges:
        if edge.visible:
            plt.plot([edge.node1.x, edge.node2.x], [edge.node1.y, edge.node2.y], c=Color.blue.value, linewidth=0.5)

    save_figure(filename)
    mplcursors.cursor()
    plt.show()


def draw_points_by_prediction_with_edges(nodes, edges, cluster_strength, filename) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["prediction"])
    for edge in edges:
        if edge.visible:
            plt.plot([edge.node1.x, edge.node2.x], [edge.node1.y, edge.node2.y], c=Color.blue.value, linewidth=0.5)

    save_figure(filename)
    mplcursors.cursor()
    plt.show()


def draw_points_by_prediction(nodes, cluster_strength, filename) -> None:
    formatted_points = format_set(nodes, cluster_strength)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["prediction"])

    save_figure(filename)
    mplcursors.cursor()
    plt.show()


def save_figure(filename):
    if save_fig:
        plt.savefig("figures/" + filename + '.png', format="png")
