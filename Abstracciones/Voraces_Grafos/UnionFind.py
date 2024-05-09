n, m = map(int, input().strip().split())    # Nodos y aristas
edges = []

for _ in range(m):
    u, v, cost = map(int, input().strip().split())  # NodoA, NodoB, Coste
    edges.append((cost, u, v))

edges.sort()  # Ordenar por costes

parent = list(range(n))  # Array que almacena 0, 1, 2, ..., n
rank = [0] * n           # Array con n ceros

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])  # Compresión del camino
    return parent[u]

def union(u, v):
    root_u = find(u)    # Buscar el árbol que contiene u
    root_v = find(v)    # Buscar el árbol que contiene v

    if root_u != root_v:    # Si no pertenecen al mismo conjunto
        if rank[root_u] > rank[root_v]:  # Unir el árbol del nodo con menor rango al otro árbol
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:   # Si son iguales, se elige uno arbitrariamente y se incrementa su rango
            parent[root_v] = root_u
            rank[root_u] += 1


mst_cost = 0    # Coste del mst
for cost, u, v in edges:
    if find(u) != find(v):  # Si los nodos no están en el mismo conjunto
        union(u, v)         # Realiza la unión
        mst_cost += cost    # Suma el coste

print(mst_cost)
