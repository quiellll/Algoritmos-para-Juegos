def select_nodes(n):
    best_node = float('inf')
    for node in n:
        best_node = min(best_node, node)
    return best_node


def topo_sort(graph):
    nodes = set()
    adjacents = [0 for _ in range(len(graph))]
    path = []

    for element in range(len(graph)):
        for edge in graph[element]:
            adjacents[edge] += 1

    for element in range(len(graph)):
        if adjacents[element] == 0:
            nodes.add(element)

    while nodes:
        best_node = select_nodes(nodes)
        path.append(best_node)
        nodes.remove(best_node)
        for edge in graph[best_node]:
            adjacents[edge] -= 1
            if adjacents[edge] == 0:
                nodes.add(edge)

    return path


n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

print(" ".join(map(str, topo_sort(g))))
