def agrupar(participantes, k):
    equipo_joven = []
    for _ in range(k):
        equipo_joven.append(participantes.pop(0))

    for p in equipo_joven:
        print(p[1], end=' ')
    print()
    for p in participantes:
        print(p[1], end=' ')


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    participantes = []
    for _ in range(n):
        nombre, edad = input().strip().split()
        edad = int(edad)
        participantes.append((edad, nombre))
    participantes.sort()
    agrupar(participantes, min(n-k, k))
