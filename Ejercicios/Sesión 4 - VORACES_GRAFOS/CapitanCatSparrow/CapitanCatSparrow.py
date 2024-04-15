import heapq


def dijkstra(graph, start, end):
    # Cola de prioridad para almacenar los nodos a explorar, con formato (coste, nodo, camino)
    heap = [(0, start, [start])]
    visited = set()
    # Using list for distances since nodes are 0-indexed and can be directly accessed
    distances = [float('inf')] * len(graph)
    distances[start] = 0

    while heap:
        cost, node, path = heapq.heappop(heap)  # Ensure this matches the tuple pushed onto the heap

        if node not in visited:
            visited.add(node)

            if node == end:
                return cost, path

            for next_node, weight in graph[node]:
                if next_node not in visited:
                    new_cost = cost + weight
                    new_path = path + [next_node]
                    if new_cost < distances[next_node]:
                        distances[next_node] = new_cost
                        heapq.heappush(heap, (new_cost, next_node, new_path))

    return float('inf'), []


n, m = map(int, input().strip().split())

g = [[] for _ in range(n)]

for i in range(m):
    n1, n2, d = map(int, input().strip().split())
    g[n1].append([n2, d])
    g[n2].append([n1, d])

c_ini, c_end = map(int, input().strip().split())

distance, path = dijkstra(g, c_ini, c_end)

print(distance)
print(" ".join(map(str, path)))
