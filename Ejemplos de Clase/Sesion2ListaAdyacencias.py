# 5 7
# 0 1
# 0 2
# 0 4
# 1 2
# 1 3
# 1 4
# 2 3


n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    g.append([])
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].append(v)
    g[v].append(u)
