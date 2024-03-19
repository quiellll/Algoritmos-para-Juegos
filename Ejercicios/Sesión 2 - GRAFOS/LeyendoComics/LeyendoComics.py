def select_node(nodos):
    mejor = float("inf")
    for n in nodos:
        mejor = min(mejor, n)
    return mejor

def topo_sort(g):
    entrantes = [0 for _ in range(len(g))]
    recorrido = []

    for v in range(len(g)):
        for a in (g[v]):
            entrantes[a] += 1

    nodos = set()

    for v in range(len(g)):
        if entrantes[v] == 0:
            nodos.add(v)

    while nodos:
        #nodos.sort()
        mejor = select_node(nodos)
        recorrido.append(mejor)
        nodos.remove(mejor)
        #g[origen].sort()
        for a in g[mejor]:
            entrantes[a] -= 1
            if entrantes[a] == 0:
                nodos.add(a)

    return recorrido


n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    g.append([])
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].append(v)

topo_order = topo_sort(g)
print(" ".join(map(str, topo_order)))
