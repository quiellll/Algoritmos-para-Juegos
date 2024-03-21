from collections import deque


def busqueda_fans(grafo, nota):

    visitados = [False] * len(grafo)
    profundidad = [0] * len(grafo)

    visitados[0] = True
    cola = deque([0])
    fans_totales = 1

    nivel_max = nota - 1

    while cola:
        nodo = cola.popleft()
        visitados[nodo] = True
        for vecino in grafo[nodo]:
            if not visitados[vecino]:
                visitados[vecino] = True
                profundidad[vecino] = profundidad[nodo] + 1
                cola.append(vecino)
                if profundidad[vecino] > nivel_max:
                    cola.clear()
                else:
                    fans_totales += 1

    return fans_totales


n = int(input().strip())

for _ in range(n):
    m, k, c = map(int, input().strip().split())
    g = [[] for _ in range(k)]

    for _ in range(c):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)

    print(busqueda_fans(g, m))

