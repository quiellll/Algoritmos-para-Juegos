def get_min_distance(dist, visit):
    min_distance = float('inf')
    best_node = 0

    for i in range(1, len(dist)):
        if not visit[i] and dist[i] < min_distance:
            min_distance = dist[i]
            best_node = i

    return best_node


def dijkstra(graph, origin):
    total_dist = [float("Inf")] * len(graph)
    visited = [False] * len(graph)

    total_dist[origin] = origin
    visited[origin] = True

    for start, end, weight in graph[origin]:
        total_dist[end] = weight
    # Bucle voraz
    for _ in range(1, len(graph) - 1):
        node = get_min_distance(total_dist, visited)
        visited[node] = True
        for start, end, weight in graph[node]:
            total_dist[end] = min(total_dist[end], total_dist[start] + weight)

    return total_dist


n, m, maxTime = map(int, input().strip().split())
g = [[] for _ in range(n)]

for _ in range(m):
    h_1, h_2, d = map(int, input().strip().split())
    g[h_1].append([h_1, h_2, d])
    g[h_2].append([h_2, h_1, d])

node_origin = 0
d_total = sum(dijkstra(g, node_origin))
print(d_total) if d_total <= maxTime else print("Aleg, a decorar!")
