def process_room(x, y, distance, room, enemies):
    n = len(room)
    m = len(room[0])

    visited = set()

    def move_weapon(x, y, range):
        hit = set()

        if range < 0 or (x, y) in visited or x < 0 or y < 0 or x >= n or y >= m:
            return hit

        visited.add((x, y))

        if (x, y) in enemies:
            hit.add((x, y))

        hit |= move_weapon(x + 1, y, range - 1)
        hit |= move_weapon(x - 1, y, range - 1)
        hit |= move_weapon(x, y + 1, range - 1)
        hit |= move_weapon(x, y - 1, range - 1)

        visited.remove((x, y))

        return hit

    enemies_hit = move_weapon(x, y, distance)

    if enemies_hit == enemies:
        return "ATACA"
    else:
        return "CORRE"


n, m, e = map(int, input().strip().split())

room = []
enemies = set()

for i in range(n):
    row = list(map(int, input().strip().split()))
    room.append(row)
    for j in range(m):
        if row[j] == 1:
            enemies.add((i, j))

x, y, d = map(int, input().strip().split())

print(process_room(x, y, d, room, enemies))

