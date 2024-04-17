from math import ceil


n, m = map(int, input().strip().split())
edges = []

for _ in range(m):
    u, v, cost = map(int, input().strip().split())
    edges.append((cost, u, v))

edges.sort()

parent = list(range(n))
rank = [0] * n


def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]


def union(u,v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

mst_cost = 0

for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst_cost += cost

print(ceil(mst_cost / 5))
