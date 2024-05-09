import heapq

def dijkstra(graph, start):

    distances = [float('inf')] * len(graph)

    distances[start] = 0

    queue = [(start, 0)]

    while queue:
        current_node, current_distance = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, neighbor_cost in graph[current_node]:
            distance = current_distance + neighbor_cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (neighbor, distance))

    return distances


n, m = map(int, input().strip().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    u, v, c = map(int, input().strip().split())
    edges[u].append([v, c])
    edges[v].append([u, c])

start_node = 0
distances_array = dijkstra(edges, start_node)

print(distances_array)
