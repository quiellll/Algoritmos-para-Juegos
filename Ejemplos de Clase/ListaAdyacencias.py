# Lista de adyacencias.

def dfs_recursivo(g_dfs, node, visited, lista):
    # Marcar el nodo como visitado
    visited.add(node)
    # Añadir el nodo a la lista de visitados
    lista.append(node)
    # Comprobar adyacencias del nodo
    for adj in g_dfs[node]:
        # Si tiene una adyacencia sin visitar, se explora ese nodo
        if adj not in visited:
            dfs_recursivo(g_dfs, adj, visited, lista)


def dfs(g_dfs):
    # Se crea el conjunto que registra los nodos visitados
    visited = set()
    # Se guarda el número de nodos del grafo
    nodos = len(g_dfs)
    # Se crea una lista vacía para almacenar el recorrido
    lista = []
    # Por si no es conexo
    for i in range(nodos):
        if i not in visited:
            dfs_recursivo(g_dfs, i, visited, lista)

    # Se devuelve la lista
    return lista


# Grafo a explorar
g = [
    [1, 2, 3],
    [0, 2, 4, 5],
    [0, 1, 5],
    [0, 6, 7],
    [1, 5],
    [1, 2, 4],
    [3, 7],
    [3, 6]
]

# Llamada al método
listaAdyacencias = dfs(g)

# Se muestra por pantalla la lista
print(listaAdyacencias)
