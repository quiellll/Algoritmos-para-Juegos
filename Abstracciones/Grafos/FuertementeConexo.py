def dfs(start, graph, visited):
    visited.add(start)
    for nodo in graph[start]:
        if nodo not in visited:
            dfs(nodo, graph, visited)


nodos = 5
aristas = 9

adyacencias = [[0, 3],
               [0, 4],
               [1, 3],
               [1, 2],
               [2, 1],
               [3, 0],
               [3, 4],
               [4, 3],
               [4, 1]]

grafo = [[] for _ in range(nodos)]
grafo_invertido = [[] for _ in range(nodos)]

for i in range(nodos):
    grafo[adyacencias[i][0]].append(adyacencias[i][1])
    grafo_invertido[adyacencias[i][1]].append(adyacencias[i][0])

nodo_inicial = 0

visitados = set()
dfs(nodo_inicial, grafo, visitados)
visitados_inverso = set()
dfs(nodo_inicial, grafo_invertido, visitados_inverso)

if len(visitados) == nodos and len(visitados_inverso) == nodos:
    print("Grafo fuertemente conexo")
else:
    print("El grafo no es fuertemente conexo")
