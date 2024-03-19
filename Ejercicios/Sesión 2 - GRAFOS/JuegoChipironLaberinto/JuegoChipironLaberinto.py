from collections import deque


def bfs(graph):
    depth = {(0, 0): 0}
    queue = deque()
    queue.append((0, 0))
    visited = set()

    def get_neighbors(node):
        neighbors = []

        rows = [0, 0, 1, -1]
        cols = [1, -1, 0, 0]
        for i in range(4):
            nr = rows[i] + node[0]
            nc = cols[i] + node[1]

            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                if graph[nr][nc] != -1 or depth[node] % 2 == 0:
                    neighbors.append((nr, nc))

        return neighbors

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)
        for neighbor in get_neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                depth[neighbor] = depth[current_node] + 1
                if graph[neighbor[0]][neighbor[1]] == 2:
                    return depth[neighbor]


n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    g.append(list(map(int, input().strip().split())))

print(bfs(g))
