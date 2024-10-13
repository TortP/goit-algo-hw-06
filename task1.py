import networkx as nx
import matplotlib.pyplot as plt

# Створимо порожній граф
G = nx.Graph()

# Додамо вершини (зупинки громадського транспорту)
G.add_nodes_from(['Зупинка A', 'Зупинка B', 'Зупинка C', 'Зупинка D', 'Зупинка E'])

# Додамо ребра (маршрути між зупинками)
G.add_edges_from([('Зупинка A', 'Зупинка B'),
                  ('Зупинка A', 'Зупинка C'),
                  ('Зупинка B', 'Зупинка D'),
                  ('Зупинка C', 'Зупинка D'),
                  ('Зупинка D', 'Зупинка E')])

# Візуалізація графу
pos = nx.spring_layout(G)  # визначаємо положення вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик графу
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступінь кожної вершини:")
for node in G.nodes:
    print(f"{node}: {G.degree(node)}")
