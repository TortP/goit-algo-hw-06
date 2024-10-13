import networkx as nx
from collections import deque

# Створимо граф з попереднього завдання
G = nx.Graph()
G.add_edges_from([('Зупинка A', 'Зупинка B'),
                  ('Зупинка A', 'Зупинка C'),
                  ('Зупинка B', 'Зупинка D'),
                  ('Зупинка C', 'Зупинка D'),
                  ('Зупинка D', 'Зупинка E')])

# Алгоритм DFS (пошук в глибину)
def dfs(graph, start):
    visited = set()  # Множина відвіданих вершин
    stack = [start]  # Стек для вершин, які потрібно відвідати
    path = []        # Список для запису порядку відвідування

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            # Додаємо сусідів вершини у стек в зворотньому порядку, щоб вірно імітувати DFS
            stack.extend(reversed(list(graph[vertex])))

    return path

# Алгоритм BFS (пошук в ширину)
def bfs(graph, start):
    visited = set()  # Множина відвіданих вершин
    queue = deque([start])  # Черга для вершин, які потрібно відвідати
    path = []               # Список для запису порядку відвідування

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            # Додаємо сусідів вершини у чергу
            queue.extend(graph[vertex])

    return path

# Виконання DFS та BFS для графа
dfs_path = dfs(G, 'Зупинка A')
bfs_path = bfs(G, 'Зупинка A')

# Виведення результатів
print("Шлях DFS:", dfs_path)
print("Шлях BFS:", bfs_path)

# Порівняння результатів
if dfs_path == bfs_path:
    print("DFS і BFS повертають однакові шляхи.")
else:
    print("DFS і BFS повертають різні шляхи.")
    print("Різниця:")
    print(f"DFS шлях: {dfs_path}")
    print(f"BFS шлях: {bfs_path}")