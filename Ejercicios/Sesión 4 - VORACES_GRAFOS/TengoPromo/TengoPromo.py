def floyd_warshall(n, graph):
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u in range(n):
        for v, d in graph[u]:
            dist[u][v] = min(dist[u][v], d)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n, m = map(int, input().strip().split())
identifiers = list(map(int, input().strip().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, input().strip().split())
    graph[u].append([v, d])
    graph[v].append([u, d])

distances = floyd_warshall(n, graph)

id_to_nodes = {}
for node, id_ in enumerate(identifiers):
    if id_ not in id_to_nodes:
        id_to_nodes[id_] = []
    id_to_nodes[id_].append(node)

results = {}
for id_, nodes in id_to_nodes.items():
    if len(nodes) > 1:
        min_dist = float("inf")
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                u, v = nodes[i], nodes[j]
                min_dist = min(min_dist, distances[u][v])
        results[id_] = min_dist

output = [results[id_] for id_ in sorted(results) if id_ in results]
print(" ".join(map(str, output)))
