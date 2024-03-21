def bfs(graph, start, visited):
    # Cola comenzando en el nodo pasado como parámetro
    queue = [start]

    # BFS simple
    while queue:
        vertex = queue.pop(0)
        # Es un poco redundante, pero no está de más comprobar si el vértice se ha visitado
        if vertex not in visited:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    # Guardar el vecino y marcar el nodo como visitado
                    queue.append(neighbor)
                    visited.add(neighbor)


def get_groups(nodes, graph):
    # Estructuras de datos
    adjacency_list = [[] for _ in range(nodes)]
    visited = set()
    # Valor solución
    groups = 0

    # Rellenar lista adyacencias
    for edge in graph:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    # Por cada vértice no visitado
    for vertex in range(nodes):
        if vertex not in visited:
            # Comenzar un BFS
            bfs(adjacency_list, vertex, visited)
            # Por cada BFS, contamos 1 componente nueva
            groups += 1

    return groups


number_of_nodes = 10
g = [[0, 1],
     [1, 5],
     [2, 4],
     [3, 9],
     [4, 9]]

print("Componentes conexas: " + str(get_groups(number_of_nodes, g)))
