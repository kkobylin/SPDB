import DataReader
import Node
import Painter
import Autoclust

if __name__ == '__main__':
    data = DataReader.read_tsv("data/Aggregation.txt")
    nodes = []
    for row in data:
        nodes.append(Node.Node(row[0], row[1], row[2]))
    # Painter.draw_points(nodes, cluster_strength=None)      #TODO kod sie zatrzymuje jak rysuje wykres w oddzielnym okienku

    autoclust = Autoclust.Autoclust(nodes)
    print("Triangulacja")
    nodes = autoclust.get_edges_from_triangulation()
    print("Rysowanie")
    # Painter.draw_nodes_with_edges(nodes, autoclust.all_edges, cluster_strength=None)

    print("Statystyki")
    autoclust.calculate_statistics()
    print("Dzielenie krawedzi")
    autoclust.split_edges()
    print("Ukrywanie krawedzi")
    autoclust.hide_long_and_short_edges()
    print("Pierwsza predykcja")
    nodes = autoclust.predict_clusters() #TODO punkty bez polaczenia w gorno-srodkowym clustrze maja ten sam kolor
    print("Rysowanie")
    Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength)

    print("Przywracanie krotkich krawedzi")
    nodes = autoclust.restore_short_edges_and_predict()     #TODO pojedyncze punkty niezlaczone z clustrem np 30.75 26.90
    print("Rysowanie")
    Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength)

    print("Secong order inconsistency")
    autoclust.detect_second_order_inconsistency()
    nodes = autoclust.repredict_clusters()
    print(" Rysowanie ")
    Painter.draw_points_by_prediction_with_edges(nodes, autoclust.all_edges, autoclust.cluster_strength)

    # TODO liczenie poprawnosci clusteringu
