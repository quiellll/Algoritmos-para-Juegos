import heapq


def dijkstra(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()

    distances = [float('inf')] * len(graph)
    distances[start] = 0

    while heap:
        cost, node, path = heapq.heappop(heap)

        if node not in visited:
            visited.add(node)

            if node == end:
                return cost, path

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    n_cost = cost + weight
                    n_path = path + [neighbor]
                    if n_cost < distances[neighbor]:
                        distances[neighbor] = n_cost
                        heapq.heappush(heap, (n_cost, neighbor, n_path))

    return float('inf'), []


n, m = map(int, input().strip().split())

g = [[] for _ in range(n)]

for i in range(m):
    n1, n2, d = map(int, input().strip().split())
    g[n1].append([n2, d])
    g[n2].append([n1, d])

c_start, c_end = map(int, input().strip().split())

d, p = dijkstra(g, c_start, c_end)
print(d)
print(" ".join(map(str, p)))

