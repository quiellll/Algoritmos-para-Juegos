def binary_search(grid, target, used_indices):
    low, high = 0, len(grid) - 1
    closest_larger = None

    while low <= high:
        mid = (low + high) // 2
        value, _ = grid[mid]

        if mid in used_indices:
            # Si ya se ha descartado a este jugador, se omite
            low = mid + 1
            continue

        if value < target:
            low = mid + 1
        elif value > target:
            if closest_larger is None or (value < grid[closest_larger][0] and closest_larger not in used_indices):
                closest_larger = mid
            high = mid - 1
        else:
            return mid  # Valor exacto encontrado

    return closest_larger  # Devolver el índice del mayor si no se ha encontrado el valor exacto


def process_grid(original_grid, discard_set):
    n = len(original_grid)
    flat_grid = [(original_grid[i][j], (i, j)) for i in range(n) for j in range(n)]
    used_indices = set()  # Almacena los índices de los valores que ya se han descartado

    # Procesa cada número en el conjunto de descartes
    for number in discard_set:
        index = binary_search(flat_grid, number, used_indices)
        if index is not None and index not in used_indices:
            _, (i, j) = flat_grid[index]
            original_grid[i][j] = 'X'  # Poner la 'X'
            used_indices.add(index)  # Marcar el índice como usado


def print_grid(grid):
    for row in grid:
        print(' '.join(str(x) for x in row))


n = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(n)]
discard_set = set(map(int, input().strip().split()))

process_grid(grid, discard_set)
print_grid(grid)
