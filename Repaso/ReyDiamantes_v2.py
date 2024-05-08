def bin_search(arr, trg, lo, hi):
    if lo >= hi:
        return lo

    mid = (lo + hi) // 2

    if trg <= arr[mid]:
        return bin_search(arr, trg, lo, mid)
    else:
        return bin_search(arr, trg, mid + 1, hi)


def discard_players(arr, discards, idx):
    for i in range(idx, len(arr)):
        if i not in discards:
            discards.add(i)
            return


def process_grid(grid, discards):
    used_idx = set()

    for number in discards:
        if number > discards[-1]: continue
        player = bin_search(grid, number, 0, len(grid) - 1)
        discard_players(grid, used_idx, player)

    return used_idx


n = int(input().strip())
g = []
for i in range(n):
    for elem in input().strip().split():
        g.append(int(elem))

discard_set = list(map(int, input().strip().split()))

eliminated = process_grid(g, discard_set)

for i in range(n * n):
    if i in eliminated:
        g[i] = 'X'
    if (i + 1) % n == 0:
        print(g[i])
    else:
        print(g[i], end=" ")


