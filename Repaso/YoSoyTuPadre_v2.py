from collections import deque

def get_tree(graph):
    tree = {}

    for member in graph:
        parent = member[0]
        children = member[1:]
        tree[parent] = children
    return tree


def calc_levels(tree, root):
    levels = {}
    queue = deque([(root, 1)])
    while queue:
        member, level = queue.popleft()
        levels[member] = level
        children = tree.get(member, [])
        for child in children:
            queue.append((child, level + 1))

    return levels



def get_level(graph, search):
    tree = get_tree(graph)
    parents = set()
    children = set()

    for element in graph:
        parents.add(element[0])
        children.update(element[1:])

    root = list(parents - children)[0]
    levels = calc_levels(tree, root)

    return [levels[s] for s in search]


n = int(input().strip())
g = [list(map(int, input().strip().split())) for _ in range(n)]

m = int(input())
search = [int(input().strip()) for _ in range(m)]

levels = get_level(g, search)
for r in levels:
    print(r)
