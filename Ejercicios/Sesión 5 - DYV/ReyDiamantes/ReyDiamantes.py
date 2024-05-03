def rec_bs(v, number, low, high):
    if low >= high: #caso base
        return low

    mid = (low + high) // 2
#    if v[mid][0] == number:
#        return mid
    if number <= v[mid]:
        return rec_bs(v, number, low, mid)
    else:
        return rec_bs(v, number, mid + 1, high)


def recBinarySearch(v, number):
    return rec_bs(v, number, 0, len(v) - 1)


def DiscardPlayers(index, used_indices, grid):
    for i in range(index, len(grid)):
        if i not in used_indices:
            used_indices.add(i)  # Marcar el índice como usado
            return

def process_grid(grid, discard_list):
    used_indices = set()  # Almacena los índices de los valores que ya se han descartado

    # Procesa cada número en el conjunto de descartes
    for number in discard_list:
        if number > grid[-1]: continue
        index = recBinarySearch(grid, number)
        DiscardPlayers(index, used_indices, grid)
    return used_indices


n = int(input().strip())
grid = []

for _ in range(n):
    for e in input().strip().split():
        grid.append(int(e))

discard_set = list(map(int, input().strip().split()))

used = process_grid(grid, discard_set)

for i in range(n * n):
    if i in used:
        grid[i] = "X"
    if (i+1) % n == 0:
        print(grid[i])
    else:
        print(grid[i], end=" ")
