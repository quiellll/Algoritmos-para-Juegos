import heapq

def dijkstra(edges, start):
    distances = [float('inf')] * len(edges)

    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, cost in edges[current_node]:
            distance = current_distance + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances



n, m = map(int, input().strip().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    u, v, cost = map(int, input().strip().split())
    edges[u].append([v, cost])
    edges[v].append([u, cost])

start_node = 0
distances = dijkstra(edges, start_node)

print(distances)

print("Distancias desde el nodo " + str(start_node))
for i, dist in enumerate(distances):
    print(f"Distancia al nodo {i}: {dist}")
