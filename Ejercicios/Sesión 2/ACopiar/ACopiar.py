# DFS simple
def bfs(start, g, visited):
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in g[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def get_groups(n, edges):
    # Crea un grafo vacío a partir del número de aristas, con un hueco para cada adyacencia
    g = {i: [] for i in range(n)}

    for edge in edges:  # Crear las adyacencias
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])  # Grafo no dirigido

    visited = {i: False for i in range(n)}
    connected = 0

    for vertex in range(n):
        if not visited[vertex]:
            # Hace una dfs en el vértice
            bfs(vertex, g, visited)
            # Cada vez que empiezo una bfs, significa que estoy en otro subgrafo/subgrupo
            connected += 1

    return connected


n, m = map(int, input().strip().split())
# Crea tuplas para ir guardando los pares de valores (adyacencias de este ejercicio)
connections = [tuple(map(int, input().strip().split())) for _ in range(m)]

print(get_groups(n, connections))
