def find_critical_points_recursive(g, node, visited, articulations, depth, eldest):
    visited[node] = True
    children = 0
    eldest[node] = min(eldest[node], depth[node])

    # por cada hijo/adyacencia del nodo actual
    for child in g[node]:
        # si no se ha visitado
        if not visited[child]:
            children += 1
            depth[child] = depth[node] + 1

            find_critical_points_recursive(g, child, visited, articulations, depth, eldest)

            eldest[node] = min(eldest[node], eldest[child])

            # nodo es p. art. si tiene un hijo u tal que profundidad[nodo] <= masviejo[u]
            if 0 != depth[node] <= eldest[child]:
                articulations[node] = True

        else:
            eldest[node] = min(eldest[node], depth[child])

    # si es nodo raíz y tiene más de un hijo, es un punto de articulacion
    if depth[node] == 0 and children > 1:
        # nodo raiz
        articulations[node] = True


def find_critical_points(g, c):
    visited = [False] * len(g)
    articulations = [False] * len(g)
    depth = [0] * len(g)
    eldest = [float('inf')] * len(g)

    for n in range(len(g)):
        if not visited[n]:
            find_critical_points_recursive(g, n, visited, articulations, depth, eldest)

    totalcost = 0

    for n in range(len(g)):
        if articulations[n]:
            totalcost += c[n]

    return totalcost


n, m = map(int, input().split())
g = [[] for _ in range(n)]
c = []

for _ in range(n):
    c.append(int(input().strip()))
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


result = find_critical_points(g, c)
print(result)

# Inicializar los nodos visitados, conjunto de resultado, y array de niveles y de ancestros
# A partir de un nodo, empezar la busqueda recursiva
# Iterar los nodos que falten (si no es un grafo conexo) y si no están visitados se hace la búsqueda otra vez.
# Identificar las articulaciones y sumar los pesos