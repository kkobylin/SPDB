import DataReader
import Node
import Painter
import Autoclust

paint = True
save_fig = True
source = "R15.txt"

if __name__ == '__main__':
    Painter.save_fig = save_fig
    if "txt" in source:
        data = DataReader.read_tsv("data/" + source)
    else:
        data = DataReader.read_csv("data/" + source)
    nodes = []
    node_id = 0
    for row in data:
        nodes.append(Node.Node(node_id, row[0], row[1], row[2]))
        node_id += 1
    if paint:
        filename = source[0:-4] + "_labels"
        Painter.draw_points_by_label(nodes, cluster_strength=None, filename=filename)

    autoclust = Autoclust.Autoclust(nodes)
    print("Triangulacja")
    nodes = autoclust.get_edges_from_triangulation()
    autoclust.remove_nodes_without_edges()

    if paint:
        print("Rysowanie")
        filename = source[0:-4] + "_triangulation"
        Painter.draw_nodes_with_edges(nodes, autoclust.all_edges, cluster_strength=None, filename=filename)

    print("Statystyki")
    autoclust.calculate_statistics()
    print("Dzielenie krawedzi")
    autoclust.split_edges()
    print("Ukrywanie krawedzi")
    autoclust.hide_long_and_short_edges()
    print("Pierwsza predykcja")
    nodes = autoclust.predict_clusters()
    if paint:
        print("Rysowanie")
        filename = source[0:-4] + "_first_pred"
        Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength, filename)

    print("Przywracanie krotkich krawedzi")
    nodes = autoclust.restore_short_edges_and_predict()
    if paint:
        print("Rysowanie")
        filename = source[0:-4] + "_restore_short"
        Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength, filename)

    print("Secong order inconsistency")
    autoclust.detect_second_order_inconsistency()
    nodes = autoclust.repredict_clusters()
    if paint:
        print(" Rysowanie ")
        filename = source[0:-4] + "_second_order"
        Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength, filename)
        filename = source[0:-4] + "_final"
        Painter.draw_points_by_prediction(nodes, autoclust.cluster_strength, filename)

