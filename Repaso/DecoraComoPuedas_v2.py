def dist_min(distancia, visitados):
    dist_min = float('inf')
    mejor_nodo = 0

    for i in range(1, len(distancia)):
        if not visitados[i] and distancia[i] < dist_min:
            dist_min = distancia[i]
            mejor_nodo = i

    return mejor_nodo


def dijkstra(grafo, inicio):
    distancia = [float('inf')] * len(grafo)
    visitados = [False] * len(grafo)

    # comienza el algoritmo, guardando la distancia 0 y marcando el origen como visitado
    distancia[inicio] = inicio
    visitados[inicio] = True

    for h1, h2, d in grafo[inicio]:
        distancia[h2] = d
    # bucle voraz
    for _ in range(1, len(grafo) - 1):
        nodo = dist_min(distancia, visitados)
        visitados[nodo] = True
        for h1, h2, d in grafo[nodo]:
            distancia[h2] = min(distancia[h2], distancia[h1] + d)

    return distancia


n, m, t = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    h1, h2, d = map(int, input().split())
    g[h1].append([h1, h2, d])
    g[h2].append([h2, h1, d])

nodo_origen = 0
d_total = sum(dijkstra(g, nodo_origen))
print(d_total) if d_total <= t else print("Aleg, a decorar!")
