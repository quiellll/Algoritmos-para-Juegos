from collections import deque

def busqueda_fans_anchura(g, nota):
    visitados = [False] * len(g)
    niveles = [0] * len(g)

    visitados[0] = True
    cola = deque([0])
    fansobtenidos = 1

    nivel_max = nota - 1

    while cola:
        nodo = cola.popleft()
        for vecino in g[nodo]:
            if not visitados[vecino]:
                visitados[vecino] = True
                cola.append(vecino)
                niveles[vecino] = niveles[nodo] + 1
                if niveles[vecino] > nivel_max:
                    cola.clear()
                else:
                    fansobtenidos += 1

    return fansobtenidos


concursantes = int(input().strip())

for i in range(concursantes):
    nota, fans, relaciones = map(int, input().strip().split())

    g = [[] for _ in range(fans)]

    for _ in range(relaciones):
        u, v = map(int, input().strip().split())
        g[u].append(v)
        g[v].append(u)

    print(busqueda_fans_anchura(g, nota))
