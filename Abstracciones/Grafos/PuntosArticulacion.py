def busqueda_art_recursiva(g, nodo, visitados, articulaciones, profundidad, ancestro):

    visitados[nodo] = True
    hijos = 0
    ancestro[nodo] = min(ancestro[nodo], profundidad[nodo])

    for hijo in g[nodo]:
        if not visitados[hijo]:
            hijos += 1
            profundidad[hijo] = profundidad[nodo] + 1

            busqueda_art_recursiva(g, hijo, visitados, articulaciones, profundidad, ancestro)

            ancestro[nodo] = min(ancestro[nodo], ancestro[hijo])

            if 0 != profundidad[nodo] <= ancestro[hijo]:
                articulaciones[nodo] = True

        else:
            ancestro[nodo] = min(ancestro[nodo], profundidad[hijo])

    if profundidad[nodo] == 0 and hijos > 1:
        articulaciones[nodo] = True


def suma_puntos_articulacion(g, c):

    visitados = [False] * len(g)
    articulaciones = [False] * len(g)
    profundidad = [0] * len(g)
    nodo_superior_alcanzable = [float('inf')] * len(g)

    for nodo in range(len(g)):
        if not visitados[nodo]:
            busqueda_art_recursiva(g, nodo, visitados, articulaciones, profundidad, nodo_superior_alcanzable)

    coste_total = 0
    for nodo in range(len(g)):
        if articulaciones[nodo]:
            coste_total += c[nodo]

    return coste_total


nodos = 6
aristas = 5

grafo = [[] for _ in range(nodos)]
costes = [50, 22, 58, 99, 38, 21]

adyacencias = [[0, 1],
               [1, 2],
               [2, 3],
               [3, 4],
               [4, 5]]

for i in range(aristas):
    grafo[adyacencias[i][0]].append(adyacencias[i][1])
    grafo[adyacencias[i][1]].append(adyacencias[i][0])

print(suma_puntos_articulacion(grafo, costes))
