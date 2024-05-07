import heapq


def dijkstra(grafo, ini, fin):
    cola = [(0, ini, [ini])]        # coste, nodo inicial, camino. se ordena en función de los pesos
    visitados = set()               # conjunto de nodos visitados

    distancias = [float('inf')] * len(grafo) # distancia infinita para cada nodo
    distancias[ini] = 0                      # distancia 0 para el nodo inicial

    while cola:
        coste, nodo, camino = heapq.heappop(cola)   # saca el elemento más pequeño (menor coste) de la cola

        if nodo not in visitados:                   # si el nodo no se ha visitado anteriormente, se guarda
            visitados.add(nodo)

            if nodo == fin:                         # si el nodo es el mismo que el de "meta", se para el algoritmo
                return coste, camino                # se devuelve el coste y el camino, que es lo que piden de salida

            for vecino, peso, in grafo[nodo]:       # por cada vecino del nodo en el que estamos
                if vecino not in visitados:         # si el vecino no está visitado
                    nuevo_coste = coste + peso      # el coste para llegar a ese nodo es el acumulado más el peso del arista que lo une con el actual
                    nuevo_camino = camino + [vecino]# el camino para llegar a ese nodo es el recorrido más el nodo vecino
                    if nuevo_coste < distancias[vecino]: # si el coste calculado es menor que el que tiene almacenado ese nodo como menor coste
                        distancias[vecino] = nuevo_coste      # lo registramos como el coste para llegar al vecino (es el menor coste encontrado para ese nodo)
                        heapq.heappush(cola, (nuevo_coste, vecino, nuevo_camino)) # a la cola añadimos el elemento con el coste, el nodo, y el camino para ese nodo

    return float('inf'), []


n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    c1, c2, d = map(int, input().split())
    g[c1].append([c2, d])
    g[c2].append([c1, d])

s, e = map(int, input().split())

total_cost, path = dijkstra(g, s, e)

print(total_cost)
print(" ".join(map(str, path)))
