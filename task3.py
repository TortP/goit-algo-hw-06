import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф з вагами ребер
G = nx.Graph()

# Додаємо вершини та ребра з вагами (відстанями між зупинками)
G.add_edge('Зупинка A', 'Зупинка B', weight=5)
G.add_edge('Зупинка A', 'Зупинка C', weight=3)
G.add_edge('Зупинка B', 'Зупинка D', weight=7)
G.add_edge('Зупинка C', 'Зупинка D', weight=2)
G.add_edge('Зупинка D', 'Зупинка E', weight=1)

# Функція для візуалізації графа з вагами ребер
def visualize_weighted_graph(graph):
    pos = nx.spring_layout(graph)  # Позиції вершин
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Транспортна мережа з вагами ребер")
    plt.show()

# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start):
    # Використовуємо функцію nx.single_source_dijkstra, яка реалізує алгоритм Дейкстри
    lengths = nx.single_source_dijkstra_path_length(graph, start)
    paths = nx.single_source_dijkstra_path(graph, start)
    
    return lengths, paths

# Знаходимо найкоротші шляхи від 'Зупинка A' до всіх інших вершин
distances, paths = dijkstra(G, 'Зупинка A')

# Виведення результатів у консоль
print("Найкоротші відстані від 'Зупинка A' до інших вершин:")
for destination, distance in distances.items():
    print(f"До {destination}: {distance} (шлях: {' -> '.join(paths[destination])})")

# Візуалізуємо граф
visualize_weighted_graph(G)
