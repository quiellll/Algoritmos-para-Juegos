def bfs(graph, start, visited):
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


def get_groups(nodes, graph):
    adjacency_list = [[] for _ in range(nodes)]
    visited = set()
    groups = 0

    for edge in graph:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    for vertex in range(nodes):
        if vertex not in visited:
            bfs(adjacency_list, vertex, visited)
            groups += 1

    return groups


number_of_nodes = 10
g = [[0, 1],
     [1, 5],
     [2, 4],
     [3, 9],
     [4, 9]]

print("Componentes conexas: " + str(get_groups(number_of_nodes, g)))
