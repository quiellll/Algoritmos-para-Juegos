import heapq

def dijkstra(n, edges, start):
    g = {i: [] for i in range(n)}
    for u, v, cost in edges:
        g[u].append((cost, v))
        g[v].append((cost, u))

    distances = [float('inf')] * n
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for cost, neighbor in g[current_node]:
            distance = current_dist + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


n, m = map(int, input().strip().split())
edges = []

for _ in range(m):
    u, v, cost = map(int, input().strip().split())
    edges.append((u, v, cost))

start = 0
distances = dijkstra(n, edges, start)

print("Distancias desde el nodo " + str(start))
for i, dist in enumerate(distances):
    print(f"Distancia al nodo {i}: {dist}")
