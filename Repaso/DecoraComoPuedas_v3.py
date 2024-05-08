def min_dist(cost, visited):
    min_d = float('inf')
    best = 0

    for i in range(1, len(cost)):
        if not visited[i] and cost[i] < min_d:
            min_d = cost[i]
            best = i

    return best


def dijkstra(graph, start):
    total = [float('inf') for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    total[start] = 0
    visited[start] = True

    for start, end, distance in graph[start]:
        total[end] = distance

    for _ in range(1, len(graph) - 1):
        node = min_dist(total, visited)
        visited[node] = True
        for start, end, distance in graph[node]:
            total[end] = min(total[end], total[start] + distance)

    return total


n, m, t = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    h1, h2, d = map(int, input().split())
    g[h1].append([h1, h2, d])
    g[h2].append([h2, h1, d])

origin = 0
total = sum(dijkstra(g, origin))
print(total) if total <= t else print("Aleg, a decorar!")
