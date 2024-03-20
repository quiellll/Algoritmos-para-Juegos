from collections import deque


def bfs(graph):
    # Profundidad de la casilla, comienza en (0, 0)
    depth = {(0, 0): 0}
    # Cola de prioridad
    queue = deque()
    # Añado la casilla de salida
    queue.append((0, 0))
    # Conjunto para las casillas visitadas
    visited = set()

    # Función para obtener los vecinos de la casilla
    def get_neighbors(node):
        # Lista vacía
        neighbors = []

        # Auxiliares para cálculo vecinos
        rows = [0, 0, 1, -1]
        cols = [1, -1, 0, 0]

        # Una casilla tiene 4 vecinos
        for i in range(4):

            # Vecino horizontalmente
            nr = rows[i] + node[0]
            # Vecino verticalmente
            nc = cols[i] + node[1]

            # Comprobar que no me salgo del laberinto
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                # Si la casilla es válida (no hay muro), o estoy en un turno par (según profundidad)
                if graph[nr][nc] != -1 or depth[node] % 2 == 0:
                    # Añado el vecino
                    neighbors.append((nr, nc))

        return neighbors

    # BFS en la lista de vecinos válidos
    while queue:
        # Elegir el nodo actual
        current_node = queue.popleft()
        # Marcarlo como visitado (evitar ciclos)
        visited.add(current_node)
        # Por cada vecino válido (obtenido antes)
        for neighbor in get_neighbors(current_node):
            # Si el vecino no ha sido visitado
            if neighbor not in visited:
                # Se añade a la cola
                queue.append(neighbor)
                # Se suma 1 a la profundidad DE ESE VECINO (almacenada en el diccionario)
                depth[neighbor] = depth[current_node] + 1
                # Si es la casilla destino
                if graph[neighbor[0]][neighbor[1]] == 2:
                    # El valor de la profundidad es el valor de la distancia más corta
                    return depth[neighbor]


n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    # Lista de listas
    g.append(list(map(int, input().strip().split())))

print(bfs(g))
