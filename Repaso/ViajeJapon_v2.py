def dfs(node, graph, visited):
    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            dfs(i, graph, visited)

n, m = map(int, input().strip().split())
g = []
ig = []

for _ in range(n):
    g.append([])
    ig.append([])
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].append(v)
    ig[v].append(u)

visit = set()
dfs(0, g, visit)
visitinverse = set()
dfs(0, ig, visitinverse)

if len(visit) == n and len(visitinverse) == n:
    print("PERFECTO")
else:
    print("CAMBIA EL ITINERARIO")
