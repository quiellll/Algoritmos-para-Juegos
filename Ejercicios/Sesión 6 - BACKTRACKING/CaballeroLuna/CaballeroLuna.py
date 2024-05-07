def puede_atacar(x, y, d, room, enemigos):
    n = len(room)
    m = len(room[0])

    visitados = set()

    def mover_arma(x, y, alcance):
        alcanzados = set()  # definir alcanzados dentro de la función mover_arma

        if alcance < 0 or (x, y) in visitados or x < 0 or y < 0 or x >= n or y >= m or room[x][y] == -1:
            return alcanzados

        visitados.add((x, y))

        if (x, y) in enemigos:
            alcanzados.add((x, y))

        #agregar los enemigos alcanzados de forma recursiva
        alcanzados |= mover_arma(x + 1, y, alcance - 1)  # Abajo
        alcanzados |= mover_arma(x - 1, y, alcance - 1)  # Arriba
        alcanzados |= mover_arma(x, y + 1, alcance - 1)  # Derecha
        alcanzados |= mover_arma(x, y - 1, alcance - 1)  # Izquierda

        visitados.remove((x, y))

        return alcanzados

    alcanzados = mover_arma(x, y, d)

    if alcanzados == enemigos:
        return "ATACA"
    else:
        return "CORRE"


# entrada
n, m, e = map(int, input().strip().split())

room = []
enemigos = set()
for i in range(n):
    fila = list(map(int, input().strip().split()))
    room.append(fila)
    for j in range(m):
        if fila[j] == 1:
            enemigos.add((i, j))
x, y, d = map(int, input().strip().split())

resultado = puede_atacar(x, y, d, room, enemigos)
print(resultado)
