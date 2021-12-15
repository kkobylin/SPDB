import DataReader
import Node
import Painter
import Autoclust

if __name__ == '__main__':
    data = DataReader.read_tsv("data/Aggregation.txt")
    nodes = []
    for row in data:
        nodes.append(Node.Node(row[0], row[1], row[2]))
    Painter.draw_points(nodes)

    autoclust = Autoclust.Autoclust(nodes)
    print("Triangulacja")
    nodes = autoclust.get_edges_from_triangulation()
    print("Rysowanie")
    Painter.draw_nodes_with_edges(nodes)

    print("Statystyki")
    autoclust.calculate_statistics()
    print("Dzielenie krawedzi")
    autoclust.split_edges()
    print("Ukrywanie krawedzi")
    autoclust.hide_long_and_short_edges()
    print("Pierwsza predykcja")
    nodes = autoclust.predict_clusters()
    print("Rysowanie")
    Painter.draw_points_by_prediction(nodes)

    print("Przywracanie krotkich krawedzi")
    nodes = autoclust.restore_short_edges()
    print("Rysowanie")
    Painter.draw_points_by_prediction(nodes)
