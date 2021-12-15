import matplotlib.pyplot as plt
from Color import Color


def format_set(nodes):
    formatted_set = {"x": [], "y": [], "label": [], "prediction": []}
    for node in nodes:
        formatted_set['x'].append(node.x)
        formatted_set['y'].append(node.y)
        formatted_set['label'].append(node.label)
        formatted_set['prediction'].append(node.prediction)

    return formatted_set


def draw_points_by_label(nodes) -> None:
    formatted_points = format_set(nodes)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["label"])
    # plt.savefig('ByLabel.png')
    plt.show()


def draw_points(nodes) -> None:
    formatted_points = format_set(nodes)
    plt.scatter(formatted_points["x"], formatted_points["y"])
    plt.show()


def draw_nodes_with_edges(nodes):
    for node in nodes:
        for edge in node.edges:
            if edge.visible:
                plt.plot([node.x, edge.node.x], [node.y, edge.node.y], c=Color.blue.value, linewidth=0.5)
        plt.scatter(node.x, node.y, c=Color.green.value)
    plt.show()

#TODO mozna cos zrobic ze jak node jest solo to zeby mialy ten sam kolor - slownik liczebnosci grup w cluster
def draw_points_by_prediction(nodes) -> None:
    formatted_points = format_set(nodes)
    plt.scatter(formatted_points["x"], formatted_points["y"],
                c=formatted_points["prediction"])
    for node in nodes:
        for edge in node.edges:
            if edge.visible:
                plt.plot([node.x, edge.node.x], [node.y, edge.node.y], c=Color.blue.value, linewidth=0.5)
    plt.show()
