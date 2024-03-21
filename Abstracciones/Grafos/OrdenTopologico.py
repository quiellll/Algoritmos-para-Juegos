def seleccionar_mejor(conjunto_nodos):
    # Ponemos como mejor el infinito
    mejor = float('inf')

    # Seleccionamos el nodo de menor valor en el conjunto
    for nodo in conjunto_nodos:
        mejor = min(mejor, nodo)

    return mejor


def orden_topologico(grafo):
    # Almacena las aristas entrantes de cada nodo
    aristas_entrantes = [0 for _ in range(len(grafo))]
    # Lista con los nodos en el orden correcto
    recorrido = []

    # Contar las adyacencias de cada vértice del grafo
    for vertice in range(len(grafo)):
        for arista in (grafo[vertice]):
            aristas_entrantes[arista] += 1

    nodos_a_explorar = set()

    # Guardar los vértices sin aristas para ponerlos como los primeros
    for vertice in range(len(grafo)):
        if aristas_entrantes[vertice] == 0:
            nodos_a_explorar.add(vertice)

    # Mientras haya nodos en el conjunto
    while nodos_a_explorar:
        # Buscar el mejor nodo
        mejor_nodo = seleccionar_mejor(nodos_a_explorar)
        # Guardarlo en la solución
        recorrido.append(mejor_nodo)
        # Eliminarlo del conjunto
        nodos_a_explorar.remove(mejor_nodo)
        # Si tiene adyacencias, por cada adyacencia, ir guardándolas en el conjunto
        for arista in grafo[mejor_nodo]:
            aristas_entrantes[arista] -= 1
            if aristas_entrantes[arista] == 0:
                nodos_a_explorar.add(arista)

    return recorrido


nodos = 5
aristas = 6

adyacencias = [[0, 2],
               [2, 4],
               [0, 1],
               [1, 2],
               [0, 4],
               [2, 3]]

g = [[] for _ in range(nodos)]

for i in range(aristas):
    g[adyacencias[i][0]].append(adyacencias[i][1])

print("Grafo ordenado: " + " ".join(map(str, orden_topologico(g))))
