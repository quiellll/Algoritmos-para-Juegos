n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    g.append([])
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].append(v)
    g[v].append(u)

print(g)